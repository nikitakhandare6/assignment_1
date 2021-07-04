#python program to check if string is pallindrome or not reverse words in a given string
a=input("enter string")
b=a[::-1]
if (a==b):
    print("pallindrome string")
else:
    print("not pallindrome string")