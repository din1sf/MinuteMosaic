import streamlit as st

# keep words in session state
if 'words' not in st.session_state:
    st.session_state.words = []

def add_word(word):
    st.session_state.words.append(word)

st.title('Minute Mosaic App')

# write number of words
st.write(f'Collected words: {len(st.session_state.words)}')

word = st.text_input('Enter new word')
st.button('Submit', key='submit', on_click=add_word, args=[word])
