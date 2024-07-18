import keyboard
from winsound import Beep
import time

N_LAND_MARKERS = 3
REC_TIME = 1 * 60 + 30

GAME_LOAD_TIME = 10

print("Switch to the window now!")
time.sleep(10)

for active_mic in range(N_LAND_MARKERS):
    # Pan us over to the active microphone
    for _ in range(active_mic + 1):
        keyboard.press_and_release('F7')
        time.sleep(.1)

    Beep(1000,100) # Notify of start

    keyboard.press_and_release('escape') # Start the mission

    time.sleep(REC_TIME)

    Beep(500,100) # Notify of end

    keyboard.press_and_release('shift+r') # Restart the sim

    time.sleep(GAME_LOAD_TIME) # Wait for the sim to reset