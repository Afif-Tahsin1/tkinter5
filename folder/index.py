import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
def show_popup():messagebox.showinfo("Photo Alert", "You clicked the photo alert button!")
def open_details_window():
    details_win = tk.Toplevel(root)
    details_win.title("Photo Details")
    details_win.geometry("300x180")
    details_label = tk.Label(details_win,text="Photo Name: img.png\nType: PNG Image\nResolution: 400x300",font=("Arial", 11),justify="left",)
    details_label.pack(pady=20)
    close_btn = tk.Button(details_win, text="Close", command=details_win.destroy)
    close_btn.pack(pady=5)
root = tk.Tk()
root.title("My Photo Album")
root.geometry("450x480")
title_label = tk.Label(root, text="My Photo Album", font=("Arial", 16, "bold"))
title_label.pack(pady=10)
raw_image = Image.open("img.png")
resized_image = raw_image.resize((350, 250))
album_photo = ImageTk.PhotoImage(resized_image)
image_label = tk.Label(root, image=album_photo)
image_label.image = album_photo
image_label.pack(pady=10)
popup_button = tk.Button(root, text="Show Alert", command=show_popup, width=15)
popup_button.pack(pady=5)
details_button = tk.Button(root, text="View Details", command=open_details_window, width=15)
details_button.pack(pady=5)
root.mainloop()