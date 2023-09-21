import tkinter as tk
import random as rd
import string
from tkinter import ttk
import timeit as time
import time as ti
from tkinter.messagebox import showinfo
import os


#function to get a random word using string and random
def get_random_phrase():
    '''get a random phrase from file'''
    current_directory = os.path.dirname(os.path.abspath(__file__)) #get current directory
    file = os.path.join(current_directory, "phrases_db.txt") #adding our file to the directory
    with open(file, "r") as database:
        phrases = database.readlines()
    random_phrase = rd.choice(phrases)
    return random_phrase

#defining the class
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.initial_time = 0 #initial time

        window_width = 400
        window_height = 200

        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.title("Fast Writing Game")
        self.resizable(0,0)

        self.createwidgets()
    



    
    def createwidgets(self):
        '''creating the widgets for our game'''

        #top label
        self.title_label = ttk.Label(self, text="Fast Writing Game!", foreground="white", background="black")
        self.title_label.pack()
        

        #instructions
        self.instructions_label = ttk.Label(self, text="Whenever you're ready, click on the Start button \nand type the phrase as fast as you can")
        self.instructions_label.pack()
        

        #random word label
        self.random_phrase = get_random_phrase()
        self.random_label = ttk.Label(self, text=self.random_phrase, font="Verdana", foreground="white", background="red")
        

        #entry
        self.phrase_entry = tk.StringVar()
        self.word_entry = ttk.Entry(self, width=30, textvariable=self.phrase_entry)
        self.word_entry.pack()
        


        #Start Button
        self.start_button = ttk.Button(self, text="Start!", command=self.start_game)
        self.start_button.pack()

        #Restart Button
        self.restart_button = ttk.Button(self, text="Restart game?", command=self.restart_game)
        

    def start_game(self):
        '''This method starts the game after hitting Start! button'''

        #show random label
        self.random_label.pack()
        

        #focus on entry
        self.word_entry.focus()

        self.initial_time = ti.time() #start game time

        def check_input():
            user_input = self.phrase_entry.get().strip() #strip to avoid any spaces at beginning or end
            if user_input == self.random_phrase.strip(): #strip to avoid spaces
                end_time = ti.time()
                elapsed_time = end_time - self.initial_time
                showinfo("Congratulations!", f"You've entered the correct phrase within {elapsed_time:.2f} seconds.")
                self.phrase_entry.set('')
                self.restart_button.pack()
            self.after(100, check_input)  # Checks after 100 miliseconds the word

        check_input()  # Initiate validation
        
    

    def restart_game(self):
        #hide previous random label
        self.random_label.pack_forget()

        # get a new random phrase
        self.random_phrase = get_random_phrase()

        #Show a new phrase
        self.random_label.config(text=self.random_phrase)
        self.random_label.pack()

        self.initial_time = ti.time() #start game time



    


if __name__ == "__main__":
    app = App()
    app.mainloop()
