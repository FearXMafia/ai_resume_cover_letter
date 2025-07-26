# AI Resume & Cover Letter Generator

This project is a web application that uses AI (GPT-2) to automatically generate professional resumes and cover letters based on user input. It features a simple Gradio interface and does not require any external API keys.

## Features

- **AI-Powered Generation:** Uses GPT-2 to create professional summaries for resumes and cover letters.
- **Customizable Templates:** Easily adapts to different job titles, experiences, skills, and education.
- **User-Friendly Interface:** Built with Gradio for quick and easy interaction.
- **No API Key Required:** All AI processing is done locally.

## Demo

After installation, run the app and access the Gradio interface in your browser. Fill in your details and instantly receive a generated resume and cover letter.

##  Features

- ✅ Generate Resume Summary using AI
- ✅ Generate Cover Letter using AI
- ✅ Simple Gradio web interface
- ❌ No API key required (uses offline models)

## 📂 Project Structure

```
ai_resume_cover_letter/
 app.py                      # Gradio app interface
 resume_cover_model.py      # AI logic for resume & cover letter
 requirements.txt           # Dependencies
 README.md                  # Project documentation
```

## Installation

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd ai_resume_cover_letter

   Install dependencies using:

```bash
pip install -r requirements.txt
```

---


app.py: Main application file. Sets up the Gradio interface and handles user input/output.
generator.py: Contains the AI summary generation logic 
templates.py: Stores the text templates for resumes and cover letters.
requirements.txt: Lists required Python packages.
.gradio/: Contains Gradio-related files 

## HOW IT WORKS:- User Input: Enter your name, job title, experience, skills, and education in the Gradio interface.
AI Summary Generation: The app uses GPT-2 (via Hugging Face Transformers) to generate a professional summary based on your experience, skills, and job title (generator.generate_summary).
Template Filling: The summary and other details are inserted into predefined templates (resume_template, cover_letter_template).
Output: The completed resume and cover letter are displayed in the interface.

#DEPENDECIES:-Gradio
Transformers
Torch

# 🤖 Model Used

- [DistilGPT2](https://huggingface.co/distilgpt2) from HuggingFace Transformers  
- Local pipeline for text-generation

LICENSE:- free to use

AUTHOR:- AAYUSH DIKSHIT 

GITHUB PROFILE:- ayudixit1207
🌐 [GitHub Profile](https://github.com/ayudixit1207)






## ▶️ How to Run

```bash
python app.py

   INSTALL DEPENDENCIES:- pip install -r requirements.txt
python version 3.8+

   USAGE:-python [app.py](http://_vscodecontentref_/0)
   

FILE STRUCTURE:-[app.py](http://_vscodecontentref_/1)
[generator.py](http://_vscodecontentref_/2)
[templates.py](http://_vscodecontentref_/3)
[requirements.txt](http://_vscodecontentref_/4)
[readme.md](http://_vscodecontentref_/5)
__pycache__/
    generator.cpython-313.pyc
    templates.cpython-313.pyc
.gradio/
    [certificate.pem](http://_vscodecontentref_/6)

   
