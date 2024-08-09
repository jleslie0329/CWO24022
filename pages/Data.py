import streamlit as st
import pandas as pd

# Set the page layout to wide
st.set_page_config(page_title="Student Bio Page", page_icon=":bust_in_silhouette:", layout="wide")

# CSS for responsive layout
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .block-container {
        padding: 1rem;
    }
    img {
        max-width: 100%;
        height: auto;
    }
    .bio-table {
        width: 100%;
        margin: auto;
        font-size: 1.1rem;
    }
    .bio-table td {
        padding: 0.5rem;
    }
    @media screen and (max-width: 600px) {
        .bio-table {
            font-size: 0.8rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Sample student bio data using the names provided
student_bio_data = {
    "SSgt Leslie": {
        "Name": "SSgt Leslie",
        "From": "Seattle, WA",
        "Favorite Movie": "Lord of the Rings - Trilogy",
        "Favorite Game": "World of Warcraft",
        "Favorite CWO Block": "Python",
        "Image": "media/SSgt_Leslie.jpg"
    },
    "SrA Snuffy": {
        "Name": "SrA Snuffy",
        "From": "Dayton, OH",
        "Favorite Movie": "Iron Man",
        "Favorite Game": "Fortnite",
        "Favorite CWO Block": "Block 2 - Linux",
        "Image": "media/SrA_Snuffy.jpg"
    },
    "Amn Packet": {
        "Name": "Amn Packet",
        "From": "San Antonio, TX",
        "Favorite Movie": "The Social Network",
        "Favorite Game": "Overwatch",
        "Favorite CWO Block": "Block 3 - Python",
        "Image": "media/Amn_Packet.jpg"
    },
    "TSgt Hackerman": {
        "Name": "TSgt Hackerman",
        "From": "Denver, CO",
        "Favorite Movie": "The Matrix",
        "Favorite Game": "Minecraft",
        "Favorite CWO Block": "Block 4 - Network Fundamentals",
        "Image": "media/TSgt_Hackerman.jpg"
    },
    "A1C RedCard": {
        "Name": "A1C RedCard",
        "From": "New York, NY",
        "Favorite Movie": "Star Wars",
        "Favorite Game": "League of Legends",
        "Favorite CWO Block": "Block 5 - Network Config",
        "Image": "media/A1C_RedCard.jpg"
    },
    "Amn YellowRope": {
        "Name": "Amn YellowRope",
        "From": "Atlanta, GA",
        "Favorite Movie": "Avengers: Endgame",
        "Favorite Game": "Valorant",
        "Favorite CWO Block": "Block 6 - Intro to CWO",
        "Image": "media/Amn_YellowRope.png"
    },
    "SrA Doubletap": {
        "Name": "SrA Doubletap",
        "From": "Phoenix, AZ",
        "Favorite Movie": "John Wick",
        "Favorite Game": "Apex Legends",
        "Favorite CWO Block": "Block 7 - Cyber Systems",
        "Image": "media/SrA_Doubletap.jpg"
    },
    "A1C Zoomer": {
        "Name": "A1C Zoomer",
        "From": "Las Vegas, NV",
        "Favorite Movie": "Fast & Furious",
        "Favorite Game": "Rocket League",
        "Favorite CWO Block": "Block 8 - OCO",
        "Image": "media/A1C_Zoomer.jpg"
    },
    "SSgt Engines": {
        "Name": "SSgt Engines",
        "From": "Houston, TX",
        "Favorite Movie": "Transformers",
        "Favorite Game": "World of Tanks",
        "Favorite CWO Block": "Block 9 - DCO",
        "Image": "media/SSgt_Engines.jpg"
    },
    "A1C S.I.A.": {
        "Name": "A1C S.I.A.",
        "From": "San Diego, CA",
        "Favorite Movie": "Interstellar",
        "Favorite Game": "Stellaris",
        "Favorite CWO Block": "Block 10 - Ops Planning",
        "Image": "media/A1C_S.I.A..jpg"
    },
    "TSgt SpaceForce": {
        "Name": "TSgt SpaceForce",
        "From": "Cape Canaveral, FL",
        "Favorite Movie": "Gravity",
        "Favorite Game": "Kerbal Space Program",
        "Favorite CWO Block": "Block 11 - Capstone",
        "Image": "media/TSgt_SpaceForce.jpg"
    }
}

# Sidebar to select a student
st.sidebar.title("Select a Student")
selected_student = st.sidebar.selectbox("Choose a student", list(student_bio_data.keys()))

# Display the selected student's bio
student = student_bio_data[selected_student]

st.title(f"Bio of {student['Name']}")

# Create responsive columns for the image and bio table
col1, col2 = st.columns([1, 2])

with col1:
    st.image(student["Image"], width=None)  # Auto-resize the image based on the column width

with col2:
    st.markdown(f"""
    <table class="bio-table">
        <tr><td><strong>Name</strong></td><td>{student['Name']}</td></tr>
        <tr><td><strong>From</strong></td><td>{student['From']}</td></tr>
        <tr><td><strong>Favorite Movie</strong></td><td>{student['Favorite Movie']}</td></tr>
        <tr><td><strong>Favorite Game</strong></td><td>{student['Favorite Game']}</td></tr>
        <tr><td><strong>Favorite CWO Block</strong></td><td>{student['Favorite CWO Block']}</td></tr>
    </table>
    """, unsafe_allow_html=True)
