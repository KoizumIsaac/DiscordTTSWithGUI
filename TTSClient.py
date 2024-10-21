#TTSClient.py

import PySimpleGUI as sg
import pyttsx3

#Initialize Window
sg.theme("DarkAmber")
window = sg.Window(title="TTSForDisord", layout=[
  [sg.Text("Enter the text you want to TTS: ")],
  [sg.Input(s=25)],
  [sg.Button("TTS", key="TTSButtonPressed"), sg.Button("Exit", key="Exit")]
  ], 
  margins=(200,150))

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