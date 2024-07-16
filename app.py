from math import fabs
from tkinter import *

from tkinter import scrolledtext
from tkcalendar import Calendar

# MAK 7/9/2024
import customtkinter
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
import os
from PIL import ImageTk, Image
# end of MAK 7/9/2024


from globals import *
from data.dataReadWrite import *

from datetime import datetime

# views
from views.main import windows

# Set initial window state
current_window = 'main'

root = Tk()
root.geometry('800x600')

# Create the main container framess
container = customtkinter.CTkFrame(root)
container.pack(fill = 'both', expand = True)

# Create the side navigation bar frame
navbar = customtkinter.CTkFrame(container, corner_radius=0, fg_color="white" ,width = 250)
navbar.pack(side = 'left', fill = 'y')

# Create the main content frame
main_content = customtkinter.CTkFrame(container, fg_color="black")
main_content.pack(side = 'right', fill = 'both', expand = True)

def clear_window():
    for widget in main_content.winfo_children():
        widget.destroy()

def render_widgets(window):
    root.title('Calorie Counter App | ' + windows[window]['title'])
    clear_window()
    if(windows[window].get('update') is not None):
        windows[window]['update']()
    for widget in windows[window]['widgets']:
        if widget['type'] == 'label':
            print(widget['text'])
            customtkinter.CTkLabel(main_content,height=30, corner_radius=5, font=("Arial",20), fg_color="darkgrey", text_color="black",width=250, text=widget['text']).pack(pady=20)
        elif widget['type'] == 'button':
            customtkinter.CTkButton(main_content, text=widget['text'], command = widget['command']).pack()
        elif widget['type'] == 'scrolledtext':
            scroll_text = scrolledtext.ScrolledText(main_content, wrap = WORD, width = 50, height = 15)
            scroll_text.pack(padx = 10, pady = 10)
            scroll_text.tag_config('header')
            lines = widget['text'].strip().split('\n')
            for line in lines:
                if line.startswith('Header'):
                    scroll_text.insert(INSERT, line + '\n', 'header')
                else:
                    scroll_text.insert(INSERT, line + '\n')
            scroll_text.config(state = DISABLED)
        elif widget['type'] == 'calorie_tracker_card':
            card = customtkinter.CTkFrame(main_content)#, padx = 10, pady = 10)
            card.pack(fill = 'x', padx = 10, pady = 5)
            for child in widget['children']:
                  customtkinter.CTkLabel(card, text = child['text']).pack(side = 'left')
            customtkinter.CTkButton(card, text = 'View', command = lambda: print('Searching for: ', widget['date'])).pack(side = 'right')
        elif widget['type'] == 'calendar':
            now = datetime.now()
            Calendar(main_content, selectmode = 'day', year = now.year, month = now.month, day = now.day).pack(side = customtkinter.TOP, pady=30)
            
def set_current_window(window):
    global current_window
    current_window = window
    render_widgets(current_window)

def create_navbar_buttons():
    nav_buttons = [
        {'text': 'Home', 'command': lambda: set_current_window('main')},
        {'text': 'Today\'s Calories', 'command': lambda: set_current_window('current_day')},
        {'text': 'Preferences', 'command': lambda: set_current_window('preferences')},
        {'text': 'Info', 'command': lambda: set_current_window('info')}
    ]
    
    for btn in nav_buttons:
        # MAK 7/9/2024
        customtkinter.CTkButton(navbar, height=40,  fg_color="#13265c", text = btn['text'], command = btn['command']).pack(fill = 'x', padx = 10, pady = 12)
       # End of MAK changes

create_navbar_buttons()
set_current_window(current_window)

root.mainloop()
