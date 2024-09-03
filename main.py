from djitellopy import Tello
import time
from vosk import Model, KaldiRecognizer
import pyaudio

tello = Tello()
tello.connect()

model = Model(r"C:/Users/angel/OneDrive/Desktop/TelloDrone/vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()

listening = False

def get_command():
    listening = True
    stream = mic.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 8192)
    while listening:
        stream.start_stream()
        try:
            data = stream.read(4096)
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                response = result[14:-3]
                print(response)
                listening = False
                stream.close()
                return response
        except OSError:
            pass

def analyze_command(command):
    try:
        if command == "take off":
            tello.takeoff()
        elif command == "land":
            tello.land()
        elif command == "move up":
            tello.move_up(30)
        elif command == "move down":
            tello.move_down(30)
        elif command == "move right":
            tello.move_right(50)
        elif command == "move left":
            tello.move_left(50)
        elif command == "move forward":
            tello.move_forward()
        elif command == "move back":
            tello.move_back()
        elif command == "alpha":
            tello.flip_right()
        elif command == "beta":
            tello.flip_left()
        elif command == "gamma":
            tello.flip_back()
        elif command == "delta":
            tello.flip_forward()
        else:
            print("I dont understand that command")
        time.sleep(1)
    except Exception:
        pass


while True:
    print("Waiting for command...")
    command = get_command()
    analyze_command(command)


# stream = mic.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 8192)
# stream.start_stream()
# while True:
#     data = stream.read(4096)
#     if recognizer.AcceptWaveform(data):
#         text = recognizer.Result()
#         print(text[14:-3])

