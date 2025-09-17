def array_of_names(persons):
    result = []
    for first, last in persons.items():
        fullname = first.capitalize() + " " + last.capitalize()
        result.append(fullname)
    return result

persons = {
    "peter": "paarker",
    "human": "dexter",
    "xavier": "kamanda",
    "cute": "lingganggoo"
}

print(array_of_names(persons))