import json

# Wrriting JSON data to a file
data = {
    "name": "Bishal Rijal",
    "age": 24,
    "city":"Chitwan",
    "hobbies": ["coding", "reading", "travelling"],
    "is_student": False,
    "school": "Green Society Public School",
    }

with open("data.json", "w") as file:
    json.dump(data, file, indent=4) # indent for pretty printing