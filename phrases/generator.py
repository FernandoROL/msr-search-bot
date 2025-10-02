import random
import time
from transformers import pipeline
from .cleaner import PhraseCleaner

class PhraseGenerator:
    def __init__(self, model="distilgpt2"):
        self.generator = pipeline("text-generation", model=model)
        self.base_prompt = """Random short phrases:
- nuclear energy
- computer science
- artificial intelligence
- right politics
- """

    def generate_short_phrases(self, n=random.randint(15,25), max_attempts=10):
        phrases = []
        for _ in range(n):
            phrase = ""
            attempts = 0
            while (len(phrase.split()) < 2 or len(phrase.split()) > 5) and attempts < max_attempts:
                result = self.generator(
                    self.base_prompt,
                    max_new_tokens=random.randint(4,8),
                    do_sample=True,
                    top_k=random.randint(50,150),
                    temperature=random.uniform(0.7,1.2)
                )
                phrase = result[0]["generated_text"].split("-")[-1].strip()
                phrase = PhraseCleaner.clean(phrase)
                attempts += 1
                time.sleep(random.uniform(0.1,0.5))

            if phrase == "":
                phrase = self.generate_short_phrases(1)[0]
            phrases.append(phrase)
            time.sleep(random.uniform(0.2,0.7))
        random.shuffle(phrases)
        return phrases
