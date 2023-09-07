#display a data
import gradio as gr

def data_display(input_img):
    return input_img

demo = gr.Interface(data_display, gr.Dataframe(), "dataframe")
demo.launch()