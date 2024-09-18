import streamlit as st

# Set up the app title and header
st.markdown("<h1 style='text-align: center; color: #FF6347;'>Welcome to the Fun Quiz!</h1>", unsafe_allow_html=True)

# Initialize session state to track score and progress
if 'score' not in st.session_state:
    st.session_state.score = 0

if 'answered_q1' not in st.session_state:
    st.session_state.answered_q1 = False
if 'answered_q2' not in st.session_state:
    st.session_state.answered_q2 = False
if 'answered_q3' not in st.session_state:
    st.session_state.answered_q3 = False

# Define the quiz function
def run_quiz():
    total_questions = 3

    # Ask if the user is ready to play
    answer = st.radio('Are you ready to play the Quiz?', ('yes', 'no'), index=1)

    if answer == 'yes':
        # Question 1
        if st.session_state.answered_q1:
            user_answer1 = st.text_input('Question 1: What is the color of the black box in an aeroplane?', value="orange" if st.session_state.score > 0 else '', disabled=True)
        else:
            user_answer1 = st.text_input('Question 1: What is the color of the black box in an aeroplane?')
            if st.button('Submit Answer 1'):
                if user_answer1 == 'Orange':
                    st.session_state.score += 1
                    st.success('Correct! 🎉')
                else:
                    st.error('Wrong Answer 😔')
                st.session_state.answered_q1 = True

        # Question 2
        if st.session_state.answered_q2:
            user_answer2 = st.text_input('Question 2: During what month do people sleep the least?', value="february" if st.session_state.score > 1 else '', disabled=True)
        else:
            user_answer2 = st.text_input('Question 2: During what month do people sleep the least?')
            if st.button('Submit Answer 2'):
                if user_answer2 == 'February':
                    st.session_state.score += 1
                    st.success('Correct! 🎉')
                else:
                    st.error('Wrong Answer 😔')
                st.session_state.answered_q2 = True

        # Question 3
        if st.session_state.answered_q3:
            user_answer3 = st.text_input('Question 3: What kind of room has no doors or windows?', value="mushroom" if st.session_state.score > 2 else '', disabled=True)
        else:
            user_answer3 = st.text_input('Question 3: What kind of room has no doors or windows?')
            if st.button('Submit Answer 3'):
                if user_answer3 == 'Mushroom':
                    st.session_state.score += 1
                    st.success('Correct! 🎉')
                else:
                    st.error('Wrong Answer 😔')
                st.session_state.answered_q3 = True

        # Display results once all questions are answered
        if st.session_state.answered_q3:
            score = st.session_state.score
            if score == 3:
                st.markdown("<h2 style='text-align: center; color: #32CD32;'>You scored 3 out of 3! 🌟</h2>", unsafe_allow_html=True)
                st.balloons()
                st.markdown("<h3 style='text-align: center; color: #FF4500;'>🎉 Congratulations! You're a Quiz Master! 🎉</h3>", unsafe_allow_html=True)
                st.markdown("<marquee style='color: #FF69B4;'>✨ Amazing job! Keep it up! ✨</marquee>", unsafe_allow_html=True)
            else:
                st.markdown(f"<h3 style='color: #FFA07A;'>You answered {score} questions correctly.</h3>", unsafe_allow_html=True)
            
            mark = (score / total_questions) * 100
            st.markdown(f"<h4 style='color: #6A5ACD;'>Marks obtained: {mark}%</h4>", unsafe_allow_html=True)

    else:
        st.warning('Please select "yes" to start the quiz!')

# Run the quiz
run_quiz()

