from tkinter import *
from tkinter import messagebox
import threading

from database import Database
from core_api import API
from gui import (
    load_login_gui,
    load_register_gui,
    load_home_gui,
    load_sentiment_gui,
    load_emotion_gui,
    load_ner_gui,
    load_summary_gui,
    load_copilot_gui,
    load_translate_gui,
    load_tone_gui,
    load_classify_gui,
)


class NLPApp:

    def __init__(self):
        self.dbo = Database()
        self.apio = API()
        self.root = Tk()
        self.root.title("Advanced NLP Workstation")
        self.root.iconbitmap("resources/favicon.ico")
        self.root.state("zoomed")
        self.root.configure(bg="#2C3E50")

        self.bg_color = "#2C3E50"
        self.card_color = "#34495E"
        self.text_light = "#ECF0F1"
        self.accent_color = "#3498DB"
        self.arrow_color = "#E74C3C"

        self.login_gui()
        self.root.mainloop()

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def move_focus(self, event):
        event.widget.tk_focusNext().focus_set()

    # ROUTERS
    def login_gui(self):
        load_login_gui(self)

    def register_gui(self):
        load_register_gui(self)

    def home_gui(self):
        load_home_gui(self)

    def sentiment_gui(self):
        load_sentiment_gui(self)

    def emotion_gui(self):
        load_emotion_gui(self)

    def ner_gui(self):
        load_ner_gui(self)

    def summary_gui(self):
        load_summary_gui(self)

    def copilot_gui(self):
        load_copilot_gui(self)

    def translate_gui(self):
        load_translate_gui(self)

    def tone_gui(self):
        load_tone_gui(self)

    def classify_gui(self):
        load_classify_gui(self)

    # AUTHENTICATION
    def perform_registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        if self.dbo.add_data(name, email, password):
            messagebox.showinfo(
                "Success", "Registration Successful. You can Login Now"
            )
            self.login_gui()
        else:
            messagebox.showerror("Error", "Email already Exists")

    def perform_login(self):
        if self.dbo.search(self.email_input.get(), self.password_input.get()):
            messagebox.showinfo("Success", "Login Successful")
            self.home_gui()
        else:
            messagebox.showerror("Error", "Incorrect Email/Password")

    # CORE PIPELINES (Threaded Ecosystem Execution Blocks)
    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        if not text.strip():
            return
        self.sentiment_result.config(text="⏳ Querying sentiment context matrix...")

        def run():
            result = self.apio.sentiment_analysis(text)
            if "sentiment" in result:
                scores = result["sentiment"]
                formatted = f"Negative Variance: {scores.get('negative', 0):.3f}\nNeutral Weighting: {scores.get('neutral', 0):.3f}\nPositive Signatures: {scores.get('positive', 0):.3f}"
                self.sentiment_result.config(text=formatted)
            elif "error" in result:
                messagebox.showerror("Error", result["error"])

        threading.Thread(target=run, daemon=True).start()

    def do_emotion_prediction(self):
        text = self.emotion_input.get()
        if not text.strip():
            return
        self.emotion_result.config(
            text="⏳ Running structured emotion taxonomy predictions..."
        )

        def run():
            result = self.apio.emotion_prediction(text)
            if "emotions" in result:
                scores = result["emotions"]
                formatted = f"Joy: {scores.get('Joy', 0)}%\nSadness: {scores.get('Sadness', 0)}%\nAnger: {scores.get('Anger', 0)}%\nFear: {scores.get('Fear', 0)}%\nSurprise: {scores.get('Surprise', 0)}%"
                self.emotion_result.config(text=formatted)
            elif "error" in result:
                messagebox.showerror("Error", result["error"])

        threading.Thread(target=run, daemon=True).start()

    def do_ner(self):
        text = self.ner_input.get()
        if not text.strip():
            return
        self.ner_result.config(text="⏳ Extracting named entities...")

        def run():
            result = self.apio.named_entity_recognition(text)
            if "entities" in result:
                formatted = "".join(
                    [
                        f"• {k}: {', '.join(v)}\n"
                        for k, v in result["entities"].items()
                        if v
                    ]
                )
                self.ner_result.config(
                    text=formatted or "No prominent entities identified."
                )
            elif "error" in result:
                messagebox.showerror("Error", result["error"])

        threading.Thread(target=run, daemon=True).start()

    def do_summary(self):
        text = self.summary_input.get()
        if not text.strip():
            return
        self.summary_result.config(text="⏳ Compiling article takeaways...")

        def run():
            result = self.apio.smart_summary(text)
            if "error" not in result:
                bullets = "\n".join(
                    [f"• {i}" for i in result.get("takeaways", [])]
                )
                formatted = f"⏱️ Reading Time: {result.get('reading_time_mins', 0)} min\n\n📝 TL;DR:\n\"{result.get('tldr')}\"\n\n📌 Takeaways:\n{bullets}"
                self.summary_result.config(text=formatted)
            else:
                messagebox.showerror("Error", result.get("error"))

        threading.Thread(target=run, daemon=True).start()

    def do_copilot(self):
        prompt = self.copilot_input.get()
        if not prompt.strip():
            return
        self.copilot_result.config(text="⏳ Waiting for copilot sandbox reply...")

        def run():
            result = self.apio.ai_copilot(prompt)
            if "reply" in result:
                self.copilot_result.config(text=result["reply"])
            elif "error" in result:
                messagebox.showerror("Error", result["error"])

        threading.Thread(target=run, daemon=True).start()

    def do_translation(self):
        target = self.lang_input.get()
        text = self.translate_input.get()
        if not target.strip() or not text.strip():
            return
        self.translate_result.config(
            text="⏳ Running contextual localizer translations..."
        )

        def run():
            result = self.apio.translator_localizer(text, target)
            if "error" not in result:
                formatted = f"🌐 Input Language: {result.get('detected_language')}\n\n✏️ Translation:\n\"{result.get('translated_text')}\"\n\n💡 Cultural Note:\n{result.get('cultural_note')}"
                self.translate_result.config(text=formatted)
            else:
                messagebox.showerror("Error", result.get("error"))

        threading.Thread(target=run, daemon=True).start()

    def do_tone_rewrite(self):
        vibe = self.tone_input_vibe.get()
        text = self.tone_input_text.get()
        if not vibe.strip() or not text.strip():
            return
        self.tone_result.config(text="⏳ Rewriting text vibe constraints...")

        def run():
            result = self.apio.tone_rewriter(text, vibe)
            if "rewritten_text" in result:
                self.tone_result.config(
                    text=f"✨ Rewritten Output:\n\n{result['rewritten_text']}"
                )
            elif "error" in result:
                messagebox.showerror("Error", result["error"])

        threading.Thread(target=run, daemon=True).start()

    def do_zero_shot_classification(self):
        text = self.classify_input.get()
        if not text.strip():
            return
        self.classify_result.config(
            text="⏳ Scoping classifications and keyword indexes..."
        )

        def run():
            result = self.apio.zero_shot_classifier(text)
            if "error" not in result:
                formatted = f"📂 Category Taxonomy: {result.get('category')}\n⚠️ System Urgency Context: {result.get('urgency')}\n🏷️ Keyword Tags: {', '.join(result.get('tags', []))}"
                self.classify_result.config(text=formatted)
            else:
                messagebox.showerror("Error", result.get("error"))

        threading.Thread(target=run, daemon=True).start()


if __name__ == "__main__":
    nlp = NLPApp()