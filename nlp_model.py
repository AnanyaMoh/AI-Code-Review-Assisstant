import tensorflow as tf
import numpy as np

# Load pre-trained model
model = tf.keras.models.load_model('model/code_model.h5')

def get_nlp_feedback(code):
    # Dummy vectorization - Replace with real tokenizer
    inputs = np.random.rand(1, 100)  
    prediction = model.predict(inputs)
    return ["Consider simplifying nested loops", "Use meaningful variable names"]
