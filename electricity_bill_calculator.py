import streamlit as st

st.set_page_config(
    page_title="Infinity Coders - Electricity Bill",
    page_icon="⚡",
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
        max-width: 820px;
        padding-top: 1.2rem;
        padding-bottom: 2rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .hero {
        text-align: center;
        padding: 1.25rem 1rem 1rem 1rem;
        border-radius: 20px;
        background: linear-gradient(135deg, #fff7e8 0%, #fffdf8 100%);
        border: 1px solid #f0dfb7;
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
        background: #fff0c9;
        font-size: 0.85rem;
        font-weight: 700;
    }

    .info-card {
        padding: 0.85rem 1rem;
        border-radius: 14px;
        background: #f8fafc;
        border: 1px solid #e5e7eb;
        margin: 0.75rem 0;
    }

    .section-title {
        font-size: 1.15rem;
        font-weight: 800;
        margin-top: 1.15rem;
        margin-bottom: 0.55rem;
    }

    .bill-card {
        padding: 1rem;
        border-radius: 16px;
        background: #fafafa;
        border: 1px solid #e5e7eb;
        margin-top: 0.75rem;
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
        <div class="hero-title">⚡ Electricity Bill Calculator</div>
        <div class="hero-subtitle">
            Calculate your energy charge using slab-based billing
        </div>
        <div class="badge">♾️ Infinity Coders</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="info-card">
        🧮 <b>Challenge:</b> Enter your electricity usage or meter readings,
        then calculate the bill using the tariff values configured for this project.
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------------------
# Tariff settings
# ---------------------------
with st.expander("⚙️ Tariff Settings — Editable"):
    st.write(
        "The rates below are the based on the Tamil Nadu electricity provider's tariff structure. "
        "They can be changed to calculate for different tariff slabs."
    )

    st.info("Consumption up to 500 units")

    c1, c2 = st.columns(2)

    with c1:
        rate_up_to_200 = st.number_input(
            "Units 1–200 — ₹ per unit",
            min_value=0.0,
            value=0.00,
            step=0.10,
            format="%.2f",
            key="rate_up_to_200",
        )
        rate_201_400 = st.number_input(
            "Units 201–400 — ₹ per unit",
            min_value=0.0,
            value=4.70,
            step=0.10,
            format="%.2f",
            key="rate_201_400",
        )

    with c2:
        rate_401_500 = st.number_input(
            "Units 401–500 — ₹ per unit",
            min_value=0.0,
            value=6.30,
            step=0.10,
            format="%.2f",
            key="rate_401_500_under_500",
        )

    st.info("Consumption above 500 units")

    c3, c4 = st.columns(2)

    with c3:
        rate_above_500_100 = st.number_input(
            "Units 1–100 — ₹ per unit",
            min_value=0.0,
            value=0.00,
            step=0.10,
            format="%.2f",
            key="rate_above_500_100",
        )
        rate_above_500_101_400 = st.number_input(
            "Units 101–400 — ₹ per unit",
            min_value=0.0,
            value=4.70,
            step=0.10,
            format="%.2f",
            key="rate_above_500_101_400",
        )
        rate_above_500_401_500 = st.number_input(
            "Units 401–500 — ₹ per unit",
            min_value=0.0,
            value=6.30,
            step=0.10,
            format="%.2f",
            key="rate_above_500_401_500",
        )

    with c4:
        rate_501_600 = st.number_input(
            "Units 501–600 — ₹ per unit",
            min_value=0.0,
            value=8.40,
            step=0.10,
            format="%.2f",
            key="rate_501_600",
        )
        rate_601_800 = st.number_input(
            "Units 601–800 — ₹ per unit",
            min_value=0.0,
            value=9.45,
            step=0.10,
            format="%.2f",
            key="rate_601_800",
        )
        rate_801_1000 = st.number_input(
            "Units 801–1000 — ₹ per unit",
            min_value=0.0,
            value=10.50,
            step=0.10,
            format="%.2f",
            key="rate_801_1000",
        )

    rate_above_1000 = st.number_input(
        "Above 1000 units — ₹ per unit",
        min_value=0.0,
        value=11.55,
        step=0.10,
        format="%.2f",
        key="rate_above_1000",
    )


# ---------------------------
# Usage input
# ---------------------------
st.markdown(
    '<div class="section-title">🔢 Enter Electricity Usage</div>',
    unsafe_allow_html=True,
)

input_method = st.radio(
    "How would you like to enter consumption?",
    ["Units consumed", "Meter readings"],
    horizontal=True,
)

if input_method == "Units consumed":
    units = st.number_input(
        "Units consumed",
        min_value=0,
        max_value=5000,
        value=250,
        step=1,
        help="Enter the electricity units consumed during the billing period.",
    )
else:
    c1, c2 = st.columns(2)

    with c1:
        old_reading = st.number_input(
            "Old meter reading",
            min_value=0,
            max_value=1000000,
            value=1000,
            step=1,
        )

    with c2:
        current_reading = st.number_input(
            "Current meter reading",
            min_value=0,
            max_value=1000000,
            value=1250,
            step=1,
        )

    units = 0


# ---------------------------
# Calculation function
# ---------------------------
def calculate_bill(u):
    if u <= 500:
        slabs = [
            ("Units 1–200", 200, rate_up_to_200),
            ("Units 201–400", 200, rate_201_400),
            ("Units 401–500", 100, rate_401_500),
        ]
    else:
        slabs = [
            ("Units 1–100", 100, rate_above_500_100),
            ("Units 101–400", 300, rate_above_500_101_400),
            ("Units 401–500", 100, rate_above_500_401_500),
            ("Units 501–600", 100, rate_501_600),
            ("Units 601–800", 200, rate_601_800),
            ("Units 801–1000", 200, rate_801_1000),
            ("Above 1000 units", float("inf"), rate_above_1000),
        ]

    remaining = u
    breakdown = []
    total = 0.0

    for slab_name, slab_limit, rate in slabs:
        if remaining <= 0:
            break

        slab_units = min(remaining, slab_limit)
        amount = slab_units * rate
        total += amount

        breakdown.append(
            {
                "Slab": slab_name,
                "Units": int(slab_units),
                "Rate": "₹{:.2f}".format(rate),
                "Amount": "₹{:,.2f}".format(amount),
            }
        )

        remaining -= slab_units

    return breakdown, total


# ---------------------------
# Calculate button
# ---------------------------
st.markdown(
    '<div class="section-title">🧾 Generate Bill</div>',
    unsafe_allow_html=True,
)

if st.button(
    "⚡ CALCULATE ELECTRICITY BILL",
    type="primary",
    use_container_width=True,
):
    if input_method == "Meter readings":
        if current_reading < old_reading:
            st.error(
                "Current meter reading must be greater than or equal "
                "to the old reading."
            )
            st.stop()

        units = current_reading - old_reading

    breakdown, total = calculate_bill(units)

    average = total / units if units else 0

    st.success("✅ Bill calculated successfully!")

    # ---------------------------
    # Summary
    # ---------------------------
    st.markdown(
        '<div class="section-title">📊 Bill Summary</div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)

    c1.metric("Units", units)
    c2.metric("Energy Charge", "₹{:,.2f}".format(total))
    c3.metric("Average / Unit", "₹{:,.2f}".format(average))

    st.markdown(
        """
        <div class="bill-card">
            <b>⚡ Estimated Energy Charge</b>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.success("### ₹{:,.2f}".format(total))

    # ---------------------------
    # Breakdown
    # ---------------------------
    st.markdown(
        '<div class="section-title">📄 Slab-wise Bill Breakdown</div>',
        unsafe_allow_html=True,
    )

    st.table(breakdown)

    st.caption(
        "The calculation demonstrates how electricity consumption can be "
        "processed through different usage slabs."
    )



# ---------------------------
# Footer
# ---------------------------
st.divider()

st.markdown(
    """
    <div class="footer">
        Developed by <b>Techno Club - Infinity Coders</b> • Sree Jayam School<br>
        Computer Science • Mathematics • Real-World Problem Solving
    </div>
    """,
    unsafe_allow_html=True,
)
