def is_isogram(string):
    lettere = [c.lower() for c in string if c.isalpha()]
    return len(set(lettere)) == len(lettere)
