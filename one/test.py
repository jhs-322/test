import streamlit as st 
import pandas as pd 

df = pd.DataFrame(
    [
        {"command" : "st.selectionbox", "rating":4, "is_widget": True},
        {"command" : "st.ballons", "rating" : 5, "is_widget" : False},
        {"command" : "st.time_input", "rating" : 3, "is_widget" : True}
        
    ]
)

edited_df = st.data_editor(df)
favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}**🎈")