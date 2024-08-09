import streamlit as st
import pandas as pd
import plotly.express as px
import base64

# Setting page configurations
st.set_page_config(page_title="CWO Class 24022 Dashboard", page_icon=":shield:", layout="wide")

# Function to insert image as background
@st.cache_data
def get_image_as_base64(file):
    with open(file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_image_as_base64('media/im11.png')
st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"]{{
    background-image: url("data:image/png;base64,{img}");
    background-color: black;
    background-size: cover;
    opacity: 0.9;
    }}
    [data-testid="stHeader"]{{
    background: rgba(0, 0, 0, 0);
    }}
    .stApp {{
        background-color: #1e1e1e;
    }}
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {{
        color: #00FFFF;
        text-shadow: 0px 0px 8px #00FFFF;
    }}
    </style>
""", unsafe_allow_html=True)

# Custom CSS to set the theme and other stylings
with open("styles/bg.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title and logo
title_cols = st.columns([10, 2])

with title_cols[0]:
    st.title(":shield: CWO Class 24022")
    st.markdown("Welcome to the CWO Class 24022 Dashboard")

with title_cols[1]:
    st.image('media/logo111.jpg')

# Blank space and divider
st.text('')
st.markdown('---')

# Sidebar Logo
with st.sidebar:
    st.image('media/logo22.png')


class_average_df = pd.read_csv('data/class_average.csv')
student_average_df = pd.read_csv('data/student_average.csv')



# Calculate the overall class average across all block tests
overall_class_average = class_average_df['Class Average'].mean()

# Display the overall class average above the graph
st.subheader(f"Overall Class Average: {overall_class_average:.2f}")

# Sort the DataFrame by the 'Current Average' column in descending order
student_average_df = student_average_df.sort_values(by='Current Average', ascending=False)

# Create a bar graph for student averages with a color gradient from blue (lowest) to green (highest)
fig_student_average = px.bar(
    student_average_df,
    x='Current Average',
    y='Student',
    orientation='h',
    title='Student Average Scores',
    color='Current Average',
    color_continuous_scale=['blue', 'green'],  # Blue to green gradient, reversed
    category_orders={"Student": student_average_df['Student'].tolist()}
)

# Update layout for the student average graph to make it transparent
fig_student_average.update_layout(
    coloraxis_colorbar=dict(
        title="Average Score",
        ticks="outside"
    ),
    plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent background
    paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent paper background
    font=dict(color='white'),
    title=dict(
        font=dict(size=24, color='#00FFFF'),
        xref='paper',
        x=0.5,
        y=0.9,
        yanchor='top'
    ),
)

# Adjusting the class average graph to improve readability and smooth the lines
fig_class_average = px.line(
    class_average_df,
    x='Test',
    y='Class Average',
    title='Class Average Scores per Block',
    markers=True,
)

# Update layout to stretch the graph, smooth the lines, set Y-axis range, and improve readability
fig_class_average.update_layout(
    xaxis=dict(
        tickangle=-45,  # Tilt the labels for better readability
        tickmode='linear'
    ),
    yaxis=dict(
        range=[70, 100],  # Set Y-axis range from 70 to 100
        title='Average Score'
    ),
    height=600,  # Increase the height of the figure
    width=1400,  # Further increase the width of the figure
    plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent background
    paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent paper background
    font=dict(color='white'),
    title=dict(
        font=dict(size=24, color='#00FFFF'),
        xref='paper',
        x=0.5,
        y=0.9,
        yanchor='top'
    ),
)

# Smooth the line by adding rounded edges
fig_class_average.update_traces(
    line_shape='spline',
    line=dict(width=4, color='#00FFFF'),
    marker=dict(
        size=10,
        color='#FFD700'  # Set marker color to a distinguishable gold
    )
)

# Display the plots in Streamlit
st.title("Class Grade Dashboard")

# Display the class average line graph
st.header("Class Average Scores per Block")
st.plotly_chart(fig_class_average)

# Display the student average bar graph
st.header("Student Average Scores")
st.plotly_chart(fig_student_average)
