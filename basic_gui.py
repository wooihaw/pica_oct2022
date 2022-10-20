import PySimpleGUI as sg

channels = tuple(range(1, 5))
vscales = ('100mV', '200mV', '500mV', '1V', '2V', '5V')
tscales = ('50us', '100us', '200us', '500us', '1ms', '2ms', '5ms')

text_size = (13, 1)
button_size = (6, 1)

layout = [  [sg.Text('Channel', size=text_size), sg.Combo(channels, default_value=channels[0], key='-channel-', expand_x=True)],
            [sg.Text('Vertical scale', size=text_size), sg.Combo(vscales, key='-vscale-', default_value=vscales[3], expand_x=True)],
            [sg.Text('Vertical Offset', size=text_size), sg.Slider(range=(-5.0, 5.0), default_value=0.0, resolution=0.1, orientation='h', key='-voffset-', expand_x=True)],
            [sg.Text('Timebase scale', size=text_size), sg.Combo(tscales, key='-tscale-', default_value=tscales[3], expand_x=True)],
            [sg.Text('Timebase position', size=text_size), sg.Slider(range=(-5.0, 5.0), default_value=0.0, resolution=0.1, orientation='h', key='-tpos-', expand_x=True)],
            [sg.Button('Send', size=button_size), sg.Button('Close', size=button_size)]
]

window = sg.Window('Oscilloscope', layout, element_justification='center')

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Close'):
        break

window.close()