from cgitb import text
from modulefinder import IMPORT_NAME
from msilib.schema import Font
from struct import pack
from telnetlib import SUPDUP
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import font
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import Menu
from tkinter import Spinbox
from tkinter import dnd



import fileinput as fi

import sys
import os
from tkinter import font
from typing_extensions import Self

import super as super


#


#






root =  tk.Tk()
# create an instance of the application

__name__= "__main__"
class App(tk.Tk):
    GUI_FULL = Tk()
    GUI_FULL.title("Home Made Malware")
    GUI_FULL.geometry('800x600')
    GUI_FULL.mainloop()


    #create init function

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Home-Made-Malware")
        self.geometry("800x600")
        self.resizable(0, 0)
        self.create_widgets()
        self.create_menu()
        self.create_toolbar()
        self.mainloop()
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

    # Create instance
    def __init__(self, master=None):
        super().__init__()
        self.title("Home-Made-Malware")
        self.geometry("800x600")
        self.resizable(0, 0)
        self.create_widgets()
        self.create_menu()
        self.create_toolbar()
        self.mainloop()





    #CREATE SAVE FILE FUNCTION
    def save_file(self):
        file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if file is None:
            return
        text2save = str(self.text.get(1.0, END))
        self.master.title("Untitled - Notepad")
        file.write(text2save)
        file.close()

   

 #CREATE OPEN FILE FUNCTION
    def open_file(self):
        file = filedialog.askopenfile(mode='r')
        if file is not None:
            content = file.read()
            self.text.insert(INSERT, content)
 #create new file function
    def new_file(self):
        self.text.delete(1.0, END)
  #create exit function      
    def exit(self):
        self.destroy()
 #CREATE UNDO FUNCTION
    def undo(self):
        self.text.edit_undo()
 #create redo function
    def redo(self):
        self.text.edit_redo()
 #create cut function
    def cut(self):
        self.text.event_generate("<<Cut>>")
 #create copy function
    def copy(self):
        self.text.event_generate("<<Copy>>")
 #create paste function       
    def paste(self):
        self.text.event_generate("<<Paste>>")
 #create find function
    def find(self):
        find_string = simpledialog.askstring("Find...", "Enter text")
        if find_string:
            idx = '1.0'
            while 1:
                idx = self.text.search(find_string, idx, nocase=1, stopindex=END)
                if not idx: break
                lastidx = '%s+%dc' % (idx, len(find_string))
                self.text.tag_add('found', idx, lastidx)
                idx = lastidx
            self.text.tag_config('found', foreground='red')
#create replace function
    def replace(self):
        find_string = simpledialog.askstring("Find...", "Enter text")
        replace_string = simpledialog.askstring("Replace...", "Replace with")
        content = self.text.get("1.0", END)
        new_content = content.replace(find_string, replace_string)
        self.text.delete("1.0", END)
        self.text.insert("1.0", new_content)
 #create save as function
    def save_as(self):
        file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if file is None:
            return
        text2save = str(self.text.get(1.0, END))
        self.master.title("Untitled - Notepad")
        file.write(text2save)
        file.close()
 #create delete function
    def delete(self):
        self.text.delete(1.0, END)
 #create select all function
    def select_all(self):
        self.text.tag_add('sel', '1.0', 'end')
 #create about function
    def about(self):

        messagebox.showinfo("About", "Home-Made-Malware")
 #create title function
    def title(self):
        self.master.title("Home-Made-Malware")
 #create save as file function
    def save_as_file(self):
        file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if file is None:
            return
        text2save = str(self.text.get(1.0, END))
        self.master.title("Untitled - Notepad")
        file.write(text2save)
        file.close()
 #CREATE COLOR FUNCTION
    def color(self):
        (triple, color) = colorchooser.askcolor()
        if color:
            self.text.config(fg=color)

    #CREATE FONT FUNCTION
    def font(self):
        (triple, color) = colorchooser.askcolor()
        if color:
            self.text.config(fg=color)
def pull_functions():

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.title("Home-Made-Malware")
         self.geometry("800x600")
         self.resizable(0, 0)
         self.create_widgets()
         self.create_menu()
         self.create_toolbar()
         self.mainloop()
    def __init__(self, master):
        super().__init__(master)
            self.pack()

            self.entrythingy = tk.Entry()
            self.entrythingy.pack()

        # Create instance
        def __init__(self, master=None):
            super().__init__()
            self.title("Home-Made-Malware")
            self.geometry("800x600")
            self.resizable(0, 0)
            self.create_widgets()
            self.create_menu()
            self.create_toolbar()
            self.mainloop()



        #CREATE HOME PAGE
        def create_widgets(self):
            self.text = scrolledtext.ScrolledText(self, wrap=WORD, width=100, height=100)
            self.text.pack(fill=BOTH, expand=1)

        #CREATE SAVE FILE FUNCTION
        def save_file(self):
            file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
            if file is None:
                return
            text2save = str(self.text.get(1.0, END))
            self.master.title("Untitled - Notepad")
            file.write(text2save)
            file.close()

    

    #CREATE OPEN FILE FUNCTION
        def open_file(self):
            file = filedialog.askopenfile(mode='r')
            if file is not None:
                content = file.read()
                self.text.insert(INSERT, content)
    #create new file function
        def new_file(self):
            self.text.delete(1.0, END)
    #create exit function      
        def exit(self):
            self.destroy()
    #CREATE UNDO FUNCTION
        def undo(self):
            self.text.edit_undo()
    #create redo function
        def redo(self):
            self.text.edit_redo()
    #create cut function
        def cut(self):
            self.text.event_generate("<<Cut>>")
    #create copy function
        def copy(self):
            self.text.event_generate("<<Copy>>")
    #create paste function       
        def paste(self):
            self.text.event_generate("<<Paste>>")
    #create find function
        def find(self):
            find_string = simpledialog.askstring("Find...", "Enter text")
            if find_string:
                idx = '1.0'
                while 1:
                    idx = self.text.search(find_string, idx, nocase=1, stopindex=END)
                    if not idx: break
                    lastidx = '%s+%dc' % (idx, len(find_string))
                    self.text.tag_add('found', idx, lastidx)
                    idx = lastidx
                self.text.tag_config('found', foreground='red')
    #create replace function
        def replace(self):
            find_string = simpledialog.askstring("Find...", "Enter text")
            replace_string = simpledialog.askstring("Replace...", "Replace with")
            content = self.text.get("1.0", END)
            new_content = content.replace(find_string, replace_string)
            self.text.delete("1.0", END)
            self.text.insert("1.0", new_content)
    #create save as function
        def save_as(self):
            file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
            if file is None:
                return
            text2save = str(self.text.get(1.0, END))
            self.master.title("Untitled - Notepad")
            file.write(text2save)
            file.close()
    #create delete function
        def delete(self):
            self.text.delete(1.0, END)
    #create select all function
        def select_all(self):
            self.text.tag_add('sel', '1.0', 'end')
    #create about function
        def about(self):

            messagebox.showinfo("About", "Home-Made-Malware")
    #create title function
        def title(self):
            self.master.title("Home-Made-Malware")
    #create save as file function
        def save_as_file(self):
            file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
            if file is None:
                return
            text2save = str(self.text.get(1.0, END))
            self.master.title("Untitled - Notepad")
            file.write(text2save)
            file.close()
    #CREATE COLOR FUNCTION
        def color(self):
            (triple, color) = colorchooser.askcolor()
            if color:
                self.text.config(fg=color)

        #CREATE FONT FUNCTION
        def font(self):
            (triple, color) = colorchooser.askcolor()
            if color:
                self.text.config(fg=color)




        #create text function
        def text():
            print("text")
        #create event function
        def event():
            print("event")
        #create event generator function
        def event_generate():
            print("event_generate")
        #create event info function
        def event_info():
            print("event_info")
        #create event widget function
        def event_widget():
            print("event_widget")
        #create focus function
        def focus():
            print("focus")
        #create focus get function
        def focus_get():
            print("focus_get")
        #create focus set function
        def focus_set():
            print("focus_set")
        #create grab function
        def grab():
            print("grab")
        #create grab current function
        def grab_current():
            print("grab_current")
        #create grab release function
        def grab_release():
            print("grab_release")
        #create grab set function
        def grab_set():
            print("grab_set")
        #create grab set global function
        def grab_set_global():
            print("grab_set_global")
        #create grab status function
        def grab_status():
            print("grab_status")
        #create handle function
        def handle():
            print("handle")
        #create iconify function
        def iconify():
            print("iconify")
        #create configuration function
        def create_config():
            #create config file
            config = open("config.txt", "w")
            #write to config file
            config.write("1")
            #close config file
            config.close()
        
            #Create edit menu functions
            
            #create undo function
            def undo(self):
                    self.text.event_generate("<<Undo>>")
            #create redo function
            def redo(self):
                    self.text.event_generate("<<Redo>>")
            #create cut function
            def cut(self):


                    self.text.event_generate("<<Cut>>")
            #create copy function
            def copy(self):
                    self.text.event_generate("<<Copy>>")
            #create paste function
            def paste(self):
                
                    self.text.event_generate("<<Paste>>")
            #create delete function
            def delete(self):




            #Create file menu functions
             def new_file(self):
                    self.text.delete(1.0, END)
                    self.filename = "Untitled"
                    self.title(self.filename)


                    
            #Create open file function
            def open_file(self):

                    self.filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
                    if self.filename == "":
                        self.filename = None
                    else:
                        self.text.delete(1.0, END)
                        file = open(self.filename, "r")
                        self.text.insert(1.0, file.read())
                        file.close()
                        self.title(os.path.basename(self.filename) + " - Notepad")
        #create text file function
        def create_text_file():
            #create text file
            text_file = open("text.txt", "w")
            #write to text file
            text_file.write("1")
            #close text file
            text_file.close()
        
        
        #create text file config function
        def create_text_file_config():
            #create text file config
            text_file_config = open("text_file_config.txt", "w")
            #write to text file config
            text_file_config.write("1")
            #close text file config
            text_file_config.close()
        #create config file function
        def create_config_file():
            #create config file
            config = open("config.txt", "w")
            #write to config file
            config.write("1")
            #close config file
            config.close()
        
        
        #create font function
        def font(self):
                (triple, color) = colorchooser.askcolor()
                if color:
                    self.text.config(fg=color)
        
        
        #create color function           
        def color(self):
                (triple, color) = colorchooser.askcolor()
                if color:
                    self.text.config(fg=color)





        #Create save file function
        def save_file(self):

                if self.filename == None:

                    self.filename = filedialog.asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

                    if self.filename == "":
                        self.filename = None
                    else:
                        file = open(self.filename, "w")
                        file.write(self.text.get(1.0, END))
                        file.close()
                        self.title(os.path.basename(self.filename) + " - Notepad")
                else:
                    file = open(self.filename, "w")
                    file.write(self.text.get(1.0, END))
                    file.close()

        #

        #Create save as file function
        def save_as_file(self):


                self.filename = filedialog.asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

                if self.filename == "":
                    self.filename = None
                else:
                    file = open(self.filename, "w")
                    file.write(self.text.get(1.0, END))
                    file.close()
                    self.title(os.path.basename(self.filename) + " - Notepad")

        #Create exit function
        def exit(self):

                self.destroy()

        #create time function
        def time(self):
                self.text.insert(INSERT, time.strftime("%H:%M:%S"))

        #create date function
        def date(self):
        #

                self.text.delete(SEL_FIRST, SEL_LAST)
        #create select all function
        def select_all(self):
                self.text.tag_add(SEL, "1.0", END)
                self.text.mark_set(INSERT, "1.0")
                self.text.see(INSERT)
                return 'break'
        #create time/date function
        def time_date(self):
                self.text.insert(INSERT, time.strftime('%I:%M:%S %p - %B %d, %Y'))
        
    #reate font functions
        def font(self):
                (triple, color) = colorchooser.askcolor()
                if color:
                    self.text.config(fg=color)
    #create color function
        def color(self):
                (triple, color) = colorchooser.askcolor()
                if color:
                    self.text.config(bg=color)
                
        # Create help menu functions
        def about(self):
            messagebox.showinfo("About", "Home Made Malware")
            showinfo = ("Notepad", "Notepad by Home Made Malware")


        #create toolbar function
        def create_toolbar(self):
                self.toolbar = Frame(self, bg="grey")
                self.open_button = Button(self.toolbar, text="Open", command=self.open_file)
                self.open_button.pack(side=LEFT, padx=2, pady=2)
                self.save_button = Button(self.toolbar, text="Save", command=self.save_file)
                self.save_button.pack(side=LEFT, padx=2, pady=2)
                self.toolbar.pack(side=TOP, fill=X)
        
        
        #create text delete function
        def delete(self):
            self.text.delete(1.0, END) 




    
        
   
 


     
     
     
     
#CREATE HOME PAGE
    def create_widgets(self):
        self.text = scrolledtext.ScrolledText(self, wrap=WORD, width=100, height=100)
        self.text.pack(fill=BOTH, expand=1)



# Create STATUS BAR
status = Label(App, text="Home-Made-Malware", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

# Create MENU BAR
menu = Menu(App)
App.config(menu=menu)

# Create FILE MENU
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=App.new_file)
filemenu.add_command(label="Open", command=App.open_file)
filemenu.add_command(label="Save", command=App.save_file)
filemenu.add_command(label="Save As", command=App.save_as_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=App.exit)

# Create EDIT MENU








# Create widgets
def create_widgets(self):
        self.text = scrolledtext.ScrolledText(self,text = "Welcome to Home Made Malware", width=100, height=30, font=("Arial", 12))
        self.text.pack(fill=BOTH, expand=1)


# Create menu
def create_menu(self):
        self.menu = Menu(self)
        self.config(menu=self.menu)

        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit) 
        self.menu.add_cascade(label="File", menu=self.file_menu)

        self.edit_menu = Menu(self.menu, tearoff=0)
        self.edit_menu.add_command(label="Undo", command=self.undo)
        self.edit_menu.add_command(label="Redo", command=self.redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.edit_menu.add_command(label="Copy", command=self.copy)
        self.edit_menu.add_command(label="Paste", command=self.paste)
        self.edit_menu.add_command(label="Delete", command=self.delete)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Select All", command=self.select_all)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Font", command=self.font)
        self.edit_menu.add_command(label="Color", command=self.color)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)

        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="About", command=self.about)
        self.menu.add_cascade(label="Help", menu=self.help_menu)




        





# Create toolbar

def create_toolbar(self):

        self.toolbar = Frame(self, bg="white")

        image_new = PhotoImage(file="icons/new.gif")

        btn_new = Button(self.toolbar, image=image_new, command=self.new_file)

        btn_new.image = image_new

        btn_new.pack(side=LEFT, padx=2, pady=2)

        image_open = PhotoImage(file="icons/open.gif")

        btn_open = Button(self.toolbar, image=image_open, command=self.open_file)

        btn_open.image = image_open

        btn_open.pack(side=LEFT, padx=2, pady=2)

        image_save = PhotoImage(file="icons/save.gif")

        btn_save = Button(self.toolbar, image=image_save, command=self.save_file)   

        btn_save.image = image_save

        btn_save.pack(side=LEFT, padx=2, pady=2)

        image_cut = PhotoImage(file="icons/cut.gif")

        btn_cut = Button(self.toolbar, image=image_cut, command=self.cut)

        btn_cut.image = image_cut

        btn_cut.pack(side=LEFT, padx=2, pady=2)

        image_copy = PhotoImage(file="icons/copy.gif")

        btn_copy = Button(self.toolbar, image=image_copy, command=self.copy)

        btn_copy.image = image_copy

        btn_copy.pack(side=LEFT, padx=2, pady=2)

        image_paste = PhotoImage(file="icons/paste.gif")

        btn_paste = Button(self.toolbar, image=image_paste, command=self.paste)

        btn_paste.image = image_paste

        btn_paste.pack(side=LEFT, padx=2, pady=2)

        image_undo = PhotoImage(file="icons/undo.gif")

        btn_undo = Button(self.toolbar, image=image_undo, command=self.undo)

        btn_undo.image = image_undo

        btn_undo.pack(side=LEFT, padx=2, pady=2)

        image_redo = PhotoImage(file="icons/redo.gif")

        btn_redo = Button(self.toolbar, image=image_redo, command=self.redo)

        btn_redo.image = image_redo

        btn_redo.pack(side=LEFT, padx=2, pady=2)

        self.toolbar.pack(side=TOP, fill=X)

# Create status bar

def create_statusbar(self):

        self.statusbar = Label(self, text="Ln 1, Col 1", bd=1, relief=SUNKEN, anchor=W)

        self.statusbar.pack(side=BOTTOM, fill=X)

# Create main window

def create_main_window(self):

        text = Text(self, undo=True)

        self.text = Text(self, undo=True)

        self.text.pack(expand=YES, fill=BOTH)

        self.scroll = Scrollbar(self.text)

        self.text.config(yscrollcommand=self.scroll.set)


        self.scroll.config(command=self.text.yview)

        self.scroll.pack(side=RIGHT, fill=Y)

        self.text.focus_set()

# Create menu bar

def create_menu(self):


        self.menu = Menu(self.master)

        self.master.config(menu=self.menu)

        # Create file menu

        self.file_menu = Menu(self.menu)

        self.file_menu.add_command(label="New", accelerator="Ctrl+N", command=self.new_file)

        self.file_menu.add_command(label="Open", accelerator="Ctrl+O", command=self.open_file)

        self.file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.save_file)

        self.file_menu.add_command(label="Save As", accelerator="Ctrl+Shift+S", command=self.save_as_file)

        self.file_menu.add_separator()

        self.file_menu.add_command(label="Exit", accelerator="Alt+F4", command=self.exit)

        self.menu.add_cascade(label="File", menu=self.file_menu)

        # Create edit menu

        self.edit_menu = Menu(self.menu)

        self.edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", command=self.undo)

        self.edit_menu.add_command(label="Redo", accelerator="Ctrl+Y", command=self.redo)

        self.edit_menu.add_separator()

        self.edit_menu.add_command(label="Cut", accelerator="Ctrl+X", command=self.cut)

        self.edit_menu.add_command(label="Copy", accelerator="Ctrl+C", command=self.copy)

        self.edit_menu.add_command(label="Paste", accelerator="Ctrl+V", command=self.paste)

        self.edit_menu.add_command(label="Delete", accelerator="Del", command=self.delete)

        self.edit_menu.add_separator()

        self.edit_menu.add_command(label="Select All", accelerator="Ctrl+A", command=self.select_all)

        self.menu.add_cascade(label="Edit", menu=self.edit_menu)

        # Create format menu

        self.format_menu = Menu(self.menu)

        self.format_menu.add_command(label="Font", command=self.font)

        self.format_menu.add_command(label="Color", command=self.color)

        self.menu.add_cascade(label="Format", menu=self.format_menu)

        # Create help menu

        self.help_menu = Menu(self.menu)

        self.help_menu.add_command(label="About", command=self.about)

        self.menu.add_cascade(label="Help", menu=self.help_menu)

# Create toolbar

def create_toolbar(self):


        self.toolbar = Frame(self, bd=1, relief=RAISED)

        image_new = PhotoImage(file="icons/new.gif")

        btn_new = Button(self.toolbar, image=image_new, command=self.new_file)

        btn_new.image = image_new

        btn_new.pack(side=LEFT, padx=2, pady=2)

        image_open = PhotoImage(file="icons/open.gif")

        btn_open = Button(self.toolbar, image=image_open, command=self.open_file)

        btn_open.image = image_open

        btn_open.pack(side=LEFT, padx=2, pady=2)

        image_save = PhotoImage(file="icons/save.gif")

        btn_save = Button(self.toolbar, image=image_save, command=self.save_file)

        btn_save.image = image_save

        btn_save.pack(side=LEFT, padx=2, pady=2)

        image_cut = PhotoImage(file="icons/cut.gif")

        btn_cut = Button(self.toolbar, image=image_cut, command=self.cut)

        btn_cut.image = image_cut

        btn_cut.pack(side=LEFT, padx=2, pady=2)

        image_copy = PhotoImage(file="icons/copy.gif")

        btn_copy = Button(self.toolbar, image=image_copy, command=self.copy)

        btn_copy.image = image_copy

        btn_copy.pack(side=LEFT, padx=2, pady=2)

        image_paste = PhotoImage(file="icons/paste.gif")

        btn_paste = Button(self.toolbar, image=image_paste, command=self.paste)

        btn_paste.image = image_paste

        btn_paste.pack(side=LEFT, padx=2, pady=2)

        image_undo = PhotoImage(file="icons/undo.gif")

        btn_undo = Button(self.toolbar, image=image_undo, command=self.undo)

        btn_undo.image = image_undo

        btn_undo.pack(side=LEFT, padx=2, pady=2)

        image_redo = PhotoImage(file="icons/redo.gif")

        btn_redo = Button(self.toolbar, image=image_redo, command=self.redo)

        btn_redo.image = image_redo

        btn_redo.pack(side=LEFT, padx=2, pady=2)

        self.toolbar.pack(side=TOP, fill=X)

# Create status bar

def create_statusbar(self):


        self.statusbar = Label(self, text="Ready", bd=1, relief=SUNKEN, anchor=W)

        self.statusbar.pack(side=BOTTOM, fill=X)


#create context menu functions

def cut(self):


        self.text.event_generate("<<Cut>>")

def copy(self):
    
            self.text.event_generate("<<Copy>>")

def paste(self):

        self.text.event_generate("<<Paste>>")

def delete(self):
    
            self.text.event_generate("<<Clear>>")

def select_all(self):
        
                self.text.event_generate("<<SelectAll>>")

def undo(self):
    
            self.text.event_generate("<<Undo>>")

def redo(self):
    
            self.text.event_generate("<<Redo>>")

def new_file(self):
        
                self.filename = "Untitled"
    
                self.title(self.filename)
    
                self.text.delete(0.0, END)

def open_file(self):
    filedialog.askopenfilename
    filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    self.filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    
    if self.filename == "":
        
                    self.filename = None
        
    else:
        
                    self.text.delete(0.0, END)
        
                    file = open(self.filename, "r")
        
                    self.text.insert(0.0, file.read())
        
                    file.close()
        
                    self.title(os.path.basename(self.filename) + " - Notepad")
# Create context menu

def create_context_menu(self):  
        context_menu=Menu(self, tearoff=0) 
        


        self.context_menu = Menu(self, tearoff=0)

        self.context_menu.add_command(label="Undo", accelerator="Ctrl+Z", command=self.undo)

        self.context_menu.add_command(label="Redo", accelerator="Ctrl+Y", command=self.redo)

        self.context_menu.add_separator()

        self.context_menu.add_command(label="Cut", accelerator="Ctrl+X", command=self.cut)

        self.context_menu.add_command(label="Copy", accelerator="Ctrl+C", command=self.copy)

        self.context_menu.add_command(label="Paste", accelerator="Ctrl+V", command=self.paste)

        self.context_menu.add_command(label="Delete", accelerator="Del", command=self.delete)

        self.context_menu.add_separator()

        self.context_menu.add_command(label="Select All", accelerator="Ctrl+A", command=self.select_all)

        self.bind("<Button-3>", self.show_context_menu) # right click

        self.bind("<Control-Button-1>", self.show_context_menu) # ctrl + left click

# Show context menu

def show_context_menu(self, event):

        self.context_menu.post(event.x_root, event.y_root)



    
# New file

def new_file(self, *args):



     self.text.delete(1.0, END)

     self.filename = None

     self.update_status(False)
    

# Open file


def open_file(self, *args):


        self.filename = filedialog.askopenfilename(defaultextension=".txt",
        
                                                   filetypes=[("All Files", "*.*"),

                                                              ("Text Documents", "*.txt")])

        if self.filename:

            self.text.delete(1.0, END)

            with open(self.filename, "r") as _file:

                self.text.insert(1.0, _file.read())

            self.update_status(False)

# Save file


def save_file(self, *args):

        if not self.filename:
                
                self.filename = filedialog.asksaveasfilename(initialfile='Untitled.txt',
    
                                                            defaultextension=".txt",
    
                                                            filetypes=[("All Files", "*.*"),
    
                                                                        ("Text Documents", "*.txt")])
    
                if not self.filename:
    
                    return

        with open(self.filename, "w") as _file:
                
                _file.write(self.text.get(1.0, END))

        self.update_status(False)

# Cut text


def cut(self, *args):


        self.copy() 

        self.delete()

# Copy text


def copy(self, *args):

        self.text.clipboard_clear()

        text = self.text.get(SEL_FIRST, SEL_LAST)

        self.text.clipboard_append(text)

# Paste text


def paste(self, *args):

        try:

            text = self.text.selection_get(selection='CLIPBOARD')

            self.text.insert(INSERT, text)

        except TclError:
                
                pass

# Delete text


def delete(self, *args):

        self.text.delete(SEL_FIRST, SEL_LAST)

# Undo


def undo(self, *args):

        try:

            self.text.edit_undo()

        except TclError:

            pass

# Redo


def redo(self, *args):


        try:

            self.text.edit_redo()

        except TclError:

            pass

# Select all text


def select_all(self, *args):

        self.text.tag_add(SEL, "1.0", END)

        self.text.mark_set(INSERT, "1.0")

        self.text.see(INSERT)

        return 'break'

# Update status


def update_status(self, *args):


        if self.filename:
                
                self.statusbar.config(text=self.filename)

        else:
                    
                    self.statusbar.config(text="Untitled")

        self.title("{} - {}".format(os.path.basename(self.filename) if self.filename else "Untitled", FULL_GUI))
update_status.pack(side=BOTTOM, fill=X)


#pack all the widgets

def pack_widgets(self):
    
    self.text.pack(expand=True, fill=BOTH)



# Run main application


if App == "__main__":

    FULL_GUI = "Full GUI"


#pack all the widgets

def pack_widgets(self):
        
        self.text.pack(expand=True, fill=BOTH)



# Run main application


if App == "__main__":

    FULL_GUI = "Full GUI"

#pack everything

def pack_widgets(self):
    
    self.text.pack(expand=True, fill=BOTH)
    
pack_widgets.pack(side=BOTTOM, fill=X)
pack_widgets.pack(side=BOTTOM, fill=X) 


#pack everything

def pack_widgets(self):
    
    self.text.pack(expand=True, fill=BOTH)


root.mainloop()








  






  