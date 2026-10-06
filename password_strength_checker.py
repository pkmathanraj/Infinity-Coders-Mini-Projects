import re
import streamlit as st

st.set_page_config(
    page_title="Infinity Coders - Password Strength",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------------------------
# Exhibition-friendly styling
# ---------------------------
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
        padding: 1.25rem 1rem 1rem 1rem;
        border-radius: 20px;
        background: linear-gradient(135deg, #f3efff 0%, #fbf9ff 100%);
        border: 1px solid #dfd6ff;
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
        background: #eee8ff;
        font-size: 0.85rem;
        font-weight: 700;
    }

    .warning {
        text-align: center;
        padding: 0.8rem;
        border-radius: 14px;
        background: #fff7e6;
        border: 1px solid #f1d28d;
        margin: 0.8rem 0 1rem 0;
    }

    .info-card {
        padding: 0.85rem 1rem;
        border-radius: 14px;
        background: #f8fafc;
        border: 1px solid #e5e7eb;
        margin-top: 0.75rem;
    }

    .section-title {
        font-size: 1.15rem;
        font-weight: 800;
        margin-top: 1.15rem;
        margin-bottom: 0.55rem;
    }

    .check-card {
        padding: 0.65rem 0.8rem;
        border-radius: 12px;
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

    @media (max-width: 640px) {
        .block-container {
            padding-left: 0.75rem;
            padding-right: 0.75rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------
# Header
# ---------------------------
st.markdown(
    """
    <div class="hero">
        <div class="hero-title">🔐 Password Strength Checker</div>
        <div class="hero-subtitle">
            Explore the basic rules behind a stronger password
        </div>
        <div class="badge">♾️ Infinity Coders • Cyber Safety</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="warning">
        ⚠️ <b> Never enter a real personal password here.
        Use a made-up sample password.</b>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------------------
# Sidebar
# ---------------------------
with st.sidebar:
    st.header("📘 How It Works")
    st.write("This demo checks five simple password rules:")
    st.write("1. At least 8 characters")
    st.write("2. Uppercase letter")
    st.write("3. Lowercase letter")
    st.write("4. Number")
    st.write("5. Special character")

# ---------------------------
# Password input
# ---------------------------
st.markdown(
    '<div class="section-title">🧪 Test a Password</div>',
    unsafe_allow_html=True,
)

password = st.text_input(
    "Enter a sample password",
    type="password",
    placeholder="Example: School@123",
    help="Use a made-up password for this demonstration.",
)

if password:
    score = 0
    checks = []

    rules = [
        (
            "At least 8 characters",
            len(password) >= 8,
        ),
        (
            "Contains uppercase letter",
            bool(re.search(r"[A-Z]", password)),
        ),
        (
            "Contains lowercase letter",
            bool(re.search(r"[a-z]", password)),
        ),
        (
            "Contains a number",
            bool(re.search(r"\d", password)),
        ),
        (
            "Contains a special character",
            bool(re.search(r"[^A-Za-z0-9]", password)),
        ),
    ]

    for label, passed in rules:
        if passed:
            score += 1
            checks.append((True, label))
        else:
            checks.append((False, label))

    # Keep the original 0-2 / 3-4 / 5 scoring levels.
    if score <= 2:
        strength = "WEAK"
        message = "Try adding more characters and different character types."
        emoji = "🔴"
    elif score <= 4:
        strength = "MEDIUM"
        message = "Good start. Add the missing requirement(s)."
        emoji = "🟡"
    else:
        strength = "STRONG"
        message = "Good! This sample password meets all five basic checks."
        emoji = "🟢"

    # ---------------------------
    # Result
    # ---------------------------
    st.markdown(
        '<div class="section-title">📊 Password Analysis</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)
    col1.metric("Score", "{}/5".format(score))
    col2.metric("Strength", "{} {}".format(emoji, strength))

    st.progress(score / 5)

    st.info(message)

    # ---------------------------
    # Checks
    # ---------------------------
    st.markdown(
        '<div class="section-title">✅ Security Checks</div>',
        unsafe_allow_html=True,
    )

    for passed, label in checks:
        icon = "✅" if passed else "❌"
        st.markdown(
            '<div class="check-card"><b>{}</b> {}</div>'.format(
                icon, label
            ),
            unsafe_allow_html=True,
        )

    # ---------------------------
    # Learning explanation
    # ---------------------------
    st.markdown(
        '<div class="section-title">🧠 What Happened?</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="info-card">
            The program checks the sample password against five simple rules.
            Each rule that passes adds <b>1 point</b> to the score.
            
        </div>
        """,
        unsafe_allow_html=True,
    )

else:
    st.info("👆 Enter a made-up sample password above to begin the analysis.")


# ---------------------------
# Cyber-safety tips
# ---------------------------
st.markdown(
    '<div class="section-title">🛡️ Cyber-Safety Tips</div>',
    unsafe_allow_html=True,
)

with st.expander("Show simple password safety tips"):
    st.write("• Do not share your password with other people.")
    st.write("• Avoid using easily guessed personal information.")
    st.write("• Do not reuse the same password everywhere.")
    st.write("• Use a password manager when appropriate.")
    st.write("• Use multi-factor authentication when available.")


# ---------------------------
# Footer
# ---------------------------
st.divider()

st.markdown(
    """
    <div class="footer">
        Developed by <b>Techno Club - Infinity Coders</b> • Sree Jayam School<br>
        Computer Science • Cyber Safety • Problem Solving
    </div>
    """,
    unsafe_allow_html=True,
)
