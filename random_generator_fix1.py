import random
import time
import threading

def random_number_generator(stop_flag):
    while not stop_flag.is_set():
        random_number = random.randint(1, 100)
        print(f"Random number: {random_number}")
        time.sleep(1)

def prompt_and_stop(stop_flag):
    while True:
        user_input = input("Enter 'q' to quit: ")
        if user_input.lower() == 'q':
            stop_flag.set()  # Set the stop flag to signal the generator to stop
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    stop_flag = threading.Event()  # Create a threading event to act as the stop flag

    # Start the random number generator in a separate thread
    thread = threading.Thread(target=random_number_generator, args=(stop_flag,))
    thread.start()

    # Start the prompt and stop function
    prompt_and_stop(stop_flag)