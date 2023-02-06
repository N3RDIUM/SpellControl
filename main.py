from listener import Listener
from config import FUZZ_MIN
from fuzzywuzzy import fuzz
import os
import sys
import json
import subprocess

# update packages
os.system(f"{sys.executable} -m pip install -r requirements.txt")

# Initialize
listener = Listener()
with open('actions/index.json') as f:
    actions = json.load(f)
    
print(f"Your wand is ready! (Fuzz min: {FUZZ_MIN})")

# Mainloop
while True:
    try:
        values = listener.listen()
        for index, value in enumerate(values):
            values[index] = value.lower()

        # Compare values with actions and find the best match
        best_match = None
        best_match_value = 0
        for action in actions:
            for value in values:
                if fuzz.ratio(action, value) > FUZZ_MIN and fuzz.ratio(action, value) > best_match_value:
                    best_match = action
                    best_match_value = fuzz.ratio(action, value)
                    
        if best_match != None:
            print(f"I think you said: {best_match}")

            # Execute the best match
            if best_match != "":
                subprocess.run([sys.executable, f"actions/{actions[best_match]}.py"])
            print("")
    except KeyboardInterrupt:
        print("Goodbye!")
        sys.exit()
    except KeyError as e:
        e = str(e)
        if e != "" and e != "None":
            print(f"KeyError: {e}")
