import hashlib
from xmlrpc.client import boolean
import pandas as pd
from itertools import product

df = pd.read_csv('hashes.csv').drop("Unnamed: 0", axis=1)
start = int(input("Starting row (0 for first):"))
upperlimit = int(input("Upper limit:"))
df = df.iloc[start: , :]


def hash(password, salt):
    i = f"potPlantSalt{password}{salt}"
    h = hashlib.sha256(i.encode('utf-8')).hexdigest()
    return h[0:32]

def crack(salt, real, user):
    attempts = 0
    chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9"," ","!","?",".",",","*","_","-"]
    for password_length in range(1, upperlimit):
        print(password_length)
        for guess in product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if hash(guess, salt) == real:
                f = open("found.txt", "a")
                f.write('password is {} for user {}. found in {} guesses. \n'.format(guess, user, attempts))
                f.close()
                return 'password is {} for user {}. found in {} guesses.'.format(guess, user, attempts)

for index, row in df.iterrows():
    user = row["User"]
    print(f"Now cracking {user}")
    crack(row["Salt"],row["Password"], user)
