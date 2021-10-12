#Using the playsound module in python
#Can be used for both .mp3 and .wav files
#Using the threading module to run functions together and stop when done.
import playsound
import threading

def play():
    global running
    while running:
        playsound.playsound("flutetone.mp3")

def stop():
    _ = input("Press enter to Stop the tune:") 
    global running
    running = False
    print("The Tune will stop after it's duration now. Thanks!\n")

if __name__ == "__main__":
    running = True
    print("\nPlaying the sound...")
    threading.Thread(target=play).start()
    threading.Thread(target=stop).start()
