""" This a GUI experiment with Tkinter library"""
import tkinter as tk


root = tk.Tk()
# root.title("Ivy Technology")
# root.geometry('840x480+300+300')
# root.resizable(False, False)
# label = tk.Label(root, text="Hello World!")
# label.pack()
root.mainloop()

# from tkinter import filedialog
 
# def open_file():
#     file_path = filedialog.askopenfilename(
#         title="Select a Text File", filetypes=[("Text files", "*.txt")])
#     if file_path:
#         with open(file_path, 'r') as file:
#             content = file.read()
#             text_widget.delete(1.0, tk.END)  # Clear previous content
#             text_widget.insert(tk.END, content)
 
 
# # Create the main window
# root = tk.Tk()
# root.title("Text File Reader")
# root.geometry("1200x800")
 
# # Create a Text widget to display the content
# text_widget = tk.Text(root, wrap="word", width=50, height=20)
# text_widget.pack(pady=10)
 
# # Create a button to open the file
# open_button = tk.Button(root, text="Open File", command=open_file)
# open_button.pack(pady=10)
 
# # Run the Tkinter event loop
# root.mainloop()