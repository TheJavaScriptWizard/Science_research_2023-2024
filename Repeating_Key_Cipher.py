import string

Alphabet = string.printable
Input = input("What is your message:")
Input2 = input("Put 1 for encode put anything else for decode:")
Input3 = input("What do you want your repeating key to be:")

def Cipher(String, Key, func):
    output = ""
    if func == "1":   
        for i in range(len(String)):
            Num_in_alphabet = Alphabet.index(String[i])
            if String[i] == " ":
                output = output + " "
            else:
                output = output + Alphabet[(Num_in_alphabet+Alphabet.index(Key[i%len(Key)]))%len(Alphabet)]
    else:
        for i in range(len(String)):
            Num_in_alphabet = Alphabet.index(String[i])
            if String[i] == " ":
                output = output + " "
            else:
                output = output + Alphabet[(Num_in_alphabet-Alphabet.index(Key[i%len(Key)]))%len(Alphabet)]
    return output

print(Input + " -> "+ Cipher(Input, Input3, Input2))

