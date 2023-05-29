def remainingwords():
    phrase=input()
    space=phrase.find(" ")
    print(phrase[space+1:])

remainingwords()
