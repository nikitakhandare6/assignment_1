# #python program to find uncommon words from two strings
#
# s1=input("Enter the first string")
# s2=input("Enter the second string")
#
# list1=s1.split()
# list2=s2.split()
#
# for i in list1:
#     if(i not in list2):
#         print(i)


class parrot:
    def fly(self):
        print("parrot can fly")
    def swim(self):
        print("parrot can't fly")

class penguin:
    def fly(self):
        print("penguin can't fly)
    def swim(self):
        print("penguin can swim)

def fly_test(bird):
    bird.fly

pa=parrot()
pe=penguin()

fly_test(pa)
fly_test(pe)

