import streamlit as st

st.set_page_config(page_title='Electricity Bill Calculator', page_icon='💡')
st.title('💡 Electricity Bill Calculator')
st.info('A simple slab-based electricity bill calculator.')

with st.sidebar:
    st.subheader('Current Tamil Nadu Tariff slab rates')
    st.write('Change these values to match your tariff.')
    st.info('Consumption up to 500 units')
    rate_up_to_200 = st.number_input('Units 1–200 — ₹ per unit', min_value=0.0, value=0.00, step=0.10)
    rate_201_400 = st.number_input('Units 201–400 — ₹ per unit', min_value=0.0, value=4.70, step=0.10)
    rate_401_500 = st.number_input('Up to 500: units 401–500 — ₹ per unit', min_value=0.0, value=6.30, step=0.10)
    st.info('Consumption above 500 units')
    rate_above_500_100 = st.number_input('Units 1–100 — ₹ per unit', min_value=0.0, value=0.00, step=0.10)
    rate_above_500_101_400 = st.number_input('Units 101–400 — ₹ per unit', min_value=0.0, value=4.70, step=0.10)
    rate_above_500_401_500 = st.number_input('Above 500: units 401–500 — ₹ per unit', min_value=0.0, value=6.30, step=0.10)
    rate_501_600 = st.number_input('Units 501–600 — ₹ per unit', min_value=0.0, value=8.40, step=0.10)
    rate_601_800 = st.number_input('Units 601–800 — ₹ per unit', min_value=0.0, value=9.45, step=0.10)
    rate_801_1000 = st.number_input('Units 801–1000 — ₹ per unit', min_value=0.0, value=10.50, step=0.10)
    rate_above_1000 = st.number_input('Above 1000 units — ₹ per unit', min_value=0.0, value=11.55, step=0.10)

st.subheader('Electricity usage')
input_method = st.radio(
    'How would you like to enter consumption?',
    ['Units consumed', 'Meter readings'],
    horizontal=True,
)

if input_method == 'Units consumed':
    units = st.number_input('Units consumed', min_value=0, max_value=5000, value=250, step=1)
else:
    old_reading = st.number_input('Old meter reading', min_value=0, max_value=1_000_000, value=1000, step=1)
    current_reading = st.number_input('Current meter reading', min_value=0, max_value=1_000_000, value=1250, step=1)

def calculate_bill(u):
    if u <= 500:
        slabs = [
            ('Units 1–200', 200, rate_up_to_200),
            ('Units 201–400', 200, rate_201_400),
            ('Units 401–500', 100, rate_401_500),
        ]
    else:
        slabs = [
            ('Units 1–100', 100, rate_above_500_100),
            ('Units 101–400', 300, rate_above_500_101_400),
            ('Units 401–500', 100, rate_above_500_401_500),
            ('Units 501–600', 100, rate_501_600),
            ('Units 601–800', 200, rate_601_800),
            ('Units 801–1000', 200, rate_801_1000),
            ('Above 1000 units', float('inf'), rate_above_1000),
        ]

    remaining = u
    breakdown = []
    total = 0.0
    for slab_name, slab_limit, rate in slabs:
        slab_units = min(remaining, slab_limit)
        amount = slab_units * rate
        total += amount
        breakdown.append({'Slab': slab_name, 'Units': int(slab_units), 'Rate': f'₹{rate:.2f}', 'Amount': f'₹{amount:.2f}'})
        remaining -= slab_units
    return breakdown, total

if st.button('Calculate Bill', type='primary'):
    if input_method == 'Meter readings':
        if current_reading < old_reading:
            st.error('Current meter reading must be greater than or equal to the old reading.')
            st.stop()
        units = current_reading - old_reading

    breakdown, total = calculate_bill(units)
    c1, c2, c3 = st.columns(3)
    c1.metric('Units', units)
    c2.metric('Energy Charge', f'₹{total:,.2f}')
    c3.metric('Average / Unit', f'₹{(total / units if units else 0):,.2f}')
    st.subheader('📄 Bill Breakdown')
    st.table(breakdown)
    st.success(f'Estimated energy charge: **₹{total:,.2f}**')

st.divider()
st.subheader('Project Done By')
st.write('.......')
