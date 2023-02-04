import speech_recognition as sr

class Listener:
    def __init__(self):
        self.r = sr.Recognizer()
        self.m = sr.Microphone()
        print("A moment of silence, please...")
        with self.m as source: self.r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(self.r.energy_threshold))
    
    def listen(self):
        values = []
        try:
            print("Say something!")
            with self.m as source: audio = self.r.listen(source)
            print("Got it! Now to recognize it...")
            try:
                # recognize speech using Google Speech Recognition
                values = [
                    self.r.recognize_google(audio),
                    self.r.recognize_google(audio, language="la"),
                ]

                # we need some special handling here to correctly print unicode characters to standard output
                if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                    print(u"You said {}".format(values).encode("utf-8"))
                else:  # this version of Python uses unicode for strings (Python 3+)
                    print("You said {}".format(values))
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
        finally:
            return values
