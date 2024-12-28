import tkinter as tk

root = tk.Tk()
root.title("Frame Border Example")
root.geometry("300x200")

# Create a frame as a border
frame = tk.Frame(root, bd=5, relief="raised")
frame.pack(padx=20, pady=20)

# Place a widget inside the frame
label = tk.Label(frame, text="This label is inside a bordered frame")
label.pack(padx=10, pady=10)

root.mainloop()