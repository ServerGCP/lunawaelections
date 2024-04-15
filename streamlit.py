from streamlit_autorefresh import st_autorefresh
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import pandas as pd
import requests, io

st_autorefresh(interval=30000, key='data_refresh')
column_names = ['Num', 'Name', 'Vaas', 'Votes']
st.set_page_config(page_title="Voting Data Dashboard", layout="wide")

def fetch_data(url):
    try:
        response = requests.get('https://lunawaelections-a3ea5ed4a880.herokuapp.com/stats/')
        if response.status_code == 200:
            return response.text
    except:
        st.error("Server Error failed to fetch Data!")
        return None
    
def main():
    if st.button('Reload Now')
        csv_data = fetch_data(api_url)
        if csv_data:
            data = pd.read_csv(io.StringIO(csv_data), names=column_names, index_col="Num")
            data["Name"] = data["Name"].str.split(' ').str[0]
            vaas_groups = data.groupby('Vaas')
    
            plots = []
            for name, group in vaas_groups:
                fig = go.Figure(data=[
                    go.Bar(
                        x=group['Name'], 
                        y=group['Votes'],
                        marker=dict(color=px.colors.qualitative.Plotly)
                    )
                ])
                fig.update_layout(
                    title=f"Votes for {name}",
                    xaxis_title="Member Name",
                    yaxis_title="Votes",
                    xaxis_tickangle=-45,
                    yaxis=dict(dtick=1),
                    height=300,
                    width=300
                )
                plots.append(fig)
    
            rows = [st.columns(4) for _ in range(3)]
            for row, fig in zip(sum(rows, []), plots):
                with row:
                    st.plotly_chart(fig, use_container_width=True)
    
if __name__ == '__main__':
    main()
