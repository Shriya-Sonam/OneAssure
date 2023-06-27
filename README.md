## OneAssure
Built a backend project for OneAssure

# Screenshots

<img width="397" alt="Screenshot 2023-06-27 231510" src="https://github.com/Shriya-Sonam/oneAssure/assets/86159436/dc61cb3e-4c83-41ca-b1fc-df4dfa108adf">

# DELIVERABLES
1. CSV --> Mongo Db documents

2. setup a repo to provide rest APIs using flask and mongo 

    a. setup a flask repo
   
    b. add connection to mongo
   
    c. create an api/function to load csv to mongo 

4. creating APIs
     
    a. i/p -->
   
        sum insured(3L,4L,5L) , city(t1,t2), tenure(1,2,3), [age(0-90)] 

    b. logic -->
   
        1. sort the ages desc  (30 , 20 , 10)
   
        2. get the rates for all the ages (query db)
   
        3. calculate the discounted price/premium
            a. total = rate of age1 + rate of age2 50%  + rate of age 3 50% and so on
   
        4. then return this as premium to the user 

6. Make a frontend repo in html,css,javascript in (VS Code):
   
   a. Install Node.js
   
   b. Install the VS Code editor

7. Make the backend in flask using mongodb as the database:
   
   a. Install Python
   
   b. Install Flask: Run the following command to install Flask:
      pip install Flask
   
   c. Install pymongo:
      pip install pymongo
   
   d. Install Flask-PyMongo: Flask-PyMongo is a Flask extension that simplifies MongoDB integration with Flask. 
      pip install Flask-PyMongo
   
   e. Install MongoDB
   
   f. Connect Flask to MongoDB
   


