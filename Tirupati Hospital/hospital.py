from tkinter import*
from tkinter import Tk
import random
import time 
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Tirupati Hospital")
        self.root.geometry("1540X800+0+0")

root=Tk()
ob = Hospital(root)        
root.mainloop()