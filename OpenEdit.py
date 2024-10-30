import tkinter as tk# import the tkinter for creating the gui
from tkinter import filedialog#opening file with gui with file dialogs
from tkinter import messagebox#to make warning if we use new file option
import os#os to open terminal,i used subprocess but it didn't worked!


def new_file(text_widget):
    if text_widget.get("1.0", tk.END).strip():
        confirm = messagebox.askyesno("Confirm New File", "Unsaved changes will be lost. Do you want to continue?")
        if not confirm:
            return  # Cancel the new file action if the we click "No"
    text_widget.delete("1.0", tk.END)

def save_file(text_widget):
#Function to save the contents of the editor to a fil20
    file_path = filedialog.asksaveasfilename(defaultextension="txt", filetypes=[("Text files", "*.txt"),("Python file","*.py"), ("C file","*c"),("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_widget.get("1.0", tk.END))

def open_file(text_widget):
    if text_widget.get("1.0", tk.END).strip():
        confirm = messagebox.askyesno("Confirm New File", "Unsaved changes will be lost. Do you want to continue?")
        if not confirm:
            return
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"),("Python file","*.py"), ("C file","*c"),("All files", "*.*")])
    if file_path:
        text_widget.delete("1.0", tk.END)
        with open(file_path, "r") as file:
            text_widget.insert(tk.END, file.read())

def auto_close(event):
    #Function to automatically close () and " "
    symbol_pairs = {'(': ')', '[': ']', '{': '}', '"': '"', "'": "'"}
    char = event.char
    if char in symbol_pairs:
        text_edit.insert("insert", symbol_pairs[char])
        text_edit.mark_set("insert", "insert-1c")#puts cursor back in()

def open_cmd():
    #Function to open cmd.exe
    try:
        os.startfile("cmd.exe")
    except Exception as e:
        print(f"An error occurred: {e}")

def toggle_theme():
    global dark_theme
    if dark_theme:
        window.config(bg="white")
        text_edit.config(bg="white", fg="black", insertbackground="sky blue")
        theme_button.config(bg="lightgrey", fg="black", text="Dark Theme")
    else:
        window.config(bg="black")
        text_edit.config(bg="black", fg="white", insertbackground="sky blue")
        theme_button.config(bg="darkgrey", fg="white", text="Light Theme")
    dark_theme = not dark_theme

def adjust_text_size(size):
    #Function for adjusting the font size of the text
    text_edit.config(font=("Courier", int(size)))#here you can change the font type, like i have used Courier

def main():
    global text_edit
    global theme_button
    global dark_theme
    global window
    
    dark_theme = False#set it True if you want to text editor to have dark theme on startup

    window = tk.Tk()
    window.title("OpenEdit")
    window.attributes("-fullscreen", False)
    """
    keyboard shortcuts for common actions (Save: Ctrl+S, Open: Ctrl+O, New: Ctrl+N)
    uncomment keyboard shortcut for new file
    i have accidents pressing wrong button so i commented it
    """

    #window.bind("<Control-n>", lambda event: new_file(text_edit))
    #uncomment above line, some like key bind to make new file
    window.bind("<Control-s>", lambda event: save_file(text_edit))
    window.bind("<Control-o>", lambda event: open_file(text_edit))
    window.bind("<Control-Shift-T>", lambda event: open_cmd())

    button_frame = tk.Frame(window)
    button_frame.pack(side=tk.BOTTOM, anchor='sw', padx=2)

    new_button = tk.Button(button_frame, text="New", command=lambda: new_file(text_edit))
    new_button.pack(side=tk.LEFT, padx=2)

    save_button = tk.Button(button_frame, text="Save", command=lambda: save_file(text_edit))
    save_button.pack(side=tk.LEFT, padx=2)

    open_button = tk.Button(button_frame, text="Open", command=lambda: open_file(text_edit))
    open_button.pack(side=tk.LEFT, padx=2)

    terminal_button = tk.Button(button_frame, text="Terminal", command=open_cmd)
    terminal_button.pack(side=tk.LEFT, padx=2)

    theme_button = tk.Button(button_frame, text="Dark Theme", command=toggle_theme)
    theme_button.pack(side=tk.LEFT, padx=2)

    text_size_slider = tk.Scale(button_frame, from_=10, to=35, orient='horizontal', label="Text Size", command=adjust_text_size)
    text_size_slider.set(12)
    text_size_slider.pack(side=tk.BOTTOM,padx=5 ,ipadx=5)

    text_edit = tk.Text(window, font="Terminal", insertbackground="sky blue", insertwidth=3, insertontime=400, insertofftime=300)
    #you can change the inserton and insert off time according to your preferences, i had set it to zero because i don't like cursor to blink but now for project i have changed it to 400 and 300 respectively :}
    text_edit.config(blockcursor=True)#using block cursor
    text_edit.pack(expand=True, fill="both")
    text_edit.bind("<Key>", auto_close)
    
    window.mainloop()#keeps the window open
#main funtion
main()
