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
    name = st.text_input("Habit name")
    icon = st.text_input("Icon (emoji)", value="✅")
    category = st.text_input("Category", value="General")
    required_days = st.multiselect("Required days", DAYS)
    flexible_pool = st.multiselect("Flexible day options", DAYS)
    flexible_needed = st.number_input("How many flexible days needed?", min_value=0, max_value=7, value=0)

    submitted = st.form_submit_button("Add Habit")

    if submitted:
        if name.strip() == "":
            st.warning("Please enter a habit name.")
        else:
            new_habit = create_habit(name, icon, category, required_days, flexible_pool, flexible_needed)
            st.session_state.habits.append(new_habit)
            st.success(f"Added habit: {name}")

st.header("Your Habits")

if len(st.session_state.habits) == 0:
    st.write("No habits yet. Add one above!")
else:
    for habit in st.session_state.habits:
        st.subheader(f"{habit['icon']} {habit['name']}")
        st.write(f"Category: {habit['category']}")
        st.write(f"Required days: {', '.join(habit['required_days']) if habit['required_days'] else 'None'}")
        st.write(f"Flexible pool: {', '.join(habit['flexible_pool']) if habit['flexible_pool'] else 'None'}")
        st.write(f"Flexible days needed: {habit['flexible_needed']}")
        st.divider()
