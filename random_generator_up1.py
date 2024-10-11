import random
import time
import threading
from tkinter import Tk, Button, Label

def random_number_generator(stop_flag, label):
    while not stop_flag.is_set():
        random_number = random.randint(1, 100)
        label.config(text=f"Random number: {random_number}")
        time.sleep(1)

def stop_generator(stop_flag):
    stop_flag.set()

if __name__ == "__main__":
    stop_flag = threading.Event()

    # Create the Tkinter window
    root = Tk()
    root.title("Random Number Generator")

    # Create a label to display the random number
    label = Label(root, text="Random number: ")
    label.pack()

    # Create a button to stop the generator
    stop_button = Button(root, text="Stop", command=lambda: stop_generator(stop_flag))
    stop_button.pack()

    # Start the random number generator in a separate thread
    thread = threading.Thread(target=random_number_generator, args=(stop_flag, label))
    thread.start()

    # Start the Tkinter event loop
    root.mainloop()