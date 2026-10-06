import random
import streamlit as st

st.set_page_config(
    page_title="Infinity Coders - Guess the Number",
    page_icon="🎯",
    layout="centered",
)

st.title("🎯 Infinity Coders – Guess the Number")
st.subheader("Grade 7 • Logic & Number Challenge")
st.write("The computer is thinking of a number between **10 and 100**. Can you find it?")

# ---------------------------
# Helper functions
# ---------------------------
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def clue_1(target: int) -> str:
    return f"💡 **Clue 1:** The number is **{'even' if target % 2 == 0 else 'odd'}**."


def clue_2(target: int) -> str:
    if target == 1:
        kind = "neither prime nor composite"
    elif is_prime(target):
        kind = "prime"
    else:
        kind = "composite"
    return f"💡 **Clue 2:** The number is **{kind}**."


def clue_3(target: int) -> str:
    # Pick a useful divisor/factor when possible.
    factors = [d for d in range(2, min(target, 10) + 1) if target % d == 0]

    if factors:
        d = random.choice(factors)
        return f"💡 **Clue 3:** The number is **divisible by {d}** (so {d} is a factor of the number)."

    # Prime numbers often have no small factor.
    return f"💡 **Clue 3:** The number is a **multiple of 1**."


def clue_4(target: int) -> str:
    # Give a narrower interval around the target.
    low = max(10, target - random.randint(4, 8))
    high = min(100, target + random.randint(4, 8))

    # Make sure target lies strictly inside when possible.
    if low == target:
        low = max(10, target - 1)
    if high == target:
        high = min(100, target + 1)

    return f"💡 **Clue 4:** The number is **between {low} and {high}**."


def get_next_clue(target, attempts):
    if attempts == 2:
        return clue_1(target)
    if attempts == 3:
        return clue_2(target)
    if attempts == 4:
        return clue_3(target)
    if attempts == 5:
        return clue_4(target)
    return None

def start_game():
    st.session_state.target = random.randint(10, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.message = "Start guessing!"
    st.session_state.last_guess = None
    st.session_state.clues = []
    st.session_state.history = []

# ---------------------------
# Session state
# ---------------------------
if "target" not in st.session_state:
    start_game()

# ---------------------------
# Sidebar: game rules
# ---------------------------
with st.sidebar:
    st.header("📘 Game Rules")

    st.write("1. Guess a number from **10 to 100**.")
    st.write("2. The computer responds")
    st.write("3. After **2 failed attempts**, clues begin.")
    st.write("4. A new clue appears after each further failed attempt.")
    st.write("5. Try to solve the number using logic.")

# ---------------------------
# New game
# ---------------------------
if st.button("🔄 New Game", use_container_width=True):
    start_game()
    st.rerun()

# ---------------------------
# Score / status
# ---------------------------
col1, col2 = st.columns(2)
col1.metric("Attempts", st.session_state.attempts)
col2.metric("Last Guess", "-" if st.session_state.last_guess is None else st.session_state.last_guess)

st.divider()

# ---------------------------
# Guess input
# ---------------------------
if not st.session_state.game_over:
    guess = st.number_input(
        "Enter your guess",
        min_value=10,
        max_value=100,
        value=10,
        step=1,
    )

    if st.button("🎯 Guess", type="primary", use_container_width=True):
        st.session_state.attempts += 1
        st.session_state.last_guess = int(guess)

        if guess < st.session_state.target:
            result = "📈 Too low!"
            st.session_state.message = result
        elif guess > st.session_state.target:
            result = "📉 Too high!"
            st.session_state.message = result
        else:
            result = "🎉 Correct!"
            st.session_state.message = result
            st.session_state.game_over = True

        st.session_state.history.append(
            {
                "Attempt": st.session_state.attempts,
                "Guess": int(guess),
                "Result": result,
            }
        )

        # Only give clues for failed attempts.
        if not st.session_state.game_over:
            new_clue = get_next_clue(st.session_state.target, st.session_state.attempts)
            if new_clue:
                st.session_state.clues.append(new_clue)

        st.rerun()

# ---------------------------
# Main message
# ---------------------------
if st.session_state.message == "🎉 Correct!":
    st.success(
        f"🎉 **Correct!** The number was **{st.session_state.target}**. "
        f"You found it in **{st.session_state.attempts} attempts**."
    )
    if st.session_state.attempts <= 3:
        st.balloons()
else:
    st.info(st.session_state.message)

# ---------------------------
# Clues
# ---------------------------
if st.session_state.clues:
    st.subheader("🧩 Clues Unlocked")
    for clue in st.session_state.clues:
        st.markdown(clue)

# ---------------------------
# History
# ---------------------------
if st.session_state.history:
    st.subheader("📋 Guess History")
    st.table(st.session_state.history)
