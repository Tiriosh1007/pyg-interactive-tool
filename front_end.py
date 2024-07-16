import pandas as pd
import pygwalker as pyg
import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer
import warnings
warnings.filterwarnings('ignore')
st.set_page_config(layout='wide')

head_button_col1, head_button_col1 = st.columns([1, 1])

if 'pyg' not in st.session_state:
  st.session_state.pyg = False

with head_button_col1:
  if st.button('Reset'):
    st.session_state.pyg = False
    st.cache_resource.clear()
with head_button_col2:
  if st.button('PyGWalker'):
    st.session_state.pyg = True
    

if st.session_state.pyg == True:
  st.header('PyGWalker Interactive Analytic Tool')
  st.write('---')
  st.write("""
    #### Please upload your dataframe here
    """)
  uploaded_file = st.file_uploader("Upload xlsx or csv", accept_multiple_files=False)
  import tempfile
  import os
  temp_dir = tempfile.mkdtemp()
  path = os.path.join(temp_dir, uploaded_file.name)
  with open(path, "wb") as f:
    f.write(uploaded_file.getvalue())
  
  try:
    df = pd.read_excel(path)
  except:
    df = pd.read_csv(path)
  pyg_app = StreamlitRenderer(df)
  pyg_app.explorer()
  
