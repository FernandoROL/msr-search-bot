import re

class PhraseCleaner:
    @staticmethod
    def clean(text: str) -> str:
        text = re.sub(r"[^a-zA-Z ]", "", text).strip()
        text = re.sub(r"\s+", " ", text)
        return text
