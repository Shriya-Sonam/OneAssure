from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
import csv
import json

app = Flask(__name__)

client = MongoClient('mongodb+srv://sonamshriya25:OqyQenGm4ioGG7jo@oneassure.sbdccvr.mongodb.net/?retryWrites=true&w=majority')

database_names = client.list_database_names()

def upload_insurance_data_to_mongo(csv_file, client,mongo_db, mongo_collection):
    print("DB entries for rates not found please wait while we upload all the data")
    db = client[mongo_db]
    collection = db[mongo_collection]
   
    # Read data from CSV and upload to MongoDB
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            insurance_data = {
                'sumInsured': row['SumInsured'],
                'rate': row['Rate'],
                'age': row['Age'],
                'tier': row['TierID'],
                'tenure': row['Tenure'],
            }
            collection.insert_one(insurance_data)

    print("All data uploaded successfully")

# Check if database exists
if 'insurance' in database_names:
    print("Database exists!")
else:
    try:
        upload_insurance_data_to_mongo('./insurance.csv', client,'insurance', 'premium_rates' )
    except:
        print("Error: Cannot upload data")


db = client.insurance
premium_rates = db.premium_rates

@app.route('/', methods=(["GET","POST"]))
def index():
    if request.method=='GET':
        return render_template('index.html')
    if request.method=='POST':
        # Here we are reading the form data as sent by the frontend i.e. index.html
        # This data key is coming from the name attribute of the i/p fields 
        sumInsured = request.form['sumInsured']
        tier = request.form['tier']
        tenure = request.form['tenure']
        noOfPeople = int(request.form['numOfPerson'])
        rates = dict()
        maxAge= 0
        totalRate = 0

        for i in range(noOfPeople): # this will start from 0 
            age = request.form[f'age{i+1}']
            if(int(age) > maxAge): maxAge = int(age)
            if age not in rates:
                rateObj = premium_rates.find_one({"age": age,"tier": tier,"tenure": tenure,"sumInsured":sumInsured})
                rates[age] =  rateObj["rate"]    

            totalRate = totalRate + int(rates[age])/2    
        
        totalRate = totalRate + (int(rates[str(maxAge)]) / 2)
        discount = 0 

        for values in rates.values():
            discount = discount + int(values)

        return render_template('result.html', tier=tier, sumInsured=sumInsured, tenure=tenure, noOfPeople = noOfPeople, totalRate=totalRate, discount=discount-totalRate )

