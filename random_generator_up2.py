import random
import time
import threading
from tkinter import Tk, Label, Entry

def random_number_generator(stop_flag):
    while not stop_flag.is_set():
        random_number = random.randint(1, 100)
        print(f"Random number: {random_number}")
        time.sleep(1)

def prompt_and_stop(stop_flag, root):
    def stop_generator(event):
        stop_flag.set()
        root.destroy()

    # Create a label to display the prompt
    label = Label(root, text="Enter 'q' to quit:")
    label.pack()

    # Create an entry field for user input
    entry = Entry(root)
    entry.pack()

    # Bind the entry field to the stop_generator function
    entry.bind("<Return>", stop_generator)

if __name__ == "__main__":
    stop_flag = threading.Event()

    # Create the Tkinter window
    root = Tk()
    root.title("Random Number Generator")

    # Start the random number generator in a separate thread
    thread = threading.Thread(target=random_number_generator, args=(stop_flag,))
    thread.start()

    # Start the prompt and stop function
    prompt_and_stop(stop_flag, root)

    # Start the Tkinter event loop
    root.mainloop()