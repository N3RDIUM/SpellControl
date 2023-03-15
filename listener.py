# imports
import speech_recognition as sr

class Listener:
	"""
	Listener

	A class which listens for words spoken in Latin
	and returns them.
	"""
    def __init__(self):
		"""
		Initialize the listener
		"""
		# Create recognizer and microphone instances
        self.r = sr.Recognizer()
        self.m = sr.Microphone()

		# Calibrate the energy threshold for ambient noise levels
        print("A moment of silence, please...")
        with self.m as source: self.r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(self.r.energy_threshold))
    
    def listen(self):
		"""
		Listen for words spoken in Latin
		"""
        values = []
        try:
			# Prompt the user to start speaking
            print("\rWhat's the spell?", end="")
			# Listen for the user's input for 5 seconds
            with self.m as source: audio = self.r.listen(source, timeout=5, phrase_time_limit=5)
            print("\rGot it! Recognizing...", end="")

			# Now that we have the audio, 
			# we'll recognize it using Google Speech Recognition
            try:
				# For testing purposes, we're just using the default API key
                values = [
                    self.r.recognize_google(audio, language="la"),
                ]
                if values[0] == "": # If the user didn't say anything
                    end = "\r"
                else:
                    end = "\n" # If the user said something
                print("\rRecognization complete!", end=end)
            except sr.UnknownValueError:
                pass # If the user said something that wasn't in Latin
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
        finally:
			# This is pretty self-explanatory
            return values
