import json
import random
import string
import logging

#importando la libreria para el loggin
logging.basicConfig(level=logging.DEBUG)

#Abriendo el archivo.json

def open_json():
    """"
    Devuelve un diccionario con los datos del archivo json
    """
    with open('words.json') as file:
        data = json.load(file)
        return data

#Seleccionando una palabra al azar
def selec_word():
    """"
    Devuelve una palabra al azar del archivo json
    """
    words = open_json()
    words = random.choice(list(words.values()))
    word = random.choice(words)
    return word.lower()

#Verificación de la palabra
def word_complete(secret_word, selec_letters):
    """"
    Devuelve True si la palabra esta completa
    """
    for letter in secret_word:
        if letter not in selec_letters:
            return False
    return True

#La solución como cadena

def solution(secret_word,selec_letters):
    """"
    Devuelve la solución como cadena
    """
    solution = ""
    for letter in secret_word:
        if letter in selec_letters:
            solution += letter
        elif letter == " ": #si es un espacio
            solution += " "
        else:
            solution += "_ "
    return solution

def letter_available(selec_letters):
    """"
    Devuelve las letras disponibles
    """
    letters_available = ""

    for letter in (string.ascii_lowercase+"ñ"+"1"+"2"+"3"+"4"+"5"+"6"+"7"+"8"+"9"+"0"):
        if letter not in selec_letters:
            letters_available += letter

    return letters_available

#letra incorrecta
def incorrect_letter(attempts, solution):


    attempts -=1

    print(f"Incorrecto, esa letra no esta en la palabra {solution}")

    return attempts

def drawing(attempts):
    stages = ["""
                       --------
                       |      |
                       |      O
                       |     \|/
                       |      |
                       |     / \  
                       -
                    """, """
                       --------
                       |      |
                       |      O
                       |     \|/
                       |      |
                       |     / 
                       -
                    """, """
                       --------
                       |      |
                       |      O
                       |     \|/
                       |      |
                       |      
                       -
                    """, """
                       --------
                       |      |
                       |      O
                       |      |
                       |      |
                       |     
                       -
                    """, """
                       --------
                       |      |
                       |      O
                       |      |
                       |      
                       |     
                       -
                    """, """
                       --------
                       |      |
                       |      O
                       |      
                       |      
                       |     
                       -
                    """]
    print(stages[attempts])

#comienza el juego

def star_game_hangman(secret_word):

    """"
    Comienza el juego
    """
    print("--------------------")
    print("Bienvenido al juego del ahorcado")
    print("Tienes 5 intentos para adivinar la palabra")
    print("Buena suerte")
    print("--------------------")

    selec_letters = []
    attempts = 5

    while not word_complete(secret_word, selec_letters) and attempts > 0:
        print("--------------------")
        print("Intentos restantes:", attempts)
        print("Letras disponibles:", letter_available(selec_letters))
        print("Solución:", solution(secret_word, selec_letters))
        drawing(attempts)
        print("--------------------")
        letter = input("Ingrese una letra: ").lower()

        if len(letter) ==1:
            if letter in selec_letters:
                print("Ya ingresaste esa letra")
            elif letter not in (string.ascii_lowercase+"ñ") \
                    and letter not in ["0","1","2","3","4","5","6","7","8","9"]:
                print("Caracter no válida")
            elif letter in secret_word:
                print("--------------------")
                print("Correcto!!!")
                print("--------------------")
                selec_letters.append(letter)
                print("Solución:", solution(secret_word, selec_letters))
            elif letter not in secret_word:
                selec_letters.append(letter)
                attempts = incorrect_letter(attempts, solution(secret_word, selec_letters))
            if solution(secret_word, selec_letters) == secret_word:
                print("Ganaste")
                break
        else:
            print("Ingrese una sola letra o número")
    if attempts == 0:

        print("--------------------")
        drawing(attempts)
        print("GAME OVER")
        print("La palabra era:", secret_word)
        print("Prueba de nuevo :D ")

def start_game():
    """
    Menú del juego
    """
    out = True
    while out:
        try:

            print("--------------------")
            print("Bienvenido al menú del juego :D ")
            print("""
                1. Jugar
                2. Salir""")
            alternative = int(input("\nEscriba el número de la opción que desea: "))
            if alternative == 1:
                star_game_hangman(selec_word())
            elif alternative == 2:
                print("--------------------")
                print("Gracias por jugar :D ")
                print("Vuelva PRONTO")
                out = False
        except ValueError:
            logging.warning("Ingrese una opción válida")

start_game()