# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 17:02:46 2021

@author: wooihaw
"""
# Create a GUI for QR code generator

import PySimpleGUI as sg
import pyqrcode

layout = [
    [sg.Text('Enter text to be encoded')],
    [sg.InputText(key='-IN-')],
    [sg.Button('Generate'), sg.Button('Save', disabled=True), sg.Button('Exit')],
]

window = sg.Window('QR Code Generator', layout)

while True:
    event, values = window.read()
    if event in ['Exit', sg.WIN_CLOSED]:
        break

window.close()