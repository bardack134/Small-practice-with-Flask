from datetime import datetime
from flask import Flask, render_template
import requests

app = Flask(__name__)


def current_year():
    year = str(datetime.now().year)
    
    print(year)
    
    return year


def gender_API(username):
    
    parameters={
      "name":username 
    }
    
    response= requests.get('https://api.genderize.io', params=parameters)
    
    response_json = response.json()
    
    print(response_json)
    
    gender=response_json['gender']
    
    print(gender)
    
    return gender
    
    
def age_api(username):
       
    parameters={
      "name":username
    }
    
    response= requests.get('https://api.agify.io', params=parameters)
    
    response_json = response.json()
    
    print(response_json)
    
    age=response_json['age']
    
    print(age)
    
    return age 


  
@app.route("/<username>")
def hello_world(username):
    
    year=current_year()
    
    
    mygender=gender_API(username)
    
    
    myage=age_api(username)
    
    
    return render_template('index.html', year=year, name=username, gender=mygender, age=myage)



if __name__ == '__main__':
    
    app.run(debug=True)