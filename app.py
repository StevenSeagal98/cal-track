from ast import Lambda
# from cgitb import text
from math import e, fabs
from tkinter import *
from tkinter import scrolledtext
from turtle import width
from tkcalendar import Calendar


import customtkinter
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
import os
from PIL import ImageTk, Image

from globals import *
from data.dataReadWrite import *

from datetime import datetime, date

from views.main import windows
import dbclass as dbc

class App(customtkinter.CTk):
    height= 600
    width=800
    titlebgcolor="darkgrey"
    titletextcolor="black"
    def __init__(self) :
        super().__init__()
        # views
        # Set initial window state
        self.current_window = 'main'
        
        #Initialize dbclass

        self.pd=dbc.sqllitecalls()

        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False,False)
        self.grid_columnconfigure(1, weight=1)

        #load background Image
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image= customtkinter.CTkImage(Image.open(self.current_path + "/images/calc2.jpg"), size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image, text="")
        self.bg_image_label.grid(row=0, column=0)

        # Create the side navigation bar frame
        self.navbar = customtkinter.CTkFrame(self, corner_radius=0, border_width=1, fg_color="white" ,width=450)
        self.navbar.grid(row=0,column=0, sticky="ns" ,padx=40)

        # # Create the main content frame
        self.create_navbar_buttons()
    
    def reloadnavbar(self,cw):
        match cw:
            case "Home":
                self.home.grid_forget()
            case "Info":
                self.info.grid_forget()
            case "Preferences":
                self.preferences.grid_forget()
            case "WC":
                self.wcalories.grid_forget()
            
        self.navbar.grid(row=0,column=0, sticky="ns")
   
    def display_calorietrackercard(self):
        #pulls the calories for the selected date
        print(self.getcalselection())
        self.calmeal_id, self.caldate, self.calories = self.pd.getcalorietrackerdata(1,self.getcalselection())
        
        #loads the current date on initialization
        self.brfstlbl = customtkinter.CTkLabel(self.card, text=" Breakfast Calories: ").grid(row=1, column=0, pady = 10)
        self.brfsttxt = customtkinter.CTkEntry(self.card, width=150, height=15)
        self.brfsttxt.insert(0,self.calories)
        self.brfsttxt.grid(row=1, column=1, pady = 10)
        
        self.lunchlbl = customtkinter.CTkLabel(self.card,text=" Lunch Calories: ").grid(row=2, column=0, pady = 10)
        self.lunchtxt = customtkinter.CTkEntry(self.card,width=150, height=15)
        self.lunchtxt.insert(0,self.calories)
        self.lunchtxt.grid(row=2, column=1, pady = 10)
        
        self.dinnerlbl = customtkinter.CTkLabel(self.card,text=" Dinner Calories: ").grid(row=3, column=0, pady = 10)
        self.dinnertxt = customtkinter.CTkEntry(self.card,width=150, height=15)
        self.dinnertxt.insert(0,self.calories)
        self.dinnertxt.grid(row=3, column=1, pady = 10)
        
        self.snacklbl = customtkinter.CTkLabel(self.card,text=" Snack Calories : ").grid(row=4, column=0, pady = 10)
        self.snacktxt = customtkinter.CTkEntry(self.card,width=150, height=15)
        self.snacktxt.insert(0,self.calories)
        self.snacktxt.grid(row=4, column=1, pady = 10)
        
        #Total of all calories entered for this date
        self.totlbl = customtkinter.CTkLabel(self.card,text=" Total Daily Calories : ").grid(row=5, column=0, pady = 10)
        self.totlbl1 = customtkinter.CTkLabel(self.card,text="700", anchor="w").grid(row=5, column=1, pady = 10)
 
        #update calorie information
        self.updatecal = customtkinter.CTkButton(self.home, text="Update",  hover=True, command=self.getcalselection)
        self.updatecal.grid(row=2, column=2,padx=10, pady=10, sticky="n")

    def getcalselection(self):
        self.seldate = self.selcalendar.selection_get()
        self.seldate_label= customtkinter.CTkLabel(self.card,height=30, corner_radius=5,fg_color="black",font=("Arial",15),
                                                   text=( f"Date Selected: {self.seldate}"))
        self.seldate_label.grid(row=0, columnspan=2, pady=20, padx=10)
        
    def display_calendar(self):
        #Initialize the calendar
        now = datetime.now()
        self.selcalendar = Calendar(self.home, showweeknumbers=False, selectmode = 'day',  year = now.year, 
                    month = now.month, day = now.day)
        self.selcalendar.grid(row=1,column=0, pady=10, padx=20, sticky="ns")
        
        #load the calorie block with the current date
        self.getcalselection()

        # date select button
        self.sel_date = customtkinter.CTkButton(self.home, text="Select Date",  hover=True, command=self.getcalselection)
        self.sel_date.grid(row=2, column=0,padx=10, pady=10, sticky="n")

        
    def loadtitle(self, name):
        self.title('Calorie Counter App | ' + name)

    def saveprefs(self):
        self.pd.updateuser(self.fname.get(), self.lname.get())      

    def display_home(self):
        self.loadtitle("Home")
        
        self.navbar.grid_forget()
        self.home = customtkinter.CTkFrame(self, fg_color="black")
        self.home.grid_columnconfigure(0, weight=1)
        self.home.grid(row=0, column=0, )
        customtkinter.CTkLabel(self.home,height=30, corner_radius=5, font=("Arial",20), 
                               fg_color=self.titlebgcolor, text_color=self.titletextcolor,width=250, text="Home").grid(row=0, columnspan=3 ,pady=20,padx=20, sticky="ew")
                # initialize the card frame
        
        #CREATES THE calories card frame
        self.card = customtkinter.CTkFrame(self.home)
        self.card.grid(row=1, column=1, columnspan=2, padx = 20, pady = 20, ipadx=10,sticky="nsew")
        self.card.columnconfigure((0,1,), weight=0)
        self.display_calendar()
        self.display_calorietrackercard()    
        
        
        #navigate back to the navbar
        self.ldnav = customtkinter.CTkButton(self.home, text="Main Menu",  hover=True, fg_color="green", command=lambda: self.reloadnavbar("Home"))
        self.ldnav.grid(row=2, column=1,padx=10, pady=10, sticky="n")
        
    def display_info(self):
        #Initialize the information window
        self.loadtitle("Info")
        
        self.navbar.grid_forget()
        self.info = customtkinter.CTkFrame(self, fg_color="black")
        self.info.grid_columnconfigure(0, weight=1)
        self.info.grid(row=0, column=0, )
        customtkinter.CTkLabel(self.info,height=30, corner_radius=5, font=("Arial",20), 
                               fg_color=self.titlebgcolor, text_color=self.titletextcolor,width=250, text="Info").grid(row=0, columnspan=3 ,pady=20,padx=20, sticky="ew")
        
        # body of form
        scroll_text = scrolledtext.ScrolledText(self.info, wrap = WORD, width = 50, height = 15)
        scroll_text.grid(columnspan=2, padx = 10, pady = 10, sticky="ew")
        scroll_text.tag_config('header')

        #navigate back to the navbars
        self.ldnav = customtkinter.CTkButton(self.info, text="Main Menu",  hover=True, fg_color="green", command=lambda: self.reloadnavbar("Info"))
        self.ldnav.grid(row=2, columnspan=2,padx=10, pady=10, sticky="n")

    def display_preferences(self):
        #loads user
        self.dbfname, self.dblname = self.pd.getuser()
        
        #Initialize Preferences
        self.loadtitle("Preferences")
        self.navbar.grid_forget()
        self.preferences = customtkinter.CTkFrame(self, fg_color="black")
        self.preferences.grid(row=0, column=0,ipadx=10)
        customtkinter.CTkLabel(self.preferences,height=30, corner_radius=5, font=("Arial",20), 
                               fg_color=self.titlebgcolor, text_color=self.titletextcolor, text="Preferences").grid(row=0, columnspan=2 ,pady=20,padx=20, sticky="ew")
        #Load the form with data
        self.fname_lbl = customtkinter.CTkLabel(self.preferences , width=120, text=" First Name: ",).grid(row=1, column=0, pady = 10, sticky="w")
        self.fname = customtkinter.CTkEntry(self.preferences, width=175, height=15, border_width=2)
        self.fname.insert(0,self.dbfname)
        self.fname.grid(row=1, column=1, pady = 10, sticky="w")
        
        self.lname_lbl = customtkinter.CTkLabel(self.preferences, width=120,text=" Last Name: ").grid(row=2, column=0, pady = 10, sticky="w")
        self.lname = customtkinter.CTkEntry(self.preferences, width=175, height=15,border_width=2)
        self.lname.insert(0,self.dblname)
        self.lname.grid(row=2, column=1, pady = 10,sticky="w")
        
        self.totlbl = customtkinter.CTkLabel(self.preferences, text="", height = 20)
        self.totlbl.grid(row=4, columnspan=2)        

        #update Preferences
        #navigate back to the navbar
        self.ldnav = customtkinter.CTkButton(self.preferences, text="Main Menu",  hover=True,  fg_color="green", command=lambda: self.reloadnavbar("Preferences"))
        self.ldnav.grid(row=5, column=0,padx=10, pady=10)
        
        self.updatepref = customtkinter.CTkButton(self.preferences, text="Update",  hover=True, command=self.saveprefs)
        self.updatepref.grid(row=5, column=1,padx=10, pady=10)
        
    def display_wcalories(self):
        self.loadtitle("Weekly Calories")
        
        self.navbar.grid_forget()
        self.wcalories = customtkinter.CTkFrame(self, fg_color="black")
        self.wcalories.grid_columnconfigure(0, weight=1)
        self.wcalories.grid(row=0, column=0, )
        customtkinter.CTkLabel(self.wcalories,height=30, corner_radius=5, font=("Arial",20), 
                               fg_color=self.titlebgcolor, text_color=self.titletextcolor,width=250, text="Weekly Calories").grid(row=0, columnspan=3 ,pady=20,padx=20, sticky="ew")
        
        #navigate back to the navbar
        self.ldnav = customtkinter.CTkButton(self.wcalories, text="Main Menu",  hover=True, fg_color="green", command=lambda: self.reloadnavbar("WC"))
        self.ldnav.grid(row=2, columnspan=2,padx=10, pady=10, sticky="n")

    def create_navbar_buttons(self):
        fgcol = "black"

        self.home =customtkinter.CTkButton(self.navbar, height=40,  fg_color=fgcol, text = "Home", command = self.display_home)
        self.home.grid(padx = 10, pady = 20)
        
        self.wc =customtkinter.CTkButton(self.navbar, height=40,  fg_color=fgcol, text = "Weekly Calories", command = self.display_wcalories)
        self.wc.grid( padx = 10, pady = 20)
        
        self.pref=customtkinter.CTkButton(self.navbar, height=40,  fg_color=fgcol, text = "Preferences", command = self.display_preferences)
        self.pref.grid( padx = 10, pady = 20)
        
        self.information=customtkinter.CTkButton(self.navbar, height=40,  fg_color=fgcol, text = "Info", command = self.display_info)
        self.information.grid( padx = 10, pady = 20)
        
if __name__ == "__main__":
    app= App()
    app.mainloop()

