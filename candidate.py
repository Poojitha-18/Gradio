import gradio as gr
import re

candidates = []

def display_candidate_details(name, age, experience, education_level, skills, email, phone_number):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "Invalid email address"

    details = f"Name: {name}\nAge: {age}\nExperience: {experience} years\nEducation Level: {education_level}\nSkills: {skills}\nEmail: {email}\nPhone Number: {phone_number}"
    candidates.append({"name": name, "skills": skills})
    return details

def clear_input_fields(name, age, experience, education_level, skills, email, phone_number):
    return "", "", "", "High School", "", "", ""

def search_candidates_by_skill(skill):
    matching_candidates = [candidate["name"] for candidate in candidates if skill.lower() in candidate["skills"].lower()]
    if matching_candidates:
        return f"Candidates with the skill '{skill}':\n\n" + "\n".join(matching_candidates)
    else:
        return f"No candidates found with the skill '{skill}'"

input_fields = [
    gr.inputs.Textbox(label="Name"),
    gr.inputs.Number(label="Age"),
    gr.inputs.Number(label="Experience (years)"),
    gr.inputs.Dropdown(["High School", "Bachelor's", "Master's", "PhD"], label="Education Level"),
    gr.inputs.Textbox(label="Skills"),
    gr.inputs.Textbox(label="Email"),
    gr.inputs.Textbox(label="Phone Number")
]

display_interface = gr.Interface(
    fn=display_candidate_details,
    inputs=input_fields,
    outputs=gr.outputs.Textbox(label="Candidate Details"),
    title="Candidate Details",
    description="Enter the candidate's details below:",
    theme="dark",
    layout="horizontal"
)

clear_interface = gr.Interface(
    fn=clear_input_fields,
    inputs=input_fields,
    outputs=[
        gr.outputs.Textbox(label="Name"),
        gr.outputs.Textbox(label="Age"),
        gr.outputs.Textbox(label="Experience (years)"),
        gr.outputs.Textbox(label="Education Level"),
        gr.outputs.Textbox(label="Skills"),
        gr.outputs.Textbox(label="Email"),
        gr.outputs.Textbox(label="Phone Number")
    ],
    title="Clear Input Fields",
    description="Click the button to clear the input fields:",
    theme="dark"
)

search_interface = gr.Interface(
    fn=search_candidates_by_skill,
    inputs=gr.inputs.Textbox(label="Skill"),
    outputs=gr.outputs.Textbox(label="Matching Candidates"),
    title="Search Candidates by Skill",
    description="Enter a skill to find candidates with the same skill:",
    theme="dark"
)

# display_interface.launch()
search_interface.launch()