import streamlit as st
from openai import OpenAI 

if 'words' not in st.session_state:
    st.session_state.words = []

def generate_mosaic(words):
    if not words:
        words = ['nothing']

    items = ', '.join(words)
    prompt = f"Create image containing all of the following items: {items}"       
    open_ai_key = st.secrets.get("OPENAI_API_KEY")                                           
    client = OpenAI(api_key=open_ai_key)
    response = client.images.generate(
        model='dall-e-3',
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    print(image_url)
    return image_url

def generate(word):
    with st.spinner('Generating...'):
        st.session_state.image_url = generate_mosaic(st.session_state.words)
        st.image(st.session_state.image_url)

st.title('Minute Mosaic Admin')

st.write('Words:', st.session_state.words)

st.button('Generate', on_click=generate, args=[st.session_state.words])
st.button('Clear', on_click=lambda: st.session_state.pop('words', None))