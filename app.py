from tkinter import *
from globals import *
from data.dataReadWrite import *
import json

# Set initial app state
current_window = 'main'

calorie_tracker_data = globals.calorie_tracker_data

windows = {
    'main': {
        'title': 'Home',
        'widgets': [
            {'type': 'label', 'text': 'Welcome to the Calorie Counter App!'},
            {'type': 'button', 'text': 'Enter Calories', 'command': lambda: set_current_window('enter_calories')},
            {'type': 'button', 'text': 'View Calories', 'command': lambda: set_current_window('list')},
            {'type': 'button', 'text': 'Preferences', 'command': lambda: set_current_window('preferences')},
        ]
    }
}

root = Tk()
root.geometry('800x600')

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def render_widgets(window):
    root.title('Calorie Counter App | ' + windows[window]['title'])
    clear_window()
    for widget in windows[window]['widgets']:
        if widget['type'] == 'label':
            Label(root, text=widget['text']).pack()
        elif widget['type'] == 'button':
            Button(root, text=widget['text'], command=widget['command']).pack()

def set_current_window(window):
    global current_window
    current_window = window
    render_widgets(current_window)

# Initial render
set_current_window(current_window)

# Print calorie tracker data for debugging
for day in calorie_tracker_data:
    obj_str = json.dumps(day, indent=4)
    print(obj_str)

root.mainloop()