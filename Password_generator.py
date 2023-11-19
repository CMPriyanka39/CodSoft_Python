#This code will generate the password
#But first it will hide and copies that password in clipboard
#Then ask you to maintain as hidden or you want to see that
import random
import string
import pyperclip

def generate_pas(length=8):
    char=string.ascii_letters+string.digits+string.punctuation
    passw=''
    for _ in range(length):
        passw+=random.choice(char)
    return passw

def toggle_hide(passw,hidden):
    if hidden:
        return "*"*len(passw)
    else:
        return passw

password=generate_pas()
print("Your Generated Password is :",toggle_hide(password,True))
pyperclip.copy(password)
input("The Password is copied to clipboard!!\n\nPress Enter")

hide_pass=input("Do you want to hide the password(Y/N): ".lower())
if hide_pass=="n":
      print("Your Generated Password is :",toggle_hide(password,False))
else:
    print("Your Generated Password is :",toggle_hide(password,True))

