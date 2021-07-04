#python program to check armstrong number
# i=int(input("Enter the number to check for armstrong"))
# orig=i
# sum=0
# while(i>0):
#     sum=sum+(i%10)*(i%10)*(i%10)
#     i=i//10
# if orig==sum:
#         print("number is armstrong")
# else:
#         print("number is not armstrong")

#second way
# n=int(input("enter the number \n"))
# sum=0
# order=len(str(n))
# copy_n=n
# while(n>0):
#     digit=n%10
#     sum+=digit**order
#     n=n//10
#     if(sum==copy_n):
#         print(f"{copy_n}is an armstrong number")
#     else:
#         print(f"{copy_n}is not an armstrong number")


#third way
for i in range(1001):
    num=i                          #i value store in num
    result=0
    n=len(str(i))
    while(i!=0):
        digit=i%10
        result=result+digit**n
        i=i//10
    if num==result:
        print(num)