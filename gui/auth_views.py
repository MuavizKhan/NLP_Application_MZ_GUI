from tkinter import *


def load_login_gui(app):
    app.clear()
    card = Frame(app.root, bg=app.card_color, bd=0, padx=40, pady=40)
    card.pack(expand=True)

    heading = Label(
        card,
        text="NLP APP LOGIN",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 22, "bold"),
    )
    heading.pack(pady=(0, 30))

    Label(
        card,
        text="Email Address",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 10, "bold"),
    ).pack(anchor=W)
    app.email_input = Entry(
        card, width=35, bg="#ECF0F1", fg="#2C3E50", font=("Verdana", 11), bd=0
    )
    app.email_input.pack(pady=(5, 15), ipady=8)
    app.email_input.bind("<Return>", app.move_focus)
    app.email_input.focus_set()

    Label(
        card,
        text="Password",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 10, "bold"),
    ).pack(anchor=W)
    app.password_input = Entry(
        card,
        width=35,
        show="*",
        bg="#ECF0F1",
        fg="#2C3E50",
        font=("Verdana", 11),
        bd=0,
    )
    app.password_input.pack(pady=(5, 25), ipady=8)
    app.password_input.bind("<Return>", lambda event: app.perform_login())

    login_btn = Button(
        card,
        text="Login",
        width=20,
        bg=app.accent_color,
        fg="white",
        font=("Verdana", 11, "bold"),
        activebackground="#2980B9",
        activeforeground="white",
        bd=0,
        cursor="hand2",
    )
    login_btn.pack(pady=(10, 20))
    login_btn.config(command=app.perform_login)

    Label(
        card, text="Not a Member?", bg=app.card_color, fg=app.text_light, font=("Verdana", 10)
    ).pack()
    Label(
        card, text="↓", bg=app.card_color, fg=app.arrow_color, font=("Verdana", 16, "bold")
    ).pack(pady=2)

    redirect_btn = Button(
        card,
        text="Register Now",
        bg=app.card_color,
        fg=app.accent_color,
        font=("Verdana", 10, "bold underline"),
        bd=0,
        activebackground=app.card_color,
        activeforeground="#2980B9",
        cursor="hand2",
    )
    redirect_btn.pack()
    redirect_btn.config(command=app.register_gui)


def load_register_gui(app):
    app.clear()
    card = Frame(app.root, bg=app.card_color, padx=40, pady=35)
    card.pack(expand=True)

    heading = Label(
        card,
        text="CREATE ACCOUNT",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 22, "bold"),
    )
    heading.pack(pady=(0, 25))

    Label(
        card,
        text="Full Name",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 10, "bold"),
    ).pack(anchor=W)
    app.name_input = Entry(
        card, width=35, bg="#ECF0F1", fg="#2C3E50", font=("Verdana", 11), bd=0
    )
    app.name_input.pack(pady=(5, 12), ipady=8)
    app.name_input.bind("<Return>", app.move_focus)
    app.name_input.focus_set()

    Label(
        card,
        text="Email Address",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 10, "bold"),
    ).pack(anchor=W)
    app.email_input = Entry(
        card, width=35, bg="#ECF0F1", fg="#2C3E50", font=("Verdana", 11), bd=0
    )
    app.email_input.pack(pady=(5, 12), ipady=8)
    app.email_input.bind("<Return>", app.move_focus)

    Label(
        card,
        text="Password",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 10, "bold"),
    ).pack(anchor=W)
    app.password_input = Entry(
        card,
        width=35,
        show="*",
        bg="#ECF0F1",
        fg="#2C3E50",
        font=("Verdana", 11),
        bd=0,
    )
    app.password_input.pack(pady=(5, 20), ipady=8)
    app.password_input.bind(
        "<Return>", lambda event: app.perform_registration()
    )

    register_btn = Button(
        card,
        text="Register",
        width=20,
        bg="#2ECC71",
        fg="white",
        font=("Verdana", 11, "bold"),
        activebackground="#27AE60",
        activeforeground="white",
        bd=0,
        cursor="hand2",
    )
    register_btn.pack(pady=(5, 15))
    register_btn.config(command=app.perform_registration)

    Label(
        card,
        text="Already a Member?",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 10),
    ).pack()
    Label(
        card, text="↓", bg=app.card_color, fg=app.arrow_color, font=("Verdana", 16, "bold")
    ).pack(pady=2)

    redirect_btn = Button(
        card,
        text="Login Now",
        bg=app.card_color,
        fg=app.accent_color,
        font=("Verdana", 10, "bold underline"),
        bd=0,
        activebackground=app.card_color,
        activeforeground="#2980B9",
        cursor="hand2",
    )
    redirect_btn.pack()
    redirect_btn.config(command=app.login_gui)