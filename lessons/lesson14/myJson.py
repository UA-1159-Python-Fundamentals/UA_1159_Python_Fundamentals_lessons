import json

json_string = """
{
"firstName": "Ivan", "lastName": "King",
"hobbies": ["reading", "traveling", "singing"],
"age": 33,
"children":
[
{
"firstName": "Vira",
"age":
3
},{
"firstName": "Maksym",
"age":
5
}
]
}
"""

from pprint import pprint

data= json.loads(json_string)
pprint(data, indent=4)

with open("lessons\\lesson14\\data\\in.json") as file:
    data= json.load(file)
    pprint(data, indent=4)



c = {
            "firstName": "Ihor",
            "age": 15
        }
data["children"].append(c)
pprint(data)
print(json.dumps(data))
with open("lessons\\lesson14\\data\\out.json", "w") as file:
   json.dump(data, file)
