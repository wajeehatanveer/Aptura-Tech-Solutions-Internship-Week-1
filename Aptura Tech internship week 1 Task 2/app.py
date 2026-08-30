import streamlit as st
from game import NumberGuessingGame


# Page Configuration

st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎯",
    layout="centered"
)


# Custom CSS

st.markdown("""
<style>

    .main {
        padding-top: 2rem;
    }

    .title {
        text-align: center;
        font-size: 44px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 17px;
        margin-bottom: 25px;
    }

    .game-card {
        padding: 25px;
        border-radius: 16px;
        border: 1px solid rgba(128, 128, 128, 0.25);
        margin-top: 10px;
        margin-bottom: 20px;
    }

    .instruction {
        text-align: center;
        font-size: 16px;
        margin-bottom: 20px;
    }

    .stButton > button {
        width: 100%;
        border-radius: 10px;
        font-weight: 600;
        height: 45px;
    }

    div[data-testid="stMetric"] {
        border: 1px solid rgba(128, 128, 128, 0.25);
        padding: 12px;
        border-radius: 12px;
    }

</style>
""", unsafe_allow_html=True)


# Initialize Game

if "game" not in st.session_state:
    st.session_state.game = NumberGuessingGame()

game = st.session_state.game


# Header

st.markdown(
    '<div class="title">🎯 Number Guessing Game</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Can you find the secret number?'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# Game Card

st.markdown(
    '<div class="instruction">'
    '🎲 I have selected a number between <b>1 and 100</b>.<br>'
    'Make a guess and I will give you a hint!'
    '</div>',
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)


# Game Statistics

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "🔢 Number Range",
        "1 – 100"
    )

with col2:
    st.metric(
        "🎯 Attempts",
        game.get_attempts()
    )


st.divider()


# Guess Section

if not game.game_over:

    st.subheader("🤔 Make Your Guess")

    guess = st.number_input(
        "Enter a number",
        min_value=1,
        max_value=100,
        step=1,
        value=50
    )

    if st.button("🎯 Submit Guess"):

        result = game.make_guess(guess)

        if result == "Too Low":
            st.warning(
                "⬆️ **Too Low!** Try a higher number."
            )

        elif result == "Too High":
            st.warning(
                "⬇️ **Too High!** Try a lower number."
            )

        elif result == "Correct":
            st.balloons()

            st.success(
                f"🎉 **Congratulations!** You guessed the correct "
                f"number in **{game.get_attempts()} attempts**!"
            )


# Game Completed

else:

    st.success(
        f"🏆 You won the game in "
        f"**{game.get_attempts()} attempts!**"
    )

    st.divider()

    st.subheader("🔄 Want to play again?")

    if st.button("🎮 Start New Game"):

        game.reset_game()

        st.rerun()


# Footer

st.divider()

st.caption(
    "Built with Python 🐍 and Streamlit"
)