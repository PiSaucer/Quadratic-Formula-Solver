import os
import math
import time
import cmath
from tkinter import*
from tkinter import messagebox
from tkinter import Tk, Menu
def clear(): print("\n" * 100)
def exit_box():
        exit_title = 'EXIT'
        exit_text = 'Do you want to EXIT?'
        answer = messagebox.askquestion(exit_title, exit_text, icon='warning')

        if answer == 'yes':
            print('Exit')
            time.sleep(3)
            exit()
        else:  # 'no'
            print('No Exit')
            time.sleep(3)
def menu():
    clear()
    print("-----------------------------------------------------")
    print("Welcome To the Quadratic Formula Solver")
    print("By: PiSaucer")
    print("ax^2 + bx + c = 0")
    print("To clear type: clear()")
    print("-----------------------------------------------------")
    a = float(input("Enter A:"))
    b = float(input("Enter B:"))
    c = float(input("Enter C:"))

    #calculate the discriminant
    d = (b**2) - (4*a*c)

    # find two solutions
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)

    #Answers
    print("The solution are {0} and {1}".format(sol1,sol2))
    time.sleep(2)

    #Restart
    print("Do you want to Calulate another formula?")
    choice = input("(y/n):")
    if choice == "y":
        print("LOADING...")
        time.sleep(2)
        menu()
    if choice == "n":
        print("EXITING...")
        time.sleep(3)
        exit_box()
#Starting Program
clear()
print("[              ]")
print("LOADING...")
time.sleep(1)
clear()
print("[|             ]")
print("LOADING ...")
time.sleep(1)
clear()
print("[||            ]")
print("LOADING...")
time.sleep(1)
clear()
print("[|||           ]")
print("LOADING ...")
time.sleep(1)
clear()
print("[||||          ]")
print("LOADING...")
time.sleep(1)
clear()
print("[|||||         ]")
print("LOADING ...")
time.sleep(1)
clear()
print("[||||||        ]")
print("LOADING...")
time.sleep(1)
clear()
print("[|||||||       ]")
print("LOADING ...")
time.sleep(1)
clear()
print("[||||||||      ]")
print("LOADING...")
time.sleep(1)
clear()
print("[|||||||||     ]")
print("LOADING ...")
time.sleep(1)
clear()
print("[||||||||||    ]")
print("LOADING...")
time.sleep(1)
clear()
print("[|||||||||||   ]")
print("LOADING ...")
time.sleep(1)
clear()
print("[||||||||||||  ]")
print("LOADING...")
time.sleep(1)
clear()
print("[||||||||||||| ]")
print("LOADING ...")
time.sleep(1)
clear()
print("[||||||||||||||]")
print("LOADING...")
time.sleep(2)
clear()
print("[||||||||||||||]")
print("DONE")
menu()
