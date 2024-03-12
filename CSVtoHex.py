import csv
import binascii
import tkinter as tk
from tkinter import filedialog, messagebox

def csv_to_hex_single(filename):
    with open(filename, 'r', encoding='utf-8') as file, open(filename + '.hex', 'w') as output_file:
        csv_data = file.read()
        hexadecimal_data = binascii.hexlify(csv_data.encode()).decode()
        output_file.write(hexadecimal_data)

def csv_to_hex_each(filename):
    def element_to_hex(element):
        return binascii.hexlify(element.encode()).decode()

    with open(filename, 'r', encoding='utf-8') as file, open(filename + '.hex', 'w') as output_file:
        csv_reader = csv.reader(file)
        hexadecimal_data = []
        for row in csv_reader:
            hex_row = [element_to_hex(element) for element in row]
            hexadecimal_data.append(hex_row)

        for row in hexadecimal_data:
            hex_row_string = ' '.join(row)
            output_file.write(hex_row_string + '\n')

def open_file():
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select CSV file",
        filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
    )
    if filename:
        return filename
    else:
        return None

def convert_to_hex_single():
    filename = open_file()
    if filename:
        csv_to_hex_single(filename)
        messagebox.showinfo("Conversion Successful!", f"Converted data saved to: {filename}.hex")
        #print(f"Converted data saved to: {filename}.hex")

def convert_to_hex_each():
    filename = open_file()
    if filename:
        csv_to_hex_each(filename)
        messagebox.showinfo("Conversion Successful!", f"Converted data saved to: {filename}.hex")
        #print(f"Converted data saved to: {filename}.hex")

# GUI
window = tk.Tk()
window.title("CSV Converter")

# Get screen width and height (optional for centering the window)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Get window width and height (assuming you have a fixed size window)
window_width = 300
window_height = 200

# Calculate x and y coordinates to center the window (optional)
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the window geometry with calculated coordinates (optional)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Buttons
single_button = tk.Button(window, text="Convert to hexadecimal(Single)", command=convert_to_hex_single)
single_button.pack(pady=10)

each_button = tk.Button(window, text="Convert to hexadecimal(Each)", command=convert_to_hex_each)
each_button.pack(pady=5)

# Event main loop
window.mainloop()
