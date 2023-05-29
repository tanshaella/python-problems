print("Enter an odd length string:")

text=input()
length=int(len(text)/2)
print("Middle character:", text[int(len(text)/2)])
print("First half:", text[:int(len(text)/2)])
print("Second half:", text[length+1:])
