import multiprocessing
import requests
import hashlib 
import random
import time
"""
program structure:
While game:
    thread1.getInput()
        => On Buzz
            -Get input
            -send to server

    thread2.getServerEvent():
        => On event():
            -Draw New Screen
"""
def h2(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

def get(i):
    r = requests.get(i)
    return r.text

name = input("Enter Username: ")
name_id = h2(name +str(time.time()) + str(random.randint(0,10000000)))

game = input("Would you like to joing a game? if so enter game id as int, if not enter a non int to make new game: ")
if game.isdigit():
    g = get("http://localhost:5000/games/{}/".format(game))
else:
    x =  int(get("http://localhost:5000/new"))
    print("your new game is {}".format(x))
    g = get("http://localhost:5000/games/{}/".format(x))

if g == "GAME NOT FOUND":
    print("Error, There is some error in getting/joining a game....")
    print("Quitting game...")
    exit(1)
else:
    
