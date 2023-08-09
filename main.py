from tkinter import *
import time
import random
from tkinter import messagebox

# Global variables
start_time = None
correct_words = 0

# Function to get new data and start the typing test
def get_data():
    global text_data, start_time
    lines = open('data.txt').read().splitlines()
    for _ in range(10):
        myline = random.choice(lines)    
    text_data = Text()
    text_data.insert("1.0", myline)
    text_data.config(height=8, width=100, font=("Arial", 15, "bold"), background="red")
    text_data.place(relx=0.5, rely=0.2, anchor=CENTER)
    start_time = time.time()

# Function to reset the typing test
def reset_data():
    text_data.delete("1.0", END)
    text_input_area.delete("1.0", END)
    update_speed_labels(0, 0)

# Function to update the speed labels
def update_speed_labels(cpm, wpm):
    speed_label.config(text=f"Speed: \n{cpm:.2f} CPM\n{wpm:.2f} WPM")

# Function to compare user input with the original text
def compare_text(event):
    global correct_words
    user_input = text_input_area.get("1.0", "end-1c")
    original_text = text_data.get("1.0", "end-1c")

    # Remove any previous highlighting
    text_input_area.tag_remove("highlight", "1.0", "end")

    # Compare user input and original text character by character
    correct_words = 0
    for i, (user_char, original_char) in enumerate(zip(user_input, original_text)):
        tag_name = "highlight_correct" if user_char == original_char else "highlight_wrong"
        tag_bg_color = "blue" if user_char == original_char else "red"
        text_input_area.tag_add(tag_name, f"1.0 + {i} chars", f"1.0 + {i + 1} chars")
        text_input_area.tag_configure(tag_name, background=tag_bg_color)

        if user_char == original_char and user_char.isspace():
            correct_words += 1

    elapsed_time = time.time() - start_time

    # Calculate CPM and WPM based on correct words
    cpm = (correct_words * 5) / elapsed_time * 60  # Assuming an average word length of 5 characters
    wpm = cpm / 5  # Assuming an average word length of 5 characters
    update_speed_labels(cpm, wpm)

# Function to show final stats in a pop-up box
def show_finish_stats():
    global start_time
    elapsed_time = time.time() - start_time
    cpm = (correct_words * 5) / elapsed_time * 60  # Assuming an average word length of 5 characters
    wpm = cpm / 5  # Assuming an average word length of 5 characters

    finish_message = f"Your final stats:\n\nCPM: {cpm:.2f}\nWPM: {wpm:.2f}"
    messagebox.showinfo("Typing Test Finish", finish_message)

# GUI setup
window = Tk()
window.geometry("1000x800")
window.title("Dev's typing test")
window.config(bg="yellow")

text_input_area = Text(height=10, width=100, font=("Helvetica", 15, "bold"), background="orange")
text_input_area.place(relx=0.5, rely=0.5, anchor=CENTER)

start_image = PhotoImage(file="start_button.png")
start_button = Button(image=start_image, highlightthickness=0, command=get_data)
start_button.place(relx=0.2, rely=0.8, anchor=CENTER)

reset_image = PhotoImage(file="reset.png")
reset_button = Button(image=reset_image, highlightthickness=0, command=reset_data)
reset_button.place(relx=0.8, rely=0.8, anchor=CENTER)

finish_button = Button(text="Finish", font=("Arial", 15, "bold"), command=show_finish_stats)
finish_button.place(relx=0.5, rely=0.9, anchor=CENTER)

speed_label = Label(text="Speed: \n0.00 CPS\n0.00 WPM")
speed_label.place(relx=0.5, rely=0.8, anchor=CENTER)

# Event bindings
text_input_area.bind("<Key>", compare_text)

# Start the GUI event loop
window.mainloop()
