import json
import os
import requests
from dotenv import load_dotenv


class API:
    def __init__(self):
        load_dotenv(dotenv_path="api_security.env")
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            print("⚠️ CRITICAL WARNING: GEMINI_API_KEY not found in api_security.env!")

    def _handle_response(self, response):
        """Universal response router to handle rate limits and API faults gracefully."""
        try:
            response_json = response.json()
            if "error" in response_json:
                api_err = response_json["error"]
                return {"error": f"Gemini API Error ({api_err.get('status')}):\n{api_err.get('message')}"}
            if "candidates" not in response_json or not response_json["candidates"]:
                return {"error": "No data returned. Content may have been blocked or throttled."}
            raw_text = response_json["candidates"][0]["content"]["parts"][0]["text"]
            return json.loads(raw_text.strip())
        except Exception as e:
            return {"error": f"Ecosystem parsing execution fault: {str(e)}"}

    def sentiment_analysis(self, text):
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={self.api_key}"
        headers = {"Content-Type": "application/json"}
        response_schema = {
            "type": "OBJECT",
            "properties": {
                "negative": {"type": "NUMBER"},
                "neutral": {"type": "NUMBER"},
                "positive": {"type": "NUMBER"}
            },
            "required": ["negative", "neutral", "positive"]
        }
        payload = {
            "contents": [{"parts": [{"text": f"Analyze text sentiment weights (0.0 to 1.0):\n\n{text}"}]}],
            "generationConfig": {"responseMimeType": "application/json", "responseSchema": response_schema}
        }
        return self._handle_response(requests.post(url, json=payload, headers=headers))

    def named_entity_recognition(self, text):
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={self.api_key}"
        headers = {"Content-Type": "application/json"}
        response_schema = {
            "type": "OBJECT",
            "properties": {
                "entities": {
                    "type": "OBJECT",
                    "properties": {
                        "Persons": {"type": "ARRAY", "items": {"type": "STRING"}},
                        "Places": {"type": "ARRAY", "items": {"type": "STRING"}},
                        "Organizations": {"type": "ARRAY", "items": {"type": "STRING"}}
                    },
                    "required": ["Persons", "Places", "Organizations"]
                }
            },
            "required": ["entities"]
        }
        payload = {
            "contents": [{"parts": [{"text": f"Extract entities matrix:\n\n{text}"}]}],
            "generationConfig": {"responseMimeType": "application/json", "responseSchema": response_schema}
        }
        return self._handle_response(requests.post(url, json=payload, headers=headers))

    def emotion_prediction(self, text):
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={self.api_key}"
        headers = {"Content-Type": "application/json"}
        response_schema = {
            "type": "OBJECT",
            "properties": {
                "emotions": {
                    "type": "OBJECT",
                    "properties": {
                        "Joy": {"type": "INTEGER"},
                        "Sadness": {"type": "INTEGER"},
                        "Anger": {"type": "INTEGER"},
                        "Fear": {"type": "INTEGER"},
                        "Surprise": {"type": "INTEGER"}
                    },
                    "required": ["Joy", "Sadness", "Anger", "Fear", "Surprise"]
                }
            },
            "required": ["emotions"]
        }
        payload = {
            "contents": [{"parts": [{"text": f"Predict emotion variances summing precisely to 100:\n\n{text}"}]}],
            "generationConfig": {"responseMimeType": "application/json", "responseSchema": response_schema}
        }
        return self._handle_response(requests.post(url, json=payload, headers=headers))

    def smart_summary(self, text):
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={self.api_key}"
        headers = {"Content-Type": "application/json"}
        response_schema = {
            "type": "OBJECT",
            "properties": {
                "tldr": {"type": "STRING"},
                "takeaways": {"type": "ARRAY", "items": {"type": "STRING"}},
                "reading_time_mins": {"type": "INTEGER"}
            },
            "required": ["tldr", "takeaways", "reading_time_mins"]
        }
        payload = {
            "contents": [{"parts": [{"text": f"Compile high-level metadata summaries:\n\n{text}"}]}],
            "generationConfig": {"responseMimeType": "application/json", "responseSchema": response_schema}
        }
        return self._handle_response(requests.post(url, json=payload, headers=headers))

    def ai_copilot(self, prompt_text):
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={self.api_key}"
        headers = {"Content-Type": "application/json"}

        # Upgraded to utilize strict structural schema output for cleaner tkinter wrapping
        response_schema = {
            "type": "OBJECT",
            "properties": {
                "reply": {"type": "STRING"}
            },
            "required": ["reply"]
        }
        payload = {
            "contents": [{"parts": [{"text": prompt_text}]}],
            "generationConfig": {"responseMimeType": "application/json", "responseSchema": response_schema}
        }
        res = self._handle_response(requests.post(url, json=payload, headers=headers))
        if "error" in res:
            return res
        return {"reply": res.get("reply", "")}

    def translator_localizer(self, text, target_language):
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={self.api_key}"
        headers = {"Content-Type": "application/json"}
        response_schema = {
            "type": "OBJECT",
            "properties": {
                "detected_language": {"type": "STRING"},
                "translated_text": {"type": "STRING"},
                "cultural_note": {"type": "STRING"}
            },
            "required": ["detected_language", "translated_text", "cultural_note"]
        }
        payload = {
            "contents": [{"parts": [{"text": f"Translate layout context into {target_language}:\n\n{text}"}]}],
            "generationConfig": {"responseMimeType": "application/json", "responseSchema": response_schema}
        }
        return self._handle_response(requests.post(url, json=payload, headers=headers))

    def tone_rewriter(self, text, style_vibe):
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={self.api_key}"
        headers = {"Content-Type": "application/json"}
        response_schema = {
            "type": "OBJECT",
            "properties": {"rewritten_text": {"type": "STRING"}},
            "required": ["rewritten_text"]
        }
        payload = {
            "contents": [{"parts": [{"text": f"Rewrite text to match {style_vibe} vibe constraints:\n\n{text}"}]}],
            "generationConfig": {"responseMimeType": "application/json", "responseSchema": response_schema}
        }
        return self._handle_response(requests.post(url, json=payload, headers=headers))

    def zero_shot_classifier(self, text):
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={self.api_key}"
        headers = {"Content-Type": "application/json"}
        response_schema = {
            "type": "OBJECT",
            "properties": {
                "category": {"type": "STRING"},
                "tags": {"type": "ARRAY", "items": {"type": "STRING"}},
                "urgency": {"type": "STRING"}
            },
            "required": ["category", "tags", "urgency"]
        }
        payload = {
            "contents": [{"parts": [{"text": f"Index tracking descriptors:\n\n{text}"}]}],
            "generationConfig": {"responseMimeType": "application/json", "responseSchema": response_schema}
        }
        return self._handle_response(requests.post(url, json=payload, headers=headers))