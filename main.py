#githelper
# Author: Lucas Arcoverde de Melo
# MIT license
#

import customtkinter as ctk

def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("800x600")
    app.title("githelper")

    app.mainloop()

if __name__ == "__main__":
    main()
