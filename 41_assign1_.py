#python ways to remove "i" th character from given string
s=input("enter the string")
n=int(input("enter the value of i"))

a=s[0:n-1]
b=s[n:]

print("resultant string is=",a+b)

#using for loop
# string1 = input("enter the string:")
# n = int(input("enter the i th value :"))
# new_string = ""
# for i in range(len(string1)):
#     if i==n:
#         continue
#     else:
#         new_string = new_string + string1[i]
#         print("your new string is :",new_string)