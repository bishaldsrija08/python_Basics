import json

data = '{"var1":"harry", "var2": "potter"}'
print(type(data))

parsed = json.loads(data)
print(type(parsed))


data2 = {
    "channel": "Digital Bishal",
    "cars": ["bmw", "audi", "ferrari"],
    "fridge": ("bhat", "chawal", 540),
    "isbad": False
}

# sort_keys: Sorts dictionary keys alphabetically
jscompacted = json.dumps(data2, sort_keys=True)
print(jscompacted)