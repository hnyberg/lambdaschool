import requests

dadata = {
    "name" : "Hannes",
    "lastname" : "Nyberg",
    "email" : "hannes.nyberg@gmail.com",
    "message" : "Love the course so far, good work!"
}

response = requests.post("https://lambdaschool.com/contact-form", json=dadata)

print(response.text)
