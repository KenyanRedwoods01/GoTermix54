# gotermix54/ai.py
import litellm
from .config import load_config

class AIRouter:
    def __init__(self):
        self.config = load_config()
        self.model = self.config["ai"]["model"]
        # Set API keys
        litellm.api_key = self.config["ai"]["mistral_api_key"]
        # Codestral can be routed via litellm too if supported, else direct

    def route(self, prompt, mode="reasoning"):
        # Choose model based on mode
        if mode == "coding" and self.model != "mistral":
            model = "codestral/latest"  # adjust as per litellm support
        else:
            model = "mistral/mistral-large-latest"

        try:
            response = litellm.completion(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
                max_tokens=2000
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"⚠️ AI Error: {str(e)}"
