import tkinter

def miles_to_km():
    # Gets the text as a string from the input field.
    miles = float(miles_input.get())
    km = miles * 1.609
    # Changes the label's text.
    kilometer_result_label.config(text=f"{km}")

# Creates a window.
window = tkinter.Tk()
# Gives the window a title.
window.title("Mile to Km Converter")
# Gives the window padding.
window.config(padx=20, pady=20)

# Creates a text input.
miles_input = tkinter.Entry(width=7)
# Places the text input in the window at these grid coordinates.
miles_input.grid(column=1, row=0)

# Creates a label.
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = tkinter.Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = tkinter.Label(text="Km")
kilometer_label.grid(column=1, row=2)

# Creates a button.
calculate_button = tkinter.Button(text="Click Me", command=miles_to_km)
calculate_button.grid(column=2, row=1)

# Keeps the window on the screen.
window.mainloop()