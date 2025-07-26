# app.py

import gradio as gr
from templates import resume_template, cover_letter_template
from generator import generate_summary

def generate_docs(name, job_title, experience, skills, education):
    summary = generate_summary(experience, skills, job_title)
    
    resume = resume_template.format(
        name=name,
        job_title=job_title,
        experience=experience,
        skills=skills,
        education=education,
        summary=summary
    )
    
    cover_letter = cover_letter_template.format(
        name=name,
        job_title=job_title,
        experience=experience,
        skills=skills,
        summary=summary
    )
    
    return resume, cover_letter

# ✅ This line is updated with `share=True`
interface = gr.Interface(
    fn=generate_docs,
    inputs=[
        gr.Textbox(label="Your Name"),
        gr.Textbox(label="Job Title"),
        gr.Textbox(label="Experience"),
        gr.Textbox(label="Skills"),
        gr.Textbox(label="Education")
    ],
    outputs=[
        gr.Textbox(label="Generated Resume"),
        gr.Textbox(label="Generated Cover Letter")
    ],
    title="AI Resume & Cover Letter Generator (No API Key)"
)

# ✅ Launch with public link enabled
interface.launch(share=True)
