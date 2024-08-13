import streamlit as st
from datetime import datetime, timedelta
import time


st.set_page_config(page_title="Graduation Countdown", page_icon=":hourglass:", layout="wide")


grad_date_group1 = datetime(2024, 10, 9, 0, 0, 0)  # Group 1 - Security+
grad_date_group2 = datetime(2024, 10, 15, 0, 0, 0)  # Group 2 - Needs to take Security+


def calculate_time_remaining(target_date):
    now = datetime.now()
    time_remaining = target_date - now
    days = time_remaining.days
    hours, remainder = divmod(time_remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return days, hours, minutes, seconds


st.title("Graduation Countdown Timer")
st.write("Timers that update every minute, requires streamlit to refresh every minute on user side.")




st.markdown("---")
st.header("Graduation Countdowns")


group1_placeholder = st.empty()
group2_placeholder = st.empty()


days1, hours1, minutes1, seconds1 = calculate_time_remaining(grad_date_group1)
with group1_placeholder.container():
    st.header("Group 1 (Security+)")
    st.metric("Days", days1)
    st.metric("Hours", hours1)
    st.metric("Minutes", minutes1)

days2, hours2, minutes2, seconds2 = calculate_time_remaining(grad_date_group2)
with group2_placeholder.container():
    st.header("Group 2 (Needs to take Security+)")
    st.metric("Days", days2)
    st.metric("Hours", hours2)
    st.metric("Minutes", minutes2)


time.sleep(60)
st.experimental_rerun()
