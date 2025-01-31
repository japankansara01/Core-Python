import json

# Open and read from JSON file
#with open("data.json", "r") as file:
  #  data = json.load(file)
#    print(data)

# Open and write JSON file
data = {
    "name": "Japan",
    "age": 22,
    "city": "Nadiad"
}
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)  # Pretty-print JSON