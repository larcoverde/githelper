#githelper
# Author: Lucas Arcoverde de Melo
# MIT license
#

import customtkinter as ctk
import subprocess as sp

def main():

    def clone_repository():
        git_url = git_url_entry.get()
        dir = directory_entry.get()

        sp.run([
            "git",
            "clone",
            git_url,
            dir
        ])

        status_label.configure(text="status: cloned")

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    app = ctk.CTk()
    app.geometry("400x300")
    app.title("githelper")

    main_title_label = ctk.CTkLabel(
        app,
        text="githelper",
        font=("Arial", 30)
    )
    main_title_label.pack(pady=30)

    git_url_entry = ctk.CTkEntry(
        app,
        placeholder_text="repository url"
    )
    git_url_entry.pack()

    directory_entry = ctk.CTkEntry(
        app,
        placeholder_text="clone to..."
    )
    directory_entry.pack(pady=20)

    clone_button = ctk.CTkButton(
        app,
        text="clone",
        command=clone_repository
    )
    clone_button.pack(pady=20)

    status_label = ctk.CTkLabel(
        app,
        text="status: ",
        font=("Arial", 15)
    )
    status_label.pack()

    app.mainloop()

if __name__ == "__main__":
    main()
