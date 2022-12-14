import hashlib
from xmlrpc.client import boolean
import pandas as pd
from itertools import product

df = pd.read_csv('hashes.csv').drop("Unnamed: 0", axis=1)
start = int(input("Starting row (0 for first):"))
lowerlimit = int(input("Starting lenght:"))
upperlimit = int(input("Upper limit:"))
amountofnumbers = int(input("Amount of suffix numbers: "))
df = df.iloc[start: , :]
set = (input("Select set: \nlowerase=1\nuppercase=2\nnumbers=3\nspecial=4\n\nAnswer as cobination as string e.g. 123: "))
res = [int(x) for x in str(set)]
#chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"," ","!","?",".",",","*","_","-"]
numsAndSpecial = ["1","2","3","4","5","6","7","8","9","0"," ","!","?",".",",","*","_","-"]
bigChars = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
chars = []
if 1 in res:
    chars += ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
if 2 in res:
    chars += ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
if 3 in res:
    chars += ["1","2","3","4","5","6","7","8","9","0"]
if 4 in res: 
    chars += [" ","!","?",".",",","*","_","-"]

print(chars)

def hash(password, salt):
    i = f"potPlantSalt{password}{salt}"
    h = hashlib.sha256(i.encode('utf-8')).hexdigest()
    return h[0:32]

def crack(salt, real, user):
    for password_length in range(lowerlimit, upperlimit):
        print(password_length)
        for big in product(bigChars, repeat=1):
            big = "".join(big)
            for guess in product(chars, repeat=password_length):
                str = ''.join(guess)
                for num in product(numsAndSpecial, repeat=amountofnumbers):
                    num = ''.join(num)
                    guess = big + str + num
                    if hash(guess, salt) == real:
                        f = open("found.txt", "a")
                        f.write('password is {} for user {}. \n'.format(guess, user))
                        f.close()
                        print('password is {} for user {}.'.format(guess, user))
                        return 0

for index, row in df.iterrows():
    user = row["User"]
    print(f"Now cracking {user}")
    crack(row["Salt"],row["Password"], user)
