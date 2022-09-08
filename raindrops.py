goccie = {3: 'Pling',5: 'Plang',7: 'Plong'}
def convert(number):
    s = ""
    for k, v in goccie.items():
        if number % k == 0:
            s += v
    return s or str(number)

print(convert(1))