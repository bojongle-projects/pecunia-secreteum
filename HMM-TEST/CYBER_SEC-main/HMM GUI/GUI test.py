from cProfile import label
from distutils.cmd import Command
from mailbox import Mailbox
from msilib import Win64
from struct import pack
import tkinter
from tkinter import *
from turtle import back, width


def project_jedi_func():
    global project_jedi_func
    win12 = Toplevel(MAIN_PAGE)
    win12.geometry("600x600")
    win12.configure(bg="Red")
    win12.title("Project Jedi")
    win12.resizable(True, True)
    win12_l1 = Label(win12, text="Project Jedi", bg="Red", fg="Black", font=("Roboto Mono", 30))
    win12_l2 = Label(win12, text="Project Jedi seeks to make fucking with 'tHE cAmERa IsnT tHaT bAD' mfs a lot easier", bg="Red", fg="Black", font=("Roboto Mono", 30))
    win12_but1 = Button(win12, text="Download .exe", command=utiligram_func2)

    win12_l1.pack()
    win12_l2.pack()
    win12_but1.pack()
    win12.mainloop()



def utiligram_func2():
    global utiligram_func2
    win11 = Toplevel(Utiligram_Func)
    win11.geometry("600x600")
    win11.configure(bg="Blue")
    win11.title("Utiligram")
    win11.resizable(True, True)
    win11_l1 = Label(win11, text="Utiligram is a lightweight Metaploit GUI", bg="Blue", fg="Green", font=("Roboto Mono", 30))
    win11_l2 = Label(win11, text="Utiligram seeks to make Metaploit more user friendly", bg="Blue", fg="Green", font=("Roboto Mono", 30))
    
    win11_bb = Button(win11, text="Back", bg="grey", command=backButt)

    win11_l1.pack()
    win11_l2.pack()
    win11_bb.pack()
    win11.mainloop()



def Pecunia_Secretum_func2():
    global Pecunia_Secretum_func2
    win10 = Toplevel(MAIN_PAGE)
    win10.geometry("1600x1600")
    win10.configure(bg="black")
    win10.title("Pecunia Secretum")
    win10.resizable(True, True)
    options1 = ["Debian", "Arch", "Fedora", "Windows", "Mac"]
    clicked1 = StringVar()
    def show1():
        label(text=clicked1.get())
    win10_l1 = Label(win10, text="Pecunia Secretum is a point and shoot crypto currency miner GUI", bg="Black", fg="Green", font=("Roboto Mono", 30))
    win10_l2 = Label(win10, text="Pecunia Secretum is latin for fuck the federal reserve.", bg="Black", fg="Green", font=("Roboto Mono", 30))
    win10_dd1 = OptionMenu(win10, clicked1, *options1, height=20, width=20)
    
    
    win10_l3 = Label(win10, text="Select your OS", bg="Black", fg="Green", font=("Roboto Mono", 30))
    
    win10_dd1.pack()
    win10_l1.pack()
    win10_l2.pack()
    win10_dd1.pack()
    win10_l3.pack()
    win10.mainloop()





def OPD_INSTALL_FUNC():
    global OPD_INSTALL_FUNC
    win5 = Toplevel(win1)
    win5.geometry("600x600")
    win5.configure(bg="Black")
    win5.title("Operation Dementia")
    win5.resizable(False, False)

    win5_l1 = Label(win5, text="Install Operation Dementia", bg="Black", fg="White", font=("Arial", 20))
    win5_l2 = Label(win5, text="This wont take long!", bg="Black", fg="White", font=("Arial", 20))
    win5_but1 = Button(win5, text="Install", command=OPD_INSTALL_FUNC)

    win5_l1.pack()
    win5_l2.pack()
    win5_but1.pack()
    win5.mainloop()


def Op_Dem_Func():
    global Op_Dem_Func
    global win1
    win1 = Toplevel(MAIN_PAGE)
    win1.geometry("600x600")
    win1.configure(bg="purple")
    win1.title("Operation Dementia")
    win1.resizable(False, False)
    
    win1_l1 = Label(win1, text="Operation Dementia", bg="purple", fg="white", font=("Arial", 20))
    win1_butt1 = Button(win1, text="Download .exe", command=OPD_INSTALL_FUNC)
    win1_t1 = Text(win1, height=10, width=50, bg="blue", font=("Arial", 20))
    win1_t1.insert(INSERT, "Not your Grandpappy's Malware")
    
    win1_l1.pack()
    win1_butt1.pack()
    win1_t1.pack()
    win1.mainloop()







def Pecunia_func():
    global Pecunia_func
    win2 = Toplevel(MAIN_PAGE)
    win2.geometry("600x600")
    win2.configure(bg="Orange")
    win2.title("Pecunia Secretum")
    win2.resizable(True, True)
    win2_l1 = Label(win2, text="Pecunia Secretum is a point and shoot crypto currency miner GUI", bg="Orange", fg="Black", font=("Roboto Mono", 30))
    win2_l2 = Label(win2, text="Pecunia Secretum is latin for fuck the federal reserve.", bg="Orange", fg="Black", font=("Roboto Mono", 30))
    win2_but1 = Button(win2, text="Download .exe", command=Pecunia_Secretum_func2)


    win2_l1.pack()
    win2_l2.pack()
    win2_but1.pack()
    win2.mainloop()








def Utiligram_Func():
    global Utiligram_Func
    win3 = Toplevel(MAIN_PAGE)
    win3.geometry("600x600")
    win3.configure(bg="black")
    win3.resizable(True, True)
    win3.title("Utiligram Installer")
    win3_l1 = Label(win3, text="Select the version below")
    win3_butt1 = Button(win3, text="FULL INSTALL", commannd=utiligram_func2)
    win3_butt2 = Button(win3, text="Lightweight Install")
    win3_butt3 = Button (win3, text="Minimal Install")
    win3_butt4 = Button (win3, text="back", command=backButt)
    


    win3_l1.pack()
    win3_butt1.pack()
    win3_butt2.pack()
    win3_butt3.pack()
    win3_butt4.pack()
    win3.mainloop()



def Triple_G_Func():
    global Triple_G_Func
    win4 = Toplevel(MAIN_PAGE)
    win4.geometry("600x600")
    win4.configure(bg="black")
    win4.resizable(True, True)
    win4.title("Triple G")
    win4_l1 = Label(win4, text="Gaslight, Gatekeep, Girlboss", bg="Black", fg="Green", font=("Roboto Mono", 30))
    win4_l2 = Label(win4, text="Gaslight: To manipulate (someone) by psychological means into questioning their own sanity.", bg="Black", fg="Green", font=("Roboto Mono", 14))
    win4_l3 = Label(win4, text="Gatekeep: To control access to (something) by controlling who is allowed to enter or leave.", bg="Black", fg="Green", font=("Roboto Mono", 14))
    win4_l4 = Label(win4, text="Girlboss: IDK what this means, but it's in the Urban Dictionary.", bg="Black", fg="Green", font=("Roboto Mono", 14))
    win4_l1.pack()
    win4_l2.pack()
    win4_l3.pack()
    win4_l4.pack()
    
    win4.mainloop()




def LogRoller_Func():
    global LogRoller_Func
    win6 = Toplevel(MAIN_PAGE)
    win6.geometry("600x600")
    win6.configure(bg="black")
    win6.title("Log Roller")
    win6.resizable(True, True)
    win6_l1 = Label(win6, text="Log Roller is a lightweight botnet GUI", bg="Black", fg="Green", font=("Roboto Mono", 30))
    win6.mainloop()




def NFC_func():
    global NFC_func
    win7 = Toplevel(MAIN_PAGE)
    win7.geometry("600x600")
    win7.configure(bg="Dark Green")
    win7.title("Near Field Cuckary")
    win7.resizable(True, True)
    win_l1 = Label(win7, text="Near Field Cuckary is a NFC programming GUI", bg="Blue", fg="Red", font=("Roboto Mono", 30))
    win_l1.pack()
    win7.mainloop()



def Unigram_Func():
    global Unigram_Func
    win8 = Toplevel(MAIN_PAGE)
    win8.geometry("600x600")
    win8.configure(bg="black")
    win8.title("Unigram")
    win8.resizable(True, True)
    win8_l1 = Label(win8, text="Unigram is a Instagram botnet GUI", bg="Black", fg="Green", font=("Roboto Mono", 30))
    win8_butt1 = Button(win8, text="Download .exe", command=utiligram_func2)
    win8_l1.pack()
    win8_butt1.pack()
    win8.mainloop()









MAIN_PAGE = Tk()

MAIN_PAGE.title("Home Made Malware")
MAIN_PAGE.geometry("600x600")
MAIN_PAGE.configure(bg="grey")
MAIN_PAGE.resizable(True,True)
Operation_Dementia = Button(MAIN_PAGE, text="Operation Dementia", command=Op_Dem_Func, bg="Purple", fg="turquoise", font=("Arial", 20)).grid(column=0, row=0)
Pecunia_Secretum = Button(MAIN_PAGE, text="Pecunia Secretum", command=Pecunia_func, bg="Orange", fg="White", font=("Arial", 20)).grid(column=0, row=1)
Utiligram = Button(MAIN_PAGE, text="Utiligram", command=Utiligram_Func, bg="Blue", fg="White", font=("Arial", 20)).grid(column=0, row=2)
Triple_G = Button(MAIN_PAGE, text="Triple G", command=Triple_G_Func, bg="Black", fg="Green", font=("Arial", 20)).grid(column=1, row=3)
LogRolling = Button(MAIN_PAGE, text="Log Rolling", command=LogRoller_Func, bg="Light Grey", fg="Green", font=("Arial", 20)).grid(column=1, row=0)
Near_Field_Communication = Button(MAIN_PAGE, text="Near Field Communication", command=NFC_func, bg="Blue", fg="Red", font=("Arial", 20)).grid(column=1, row=1)
Unigram = Button(MAIN_PAGE, text="Unigram", command=Unigram_Func, bg="Red", fg="Orange", font=("Arial", 20)).grid(column=1, row=2)
TensorMole = Button(MAIN_PAGE, text="")
Project_Jedi = Button(MAIN_PAGE, text="Project Jedi", command=project_jedi_func, bg="purple", fg="white", font=("Arial", 20)).grid(column=0, row=3)

MAIN_PAGE.mainloop()



def backButt():
    global backButt
backbutt = command=MAIN_PAGE