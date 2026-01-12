import streamlit as st
import random
import time

st.set_page_config(page_title="Guess the Number", page_icon="🎯")

st.title("🎯 Guess The Number – Car Race Edition 🚗")


level = st.selectbox("Choose Difficulty", ["Easy", "Medium", "Hard"])

if level == "Easy":
    max_num = 50
    max_tries = 10
elif level == "Medium":
    max_num = 100
    max_tries = 7
else:
    max_num = 500
    max_tries = 5


if "number" not in st.session_state:
    st.session_state.number = random.randint(1, max_num)
    st.session_state.tries = 0
    st.session_state.win = False
    st.session_state.game_over = False


st.write(f"Guess a number between *1 and {max_num}*")
st.write(f"Attempts left: *{max_tries - st.session_state.tries}*")

guess = st.number_input("Enter your guess", 1, max_num, step=1)


if st.button("Submit Guess") and not st.session_state.game_over:
    st.session_state.tries += 1

    if guess == st.session_state.number:
        st.success(f"🎉 You won in {st.session_state.tries} tries!")
        st.session_state.win = True
        st.session_state.game_over = True

    elif st.session_state.tries == max_tries:
        st.error("😢 You lost!")
        st.write(f"Correct number was *{st.session_state.number}*")
        st.session_state.game_over = True

    elif guess < st.session_state.number:
        st.warning("⬆️ Go higher")
    else:
        st.warning("⬇️ Go lower")

if st.session_state.win:
    st.subheader("🏁 Car is racing...")
    progress = st.progress(0)

    for i in range(101):
        time.sleep(0.02)
        progress.progress(i)

    score = max(0, 100 - st.session_state.tries * 10)
    st.success(f"🚗💨 Finished! Your Score: *{score}*")


if st.button("🔄 Restart Game"):
    st.session_state.clear()

    st.experimental_rerun()
