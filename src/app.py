import customtkinter
from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog
from customtkinter import CTkProgressBar
import split

customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):
    width = 800
    height = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("SplitRight")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)
        
        self.iconbitmap(os.path.join("..", "Images", "icon.ico"))

        # load and create background image
        self.bg_image = customtkinter.CTkImage(Image.open(os.path.join("..", "Images", "bg_gradient.jpg")),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        # create login frame
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")
        self.login_label = customtkinter.CTkLabel(self.login_frame, text="SplitRight", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=0, pady=(150, 15))


        self.login_frame.pack_propagate(False)

        self.config_label = customtkinter.CTkLabel(self.login_frame, text="Config File Path", font=customtkinter.CTkFont(size=12))
        self.config_label.grid(row=1, column=0, padx=40, pady=(20, 0), sticky="w")
        self.file_path = customtkinter.StringVar() 
        self.file_path.set("Enter Config File Path...")
        self.username_entry = customtkinter.CTkEntry(self.login_frame, width=200, textvariable=self.file_path, placeholder_text="Enter File Path...")
        self.username_entry.grid(row=2, column=0, padx=40, pady=(3, 10))
        

        self.checkbox = customtkinter.CTkCheckBox(self.login_frame, text="Preserve Folder Structure", command=self.on_checkbox_click)
        self.checkbox.grid(row=5, column=0, pady=(20, 0), padx=40, sticky="w")
        
        self.upload_button = customtkinter.CTkButton(self.login_frame, text="Browse", command=self.browse_file, width=200)
        self.upload_button.grid(row=6, column=0, padx=40, pady=(15, 15))
        
        self.convert_button = customtkinter.CTkButton(self.login_frame, text="Convert", command=self.convert_file, width=200)
        self.convert_button.grid(row=7, column=0, padx=40, pady=(15, 15))

    def on_checkbox_click(self):
        if self.checkbox.get() == 1:
            print("Checkbox is enabled")
            split.preserve_folder_structure = True
        else:
            print("Checkbox is disabled")
            split.preserve_folder_structure = False


    def browse_file(self):
        global label
        file_path = filedialog.askopenfilename()
        if file_path:
            self.username_entry.delete(0, tk.END)

            self.username_entry.insert(0, file_path)

            self.input_path_label = customtkinter.CTkLabel(self.login_frame, 
                                                        text="Input Directory:"+split.getParsedConfig(self.file_path.get()).get("INPUT"),
                                                        font=customtkinter.CTkFont(size=12))
            self.input_path_label.grid(row=3, column=0, padx=40, pady=(10, 0), sticky="w")
            self.output_path_label = customtkinter.CTkLabel(self.login_frame, 
                                                        text="Output Directory:"+split.getParsedConfig(self.file_path.get()).get("OUTPUT"),
                                                        font=customtkinter.CTkFont(size=12))
            self.output_path_label.grid(row=4, column=0, padx=40, pady=(10, 0), sticky="w")

    def convert_file(self):
        print("Convert pressed - file path:", self.file_path.get())
        
        split.start_splitting(self.file_path.get())

        # self.progress_bar = CTkProgressBar(self.login_frame, width=200)
        # self.progress_bar.grid(row=3, column=0, padx=30, pady=(15, 15))

        # for i in range(101):
        #     progress_bar_convert['value'] = i
        #     progress_label_convert.configure(text=f'{i}%')
        #     progress_bar_convert.update()
        #     time.sleep(0.03)


if __name__ == "__main__":
    app = App()
    app.mainloop()