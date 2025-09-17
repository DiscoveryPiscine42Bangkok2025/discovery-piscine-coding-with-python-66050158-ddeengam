def famous_births(figures):
    sorted_people = sorted(figures.values(), key=lambda x: x["date_of_birth"])
    for person in sorted_people:
        print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")

women_scientists = {
    "Karina": { "name": "Yoo Ji-min", "date_of_birth": "2000" },
    "Ningning": { "name": "Ning Yizhuo", "date_of_birth": "2002" },
    "Giselle": { "name": "Aeri Uchinaga", "date_of_birth": "2000" },
    "Winter": { "name": "Kim Min-jeong  ", "date_of_birth": "2001" }
}

famous_births(women_scientists)