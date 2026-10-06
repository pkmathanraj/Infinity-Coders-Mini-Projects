import re
import streamlit as st

st.set_page_config(page_title='Password Strength Checker', page_icon='🔐')
st.title('🔐 Password Strength Checker')
st.caption('Educational demonstration only — do not enter a real personal password.')

password = st.text_input('Enter a sample password to test', type='password')

if password:
    score = 0
    checks = []
    rules = [
        ('At least 8 characters', len(password) >= 8),
        ('Contains uppercase letter', bool(re.search(r'[A-Z]', password))),
        ('Contains lowercase letter', bool(re.search(r'[a-z]', password))),
        ('Contains a number', bool(re.search(r'\d', password))),
        ('Contains a special character', bool(re.search(r'[^A-Za-z0-9]', password))),
    ]

    for label, passed in rules:
        if passed:
            score += 1
            checks.append(f'✅ {label}')
        else:
            checks.append(f'❌ {label}')

    if score <= 2:
        strength = 'WEAK'
        message = 'Try adding more characters and different character types.'
    elif score <= 4:
        strength = 'MEDIUM'
        message = 'Good start. Add the missing requirement(s).'
    else:
        strength = 'STRONG'
        message = 'Good! This sample password meets all five basic checks.'

    st.subheader(f'Strength: **{strength}**')
    st.write(message)
    st.progress(score / 5)
    st.write('### Checks')
    for item in checks:
        st.write(item)
    st.caption('This checker evaluates simple rules only. It does not prove that a password is safe.')
else:
    st.info('Enter a sample password above to see the checks.')

st.divider()
st.subheader('🧠 What students learn')
st.write('Strings • pattern matching (regular expressions) • conditions • scoring')
