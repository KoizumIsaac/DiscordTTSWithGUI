#TTSClient.py

import PySimpleGUI as sg
import pyttsx3

#Setting up layout
first_column = [
    [sg.Text("Enter the text you want to TTS: ")],
    [sg.Input(s=25)],
    [sg.Button("TTS", key="TTSButtonPressed"), sg.Button("Exit", key="Exit")]
    ]

second_column = [
    [sg.Text("Volume:")],
    [sg.Slider((0,10), orientation='v', key="VolumeChanged")]
    ]

#Initialize Window
sg.theme("DarkAmber")
window = sg.Window(title="TTSForDisord", layout=[
  [sg.Column(first_column),
  sg.VSeparator(pad=(0,0)),
  sg.Column(second_column)]
],
margins=(150,100))

#Initialize TTS
engine = pyttsx3.init()

#Event Loop
while True:
  event, values = window.read()
  # sg.Print(event, values)
  if event == sg.WIN_CLOSED or event == "Exit":
    break
  if event == "TTSButtonPressed":
     engine.say(values[0])
     engine.runAndWait()

# Close the window
window.close()
exit()