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
            print("\rWhat's the spell?", end="")
            with self.m as source: audio = self.r.listen(source, timeout=5, phrase_time_limit=5)
            print("\rGot it! Recognizing...", end="")
            try:
                # recognize speech using Google Speech Recognition
                values = [
                    self.r.recognize_google(audio, language="la"),
                ]
                if values[0] == "":
                    end = "\r"
                else:
                    end = "\n"
                print("\rRecognization complete!", end=end)
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
        finally:
            return values
