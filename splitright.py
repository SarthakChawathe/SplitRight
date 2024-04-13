import customtkinter as ctk
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
from threading import Thread
import tkinterDnD
import time
import split 

label = None
progress_bar = None
progress_label = None
result_text = None
progress_bar_convert = None
progress_label_convert = None

def open_file():
    global label
    filepath = filedialog.askopenfilename()
    if filepath:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, filepath)
        label.configure(text='Selected file: ' + filepath)
        simulate_upload()
    else:
        label.configure(text='No file selected')

def simulate_upload():
    global progress_bar, progress_label
    for i in range(101):
        progress_bar['value'] = i
        progress_label.configure(text=f'{i}%')
        progress_bar.update()
        time.sleep(0.03)
    if i == 100:
        convert_button.configure(state=tk.NORMAL)

def run_conversion():
    global progress_bar_convert, progress_label_convert
    progress_bar_convert['value'] = 0
    convert_button.configure(state=tk.DISABLED)
    file_path = file_entry.get()
    if not os.path.exists(file_path):
        messagebox.showerror('Error', 'File does not exist.')
        convert_button.configure(state=tk.NORMAL)
        return
    output_dir = '/path/to/default/output/directory'
    thread = Thread(target=start_conversion, args=(file_path, output_dir))
    thread.start()

def start_conversion(file_path, output_dir):
    global result_text
    try:
        # result = subprocess.run(['python', 'dummy.py', file_path], capture_output=True, text=True, check=True)
        # result_text = result.stdout
        split.start_splitting(file_path)

        for i in range(101):
            progress_bar_convert['value'] = i
            progress_label_convert.configure(text=f'{i}%')
            progress_bar_convert.update()
            time.sleep(0.03)
        # if i == 100:
        #     show_result(result.stdout)
    except subprocess.CalledProcessError as e:
        print('Error:', e)
    finally:
        convert_button.configure(state=tk.NORMAL)

def show_result(result):
    if result in result:
        messagebox.showinfo('Conversion Result', 'Success')
        save_button.configure(state=tk.NORMAL)
    else:
        messagebox.showinfo('Conversion Result', 'Failure')
        save_button.configure(state=tk.DISABLED)

def save_result():
    global result_text
    if result_text:
        output_dir = '/Users/sarthakchawathe/Desktop/Hackathon'
        output_file = os.path.join(output_dir, 'output.txt')
        with open(output_file, 'w') as f:
            f.write(result_text)
        messagebox.showinfo('Save Result', f'Result saved to {output_file}')
    else:
        messagebox.showwarning('Save Result', 'No result to save.')



#MAIN

ctk.set_ctk_parent_class(tkinterDnD.Tk)
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title('File Selection App')

root.geometry("800x500")
frame_1 = ctk.CTkFrame(master=root)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

file_label = ctk.CTkLabel(master=frame_1, text='Enter file path:')
file_label.pack(pady=10, padx=10)
file_entry = ctk.CTkEntry(master=frame_1, width=200)
file_entry.pack(pady=10, padx=10)
open_button = ctk.CTkButton(master=frame_1, text='Browse File', command=open_file)
open_button.pack(pady=10, padx=10)
label = ctk.CTkLabel(master=frame_1, text='', font=('Helvetica', 12))
label.pack(pady=10, padx=10)
progress_bar = ctk.CTkProgressBar(master=frame_1,mode='determinate')
progress_bar.pack(pady=10, padx=10)
progress_label = ctk.CTkLabel(master=frame_1, text='0%', font=('Helvetica', 10))
progress_label.pack()
convert_button = ctk.CTkButton(master=frame_1, text='Convert', command=run_conversion)
convert_button.pack(pady=10, padx=10)
progress_bar_convert = ctk.CTkProgressBar(master=frame_1, mode='determinate')
progress_bar_convert.pack(pady=10, padx=10)
progress_label_convert = ctk.CTkLabel(master=frame_1, text='0%', font=('Helvetica', 10))
progress_label_convert.pack()
save_button = ctk.CTkButton(master=frame_1, text='Save Result', command=save_result, state=tk.DISABLED)
save_button.pack(pady=10, padx=10)
root.mainloop()