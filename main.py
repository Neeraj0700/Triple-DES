import tkinter as tk
from tkinter import messagebox
from tkinter import *
import os
from twilio.rest import Client
import random

root = tk.Tk()
root.config(bg="peach puff")
Title = root.title("Triple DES")
root.geometry('400x200')
root.resizable(0, 0)

def verifyOTP():
	userinput = int(otp.get())
	if userinput==n:
		messagebox.showinfo("showinfo","Login Success")
	else:
		messagebox.showinfo("showinfo","Wrong OTP")


def adminwindow():
	root1 = tk.Toplevel(root)
	root1.config(bg="peach puff")
	root1.title("Triple DES")
	root1.geometry('400x200')
	root1.resizable(0, 0)
	global n
	global otp 
	global username
	global password
	otp=StringVar()
	username=StringVar()
	password=StringVar()
	n = random.randint(1000,9999)
	account_sid = 'ACd138af6647dbc2811972df9bae2815fe'
	auth_token = 'fd5b366509aa4af1c5384718dae52e07'
	client = Client(account_sid, auth_token)
	message = client.messages \
    .create(
         body=n,
         from_='+18645138747',
         to='+919354433899'
    )

	label1 = Label(root1, text = " Enter Username :",  background = 'salmon', foreground ="white", font = ("Times New Roman", 11),anchor=N)
	label1.place(x=10,y=50)

	l1 = tk.Entry(root1, textvariable = username, width = 31)
	l1.place(x=150,y=50)

	label2 = Label(root1, text = " Enter Password :",  background = 'salmon', foreground ="white", font = ("Times New Roman", 11),anchor=N)
	label2.place(x=10,y=80)

	l2 = Entry(root1,textvariable = password, show='*', width = 31)
	l2.place(x=150,y=80)

	label3 = Label(root1, text = " Enter OTP :",  background = 'salmon', foreground ="white", font = ("Times New Roman", 11),anchor=N)
	label3.place(x=10,y=110)

	l3 = tk.Entry(root1,textvariable = otp, width = 31)
	l3.place(x=150,y=110)

	loginButton = Button(root1, text="Login", command=verifyOTP, bg='salmon', fg='white', font=("Times New Roman", 14), borderwidth=0, relief="sunken")
	loginButton.place(x=175,y=150)


def userwindow():
	root2 = tk.Toplevel(root)
	root2.config(bg="peach puff")
	Title = root2.title("Triple DES")
	root2.geometry('400x200')
	root2.resizable(0, 0)
	global otp1 
	global username1
	global password1
	otp1=StringVar()
	username1=StringVar()
	password1=StringVar()
	n = random.randint(1000,9999)
	account_sid = 'ACd138af6647dbc2811972df9bae2815fe'
	auth_token = 'fd5b366509aa4af1c5384718dae52e07'
	client = Client(account_sid, auth_token)
	message = client.messages \
    .create(
         body=n,
         from_='+18645138747',
         to='+919354433899'
    )

	label1 = Label(root2, text = " Enter Username :",  background = 'salmon', foreground ="white", font = ("Times New Roman", 11),anchor=N)
	label1.place(x=10,y=50)

	l1 = tk.Entry(root2, textvariable = username1, width = 31)
	l1.place(x=150,y=50)

	label2 = Label(root2, text = " Enter Password :",  background = 'salmon', foreground ="white", font = ("Times New Roman", 11),anchor=N)
	label2.place(x=10,y=80)

	l2 = Entry(root2,textvariable = password1, show='*', width = 31)
	l2.place(x=150,y=80)

	label3 = Label(root2, text = " Enter OTP :",  background = 'salmon', foreground ="white", font = ("Times New Roman", 11),anchor=N)
	label3.place(x=10,y=110)

	l3 = tk.Entry(root2,textvariable = otp1, width = 31)
	l3.place(x=150,y=110)

	loginButton = Button(root2, text="Login", command=verifyOTP, bg='salmon', fg='white', font=("Times New Roman", 14), borderwidth=0, relief="sunken")
	loginButton.place(x=175,y=150)



label = Label(root, text = " Implementation of Triple DES ",  background = 'salmon', foreground ="white", font = ("Times New Roman", 15),anchor=N)
label.place(x=70,y=20)

adminButton = Button(root, text=" Admin ", command=adminwindow, bg='salmon', fg='white', font=("Times New Roman", 14), borderwidth=0, relief="sunken")
adminButton.place(x=10,y=80)

userButton = Button(root, text=" Customer ", command=userwindow, bg='salmon', fg='white', font=("Times New Roman", 14), borderwidth=0, relief="sunken")
userButton.place(x=295,y=80)

root.mainloop();