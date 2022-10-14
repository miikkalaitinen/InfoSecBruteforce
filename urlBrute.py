# http://cdn1.vikaa.fi:52645/photos/0421ed56/8131b1005f7ed492ffff010b00003420.png
# http://cdn1.vikaa.fi:52645/photos/0421ed56/8131b1005f7e???ffff010b000034??.png

import requests
from itertools import product

r = requests.get("http://cdn1.vikaa.fi:52645/photos/0421ed56/8131b1005f7ed492ffff010b00003420.png")

print(r.status_code)
# print(r.headers)

chars = []
chars += ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
chars += ["1","2","3","4","5","6","7","8","9","0"]
nums = ["1","2","3","4","5","6","7","8","9","0", "a"]

first = ["c","d","e","f","g","h"]
for fs in product(first, repeat=1):
    f = "".join(fs)
    for guess in product(nums, repeat=3):
        str = ''.join(guess)
        for num in product(nums, repeat=2):
            lsdgfg = ''.join(num)
            get = "http://cdn1.vikaa.fi:52645/photos/0421ed56/8131b1005f7e" + f + str + "ffff010b000034"+ lsdgfg + ".png"
            print(get)
            r = requests.get(get)
            print(r.status_code)
            if r.status_code == 200:
                print(r.status_code)
                print(r.headers)
                print(guess)
                f = open("foundurlss.txt", "a")
                f.write('url is {} \n'.format(get))
                f.close()