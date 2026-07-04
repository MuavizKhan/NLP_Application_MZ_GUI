from tkinter import *


def load_home_gui(app):
    app.clear()

    main_container = Frame(app.root, bg=app.bg_color, padx=40, pady=30)
    main_container.pack(fill=BOTH, expand=True)

    heading = Label(
        main_container,
        text="NLP SERVICES WORKSTATION",
        bg=app.bg_color,
        fg=app.text_light,
        font=("Verdana", 24, "bold"),
    )
    heading.pack(pady=(10, 30))

    grid_frame = Frame(main_container, bg=app.bg_color)
    grid_frame.pack(expand=True, fill=BOTH)

    for col in range(4):
        grid_frame.grid_columnconfigure(col, weight=1, uniform="equal")
    for row in range(2):
        grid_frame.grid_rowconfigure(row, weight=1, uniform="equal")

    services_matrix = [
        (
            0,
            0,
            "📊 Sentiment Analysis Engine",
            "Evaluates text snippets to determine overall \npositive, negative, or neutral sentiment weights.",
            app.sentiment_gui,
        ),
        (
            0,
            1,
            "🎭 Emotion Prediction Engine",
            "Breakdowns text into core emotional variances \nlike joy, sadness, anger, fear, and surprise.",
            app.emotion_gui,
        ),
        (
            0,
            2,
            "🔍 Named Entity Matrix (NER)",
            "Extracts and categorizes core text metrics \nsuch as specific people, places, and brands.",
            app.ner_gui,
        ),
        (
            0,
            3,
            "📝 Smart Summarizer & TL;DR",
            "Condenses lengthy articles into single-sentence \nsummaries and clean key-takeaway bullet points.",
            app.summary_gui,
        ),
        (
            1,
            0,
            "🤖 Interactive AI Copilot",
            "An open-ended sandbox to execute custom \ninstructions or talk freely with the model.",
            app.copilot_gui,
        ),
        (
            1,
            1,
            "✍️ Grammar & Tone Rewriter",
            "Fixes punctuation syntax and transforms vocabulary \nvibes (e.g., casual to corporate professional).",
            app.tone_gui,
        ),
        (
            1,
            2,
            "🏷️ Zero-Shot Classification",
            "Scans text layout copy to auto-assign categories, \nmetadata keywords, and priority urgency scores.",
            app.classify_gui,
        ),
        (
            1,
            3,
            "🌐 Translator & Localizer",
            "Converts text between foreign languages while \nmapping out cultural metaphors and regional slang.",
            app.translate_gui,
        ),
    ]

    for row, col, title, desc, command_target in services_matrix:
        card = Frame(
            grid_frame, bg=app.card_color, bd=0, relief=FLAT, padx=15, pady=15
        )
        card.grid(row=row, column=col, padx=12, pady=12, sticky="nsew")

        btn = Button(
            card,
            text=title,
            bg="#1ABC9C",
            fg="white",
            font=("Verdana", 11, "bold"),
            height=2,
            bd=0,
            cursor="hand2",
            activebackground="#16A085",
            activeforeground="white",
            command=command_target,
        )
        btn.pack(fill=X, pady=(5, 10))

        desc_lbl = Label(
            card,
            text=desc,
            bg=app.card_color,
            fg="#BDC3C7",
            font=("Verdana", 9, "italic"),
            justify=CENTER,
            wraplength=220,
        )
        desc_lbl.pack(fill=BOTH, expand=True)

    footer_frame = Frame(main_container, bg=app.bg_color)
    footer_frame.pack(fill=X, pady=(20, 0))

    logout_btn = Button(
        footer_frame,
        text="Logout Safe",
        bg="#E74C3C",
        fg="white",
        font=("Verdana", 10, "bold"),
        width=14,
        height=1,
        bd=0,
        cursor="hand2",
        activebackground="#C0392B",
        activeforeground="white",
        command=app.login_gui,
    )
    logout_btn.pack(side=RIGHT, padx=10)