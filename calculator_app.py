# Tkinter is a built-in Python library for making windows and buttons.
# No need to install anything!
import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")  # width x height in pixels
window.configure(bg="#1e1e1e")

# Label to show "History" heading
tk.Label(window, text="History", bg="#1e1e1e", fg="gray", font=("Arial", 12)).pack()

# Listbox to display past calculations
history_box = tk.Listbox(window, font=("Arial", 12), bg="#333333", fg="white",
                         bd=0, height=4, selectbackground="#555555")
history_box.pack(fill="x", padx=10)

# Entry is a text input box — we'll use it as the calculator display
display = tk.Entry(window, font=("Arial", 24), justify="right", bd=10, bg="#333333", fg="white", insertbackground="white")

display.pack(fill="x")  # fill="x" stretches it across the full width

# This function runs when a button is clicked.
# It adds the button's text to the display.
def button_click(value):
    if value == "=":
        calculate()
    else:
        display.insert("end", value)

def calculate():
    try:
        expression = display.get()
        answer = eval(expression)
        history_box.insert(0, f"{expression} = {answer}")
        display.delete(0, "end")
        display.insert(0, str(answer))
    except:
        display.delete(0, "end")
        display.insert(0, "Error")

def clear():
    display.delete(0, "end")

#Create a frame to hold the buttons
button_frame = tk.Frame(window, bg="#1e1e1e")

button_frame.pack()

# List of buttons in order, row by row
buttons = [ 
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
 ]

# Loop through the list and create each button
for i, btn in enumerate(buttons):
    if btn in ["/", "*", "-", "+"]:
        color = "#FF9500"  # orange for operators
    elif btn == "=":
        color = "#4CAF50"  # green for equals
    else:
        color = "#333333"  # dark gray for numbers

    tk.Button(button_frame, text=btn, font=("Arial", 18), width=5, height=2,
              fg="white", bg=color, activebackground=color,
              command=lambda v=btn: button_click(v)).grid(row=i//4, column=i%4)

tk.Button(window, text="Clear", font=("Arial", 18), width=16, height=2,
        fg="white", bg="#FF3B30", activebackground="#FF3B30", command=clear).pack()

# This line starts the window and keeps it open.
# It must always be the LAST line.
window.mainloop()
