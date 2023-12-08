#Ceaser_Cipher
import string

Alphabet = string.printable
Input = input("enter sentance:")
Input2 = input("Put 1 for encode put anything for otherwise:")
Input3 = input("How many do you want to shift by, numbers only:")
String_Num_of_Letters = len(Input)-1

def Shift(String, Shift_By, func):
    output = ""
    if func == "1":   
        for i in range(len(String)):
            Num_in_alphabet = Alphabet.index(String[i])
            if String[i] == " ":
                output = output + " "
            else:
                output = output + Alphabet[(Num_in_alphabet+Shift_By)%len(Alphabet)]
    else:
        for i in range(len(String)):
            Num_in_alphabet = Alphabet.index(String[i])
            if String[i] == " ":
                output = output + " "
            else:
                output = output + Alphabet[(Num_in_alphabet-Shift_By)%len(Alphabet)]
    return output

print(Input + " -> "+ Shift(Input, int(Input3), Input2))

