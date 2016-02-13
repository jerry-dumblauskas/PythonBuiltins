"""
quick script to do the tabata protocol with Spotify
calling out to osascript, so this is mac os only :)
"""

import os
import time


def run_it():
    for _ in range(8):
        '''
        standard tabata time
        '''
        print("running: ", _ + 1)
        os.system('osascript -e \'tell application "Spotify" to play\'')
        time.sleep(20)
        print("sleeping")
        os.system('osascript -e \'tell application "Spotify" to pause\'')
        time.sleep(10)


if __name__ == "__main__":
    run_it()
