shift = 0
entry = ''

def enter_text():
    global entry # make changes to the variable globally
    entry = input("Text to encrypt: ") # ask user to input string and assign to entry variable
    return entry # return the entry variable

def enter_shift():
    global shift # make changes to the variable globally
    while shift < 1 or shift > 25: # while the shift value is invalid
        shift = int(input("Enter a shift value from 1-25: ")) # ask user to enter new shift value
        if shift < 1 or shift > 25: # if the shift value is invalid
            print("Shift value is incorrect. Try again.") # advise user to re-enter
    return shift # return the shift variable

enter_text()
enter_shift()
for letter in entry: # iterate through each letter in the entry string
    if ord(letter) >=65 and ord(letter) <= 90: # check that letter is within uppercase constraint
        if (ord(letter) + shift) > 90: # if we cross the upperbound past the uppercase constraint
            overload_amount = (ord(letter) + shift) - 90 # assign the numerical value of how much we are crossing the bound
            non_overload = 65 + overload_amount - 1 # push back to the beginning of uppercase constrain while adding the extra amount
            print(chr(non_overload), end='') # print the resulting ASCII character
        else: # if we do not cross the upper bound 
            print(chr(ord(letter) + shift), end='') # print the shifted character
    elif ord(letter) >=97 and ord(letter) <= 122: # check that letter is within lowercase constraint
        if (ord(letter) + shift) > 122: # if we cross the upper bound past the lowercase constraint
            overload_amount = (ord(letter) + shift) - 122 # assign the numerical value of how much we are crossing the bound
            non_overload = 97 + overload_amount - 1 # push back to the beginning of lowercase constraint while adding the extra amount
            print(chr(non_overload), end='') # print the resulting ASCII character
        else: # if we do not cross the upper bound
            print(chr(ord(letter) + shift), end='') # print the shifted character
    else: # if the supposed letter is not uppercase or lowercase
        print(letter, end='') # print the supposed letter itself
print("\n")