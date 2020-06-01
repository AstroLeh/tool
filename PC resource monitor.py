import PySimpleGUI as sg
import psutil

theme = 'Green'

choices = ('DarkBlue', 'LightPurple', 'DarkTeal10', 'DarkAmber', 'DarkGreen6', 'GreenMono', 'DarkGreen6')



layout_t1 =[[sg.Text('What theme you want to use?')],
            [sg.Listbox(choices, size=(15, len(choices)), key='-COLOR-')],
            [sg.Button('Show theme')],
            [sg.Button('Start monitor', button_color=('white', 'firebrick4'))]]
 
layout_t2 = [[sg.T('This is inside tab 2')],    
               [sg.In(key='in1')]]    

layout_t3 = [[sg.T('This is in developer tab ')],
               [sg.Button('Read')],    
               [sg.In(key='in2')]]     

layout = [[sg.TabGroup([[sg.Tab('PC monitoring', layout_t1, tooltip='You may monitor your pc resources here'), sg.Tab('Themes', layout_t2, tooltip='tip'), sg.Tab('Developer', layout_t3)]], tooltip='TIP2')]] 

window = sg.Window('MDM Tool', layout, no_titlebar=True)

while True:                  # the event loop
    event, values = window.read()
    if event == 'Read':
        print(values)
    if event is None or event == 'Start monitor':
        theme = values['-COLOR-'][0]
        break
    if event == 'Show theme':
        theme = values['-COLOR-'][0]
        sg.ChangeLookAndFeel(theme)
        if values['-COLOR-']:    # if something is highlighted in the list
            sg.popup(f"PC resource monitor will use theme {values['-COLOR-'][0]}")
window.close()

# ----------------  Create Window  ----------------
sg.ChangeLookAndFeel(theme)
layout = [[sg.Text('PC resource monitor')] ,
          [sg.Text('', size=(12, 3), font=('Helvetica', 16), justification='center', key='text')],
          [sg.Exit(button_color=('white', 'firebrick4'), pad=((15, 0), 0)),
           sg.Spin([x + 1 for x in range(10)], 1, key='spin')]]

window = sg.Window('Running Timer', layout, no_titlebar=True, auto_size_buttons=False, alpha_channel=.9, keep_on_top=True,
                   grab_anywhere=True)

# ----------------  main loop  ----------------
while (True):
    # --------- Read and update window --------
    event, values = window.read(timeout=0)

    # --------- Do Button Operations --------
    if event is None or event == 'Exit':
        break
    try:
        interval = int(values['spin'])
    except:
        interval = 1

    cpu_percent = psutil.cpu_percent(interval=interval)
    ram_percent = psutil.virtual_memory()[2]

    # --------- Display timer in window --------

    window['text'].update(f'CPU {cpu_percent:02.1f}%   RAM {ram_percent:02.1f}%')
# Broke out of main loop. Close the window.
window.close()