import random
print("***** WELCOME TO PASSWORD GENERATOR *****")
upperalpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
loweralpha = 'abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'
specialchar = '!@#$%^&*'
all = upperalpha + loweralpha + numbers + specialchar
length = int(input("Enter the length of password:"))
print("Any specifications? (yes/no)")
option = input()
list1 = []
if option == 'yes':
    upalph = int(input("Specify the no.of uppercase alphabets: "))
    lowalph = int(input("Specify the no.of lowercase alphabets: "))
    num = int(input("Specify the no.of digits: "))
    spclchar = int(input("Specify the no.of special characters: "))
    if upalph+lowalph+num+spclchar != length:
        print("Your specifications do not match the length of password.Do you want to continue?")
        inp = input()
    if inp == 'yes':
        for i in range(0,upalph):
            list1.append(random.choice(upperalpha))
        for j in range(0,lowalph):
            list1.append(random.choice(loweralpha))
        for k in range(0,num):
            list1.append(random.choice(numbers))
        for l in range(0,spclchar):
            list1.append(random.choice(specialchar))
    else:
        for i in range(0,length):
            list1.append(random.choice(all))
else:
    for i in range(0,length):
            list1.append(random.choice(all))
random.shuffle(list1)
password = ''
for i in range(0,len(list1)):
    password += list1[i]
print("Your Customized Password: ",password)


