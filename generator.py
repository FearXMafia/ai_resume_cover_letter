# generator.py

from transformers import pipeline, set_seed

# Load GPT-2 model (no API key needed)
generator = pipeline('text-generation', model='gpt2')
set_seed(42)

def generate_summary(experience, skills, job_title):
    input_text = f"I am applying for the role of {job_title}. I have experience in {experience} and skills in {skills}. I am a"
    output = generator(input_text, max_length=80, num_return_sequences=1)
    return output[0]['generated_text']
