import gradio as gr
import numpy as np

def img2img_handler(model_tag, image):
    return np.zeros((400,400))

def img2text_handler(model_tag, image):
    return model_tag

with gr.Blocks() as demo:
    with gr.Tabs():
        with gr.TabItem("Image to Image"):
            with gr.Row():
                with gr.Column():
                    img2img_options = ["UNet", "pix2pix"]
                    img2img_model = gr.Dropdown(choices=img2img_options, label="Select Model", info="Select model")
                    img2img_input = gr.Image(label="Input Image")
                    img2img_button = gr.Button("Inference")
                with gr.Column():
                    img2img_output = gr.Image(label="Output Image")

        with gr.TabItem("Image to Text"):
            with gr.Row():
                with gr.Column():
                    img2text_options = ["ResNet", "ImageNet"]
                    img2text_model = gr.Dropdown(choices=img2text_options, label="Select Model", info="Select model")
                    img2text_input = gr.Image(label="Input Image")
                    img2text_button = gr.Button("Inference")

                with gr.Column():
                    img2text_output = gr.Text()
        img2img_button.click(
            fn=img2img_handler,
            inputs=[img2img_model, img2img_input],
            outputs=img2img_output,
        )
        img2text_button.click(
            fn=img2text_handler,
            inputs=[img2text_model, img2text_input],
            outputs=img2text_output,
        )
if __name__ == "__main__":
    demo.launch()
