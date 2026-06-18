import streamlit as st

st.title("Habit Tracker")

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Initialize habit storage (persists across reruns)
if "habits" not in st.session_state:
    st.session_state.habits = []

def create_habit(name, icon, category, required_days, flexible_pool, flexible_needed):
    return {
        "name": name,
        "icon": icon,
        "category": category,
        "required_days": required_days,
        "flexible_pool": flexible_pool,
        "flexible_needed": flexible_needed
    }

st.header("Add a Habit")

with st.form("add_habit_form"):
