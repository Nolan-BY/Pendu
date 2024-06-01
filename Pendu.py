"""
Projet de pendu en Python
24/09/2022 - 22h59
"""

from PenduClasses import WordGuess

def Game():
    print("Bienvenue dans le jeu du pendu !\n")
    while True:
        try:
            choice = str(input("Entrez un mode de difficulté (F pour Facile, D pour Difficile et Q pour Quitter) : ")).upper()
            if len(choice) > 1 or choice not in ["F", "D", "Q"]:
                raise ValueError
        except ValueError:
                print("\nERREUR ! Veuillez ne renseigner que F pour Facile, D pour Difficile ou Q pour Quitter !")
        else:
            if choice in ["F", "D"]:
                guesser = WordGuess()
                guesser.ChooseWord()
                print(guesser.rules(choice))
                print("\n" + ' '.join(guesser.get_display()))
                while len(guesser.get_good_guesses()) != len(guesser.get_word()) and guesser.get_pendu() != 10:
                    try:
                        guess = str(input("\nEntrez une lettre : ")).lower()
                        if len(guess) > 1 or guess.isalpha() == False:
                            raise ValueError
                    except ValueError:
                        print("\nERREUR ! Veuillez ne renseigner qu'une seule lettre !")
                    else:
                        print(guesser.Guess(choice, guesser.get_word(), guess))

        if len(guesser.get_good_guesses()) == len(guesser.get_word()) and guesser.get_pendu() != 10:
            print("\nBravo vous avez trouvé !")
            print("\nLe mot était : " + guesser.get_original_word())
            print("Définition : " + guesser.get_word_definition())
            print("\nMerci d'avoir joué et à bientôt !")
            break

        elif len(guesser.get_good_guesses()) != len(guesser.get_word()) and guesser.get_pendu() == 10:
            print("\nDommage, vous avez perdu !")
            print("\nLe mot était : " + guesser.get_original_word())
            print("Définition : " + guesser.get_word_definition())
            print("\nMerci d'avoir joué et à bientôt !")
            break
        else:
            print("\nMerci d'avoir joué et à bientôt !")
            break

if __name__ == "__main__":
    Game()