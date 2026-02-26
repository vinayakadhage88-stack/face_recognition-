import tkinter as tk
from tkinter import messagebox
import os
import subprocess

# Admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"


# ---------------- LOGIN FUNCTION ----------------
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        root.destroy()
        open_dashboard()
    else:
        messagebox.showerror("Error", "Invalid login")


# ---------------- DASHBOARD ----------------
def open_dashboard():
    dash = tk.Tk()
    dash.title("Face Attendance System")
    dash.geometry("400x350")

    tk.Label(dash, text="Dashboard", font=("Arial", 18, "bold")).pack(pady=20)

    tk.Button(dash, text="Register Student", width=20, height=2,
              command=run_register).pack(pady=10)

    tk.Button(dash, text="Start Attendance", width=20, height=2,
              command=run_attendance).pack(pady=10)

    tk.Button(dash, text="Export to Excel", width=20, height=2,
              command=run_export).pack(pady=10)

    tk.Button(dash, text="Exit", width=20, height=2,
              command=dash.destroy).pack(pady=10)

    dash.mainloop()


# ---------------- BUTTON ACTIONS ----------------
def run_register():
    subprocess.call(["python", "register_student.py"])


def run_attendance():
    subprocess.call(["python", "attendance.py"])


def run_export():
    subprocess.call(["python", "aexport_excel.py"])


# ---------------- LOGIN WINDOW ----------------
root = tk.Tk()
root.title("Admin Login")
root.geometry("350x250")

tk.Label(root, text="Admin Login", font=("Arial", 16, "bold")).pack(pady=15)

tk.Label(root, text="Username").pack()
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

tk.Button(root, text="Login", width=15, command=login).pack(pady=15)

root.mainloop()
