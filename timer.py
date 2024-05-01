import tkinter as tk
from tkinter import messagebox
import time

class CountdownTimer:
    def __init__(self, root):
        # Initialize the timer GUI
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("300x200")

        # Label to display the time remaining
        self.time_label = tk.Label(root, text="00:00", font=("Helvetica", 48))
        self.time_label.pack(pady=20)

        # Button to start the timer
        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)

        # Button to stop/pause the timer
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        # Initialize timer variables
        self.time_remaining = 0
        self.running = False

    def start_timer(self):
        # Start the timer
        if not self.running:
            self.time_remaining = 60  # 1 minute
            self.running = True
            self.update_time()
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)

    def stop_timer(self):
        # Stop/pause the timer
        if self.running:
            self.running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def update_time(self):
        # Update the time display every second
        if self.running:
            minutes = self.time_remaining // 60
            seconds = self.time_remaining % 60
            time_str = "{:02d}:{:02d}".format(minutes, seconds)
            self.time_label.config(text=time_str)
            if self.time_remaining > 0:
                self.time_remaining -= 1
                self.root.after(1000, self.update_time)  # Schedule the next update after 1 second
            else:
                # Timer has reached 00:00
                self.running = False
                messagebox.showinfo("Time's Up!", "The countdown timer has ended.")
                self.time_label.config(text="00:00")
                self.start_button.config(state=tk.NORMAL)
                self.stop_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    # Create and run the timer application
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()
