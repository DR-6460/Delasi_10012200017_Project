import tkinter as tk
from tkinter import ttk, messagebox
from generator import generate


def generate_password():
    generate_window = tk.Tk(className=" Password Generator")

    # ###### FIRST FRAME #####
    settings_frame = ttk.LabelFrame(generate_window, text="Settings", relief=tk.RIDGE, padding=6)
    settings_frame.grid(row=1, column=1, sticky=tk.E + tk.N + tk.W + tk.S, padx=20, pady=10)

    alpha_setting_value = tk.BooleanVar()
    numb_setting_value = tk.BooleanVar()
    sym_setting_value = tk.BooleanVar()
    length_setting_value = tk.IntVar()

    alpha_setting = ttk.Checkbutton(settings_frame, text="Add alphabets", variable=alpha_setting_value)
    numb_setting = ttk.Checkbutton(settings_frame, text="Add numbers", variable=numb_setting_value)
    sym_setting = ttk.Checkbutton(settings_frame, text="Add symbols", variable=sym_setting_value)
    length_setting = ttk.LabeledScale(settings_frame, from_=3, to=30, variable=length_setting_value)

    alpha_setting.grid(row=1, column=1, padx=30)
    numb_setting.grid(row=2, column=1, padx=30)
    sym_setting.grid(row=3, column=1, padx=30)
    length_setting.grid(row=4, column=2, padx=30, pady=5)

    length_label = ttk.Label(settings_frame, text="Length of the password:")
    length_label.grid(row=4, column=1, padx=30)

    # ##### PASSWORD FRAME #####
    password_frame = ttk.LabelFrame(generate_window, text="Password", relief=tk.RIDGE, padding=6)
    password_frame.grid(row=1, column=2, sticky=tk.E + tk.N + tk.W + tk.S, padx=80, pady=10)

    text1 = tk.StringVar()
    password_label = ttk.Label(password_frame, textvariable=text1)
    password_label.grid(row=1, column=2, padx=50)

    # ##### BUTTON #####
    generate_button = ttk.Button(generate_window, text="Generate", command=lambda: generate_action(alpha_setting_value.get(),
                                numb_setting_value.get(), sym_setting_value.get(), length_setting_value.get()))
    generate_button.grid(row=2, column=2)

    # if alpha_setting_value.get() is True:
    #     if numb_setting_value.get() is True:
    #         if sym_setting_value.get() is True:
    #             text.set(generate(length=length_setting_value.get(), alphabet=alpha_setting_value.get(),
    #                              number=numb_setting_value.get(), symbol=sym_setting_value.get()))

    # ##### BUTTON ACTION FUNCTION #####

    def generate_action(alpha: bool, num: bool, sym: bool, length: int):
        if alpha or num or sym:
            password = generate(length=length, alphabet=alpha, number=num, symbol=sym)
            text1.set(password)
            # delete_label()
            # text = password
            # password_label = ttk.Label(password_frame, text=f"{text}")
            # password_label.grid(row=2, column=1, padx=50)
        else:
            messagebox.showerror(title=" Parameter Error",
                                 message="Select one of the following: alphabet, number or symbol")

    # def delete_label():
    #     password_label.destroy()

    generate_window.mainloop()


def display_password():
    display_window = tk.Tk(className=" Passwords")

    # ###### FIRST FRAME #####
    settings_frame = ttk.LabelFrame(display_window, text="Passwords", relief=tk.RIDGE, padding=6)
    settings_frame.grid(row=1, column=1, sticky=tk.E + tk.N + tk.W + tk.S, padx=20, pady=10)

    display_window.mainloop()


generate_password()
