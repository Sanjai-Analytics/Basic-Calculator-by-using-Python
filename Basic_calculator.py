import streamlit as st

st.title("Simple Calculator")

# 1. Initialize the screen value in Streamlit's "memory" (session state)
if "screen_value" not in st.session_state:
    st.session_state.screen_value = ""

# 2. Define what happens when a button is clicked
def button_click(value):
    if value == "=":
        try:
            # Evaluate the math string
            st.session_state.screen_value = str(eval(st.session_state.screen_value))
        except Exception:
            st.session_state.screen_value = "Error"
    elif value == "C":
        st.session_state.screen_value = ""
    elif value == "Guvi":
        st.session_state.screen_value = "I Learned Python at Guvi"
    else:
        st.session_state.screen_value += str(value)

# 3. Display the calculator screen
st.text_input("Display", value=st.session_state.screen_value, disabled=True, label_visibility="collapsed")

# 4. Create the button layout using columns
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

for row in buttons:
    # Create 4 equal columns for each row
    cols = st.columns(4) 
    for i, button_text in enumerate(row):
        with cols[i]:
            # Create a button that triggers the button_click function
            st.button(
                button_text, 
                on_click=button_click, 
                args=(button_text,), 
                use_container_width=True
            )

# 5. Add the extra bottom buttons
st.button("C", on_click=button_click, args=("C",), use_container_width=True)
st.button("Guvi", on_click=button_click, args=("Guvi",), use_container_width=True)