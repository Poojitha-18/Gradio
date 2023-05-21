import gradio as gr
def reverse_text(text):
    return text[::-1]

iface = gr.Interface(fn=reverse_text, inputs="text", outputs="text", title="Text Reverser")
iface.launch()