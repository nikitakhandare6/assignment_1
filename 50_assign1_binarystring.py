#python program to find the given string is binary or not
# s=input("Enter the binary string")
# set1=set(s)
# p={'1','0'}
#if (set1==p or set1=={'1'} or set1=={'0'}):
#     print("string is binary")
# #else:
#     print("string is not binary")

# stri = input('Enter string ')
# stri = set(stri)
# bin=['0','1']
# flag = 0
# for i in stri:
#     if i in bin:
#        flag = 0
#     else:
#         flag = 1
#
#
# if flag == 0:
#     print("binary")
# else:
#     print("not binary")

stri = input('Enter string ')
stri = set(stri)
bin={'0','1'}
if stri==bin:
    print('This is binary')
else:
    print('This is not bibnary')
