import tkinter as tk
from tkinter import messagebox

# Default Admin Credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        messagebox.showinfo("Login Success", "Welcome Admin!")
        root.destroy()
        open_dashboard()
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

def open_dashboard():
    dashboard = tk.Tk()
    dashboard.title("Face Attendance System - Dashboard")
    dashboard.geometry("400x300")
    dashboard.configure(bg="#f0f0f0")

    tk.Label(dashboard, text="Dashboard", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=20)

    tk.Button(dashboard, text="Register Student", width=20, height=2).pack(pady=10)
    tk.Button(dashboard, text="Start Attendance", width=20, height=2).pack(pady=10)
    tk.Button(dashboard, text="View Attendance", width=20, height=2).pack(pady=10)

    dashboard.mainloop()


# Login Window
root = tk.Tk()
root.title("Admin Login")
root.geometry("350x250")
root.configure(bg="#e6f2ff")

tk.Label(root, text="Admin Login", font=("Arial", 16, "bold"), bg="#e6f2ff").pack(pady=15)

tk.Label(root, text="Username:", bg="#e6f2ff").pack()
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

tk.Label(root, text="Password:", bg="#e6f2ff").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

tk.Button(root, text="Login", width=15, command=login).pack(pady=15)

root.mainloop()
