print("Enter a character:")
char = input()

if (char.isupper() == True):
    print(char, " is a upper case letter.")
elif (char.islower() == True):
    print(char, " is an lower case letter.")
elif (char.isdigit() == True):
    print(char, " is a digit.")
else:
    print(char, " is a non-alphanumeric character.")
