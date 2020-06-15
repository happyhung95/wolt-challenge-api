### Task
>
>Create a REST API endpoint that allows searching restaurants. API needs to accept three parameters:  
>- q: query string.  
(Full or partial match for the string is searched from name, description and tags fields. A minimum length for the query string is one character.)  
>- lat: latitude coordinate (customer's location)
>- lon : longitude coordinate (customer's location)  
>API should return restaurant (objects) which match the given query string and are closer than 3 kilometers from coordinates.  
>
>Example query:
>
>/restaurants/search?q=sushi&lat=60.17045&lon=24.93147  
This search would return restaurants (in JSON format) which contain a word sushi and are closer than 3km to the point (60.17045, 24.93147).
>
>Please do not use any on-disk database (MySQL, PostgreSQL, ...) or ElasticSearch in this assignment. The task can be completed without them.

### Hung's API
The API was written in Python 3.8 with Django framework.  
The main codes are in /Wolt_app/methods.py  


Required packages:
- Django  
- Geopy  

Instruction for testing the API:
1. Open the folder in terminal.  
(or change directory to the folder in Terminal) 
2. Install Django and Geopy by command:  
`pip install -r requirements.txt`   
OR run these commands separately:  
`pip install django`  
`pip install geopy`

3. Run local server by command:  
`python manage.py runserver`
4. Test the API by opening [localhost:8000](http://localhost:8000/) in browser.
5. Copy and paste some URLs given in the homepage.

*Note: the API also returns the number of restaurants found outside 3km 
search range, if there are no matches found inside the range.*  
  
Hung Nguyen
