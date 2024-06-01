"""
Projet de pendu en Python
24/09/2022 - 22h59
"""

from randomwordfr import RandomWordFr
import unidecode

class WordGuess():
    def __init__(self) -> None:
        self.__guesses = []
        self.__good_guesses = []
        self.__pendu = 0
        self.__original_word = ""
        self.__word = ""
        self.__word_definition = ""
        self.__display = []

    def ChooseWord(self):
        word = RandomWordFr().get()
        self.__original_word = word['word']
        self.__word_definition = word['definition']
        self.__word = unidecode.unidecode(self.__original_word).lower()
        for n in range(len(self.__word)):
            self.__display.append("_")

    def Guess(self, difficulty, word, letter):
        self.__windex = []
        if difficulty == "F":
            if letter not in self.__guesses:
                if letter in word:
                    for pos, char in enumerate(word):
                        if char == letter:
                            self.__windex.append(pos)
                            self.__good_guesses.append(letter)
                            for i in self.get_windex():
                                self.set_display_letter(i, letter)
                                self.__guesses.append(letter)
                    return("\n\nLettres utilisées : " + ", ".join(self.get_guesses()) + "\n" + " ".join(self.get_display()) + "\n")
                else:
                    self.__guesses.append(letter)
                    self.set_pendu(self.get_pendu() + 1)
                    return(self.affiche_pendu() + "\nLa lettre " + letter + " n'est pas dans le mot !\n\n" + "Lettres utilisées : " + ", ".join(self.get_guesses())     + "\n\n" + " ".join(self.get_display()) + "\n")
            else:
                return(self.affiche_pendu() + "\nVous avez déjà demandé la lettre " + letter + " !\n\n" + "Lettres utilisées : " + ", ".join(self.get_guesses()) + "\n\n" + " ".join(self.get_display()) + "\n")

        elif difficulty == "D":
            if letter not in self.__guesses:
                if letter in word:
                    self.__windex.append(word.find(letter))
                    for i in self.get_windex():
                        self.set_display_letter(i, letter)
                        self.__guesses.append(letter)
                        self.__good_guesses.append(letter)
                        return("\n" + " ".join(self.get_display()) + "\n")
                else:
                    self.__guesses.append(letter)
                    self.set_pendu(self.get_pendu() + 1)
                    return(self.affiche_pendu() + "\nLa lettre " + letter + " n'est pas dans le mot !\n\n" + " ".join(self.get_display()) + "\n")
            else:
                if letter in word:
                    for pos, char in enumerate(word):
                        if char == letter:
                            self.__windex.append(pos)
                            if self.__good_guesses.count(letter) < len(self.__windex):
                                self.set_display_letter(self.__windex[self.__good_guesses.count(letter)], letter)
                                self.__guesses.append(letter)
                                self.__good_guesses.append(letter)
                                return("\n" + " ".join(self.get_display()) + "\n")
                        else:
                            self.set_pendu(self.get_pendu() + 1)
                            return(self.affiche_pendu() + "\nLa lettre " + letter + " est déjà complètement révélée !\n\n" + " ".join(self.get_display()) + "\n")
                else:
                    self.set_pendu(self.get_pendu() + 1)
                    return(self.affiche_pendu() + "\nLa lettre " + letter + " n'est pas dans le mot !\n\n" + " ".join(self.get_display()) + "\n")


    def rules(self, difficulty):
        if difficulty == "F":
            return ("\nVous êtes dans le mode facile !"
    "\nSi une lettre apparaît plusieurs fois dans le mot, elle sera complètement révélée."
    "\nToutes les lettres essayées seront montrées avant chaque essai."
    "\nAucune erreur ne sera comptée pour avoir essayé une lettre plus d'une fois.")
        elif difficulty == "D":
            return ("\nVous êtes dans le mode difficile !"
    "\nSi une lettre apparaît plusieurs fois dans le mot, seule la première ou celle suivante sera révélée."
    "\nLes lettres essayées ne seront pas montrées avant chaque essai."
    "\nUne erreur sera comptée pour avoir essayé une lettre plus d'une fois.")

    def get_guesses(self):
        return self.__guesses

    def set_guesses(self, g):
        self.__guesses = g

    def get_good_guesses(self):
        return self.__good_guesses

    def set_good_guesses(self, gg):
        self.__good_guesses = gg

    def get_windex(self):
        return self.__windex

    def set_windex(self, wi):
        self.__windex = wi

    def affiche_pendu(self):
        return ("\nVous êtes actuellement à " + str(self.__pendu) + "/10 erreurs !")

    def get_pendu(self):
        return self.__pendu

    def set_pendu(self, p):
        self.__pendu = p

    def get_word(self):
        return self.__word

    def set_word(self, w):
        self.__word == w

    def get_original_word(self):
        return self.__original_word

    def set_original_word(self, ow):
        self.__original_word == ow

    def get_word_definition(self):
        return self.__word_definition

    def set_word_definition(self, wd):
        self.__word_definition == wd

    def get_display(self):
        return self.__display

    def set_display(self, disp):
        self.__display = disp

    def set_display_letter(self, index, let):
        self.__display[index] = let