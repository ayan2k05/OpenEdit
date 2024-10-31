import tkinter as tk## import the tkinter for creating the gui
from tkinter import filedialog#opening file with gui with file dialogs
from tkinter import messagebox #to make warning if we use new file option
import os#os to open terminal,i used subprocess but it didn't worked!

def new_file(text_widget):
    if text_widget.get("1.0", tk.END).strip():
        confirm = messagebox.askyesno("Confirm New File", "Unsaved changes will be lost. Do you want to continue?")
        if not confirm:
            return # Cancel the new file action if the we click "No"
    text_widget.delete("1.0", tk.END)
    
def save_file(text_widget):
    #Function to save the contents of the editor to a file
    file_path = filedialog.asksaveasfilename(defaultextension="txt", filetypes=[("Python file", "*.py"), ("C file", "*c"),("C++","*cpp"),("Java",".*jar"),("Text files", "*.txt"),  ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_widget.get("1.0", tk.END))

def open_file(text_widget):
    #Function to open the contents of other file
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("Python file", "*.py"), ("C file", "*c"), ("All files", "*.*")])
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
        text_edit.mark_set("insert", "insert-1c")#puts the cursor back in ()

def open_cmd():
    #Function to open cmd.exe
    try:
        os.startfile("cmd.exe")
    except Exception as e:
        print(f"An error occurred: {e}")

def toggle_theme():
    global is_dark_theme
    if is_dark_theme:
        window.config(bg="#dae6da")
        text_edit.config(bg="#f8fdf8", fg="#3b3b3b", insertbackground="#4a90e2")
        line_numbers.config(bg="#c5d6c5", fg="#4b4b4b")
        button_frame.config(bg="#dae6da")
        theme_button.config(bg="#c5d6c5", fg="#3b3b3b", text="Dark Theme")

        # Set color for all buttons in light theme
        for button in all_buttons:
            button.config(bg="#c5d6c5", fg="#3b3b3b")
    else:
        window.config(bg="#1e1e1e")
        text_edit.config(bg="#2e2e2e", fg="#dcdcdc", insertbackground="#4a90e2")
        line_numbers.config(bg="#3a3a3a", fg="#dcdcdc")
        button_frame.config(bg="#1e1e1e")
        theme_button.config(bg="#3a3a3a", fg="#dcdcdc", text="Light Theme")

        # Set color for all buttons in dark theme
        for button in all_buttons:
            button.config(bg="#3a3a3a", fg="#dcdcdc")
    is_dark_theme = not is_dark_theme

    """
    Toggles the application's theme between light and dark modes.

    ~~~~~~~~~~~~~~~Light Theme Colors:
    --> Background: #dae6da (window), #f8fdf8 (text editor), #c5d6c5 (line numbers), #dae6da (button frame)
    --> Foreground: #3b3b3b (text editor text), #4b4b4b (line numbers text), #3b3b3b (theme button text)
    --> Insert Background: #4a90e2 (text cursor)
    --> Button Background: #c5d6c5 (all buttons)

    ~~~~~~~~~~~~~~~Dark Theme Colors:
    --> Background: #1e1e1e (window), #2e2e2e (text editor), #3a3a3a (line numbers), #1e1e1e (button frame)
    --> Foreground: #dcdcdc (text editor text), #dcdcdc (line numbers text), #dcdcdc (theme button text)
    --> Insert Background: #4a90e2 (text cursor)
    --> Button Background: #3a3a3a (all buttons)

    I have stated all the colors and their logic, if you want to personalize, use google color picker
    """

def adjust_text_size(size):
    text_edit.config(font=("Courier", int(size)))
    line_numbers.config(font=("Courier", int(size)))
#Function for adjusting the font size of the text

def update_line_numbers(event=None):
    line_numbers.config(state="normal")
    line_numbers.delete("1.0", tk.END)
    for i in range(1, int(text_edit.index('end').split('.')[0])):
        line_numbers.insert(tk.END, f"✎{i}\n")#pencil mark copied from https://coolsymbol.com/
    line_numbers.config(state="disabled")

def main():
    global text_edit, theme_button, is_dark_theme, window, line_numbers, button_frame, all_buttons

    is_dark_theme = True #Set it to false if you want to start with Dark theme
    window = tk.Tk()
    window.title("OpenEdit")
    window.attributes("-fullscreen", False)

    """Key Binding or Shortcuts"""
    #window.bind("<Control-n>", lambda event: new_file(text_edit))
    """uncomment above line, some like key bind to make new file"""
    window.bind("<Control-s>", lambda event: save_file(text_edit))
    window.bind("<Control-o>", lambda event: open_file(text_edit))
    window.bind("<Control-Shift-T>", lambda event: open_cmd())

    button_frame = tk.Frame(window)
    button_frame.pack(side=tk.BOTTOM, anchor='sw', ipadx=2, ipady=1)

    #Buttons
    new_button = tk.Button(button_frame, text="New", command=lambda: new_file(text_edit))
    save_button = tk.Button(button_frame, text="Save ✔", command=lambda: save_file(text_edit))#Tick mark copied from https://coolsymbol.com/
    open_button = tk.Button(button_frame, text="Open", command=lambda: open_file(text_edit))
    terminal_button = tk.Button(button_frame, text="Terminal", command=open_cmd)
    theme_button = tk.Button(button_frame, text="Light Theme", command=toggle_theme)

    all_buttons = [new_button, save_button, open_button, terminal_button, theme_button]

    # packing all buttons
    for button in all_buttons:
        button.pack(side=tk.LEFT,ipadx=2, ipady=1)

    text_size_slider = tk.Scale(button_frame, from_=8, to=25, orient='horizontal', label="Text Size", command=adjust_text_size)
    text_size_slider.set(12)
    text_size_slider.pack(side=tk.LEFT, ipadx=2, ipady=1)

    line_numbers = tk.Text(window, width=4, padx=5, takefocus=0, border=0, background="darkgrey", state="disabled", font=("Terminal", 12))#state="disabled" = read-only
    line_numbers.pack(side=tk.LEFT, fill="y")

    text_edit = tk.Text(window, font="Courier", insertbackground="sky blue", insertwidth=2, insertontime=300, insertofftime=300)
    text_edit.config(blockcursor=True)#set False for | cursor
    text_edit.pack(expand=True, fill="both", side=tk.LEFT)
    text_edit.bind("<Key>", auto_close)
    text_edit.bind("<KeyRelease>", update_line_numbers)
    text_edit.bind("<MouseWheel>", update_line_numbers)

    update_line_numbers()#add new line index
    toggle_theme()#for theme

    window.mainloop()

main()
