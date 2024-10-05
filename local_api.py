import json
import requests

# TODO: send a GET using the URL http://127.0.0.1:8000
url = 'http://127.0.0.1:8000'
url2 = requests.get(url)
 # Your code here

# TODO: print the status code
print(f"Status Code: {url2.status_code}")

response_json = url2.json()

# TODO: print the welcome message
print(f"Result: {response_json}")


data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# TODO: send a POST using the data above
url_data = 'http://127.0.0.1:8000/data/'
 
re = requests.post(url_data, json = data)

# TODO: print the status code
print("Status code: ", re.status_code)

# TODO: print the result
print(re.json())
