import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import requests
import threading

def get_definition(word):
    if not word:
        return "Please enter a word."
    
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    if response.status_code == 200:
        data = response.json()
        if data:
            meanings = data[0]['meanings']
            definitions = []
            for meaning in meanings:
                definitions.append(f"• Meaning: {meaning['partOfSpeech']}\nDefinition: {meaning['definitions'][0]['definition']}\n")
            return '\n'.join(definitions)
        return "No definition found."
    else:
        return "Error fetching definition."

def search_definition():
    word = entry_word.get()
    loading_label.config(text="Searching... Please wait.", background='#f0f0f0')  # Set background color
    text_output.configure(state='normal')
    text_output.delete('1.0', tk.END)
    text_output.configure(state='disabled')
    
    # Run the search in a separate thread to prevent freezing the GUI
    search_thread = threading.Thread(target=perform_search, args=(word,))
    search_thread.start()

def perform_search(word):
    definition = get_definition(word)
    text_output.configure(state='normal')
    text_output.delete('1.0', tk.END)
    text_output.insert(tk.END, definition)
    text_output.configure(state='disabled')
    loading_label.config(text="", background='#f0f0f0')  # Clear the loading message and set background color back

root = tk.Tk()
style = Style(theme='darkly') # Specifying the 'darkly' theme
root.title("WORDY")
root.geometry("800x500")

# Get the background color of the search button
search_button_bg_color = style.lookup('TButton', 'background')

# Customize the Style object
style.configure('TFrame', background='#f0f0f0', font=('Times New Roman', 12))  # Set background color to gray and font to Times New Roman
style.configure('TLabel', background='#f0f0f0', foreground='#000000', font=('Times New Roman', 12)) # Set background color of labels to match container, text color to black, and font to Times New Roman
style.configure('Wordy.TLabel', background=search_button_bg_color, foreground='#007bff', font=('Times New Roman', 30, 'bold')) # Set style for the title label

# Title label
label_title = ttk.Label(root, text="WORDY DICTIONARY", style='Wordy.TLabel')
label_title.place(relx=0.5, rely=0.1, anchor='center')

# Search frame
frame_search = ttk.Frame(root)
frame_search.place(relx=0.5, rely=0.3, anchor='center')

# Label for the word entry field
label_word = ttk.Label(frame_search, text="Enter a word:", font=('Times New Roman', 15, 'bold'))
label_word.grid(row=0, column=0, padx=5, pady=5)

# Entry field for the word
entry_word = ttk.Entry(frame_search, width=20, font=("Times New Roman", 12))
entry_word.grid(row=0, column=1, padx=5, pady=5)

# Search button
button_search = ttk.Button(frame_search, text="Search", command=search_definition, style='Search.TButton', takefocus=False)
button_search.grid(row=0, column=2, padx=5, pady=5)

# Output frame
frame_output = ttk.Frame(root)
frame_output.place(relx=0.5, rely=0.6, anchor='center')

# Text output field for displaying the definition
text_output = tk.Text(frame_output, height=10, state='disabled', font=('Times New Roman', 15))
text_output.pack()

# Loading label
loading_label = ttk.Label(root, text="", font=('Times New Roman', 12))
loading_label.place(relx=0.5, rely=0.9, anchor='center')

# Designer label
label_designer = ttk.Label(root, text="Designed by: Anusigan Sivananthan", font=('Times New Roman', 10))
label_designer.place(relx=1, rely=1, anchor='se')
label_designer.config(background=root.cget('bg'), foreground='white')  # Make the label transparent

root.mainloop()


#Designed and Developed by Anusigan Sivananthan 
