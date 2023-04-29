import tkinter as tk
from tkinter import filedialog

import parser


def select_file():
    input_file = filedialog.askopenfilename()
    input_label.config(text=input_file)


def submit():
    input_file = input_label.cget("text")
    output_name = output_entry.get()
    parser.parse(input_file, output_name)
    # print(f"Input file: {input_file}")
    # print(f"Output file name: {output_name}")


root = tk.Tk()

input_label = tk.Label(root, text="Select input file")
input_label.pack()

input_button = tk.Button(root, text="Select", command=select_file)
input_button.pack()

output_label = tk.Label(root, text="Enter output file name")
output_label.pack()

output_entry = tk.Entry(root)
output_entry.pack()

submit_button = tk.Button(root, text="Create SVG", command=submit)
submit_button.pack()

root.mainloop()
