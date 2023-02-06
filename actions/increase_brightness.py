# Python script to increase brightness of the screen
import screen_brightness_control as sbc

def execute():
    # Get current brightness
    current_brightness = sbc.get_brightness()
    print(f"Current brightness: {current_brightness[0]}%", end=", ")

    # Increase brightness by 10%
    new_brightness = current_brightness[0] + 10
    if new_brightness > 100:
        new_brightness = 100
    sbc.set_brightness(new_brightness)
    print(f"New brightness: {new_brightness}%")

if __name__ == "__main__":
    execute()
