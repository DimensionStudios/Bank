import tkinter as tk

def toggle_light(event=None):
    # Check the current state and toggle
    if canvas.itemcget(toggle_circle, "fill") == "white":
        # Switch to ON state
        canvas.itemconfig(toggle_circle, fill="yellow")
        canvas.move(toggle_circle, 40, 0)  # Move circle to the right
        label.config(text="Light ON", fg="yellow")
        root.config(bg="yellow")
    else:
        # Switch to OFF state
        canvas.itemconfig(toggle_circle, fill="white")
        canvas.move(toggle_circle, -40, 0)  # Move circle to the left
        label.config(text="Light OFF", fg="gray")
        root.config(bg="gray")

# Create the main window
root = tk.Tk()
root.title("Light Toggle Switch")
root.geometry("300x150")
root.config(bg="gray")

# Label to display light status
label = tk.Label(root, text="Light OFF", font=("Arial", 14), bg="gray", fg="gray")
label.pack(pady=10)

# Canvas for the toggle switch
canvas = tk.Canvas(root, width=100, height=50, bg="gray", highlightthickness=0)
canvas.pack()

# Base rectangle (toggle track)
canvas.create_rectangle(10, 10, 90, 40, fill="lightgray", outline="")

# Toggle circle (switch knob)
toggle_circle = canvas.create_oval(12, 12, 38, 38, fill="white", outline="")

# Bind click event to the canvas
canvas.bind("<Button-1>", toggle_light)

# Start the main loop
root.mainloop()
