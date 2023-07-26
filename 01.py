import tkinter as tk
from customtkinter import CTkEntry

def get_table_data():
    table_data = []
    for row in range(1, len(data) + 1):
        row_data = []
        for col in range(len(headers)):
            entry = root.grid_slaves(row=row, column=col)[0]
            row_data.append(entry.get())
        table_data.append(row_data)
    return table_data

def handle_submit():
    table_data = get_table_data()
    # Perform desired actions with the table data
    print(table_data)

root = tk.Tk()
root.title("CustomTkinter Table")

headers = ["Name", "Age", "Email"]
for col, header in enumerate(headers):
    label = tk.Label(root, text=header, font=("Arial", 12, "bold"))
    label.grid(row=0, column=col, padx=10, pady=5)

data = [
    ["John Doe", "25", "johndoe@example.com"],
    ["Jane Smith", "30", "janesmith@example.com"],
    # Add more rows as needed
]

widths = [100, 50, 200]
for row, row_data in enumerate(data, start=1):
    for col, value in enumerate(row_data):
        entry = CTkEntry(root, width=widths[col])
        entry.insert(tk.END, value)
        entry.grid(row=row, column=col, 
                   padx=10, pady=5)

submit_button = tk.Button(root, text="Submit", 
                          command=handle_submit)
submit_button.grid(row=len(data) + 1, 
                   columnspan=len(headers), 
                   padx=10, pady=10)

root.mainloop()
