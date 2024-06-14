# Functie om de console te wissen
def clear_screen():
    print("\n" * 50)

# Functie om het woord van de eerste speler te krijgen
def word():
    print('Speler 1: Voer een woord in: ')
    word_list = list(input().strip().lower())  # Invoer omzetten naar een lijst van kleine letters zonder spaties
    return word_list  # Geeft het ingevoerde woord terug als een lijst

# Functie om het spel te runnen
def game():
    word_list = word()  # Haal het woord van de eerste speler op
    guessed_letters = []  # Lijst om geraden letters bij te houden
    attempts = 9  # Aantal pogingen dat de tweede speler heeft

    clear_screen()  # Wis de console om het woord te verbergen

    while attempts > 0:  # Loop zolang er pogingen over zijn
        guess = input('Speler 2: Raad een letter: ').strip().lower()  # Vraag de tweede speler om een letter te raden

        clear_screen()  # Wis de console na elke invoer

        if guess in guessed_letters:  # Controleer of de letter al is geraden
            print('Je hebt deze letter al geraden.')
        elif guess in word_list:  # Controleer of de letter in het woord voorkomt
            guessed_letters.append(guess)  # Voeg de geraden letter toe aan de lijst
            print('Goed geraden!')
            print(f'Geraden letters: {guessed_letters}')  # Toon de lijst met geraden letters

            # Controleer of alle letters in het woord zijn geraden
            if set(word_list) <= set(guessed_letters):
                print(f'Gefeliciteerd! Je hebt het woord geraden, het woord was "{ "".join(word_list) }"')
                break  # Verlaat de loop als het woord is geraden
        else:
            attempts -= 1  # Verminder het aantal pogingen als de letter fout is
            print(f'Fout geraden, je hebt nog {attempts} pogingen over')

    # Als de pogingen op zijn, toon een verliesbericht
    if attempts == 0:
        print(f'Je hebt verloren. Het woord was "{ "".join(word_list) }"')

game()  # Start het spel
