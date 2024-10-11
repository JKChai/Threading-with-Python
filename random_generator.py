import threading
import random
import time

def random_number_generator():
    while True:
        random_number = random.randint(1, 100)
        print(f"Random number: {random_number}")
        time.sleep(1)

def prompt_and_stop():
    while True:
        user_input = input("Enter 'q' to quit: ")
        if user_input.lower() == 'q':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    # Start the random number generator in a separate thread
    thread = threading.Thread(target=random_number_generator)
    thread.start()

    # Start the prompt and stop function
    prompt_and_stop()