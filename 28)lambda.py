people = [
    {"name":"Harry", "house":"Gryffindor"},
    {"name":"Cho","house":"Ravenclaw"},
    {"name":"Draco","hosue":"Slytherin"}
]

people.sort(key=lambda person: person["name"])

print(people)
