# OneAssure
Built a backend project for OneAssure
## DELIVERABLES
1. CSV --> Mongo Db documents

2. setup a repo to provide rest APIs using flask and mongo 

    a. setup a flask repo 
    b. add connection to mongo
    c. create an api/function to load csv to mongo 

3. creating APIs
     
    a. i/p --> 
        sum insured(3L,4L,5L) , city(t1,t2), tenure(1,2,3), [age(0-90)] 

    b. logic -->  
        1. sort the ages desc  (30 , 20 , 10)
        2. get the rates for all the ages (query db)
        3. calculate the discounted price/premium
            a. total = rate of age1 + rate of age2 50%  + rate of age 3 50% and so on 
        4. then return this as premium to the user 

4. Make a frontend repo in html,css,javascript.

Steps 
