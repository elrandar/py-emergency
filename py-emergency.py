"""The main entry point"""

import pash.misc, pash.cmds, sys, signal, time
from argparse import ArgumentParser

from lib import cmd, params
import sys
import glob

# import PySimpleGUIWx as sg
import PySimpleGUI as sg

def set_theme():
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
    sg.theme(theme)   # Add a touch of color

def get_file_list():
    return glob.glob('*.mp3')


def simplegui(inputs, outputs):
    # All the stuff inside your window.
    set_theme()
    files = get_file_list()

    tab_params_layout = [
        [sg.Text('Input', size=(5, 1)), sg.Combo(values=inputs, size=(30, 1), default_value=inputs[0], key='input')],
        [sg.Text('Output', size=(5, 1)), sg.Combo(values=outputs, size=(30, 1), default_value=outputs[0], key='output')],
        [sg.Button('Start Loopback')],
        [sg.Text('File to play'), sg.Combo(values=files, size=(25, 1), default_value=files[0] if len(files) != 0 else "", key = 'file')]
        ]
    tab_exec_layout = [
        [sg.Text('Volume level'), sg.Spin([i for i in range(1,11)], initial_value=1, size=(25, 1), key='volume')],
        [sg.Button('Send message', button_color='red', size=(30, 30))]
    ]

    layout = [[sg.TabGroup([[sg.Tab('Main', tab_exec_layout), sg.Tab('Configuration', tab_params_layout)]])]]
    # Create the Window
    window = sg.Window('py-emergency', layout, size=(300,300), resizable=False)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        # if user closes window or clicks cancel
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'Send message':
            sound = [values['file'], str(values['volume'])]
            cmd.on_start_sound(None, sound, sound, None)
        elif event == 'Start Loopback':
            cmd.on_start_input(None, None, int(values['input'][:2]), None)
            cmd.on_start_output(None, None, int(values['output'][:2]), None)
            cmd.on_start(None, None, None)
    window.close()
    cmd.on_exit(None, None)

def main():
    inputs, outputs = cmd.on_show_devices(None, None, None)

    simplegui(inputs,outputs)
    return

if __name__ == '__main__':
    main()