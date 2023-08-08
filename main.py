from tkinter import *
import time
import random
window = Tk()
window.geometry("1000x800")
window.title("Dev's typing test")
window.config(bg="yellow")

data_loaded = False
data = ""

def get_data():
    global text_data
    lines = open('data.txt').read().splitlines()
    for _ in range(10):
        myline = random.choice(lines)    
    text_data = Text()
    text_data.insert("1.0",myline)
    text_data.config(height=8, width=100,font=("Arial",15,"bold"))
    text_data.place(relx=0.5,rely=0.3,anchor=CENTER)
   
    
def highlight_text_blue(event):
    current_index = text_input_area.index(INSERT)
    text = text_input_area.get("1.0", "end-1c")
    text_input_area.tag_remove("highlight", "1.0", "end")
    for word in text.split():
        start_index = text.find(word)
        end_index = start_index + len(word)
        text_input_area.tag_add("highlight", f"1.0 + {start_index} chars", f"1.0 + {end_index} chars")
    text_input_area.tag_configure("highlight", background="blue")


def highlight_text_red(event):
    current_index = text_input_area.index(INSERT)
    text = text_input_area.get("1.0", "end-1c")
    text_input_area.tag_remove("highlight", "1.0", "end")
    for word in text.split():
        start_index = text.find(word)
        end_index = start_index + len(word)
        text_input_area.tag_add("highlight", f"1.0 + {start_index} chars", f"1.0 + {end_index} chars")
    text_input_area.tag_configure("highlight", background="red")

def reset_data():
   text_data.delete("1.0",END)
   text_input_area.delete("1.0",END)

#addint the text input area
text_input_area = Text(height=10,width=100,font=("Helvetica",15,"bold"))
text_input_area.place(relx=0.5,rely=0.5,anchor=CENTER)

start_image = PhotoImage(file="/Users/dhaivatpachchigar/Documents/python_personal_projects/typing_test/start_button.png")
start_button = Button(image=start_image, highlightthickness=0, command=lambda: [get_data(), start_typing_time()])
start_button.place(relx=0.2, rely=0.8, anchor=CENTER)


reset_image = PhotoImage(file="/Users/dhaivatpachchigar/Documents/python_personal_projects/typing_test/reset.png")
reset_button = Button(image=reset_image,highlightthickness=0,command=reset_data)
reset_button.place(relx=0.8,rely=0.8,anchor=CENTER)



def compare_text(event):
 

    user_input = text_input_area.get("1.0", "end-1c")
    original_text = text_data.get("1.0", "end-1c")

    # Compare user input and original text character by character
    for i, (user_char, original_char) in enumerate(zip(user_input, original_text)):
        if user_char == original_char:
            text_input_area.tag_add("highlight", f"1.0 + {i} chars", f"1.0 + {i + 1} chars")
            text_input_area.tag_configure("highlight", background="blue")
        else:
            text_input_area.tag_add("highlight", f"1.0 + {i} chars", f"1.0 + {i + 1} chars")
            text_input_area.tag_configure("highlight", background="red")
    if user_input == original_text:
        end_time = time.time()
        typing_time = end_time - start_time
        typing_speed = len(original_text) / (typing_time / 60)  # Characters per minute
        typing_speed_label.config(text=f"Typing Speed: {typing_speed:.2f} characters per minute")
    

text_input_area.bind("<Key>", compare_text)
def start_typing_time():
    global start_time
    start_time = time.time()
typing_speed_label = Label(text="", font=("Helvetica", 12))
typing_speed_label.place(relx=0.5, rely=0.9, anchor=CENTER)
    
window.mainloop()