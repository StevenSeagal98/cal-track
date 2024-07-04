from tkinter import *
from tkinter import scrolledtext
from tkcalendar import Calendar

from globals import *
from data.dataReadWrite import *

from datetime import datetime

# views
from views.main import windows

# Set initial window state
current_window = 'main'

root = Tk()
root.geometry('800x600')

# Create the main container frames
container = Frame(root)
container.pack(fill = 'both', expand = True)

# Create the side navigation bar frame
navbar = Frame(container, bg = 'lightgray', width = 200)
navbar.pack(side = 'left', fill = 'y')

# Create the main content frame
main_content = Frame(container, bg = 'white')
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
            Label(main_content, text=widget['text']).pack()
        elif widget['type'] == 'button':
            Button(main_content, text=widget['text'], command = widget['command']).pack()
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
            card = Frame(main_content, bg = 'lightgrey', padx = 10, pady = 10)
            card.pack(fill = 'x', padx = 10, pady = 5)
            for child in widget['children']:
                Label(card, text = child['text']).pack(side = 'left')
            Button(card, text = 'View', command = lambda: print('Searching for: ', widget['date'])).pack(side = 'right')
        elif widget['type'] == 'calendar':
            now = datetime.now()
            Calendar(main_content, selectmode = 'day', year = now.year, month = now.month, day = now.day).pack(side = 'right')

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
        Button(navbar, text = btn['text'], command = btn['command']).pack(fill = 'x', padx = 5, pady = 5)

create_navbar_buttons()
set_current_window(current_window)

root.mainloop()
