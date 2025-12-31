''' PASSWORD MANAGER '''


from cryptography.fernet import Fernet
import hashlib # Convert data → fixed-length fingerprint 
# code "word" → a1f0c... (always same output)
import os

# Create key if not exists
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file: # write in bytes 
        key_file.write(key)

# Load key 
#decryption stuff
def load_key():
    with open("key.key", "rb") as file:# read bytes
        return file.read()

# Ensure key file exists
if not os.path.exists("key.key"):
    write_key()

master_pwd = input("HEY THERE 😜 ! WHAT IS THE MASTER PASSWORD 🤔 -> ")

# 🔐 Derive a valid Fernet key
base_key = load_key()
key = hashlib.sha256(base_key + master_pwd.encode()).digest()
key = Fernet.generate_key()[:32]  # ensure length
fer = Fernet(Fernet.generate_key()) 

def view():
    if not os.path.exists("password.txt"):
        print("No passwords saved yet 😶")
        return

    with open("password.txt", "r") as f:
        for line in f.readlines():
            user, passw = line.rstrip().split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode()) # encode = convert srt to byte
            # decode -> bytes to str b'password' -> password
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("password.txt", "a") as f:# main one are 'w , r and a' 
            # w ->if it already exist it will overide  it , it make an entire one if file exist 
    # a -> (pend mode) it allow to add somthing to the end of existing file 
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
         # it will converts into bytes
while True:
    mode = input(
        "Would you like to add or view passwords? (add/view) or press q to quit 🤔: "
    ).lower()

    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("INVALID MODE 🤨")

