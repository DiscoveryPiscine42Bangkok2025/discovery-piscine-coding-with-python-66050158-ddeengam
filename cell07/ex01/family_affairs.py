def find_the_redheads(family):
    redheads = filter(lambda name: family[name] == "red", family)
    return list(redheads)

dupont_family = {
    "lungtu": "red",
    "unging": "blond",
    "anuthin": "brunette",
    "bigpom": "red",
    "srettha": "red"
}

print(find_the_redheads(dupont_family))