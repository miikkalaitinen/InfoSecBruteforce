import hashlib
import pandas as pd

df = pd.read_csv('hashes.csv').drop("Unnamed: 0", axis=1)

starting = int(input("Start reading from line:"))
def hash(password, salt):
    i: string = f"potPlantSalt{password}{salt}"
    h = hashlib.sha256(i.encode('utf-8')).hexdigest()
    return h[0:32]

counter = 0
print(hash("testi", "asd"))

def crack(password):
    for index, row in df.iterrows():
        h = hash(password, row["Salt"])
        r = row["Password"]
        u = row["User"]
        if h == row["Password"]:
          f = open("found.txt", "a")
          f.write('password is {} for user {}. \n'.format(password, u))
          f.close()
          print(f"User: {u}, Password: {password}")
        counter =+ 1
        if counter%10000 == 0:
          print(f"{counter} passwords processed")

lines = []
with open("rockyou.txt") as f:
    lines = f.read().splitlines()
lines = lines[starting:-1]
print(lines[0:5])

for line in lines:
  crack(line)

print("Ended")