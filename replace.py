import gradio as gr

def replace_character(text, old_char, new_char, replace_all):
    if replace_all:
        replaced_text = text.replace(old_char, new_char)
    else:
        replaced_text = text.replace(old_char, new_char, 1)
    return replaced_text

iface = gr.Interface(
    fn=replace_character,
    inputs=["text", "text", "text", gr.inputs.Checkbox(label="Replace All")],
    outputs="text",
    title="Character Replacer",
    description="Enter a text, the character to replace, and the replacement character.",
)

iface.launch()