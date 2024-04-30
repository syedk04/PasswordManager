from cryptography.fernet import Fernet # Module that allows us to encrpyt text

#this function was used to create the encrypted key.key file. But since we only want it to run once after key.key was created it was commented out
"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) """
        
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("Enter Master Password: ")
key = load_key() # encode: takes string and turns it into bytes... could also use .bytes()
fer = Fernet(key)

def view():
    with open("passwords.txt", "r") as f: # using with will close the file automatically after it is done being created 
        for line in f.readlines(): #read all lines
            data = line.rstrip()
            user, passw = data.split("|") # assigns first element to user, then second element to passw
            print("User: ", user, "| Password: ", fer.decrypt(passw.encode())) # decrypted password when viewing

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    # three main types of opening file, "w" "r" "a": w rewrites file, r is a file that can only be read, a is a file that adds info onto a file that exists or if it doesn't exist then creates file and adds info
    # file = open() --> file.close() is another way to open a file and close but it is the long way as you need to close
    with open("passwords.txt", "a") as f: # using with will close the file automatically after it is done being created 
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n")
     
while True:
    mode = input("Would you like to add password (add) or view existing password (view)? To exit press 'x' ").lower() #turns user input into lower case
    if mode == "x":
        break # quit() works
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Enter a valid option. View or Add")
        continue # can only be used with a loop