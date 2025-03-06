import streamlit as st 
import pandas as pd 
import datetime

current_date = datetime.date.today()

df = pd.DataFrame(
    [
        {"날짜" : "2020-12-01", "제목" : "a", "관람 여부" : True, "평점" : 3},
        {"날짜" : "2020-03-06", "제목" : "b", "관람 여부" : True, "평점" : 5},
        {"날짜" : "2020-12-03", "제목" : "v", "관람 여부" : True, "평점" : 4},
        {"날짜" : "2020-12-04", "제목" : "e", "관람 여부" : True, "평점" : 2}
        
    ]
)

edited_df = st.data_editor(
    df,
    column_config={
        "평점" : st.column_config.NumberColumn(
            "평점",
            help = "1~5점 사이로 평가하세요",
            min_value=1,
            max_value=5,
            step = 1,
            format = "%d ⭐"
            ),
    },
    hide_index=True,
)


# 인생 영화
watched_movies = edited_df[edited_df["관람 여부"] == True]

# 비어 있지 않을 때만 실행
if not watched_movies.empty:  
    favorite_movie = watched_movies.loc[watched_movies["평점"].idxmax()]["제목"]
    
    favorite_date = watched_movies.loc[watched_movies["평점"].idxmax()]["날짜"]
    saved_date = pd.to_datetime(favorite_date).date()  
    lasted_days = (current_date - saved_date).days
    # lasted_days = favorite_date

else:
    favorite_movie = "-"  # 관람한 영화가 없을 경우 예외 처리
    lasted_days = None


# # 그 영화를 본 지 얼마나 되었는지
# favorite_date = edited_df.loc[edited_df["평점"].idxmax()]["날짜"]

# saved_date = pd.to_datetime(favorite_date).date()  
# lasted_days = (current_date - saved_date).days

st.markdown(f"현재까지 당신의 인생영화는 **{favorite_movie}** , D+{lasted_days}")
