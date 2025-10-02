# 🔍 Bing Search Automation with AI Phrase Generator

This project automates Bing searches using **AI-generated random short phrases**.  
It was designed to help with automatic query farming (e.g., Microsoft Rewards) in a way that mimics natural typing and browsing behavior.  

The program uses:
- **HuggingFace Transformers** for text generation (GPT-based short phrases).
- **Selenium + undetected-chromedriver** for browser automation.
- **Tkinter** for a simple user interface. (Not yet done)


# 

## Features
- Customize the **base prompt** for phrase generation.
- Set the **number of searches** you want to perform.

(For future updates)
- Start automation with a single **Start button**.
- A **success screen** pops up when finished.
- Compiled executable


## Requirements

- Python **3.9+**
- Google Chrome installed  
- ChromeDriver (handled automatically by `undetected-chromedriver`)


## Installation

Clone the repository:

```bash
git clone https://github.com/FernandoROL/msr-search-bot.git
cd msr-search-bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Make the `cookies.json` file*

- Log into bing on any browser
- Install an extension like [Export cookies JSON file](https://chromewebstore.google.com/detail/export-cookie-json-file-f/nmckokihipjgplolmcmjakknndddifde)
- Export the cookies from the bing page using the extension
- Copy the file to the root of the project


## How to Run

```
python main.py
```