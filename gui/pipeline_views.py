from tkinter import *


def load_sentiment_gui(app):
    app.clear()
    card = Frame(app.root, bg=app.card_color, padx=50, pady=40)
    card.pack(expand=True)

    heading = Label(
        card,
        text="SENTIMENT ANALYSIS",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 22, "bold"),
    )
    heading.pack(pady=(0, 20))

    Label(
        card,
        text="Enter source text snippet below:",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 11),
    ).pack(anchor=W)
    app.sentiment_input = Entry(
        card, width=45, bg="#ECF0F1", fg="#2C3E50", font=("Verdana", 11), bd=0
    )
    app.sentiment_input.pack(pady=(5, 15), ipady=8)
    app.sentiment_input.bind(
        "<Return>", lambda event: app.do_sentiment_analysis()
    )
    app.sentiment_input.focus_set()

    sentiment_btn = Button(
        card,
        text="Analyze Sentiment",
        bg=app.accent_color,
        fg="white",
        font=("Verdana", 11, "bold"),
        bd=0,
        width=25,
        height=2,
        cursor="hand2",
        activebackground="#2980B9",
    )
    sentiment_btn.pack(pady=5)
    sentiment_btn.config(command=app.do_sentiment_analysis)

    app.sentiment_result = Label(
        card,
        text="",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 12, "italic"),
        justify=LEFT,
    )
    app.sentiment_result.pack(pady=20)

    goback_btn = Button(
        card,
        text="← Back to Workstation",
        bg="#7F8C8D",
        fg="white",
        font=("Verdana", 10, "bold"),
        bd=0,
        cursor="hand2",
        activebackground="#95A5A6",
    )
    goback_btn.pack(pady=(10, 0))
    goback_btn.config(command=app.home_gui)


def load_emotion_gui(app):
    app.clear()
    card = Frame(app.root, bg=app.card_color, padx=50, pady=40)
    card.pack(expand=True)

    heading = Label(
        card,
        text="EMOTION PREDICTION",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 22, "bold"),
    )
    heading.pack(pady=(0, 20))

    Label(
        card,
        text="Enter source text snippet below:",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 11),
    ).pack(anchor=W)
    app.emotion_input = Entry(
        card, width=45, bg="#ECF0F1", fg="#2C3E50", font=("Verdana", 11), bd=0
    )
    app.emotion_input.pack(pady=(5, 15), ipady=8)
    app.emotion_input.bind(
        "<Return>", lambda event: app.do_emotion_prediction()
    )
    app.emotion_input.focus_set()

    predict_btn = Button(
        card,
        text="Run Prediction Engine",
        bg=app.accent_color,
        fg="white",
        font=("Verdana", 11, "bold"),
        bd=0,
        width=25,
        height=2,
        cursor="hand2",
        activebackground="#2980B9",
    )
    predict_btn.pack(pady=5)
    predict_btn.config(command=app.do_emotion_prediction)

    app.emotion_result = Label(
        card,
        text="",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 12, "italic"),
        justify=LEFT,
    )
    app.emotion_result.pack(pady=20)

    goback_btn = Button(
        card,
        text="← Back to Workstation",
        bg="#7F8C8D",
        fg="white",
        font=("Verdana", 10, "bold"),
        bd=0,
        cursor="hand2",
        activebackground="#95A5A6",
    )
    goback_btn.pack(pady=(10, 0))
    goback_btn.config(command=app.home_gui)


def load_ner_gui(app):
    app.clear()
    card = Frame(app.root, bg=app.card_color, padx=50, pady=40)
    card.pack(expand=True)

    heading = Label(
        card,
        text="NAMED ENTITY RECOGNITION (NER)",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 20, "bold"),
    )
    heading.pack(pady=(0, 20))

    Label(
        card,
        text="Enter target text layout block below:",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 11),
    ).pack(anchor=W)
    app.ner_input = Entry(
        card, width=45, bg="#ECF0F1", fg="#2C3E50", font=("Verdana", 11), bd=0
    )
    app.ner_input.pack(pady=(5, 15), ipady=8)
    app.ner_input.bind("<Return>", lambda event: app.do_ner())
    app.ner_input.focus_set()

    ner_btn = Button(
        card,
        text="Extract Entities Matrix",
        bg=app.accent_color,
        fg="white",
        font=("Verdana", 11, "bold"),
        bd=0,
        width=25,
        height=2,
        cursor="hand2",
        activebackground="#2980B9",
    )
    ner_btn.pack(pady=5)
    ner_btn.config(command=app.do_ner)

    app.ner_result = Label(
        card,
        text="",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 12),
        justify=LEFT,
    )
    app.ner_result.pack(pady=20)

    goback_btn = Button(
        card,
        text="← Back to Workstation",
        bg="#7F8C8D",
        fg="white",
        font=("Verdana", 10, "bold"),
        bd=0,
        cursor="hand2",
        activebackground="#95A5A6",
    )
    goback_btn.pack(pady=(10, 0))
    goback_btn.config(command=app.home_gui)


def load_summary_gui(app):
    app.clear()
    card = Frame(app.root, bg=app.card_color, padx=50, pady=40)
    card.pack(expand=True)

    heading = Label(
        card,
        text="SMART SUMMARIZER",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 22, "bold"),
    )
    heading.pack(pady=(0, 20))

    Label(
        card,
        text="Paste your long article or text layout block below:",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 11),
    ).pack(anchor=W)
    app.summary_input = Entry(
        card, width=45, bg="#ECF0F1", fg="#2C3E50", font=("Verdana", 11), bd=0
    )
    app.summary_input.pack(pady=(5, 15), ipady=8)
    app.summary_input.bind("<Return>", lambda event: app.do_summary())
    app.summary_input.focus_set()

    summary_btn = Button(
        card,
        text="Generate Core Summary",
        bg=app.accent_color,
        fg="white",
        font=("Verdana", 11, "bold"),
        bd=0,
        width=25,
        height=2,
        cursor="hand2",
        activebackground="#2980B9",
    )
    summary_btn.pack(pady=5)
    summary_btn.config(command=app.do_summary)

    app.summary_result = Label(
        card,
        text="",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 12),
        justify=LEFT,
    )
    app.summary_result.pack(pady=20)

    goback_btn = Button(
        card,
        text="← Back to Workstation",
        bg="#7F8C8D",
        fg="white",
        font=("Verdana", 10, "bold"),
        bd=0,
        cursor="hand2",
        activebackground="#95A5A6",
    )
    goback_btn.pack(pady=(10, 0))
    goback_btn.config(command=app.home_gui)


def load_copilot_gui(app):
    app.clear()
    card = Frame(app.root, bg=app.card_color, padx=50, pady=40)
    card.pack(expand=True)

    heading = Label(
        card,
        text="AI COPILOT SANDBOX",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 22, "bold"),
    )
    heading.pack(pady=(0, 20))

    Label(
        card,
        text="Ask the AI Copilot anything or give structural commands:",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 11),
    ).pack(anchor=W)
    app.copilot_input = Entry(
        card, width=50, bg="#ECF0F1", fg="#2C3E50", font=("Verdana", 11), bd=0
    )
    app.copilot_input.pack(pady=(5, 15), ipady=8)
    app.copilot_input.bind("<Return>", lambda event: app.do_copilot())
    app.copilot_input.focus_set()

    ask_btn = Button(
        card,
        text="Transmit Command",
        bg=app.accent_color,
        fg="white",
        font=("Verdana", 11, "bold"),
        bd=0,
        width=25,
        height=2,
        cursor="hand2",
        activebackground="#2980B9",
    )
    ask_btn.pack(pady=5)
    ask_btn.config(command=app.do_copilot)

    app.copilot_result = Label(
        card,
        text="",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 11),
        justify=LEFT,
        wraplength=550,
    )
    app.copilot_result.pack(pady=20)

    goback_btn = Button(
        card,
        text="← Back to Workstation",
        bg="#7F8C8D",
        fg="white",
        font=("Verdana", 10, "bold"),
        bd=0,
        cursor="hand2",
        activebackground="#95A5A6",
    )
    goback_btn.pack(pady=(10, 0))
    goback_btn.config(command=app.home_gui)


def load_translate_gui(app):
    app.clear()
    card = Frame(app.root, bg=app.card_color, padx=50, pady=40)
    card.pack(expand=True)

    heading = Label(
        card,
        text="TRANSLATOR & LOCALIZER",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 22, "bold"),
    )
    heading.pack(pady=(0, 20))

    Label(
        card,
        text="Target Language (e.g. Hindi, Spanish, German):",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 10, "bold"),
    ).pack(anchor=W)
    app.lang_input = Entry(
        card, width=45, bg="#ECF0F1", fg="#2C3E50", font=("Verdana", 11), bd=0
    )
    app.lang_input.pack(pady=(5, 15), ipady=6)
    app.lang_input.bind("<Return>", app.move_focus)
    app.lang_input.focus_set()

    Label(
        card,
        text="Enter text layout block to translate:",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 11),
    ).pack(anchor=W)
    app.translate_input = Entry(
        card, width=45, bg="#ECF0F1", fg="#2C3E50", font=("Verdana", 11), bd=0
    )
    app.translate_input.pack(pady=(5, 15), ipady=8)
    app.translate_input.bind("<Return>", lambda event: app.do_translation())

    run_btn = Button(
        card,
        text="Translate & Localize Context",
        bg=app.accent_color,
        fg="white",
        font=("Verdana", 11, "bold"),
        bd=0,
        width=25,
        height=2,
        cursor="hand2",
        activebackground="#2980B9",
    )
    run_btn.pack(pady=5)
    run_btn.config(command=app.do_translation)

    app.translate_result = Label(
        card,
        text="",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 11),
        justify=LEFT,
        wraplength=550,
    )
    app.translate_result.pack(pady=20)

    goback_btn = Button(
        card,
        text="← Back to Workstation",
        bg="#7F8C8D",
        fg="white",
        font=("Verdana", 10, "bold"),
        bd=0,
        cursor="hand2",
        activebackground="#95A5A6",
    )
    goback_btn.pack(pady=(10, 0))
    goback_btn.config(command=app.home_gui)


def load_tone_gui(app):
    app.clear()
    card = Frame(app.root, bg=app.card_color, padx=50, pady=40)
    card.pack(expand=True)

    heading = Label(
        card,
        text="GRAMMAR & TONE REWRITER",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 20, "bold"),
    )
    heading.pack(pady=(0, 20))

    Label(
        card,
        text="Choose Target Persona/Vibe Style:",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 10, "bold"),
    ).pack(anchor=W)
    app.tone_input_vibe = Entry(
        card, width=45, bg="#ECF0F1", fg="#2C3E50", font=("Verdana", 11), bd=0
    )
    app.tone_input_vibe.insert(0, "Professional Corporate Email")
    app.tone_input_vibe.pack(pady=(5, 15), ipady=6)

    Label(
        card,
        text="Enter target rough text script block:",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 11),
    ).pack(anchor=W)
    app.tone_input_text = Entry(
        card, width=45, bg="#ECF0F1", fg="#2C3E50", font=("Verdana", 11), bd=0
    )
    app.tone_input_text.pack(pady=(5, 15), ipady=8)
    app.tone_input_text.bind("<Return>", lambda event: app.do_tone_rewrite())

    run_btn = Button(
        card,
        text="Execute Tone Reconstruction",
        bg=app.accent_color,
        fg="white",
        font=("Verdana", 11, "bold"),
        bd=0,
        width=25,
        height=2,
        cursor="hand2",
        activebackground="#2980B9",
    )
    run_btn.pack(pady=5)
    run_btn.config(command=app.do_tone_rewrite)

    app.tone_result = Label(
        card,
        text="",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 11, "italic"),
        justify=LEFT,
        wraplength=550,
    )
    app.tone_result.pack(pady=20)

    goback_btn = Button(
        card,
        text="← Back to Workstation",
        bg="#7F8C8D",
        fg="white",
        font=("Verdana", 10, "bold"),
        bd=0,
        cursor="hand2",
        activebackground="#95A5A6",
    )
    goback_btn.pack(pady=(10, 0))
    goback_btn.config(command=app.home_gui)


def load_classify_gui(app):
    app.clear()
    card = Frame(app.root, bg=app.card_color, padx=50, pady=40)
    card.pack(expand=True)

    heading = Label(
        card,
        text="ZERO-SHOT INDEXER & TAGGER",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 18, "bold"),
    )
    heading.pack(pady=(0, 20))

    Label(
        card,
        text="Paste your item copy block context to index:",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 11),
    ).pack(anchor=W)
    app.classify_input = Entry(
        card, width=45, bg="#ECF0F1", fg="#2C3E50", font=("Verdana", 11), bd=0
    )
    app.classify_input.pack(pady=(5, 15), ipady=8)
    app.classify_input.bind(
        "<Return>", lambda event: app.do_zero_shot_classification()
    )
    app.classify_input.focus_set()

    run_btn = Button(
        card,
        text="Index Content Tags",
        bg=app.accent_color,
        fg="white",
        font=("Verdana", 11, "bold"),
        bd=0,
        width=25,
        height=2,
        cursor="hand2",
        activebackground="#2980B9",
    )
    run_btn.pack(pady=5)
    run_btn.config(command=app.do_zero_shot_classification)

    app.classify_result = Label(
        card,
        text="",
        bg=app.card_color,
        fg=app.text_light,
        font=("Verdana", 12),
        justify=LEFT,
    )
    app.classify_result.pack(pady=20)

    goback_btn = Button(
        card,
        text="← Back to Workstation",
        bg="#7F8C8D",
        fg="white",
        font=("Verdana", 10, "bold"),
        bd=0,
        cursor="hand2",
        activebackground="#95A5A6",
    )
    goback_btn.pack(pady=(10, 0))
    goback_btn.config(command=app.home_gui)