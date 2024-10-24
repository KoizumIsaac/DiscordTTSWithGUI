#TTSClient.py

import PySimpleGUI as sg
import pyttsx3
import sounddevice as sd
import soundfile as sf

#Setting up layout
first_column = [
    [sg.Text("Enter the text you want to TTS: ")],
    [sg.Input(s=25)],
    [sg.Button("TTS", key="TTSButtonPressed"), sg.Button("Exit", key="Exit")]
    ]

second_column = [
    [sg.Text("Volume:")],
    [sg.Slider((0,10), default_value=5, orientation='v', key="VolumeChanged", enable_events=True)]
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
engine.setProperty("volume", 0.5)
engine.setProperty("Rate",0.5)
engine.setProperty("voice", engine.getProperty("voices")[1].id)



audio_cable = sd.query_devices()[3]

def text_to_speech(text):
  engine.say(text)
  engine.save_to_file(text, "tempSpeech.wav")
  engine.runAndWait()

#Event Loop
while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED or event == "Exit":
    break
  if event == "TTSButtonPressed":
    text_to_speech(values[0])
  if event == "VolumeChanged":
    engine.setProperty('volume', values["VolumeChanged"]/10)

# Close the window
window.close()
engine.stop()
exit()