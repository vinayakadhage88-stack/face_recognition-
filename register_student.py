import tkinter as tk
from tkinter import messagebox
import cv2
import os

def capture_face():
    name = name_entry.get()
    roll = roll_entry.get()

    if name == "" or roll == "":
        messagebox.showerror("Error", "Enter Name and Roll Number")
        return

    cap = cv2.VideoCapture(0)


    messagebox.showinfo("Instructions", "Press SPACE to capture face")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Capture Face", frame)

        key = cv2.waitKey(1)

        if key == 32:  # SPACE key
            if not os.path.exists("dataset"):
                os.makedirs("dataset")

            filename = f"dataset/{name}_{roll}.jpg"
            cv2.imwrite(filename, frame)
            messagebox.showinfo("Success", "Face Captured Successfully")
            break

        elif key == 27:  # ESC to cancel
            break

    cap.release()
    cv2.destroyAllWindows()


# GUI Window
root = tk.Tk()
root.title("Register Student")
root.geometry("350x250")

tk.Label(root, text="Register Student", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Student Name").pack()
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

tk.Label(root, text="Roll Number").pack()
roll_entry = tk.Entry(root)
roll_entry.pack(pady=5)

tk.Button(root, text="Capture Face", command=capture_face).pack(pady=20)

root.mainloop()
