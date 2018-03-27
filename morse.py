from time import sleep
import pyautogui as py


def dot():
    py.hotkey('capslock')
    sleep(0.25)
    py.hotkey('capslock')
    sleep(0.25)


def dash():
    py.hotkey('capslock')
    sleep(0.75)
    py.hotkey('capslock')
    sleep(0.25)

def main():
    CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
            'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..',
            'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-',
            'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', ' ': ' ',

            '0': '-----', '1': '.----', '2': '..---',
            '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..',
            '9': '----.'
            }
    message = input('type your message: ')
    uppermessage = []
    for char in message:
        uppermessage.append(CODE[char.upper()])
    morse = str(uppermessage)
    for symbole in morse:
        if symbole == '.':
            dot()
        elif symbole == '-':
            dash()
        elif symbole == ' ':
            sleep(0.25)

main()
