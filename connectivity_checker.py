import tkinter as tk
from tkinter import messagebox
import requests

def check_website():
    url = url_entry.get()
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url
    try:
        response = requests.get(url)
        if response.status_code == 200:
            messagebox.showinfo("Website Status", f"{url} is reachable.")
        else:
            messagebox.showerror("Website Status", f"{url} is not reachable. Status code: {response.status_code}")
    except requests.ConnectionError:
        messagebox.showerror("Connection Error", f"Could not connect to {url}. Check your internet connection or the website URL.")

# Create main window
root = tk.Tk()
root.title("Website Connectivity Checker")

# Create URL entry
url_label = tk.Label(root, text="Enter Website URL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Create Check button
check_button = tk.Button(root, text="Check Connectivity", command=check_website)
check_button.pack()

# Run the GUI
root.mainloop()
