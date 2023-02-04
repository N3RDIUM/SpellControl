from listener import Listener
from config import FUZZ_MIN
from fuzzywuzzy import fuzz
import importlib
import json

# Initialize
listener = Listener()
with open('actions/index.json') as f:
    actions = json.load(f)

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

        # Execute the best match
        exec("""
import actions.{0}
actions.{0}.execute()
        """.format(actions[best_match]))
    except KeyboardInterrupt:
        break
