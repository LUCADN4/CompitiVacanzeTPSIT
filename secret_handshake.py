def commands(binary_str):
    shakes = ["wink", "double blink", "close your eyes", "jump"]
    handshake = []
    new_string = binary_str[::-1]
    for index, digit in enumerate(new_string):
        if (index == 4) and (digit == "1"):
            handshake.reverse()
            break
        elif digit == "1":
            handshake.append(shakes[index])
    return handshake
    