# Jackson Weigand
# 9/21/21
# Random ceaser shift
import random


# alpha = "abcdefghijklmnopqrstuvwwyz ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
alpha = "5n3ofO9 LdeVNb7pEhYWFMGKwP cRgqXHjDQZJrBwuizIvs1T26mkSaUy4C8Atl"
# enc = "gkglkfgldfkglkklgkdfslgkerlgkkgmf"



# ct = int(input("shift value"))
# shiftalpha = alpha[ct:] + alpha[0:ct]
# print(shiftalpha)
def encode(message):
    for letter in message:
        print(alpha[encps.find(letter)], end="")
def decode(message):
    for letter in message:
        print(alpha[encps.find(letter)], end="")
def read(filename, key):
    file = open(filename)
    key = file.read()
    file.close()

def write(filename, key):
    file = open(filename, "w+")
    key = file.writelines(key)
    file.close()
encp = [] #create empty list

for letter in range(0,len(alpha)):
    encp.append(" ") #loads the list with spaces





# letter == random.randint(0, int(alpha - 1))
for i in range (0,len(alpha)-1):
    letter = random.randint(0, len(alpha) - 1)
    file = open("encp.txt", "a+")
    while encp[letter] != " ":
        letter = random.randint(0, len(alpha)- 1)
    encp[letter] = alpha[i]


print(encp)
encps = "".join(encp)
print(encps)


for letter in range(0,26):
   print(alpha[letter], "=", encps[letter])
task = input("encode or decode ")
if task.upper() == "DECODE":
    code = input("what do you want to decode ")
    decode(code)
elif task.upper() == "ENCODE":
    code = input("what do you wanna encode ")
    encode(code)