def multiple_upcase_it(words):
    result = []
    for w in words:
        result.append(w.upper())
    return result

print(multiple_upcase_it(["hello", "world", "python"]))