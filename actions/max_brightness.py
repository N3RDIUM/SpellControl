# Python script to maximize brightness of the screen
import screen_brightness_control as sbc

def execute():
    # Get current brightness
    current_brightness = sbc.get_brightness()
    print(f"Current brightness: {current_brightness[0]}%", end=", ")

    # Max brightnes
    sbc.set_brightness(100)
    print("New brightness: 100%")

if __name__ == "__main__":
    execute()
