import pyaudio
import wave
import speech_recognition as sr
import subprocess
from commands import Commander

running = True

def say(text):
    subprocess.call('echo ' + text + ' | cscript "C:\Program Files\Jampal\ptts.vbs"', shell=True)
    #subprocess.call(text, shell=True)

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()


r = sr.Recognizer()
cmd = Commander()

def initSpeech():
    print("Listening...")

    play_audio("./notification_sound/Alesis-Fusion-Nylon-String-Guitar-C4.wav")

    with sr.Microphone() as source:
       # r.adjust_for_ambient_noise(source, duration=1)
        print("Say Something")
        audio = r.listen(source)
    play_audio("./notification_sound/Alesis-Fusion-Nylon-String-Guitar-C4.wav")

    command = ""

    try:
        command = r.recognize_google(audio)
    except:
        print("Couldn't understand you")

    print("Your command:")
    print(command)
    if command in ["quit", "exit", "bye", "goodbye"]:
        global running
        running = False
    else:
        cmd.discover(command)

#    say(command)

while running == True:
    initSpeech()


