import tkinter as tk
import os

def show_files():
    files = os.listdir("attendance")
    for file in files:
        listbox.insert(tk.END, file)

root = tk.Tk()
root.title("Attendance Files")
root.geometry("300x300")

tk.Label(root, text="Attendance Records", font=("Arial", 14)).pack(pady=10)

listbox = tk.Listbox(root, width=30)
listbox.pack(pady=10)

tk.Button(root, text="Load Files", command=show_files).pack(pady=10)

root.mainloop()
