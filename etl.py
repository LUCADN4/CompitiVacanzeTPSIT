def transform(legacy_data):
    new_data = {}
    for x, letters in legacy_data.items():
        for letter in letters:
            new_data[letter.lower()] = x
    return new_data