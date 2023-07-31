# This program simulates the ROT13 Cryptography protocal
# essentially, it will take an input from the user, use ROT13 to encrypt it, then spit out the encrypted text. 
# the start menu will ask whether you'd like to encrypt or decrypt the text. 



#FUNCTION FOR ENCRYPTION: 
 # I seperated bewteen capital and lowercase using comparison operators
 # new char is calculted by taking the charecter, 
 # switching to unicode, then subtracting the amount it needs to be shifted which is the unicode for 'A" or 'a' (respectively) then add 13 to get the number subtracted for rotation. 
 # this results in the resulting new charecter as a rotation of ROT13
# the modulo %26 ensures that the chareters don't exceed a-z. 

def rot13(input_string):
    
    # since we're crypting entire strings, start with an empty string: 
    output_string = ""
    # loop through each charecter in the string:
    
    for char in input_string: 
    # uppercase 
            if 'A' <= char <= 'Z':
                newchar = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
    
    # lowercase 
            elif 'a' <= char <= 'z':
                newchar = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
    
    # this deals with charecters outside of ASCII 
            else:
                newchar = char
            output_string += newchar
    return output_string # return the final string.





# start menu: 

print("-------------------- ROT13.py ----------------------")
print("") 
print("")
# create a basic loop with a switch to run as many times as the user would like, print the results of ROT13:

run = True 
while run:
    input_string = input("Enter the message you'd like to encrypt/decrypt using ROT13: ")
    print("RESULT: ")
    print(rot13(input_string))
    switch = input("Would you like to run again? [Y/n]? ")
    switch = switch.lower()

    if switch == 'y':
        run = True
    if switch == 'n':
         run = False

