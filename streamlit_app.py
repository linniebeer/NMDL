import streamlit as st
import pandas as pd

def main():
    st.title("File uploader")
    
    data_file = st.file_uploader("Upload xlsx", type=["xlsx"])
    
    if data_file is not None:
        file_details = {"filename": data_file.name, "filetype":data_file.type,
                        "filesize":data_file.size}
        
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
