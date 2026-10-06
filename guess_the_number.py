import random
import streamlit as st

st.set_page_config(
    page_title="Infinity Coders - Guess the Number",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .block-container {
        max-width: 760px;
        padding-top: 1.2rem;
        padding-bottom: 2rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    .hero {
        text-align: center;
        padding: 1.2rem 1rem 1rem 1rem;
        border-radius: 20px;
        background: linear-gradient(135deg, #eef5ff 0%, #f8fbff 100%);
        border: 1px solid #d9e6f7;
        margin-bottom: 1rem;
    }
    .hero-title {
        font-size: clamp(2rem, 8vw, 3rem);
        font-weight: 800;
        margin: 0;
        line-height: 1.1;
    }
    .hero-subtitle {
        font-size: 1rem;
        margin-top: 0.45rem;
        color: #4b5563;
    }
    .badge {
        display: inline-block;
        margin-top: 0.65rem;
        padding: 0.28rem 0.7rem;
        border-radius: 999px;
        background: #e8f0ff;
        font-size: 0.85rem;
        font-weight: 700;
    }
    .tip {
        text-align: center;
        padding: 0.8rem;
        border-radius: 14px;
        background: #fff8e7;
        border: 1px solid #f4df9b;
        margin: 0.8rem 0 1rem 0;
    }
    .section-title {
        font-size: 1.15rem;
        font-weight: 800;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }
    .history-card {
        border-radius: 12px;
        padding: 0.55rem 0.75rem;
        border: 1px solid #e5e7eb;
        margin-bottom: 0.45rem;
        font-size: 0.95rem;
    }
    .footer {
        text-align: center;
        color: #6b7280;
        font-size: 0.85rem;
        padding-top: 1.2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def is_prime(n):
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


def clue_1(target):
    kind = "even" if target % 2 == 0 else "odd"
    return "💡 **Clue 1:** The number is **{}**.".format(kind)


def clue_2(target):
    kind = "prime" if is_prime(target) else "composite"
    return "💡 **Clue 2:** The number is **{}**.".format(kind)


def clue_3(target):
    factors = [d for d in range(2, min(target, 10) + 1) if target % d == 0]
    if factors:
        d = max(factors)
        return (
            "💡 **Clue 3:** The number is **divisible by {}** "
            "(so {} is a factor).".format(d, d)
        )
    return "💡 **Clue 3:** The number is **not divisible by 4, 6, 8 or 9**."


def clue_4(target):
    if target == 100:
        low, high = 90, 100
    else:
        low = (target // 10) * 10
        high = low + 10
    return "💡 **Clue 4:** The number is **between {} and {}**.".format(low, high)


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
    st.session_state.score = 100


if "target" not in st.session_state:
    start_game()

st.markdown(
    """
    <div class="hero">
        <div class="hero-title">🎯 Guess the Number</div>
        <div class="hero-subtitle">
            Think logically. Use the clues. Beat your best score!
        </div>
        <div class="badge">♾️ Infinity Coders</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="tip">
        🧠 <b>Challenge:</b> I am thinking of a number from <b>10 to 100</b>.
        Can you find it?
    </div>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("📘 How to Play")
    st.write("1. Guess a number from **10 to 100**.")
    st.write("2. You will be told **Too high**, **Too low**, or **Correct**.")
    st.write("3. After **2 failed attempts**, clues begin.")
    st.write("4. Each further failed attempt unlocks another clue.")
    st.write("5. Use mathematics and logic to narrow the answer.")
    st.divider()
    st.write("🎓 **What you learn**")
    st.write("• Comparison")
    st.write("• Even / odd numbers")
    st.write("• Prime / composite numbers")
    st.write("• Factors and divisibility")
    st.write("• Logical thinking")

left, right = st.columns(2)
with left:
    if st.button("🔄 New Game", use_container_width=True):
        start_game()
        st.rerun()
with right:
    st.metric("🏆 Score", st.session_state.score)

col1, col2, col3 = st.columns(3)
col1.metric("Attempts", st.session_state.attempts)
col2.metric(
    "Last Guess",
    "-" if st.session_state.last_guess is None else st.session_state.last_guess,
)
col3.metric("Clues", len(st.session_state.clues))

st.divider()

if not st.session_state.game_over:
    st.markdown('<div class="section-title">🎲 Make Your Guess</div>', unsafe_allow_html=True)
    with st.form("guess_form", clear_on_submit=False):
        guess = st.number_input(
            "Enter a whole number",
            min_value=10,
            max_value=100,
            value=50,
            step=1,
            help="Choose a number between 10 and 100.",
        )
        submitted = st.form_submit_button(
            "🎯 GUESS",
            type="primary",
            use_container_width=True,
        )

    if submitted:
        guess = int(guess)
        st.session_state.attempts += 1
        st.session_state.last_guess = guess

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
            st.session_state.score = max(10, 110 - (st.session_state.attempts * 10))

        st.session_state.history.append(
            {
                "Attempt": st.session_state.attempts,
                "Guess": guess,
                "Result": result,
            }
        )

        if not st.session_state.game_over:
            new_clue = get_next_clue(st.session_state.target, st.session_state.attempts)
            if new_clue:
                st.session_state.clues.append(new_clue)
            st.session_state.score = max(10, 100 - (st.session_state.attempts * 5))

        st.rerun()

if st.session_state.message == "🎉 Correct!":
    st.success(
        "🎉 **Fantastic!** The number was **{}**. You found it in **{} attempts**."
        .format(st.session_state.target, st.session_state.attempts)
    )
    st.markdown(
        """
        <div class="tip">
            🏆 <b>Great logical thinking!</b> Try a new game and beat your score.
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.session_state.attempts <= 3:
        st.balloons()
else:
    st.info(st.session_state.message)

if st.session_state.clues:
    st.markdown('<div class="section-title">🧩 Clues Unlocked</div>', unsafe_allow_html=True)
    for clue in st.session_state.clues:
        st.markdown(clue)

if st.session_state.history:
    st.markdown('<div class="section-title">📋 Your Guess History</div>', unsafe_allow_html=True)
    for item in reversed(st.session_state.history):
        icon = "✅" if item["Result"] == "🎉 Correct!" else "🔹"
        st.markdown(
            '<div class="history-card">{} <b>Attempt {}</b> &nbsp; → &nbsp; '
            'Guess: <b>{}</b> &nbsp; → &nbsp; {}</div>'.format(
                icon,
                item["Attempt"],
                item["Guess"],
                item["Result"],
            ),
            unsafe_allow_html=True,
        )

st.markdown(
    """
    <div class="footer">
        Developed by <b>Infinity Coders - Techno Club</b> • Sree Jayam School<br>
        Pragnya • Logic • Problem Solving
    </div>
    """,
    unsafe_allow_html=True,
)
