import sys

import PySimpleGUIWx as sg

def simplegui():

    # All the stuff inside your window.
    layout = [
        [sg.Text("File:"),     sg.Text('deed')],
        [sg.Text("Title:"),    sg.InputText('Game of Thrones')],
        [sg.Text("Year:"),     sg.InputText(2013)],
        [sg.Text("Season:"),   sg.InputText(4), sg.Text("Episode:"), sg.InputText(1)],
        [sg.Text("Category:"), sg.InputText('episode')],
        [sg.Button('Ok'),      sg.Button('Cancel')]
    ]
    # Create the Window
    window = sg.Window('LegendasTV API', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        # if user closes window or clicks cancel
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        print('You entered ', values)

    window.close()

theme = "Native"

sg.LOOK_AND_FEEL_TABLE['Native'] = {
    'BACKGROUND': sg.COLOR_SYSTEM_DEFAULT,
    'TEXT':       sg.COLOR_SYSTEM_DEFAULT,
    'INPUT':      sg.COLOR_SYSTEM_DEFAULT,
    'TEXT_INPUT': sg.COLOR_SYSTEM_DEFAULT,
    'SCROLL':     sg.COLOR_SYSTEM_DEFAULT,
    'BUTTON':    (sg.COLOR_SYSTEM_DEFAULT, sg.COLOR_SYSTEM_DEFAULT),
    'PROGRESS':   sg.DEFAULT_PROGRESS_BAR_COLOR,
    'BORDER': 1,
    'SLIDER_DEPTH': 0,
    'PROGRESS_DEPTH': 0,
}
if theme == 'Native':
    sg.wx.NO_BORDER = 0  # No styling
    sg.DEFAULT_FONT = ("", -1)
else:
    sg.wx.NO_BORDER = sg.wx.BORDER_NONE
    sg.DEFAULT_FONT = ("Helvetica", 10)
sg.theme(theme)   # Add a touch of color

if __name__ == "__main__":
    simplegui()