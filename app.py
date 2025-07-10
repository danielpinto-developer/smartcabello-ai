import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("hair_length_model.h5")
class_names = ['Corto', 'Medio', 'Largo']
price_map = {
    'Corto': '$850 MXN',
    'Medio': '$1050 MXN',
    'Largo': '$1250 MXN'
}

def preprocess_image(image):
    image = image.resize((224, 224))
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def predict(image):
    img = preprocess_image(image)
    preds = model.predict(img)[0]
    confidence = np.max(preds)
    label_index = np.argmax(preds)
    label = class_names[label_index]

    if confidence < 0.60:
        return "🤔 Imagen menos de 60% confianza. Sube otra foto con mejor iluminación y enfoque."

    price = price_map[label]
    return f"💇‍♀️ Estilo Detectado: {label}\n🔍 Confianza: {confidence:.2%}\n💰 Precio Aproximado: {price}"

examples = [
    ["short_example.jpg"],
    ["medium_example.jpg"],
    ["long_example.jpg"]
]

with gr.Blocks() as demo:
    gr.Markdown("🤖 SmartCabello IA")
    gr.Markdown("Sube una imagen clara del cabello. Nuestra IA detecta si es corto, medio o largo y te muestra el precio estimado.")

    image_input = gr.Image(type="pil", label="Ejemplos de imágenes aceptadas ⏬️")
    submit_btn = gr.Button("Enviar")
    output = gr.Textbox(label="Resultado")
    gr.Examples(examples=examples, inputs=image_input)

    submit_btn.click(fn=predict, inputs=image_input, outputs=output)

if __name__ == "__main__":
    demo.launch()
