vowles = {
    'a' : 0,
    'e' : 0,
    'i' : 0,
    'o' : 0,
    'u' : 0
}

def count_vowels(string):
    return string.count("a") + string.count("e") + string.count("i") + string.count("o") + string.count("u")

print(count_vowels("Emiliano"))