alphabet = "EKSZJTCMXOQUDYLFABGPHNRVIW"
message = ""

with open("message.txt", "r") as f:
    file = f.read()

    for letter in file:
        if letter.islower():
            pos = alphabet.find(letter.capitalize())
            message += chr(pos + 97)
        elif letter.isupper():
            pos = alphabet.find(letter)
            message += chr(pos + 65)
        else:
            message += letter

print(message)