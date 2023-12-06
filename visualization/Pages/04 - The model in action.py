import os
import streamlit as st
import tensorflow as tf
import base64
st.set_page_config(page_title="RAP GPT", page_icon=":microphone:", layout="wide")

st.header("The model in action!")
st.markdown("Somehow Streamlit is not processing the line breaks '\n' as I'd like it too, so, have a gif of the model at work in Jupyter too!")


# I had to enable eager execution cause for some reason, importing the model as it was was not working...
tf.config.run_functions_eagerly(True)

# 🤷🏻‍♂️🤷🏻‍♂️🤷🏻‍♂️ getting the directory of the current script, I had to use __file__ cause telling the streamlit script where this file is was not working either
script_directory = os.path.dirname(os.path.abspath(__file__))

# I am storing the models inside the "main folder" of this project in the correspondoing Rap_GPT_06_12 folder (or whatever other)
model_path = os.path.join(script_directory, os.pardir, os.pardir, "Rap_GPT_06_12")

# Here I need to load the RNN model in eager execution mode
one_step_reloaded = tf.saved_model.load(model_path)

# the user should write something here and I'll save their input for later
text_introduction_for_rap_GPT = st.text_input("Write sumtin' for the RAP GPT to pick up on:")

# Generate RAP text - this is basically copying my RAP GPT code
if st.button("Generate RAP"):
    st.markdown("### Generated RAP:")
    
    # Initialize model state
    states = None
    next_char = tf.constant([text_introduction_for_rap_GPT])
    result = [next_char]

    for _ in range(1000):
        next_char, states = one_step_reloaded.generate_one_step(next_char, states=states)
        result.append(next_char)

    result = tf.strings.join(result)

    # Display generated text
    st.write(result[0].numpy().decode('utf-8'))

# Inserting a gif:
model_at_work_gif = open("../images/GIF Model at work.gif", "rb")
contents = model_at_work_gif.read()
data_url = base64.b64encode(contents).decode("utf-8")
model_at_work_gif.close()
st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="model working in Jupyter" width="1030">',
    unsafe_allow_html=True,
)



st.caption("_(...) I said-a hip, hop, the hippie, the hippie / To the hip hip hop-a you don't stop the rock / It to the bang-bang boogie, say up jump the boogie / To the rhythm of the boogie, the beat._")
