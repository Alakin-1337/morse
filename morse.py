# pylint: disable=missing-docstring

def decode(message):
    morse_dict = {"/": " ", ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G", "....": "H", "..": "I",".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z", "... --- ...": "SOS",}
    morses = message.replace('/', '')
    morses = message.split(" ")
    result = ""
    for key in morses:
        result += morse_dict.get(key) or ""
    return result

#sentence = decode(".- .-.. .-.. / -.-- --- ..- / -. . . -.. / .. ... / -.-. --- -.. .")
