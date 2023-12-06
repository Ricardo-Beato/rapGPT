import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import base64
st.set_page_config(page_title="RAP GPT", page_icon=":microphone:", layout="wide")

st.header("How do we really teach the model how to rap?")

# 1 and 2 denote that column 1 (where I put my rap_genius img) is 1/3 of the width and col2 is 2/3
col1, col2 = st.columns([1, 1])

# image to the first column
genius_logo = "../images/teaching the model.png"
col1.image(genius_logo, caption="Hi model! Hi Ricardo", width=450)

# text to the second column
col2.write("The model does not understand letters or words at first. But it does understand numbers! So first thing is to convert the input (our lyrics dataset) into vectors of numbers that the model can decode and find patterns in.")
col2.write("Just the same way, the response we get from the model is not comprised of words properly formed but rather vectors of numbers that we need to convert back to characters. I say Hello, translate to [8, 5, 12, 12, 15] and the model understands it. Then back at me: [8, 9] --> 'Hi'.")
col2.write("Notice that too much a big dataset does not equate to better learnings. Our model got pretty confused and most of all exhausted when the dataset was 35M characters long!")

st.subheader("The model is comprised of 3 layers, but what's that?")
st.markdown("We've got an **embedding layer** - this is where the model places ~words~ vectors of characters in a hypothetical space.")
st.markdown("We've got an **GRU (Gated Recurrent Unit) layer** - this is the layer where the model trains with each vector to better understand it in the context of a text.")
st.markdown("We've got an **dense layer** - this is the creative layer, where the model adjusts the previous knowledge to generate Logits which are probabilities associated to the next character. The model chooses the highest logit, meaning, the most likely character to follow the current one.")

model_summary = "../images/model_summary.png" 
st.image(model_summary, use_column_width=True)

st.subheader("We introduce a loss factor, an optimizer (Adam) and run EPOCHs")
st.markdown("The **loss factor** will help us keep track of how well the model is learning. Starts at around 4 when it suggests strange text like $/bdtnr45xxxx*35y4b and we optimize it with:")
st.markdown("the **Adam optimizer** which makes adjustments to the model's parameters with a balance of careful steps and momentum, ensuring a more efficient and adaptive descent toward the minimum error at each:")
st.markdown("**EPOCH**  - basically we split the dataset into several training sequences (batches). Everytime the model goes through ALL of these batches to learn from them, that's an EPOCH. Any time we run EPOCHs, the model is learning and optimizing.")

# Inserting a gif:
running_EPOCHs_gif = open("../images/GIF running EPOCHS.gif", "rb")
contents = running_EPOCHs_gif.read()
data_url = base64.b64encode(contents).decode("utf-8")
running_EPOCHs_gif.close()
st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="model learning at each EPOCH" width="1030">',
    unsafe_allow_html=True,
)


st.caption("_(...) Now I just wanna know / Don't just sugar coat / Or say it all if you want / Now could you tell me like it is? / Pretty little fears / Music to my ears(...)_")


