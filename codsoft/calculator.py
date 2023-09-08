import tkinter as tk

def press(key):
    entry_text = entry.get()
    if key == '=':
        try:
            result = str(eval(entry_text))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif key == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, key)

# Create main window
root = tk.Tk()
root.title("Calculator")
root.config(bg='lightblue')  # Set the background color to light blue


# Entry field
entry = tk.Entry(root, font=('Arial', 20), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons for numbers and operations
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

# button_padding_x = 10
# button_padding_y = 10

for button in buttons:
    tk.Button(root, text=button, padx=30, pady=15, font=('Arial', 15), command=lambda b=button: press(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the GUI event loop
root.mainloop()
