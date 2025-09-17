def average(scores):
    total = 0
    count = 0
    for value in scores.values():
        total += value
        count += 1
    return total / count

class_3B = {
    "gooddy": 18,
    "jenny": 15,
    "sane": 8,
    "fah": 9
}

class_3C = {
    "ning": 15,
    "karina": 20,
    "winter": 18,
    "giselle": 16,
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")