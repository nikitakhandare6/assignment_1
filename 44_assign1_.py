#python program to accept the strings which contain all vowels
string=input("enter the string")
string=string.lower()
vowels= ['a','e','i','o','u']
Absent =[]
for i in vowels:
    if i not in string:
        Absent.append(i)
if len(Absent)>=0 and len(Absent)<5:
        print("accepted")
else:
        print("not accepted")













# def check(string):
#     vowels =set("aeiou")                       #Initialize
#     dict1= set({})
#     for i in string :                          #iterations
#         if i in vowels :
#             dict1.add(i)
#         else:
#             pass
#
#         #output
#     if len(dict1)==len(vowels):
#             print("accepted")
#     else:
#             print("not accepted")
#
# str1= "welcome"
# check(str1)