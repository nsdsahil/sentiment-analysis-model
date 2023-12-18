# enhanced_streamlit_app.py
import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
# Custom CSS for enhanced styling
custom_css = """
<style>
body {
    color: #1C1E21;
    background-color: #E1E8ED;
}

.stTextInput textarea {
    background-color: #F5F8FA;
}

.stButton button {
    background-color: #1DA1F2;
    color: #FFFFFF;
    font-weight: bold;
    border-radius: 5px;
}

.stButton button:hover {
    background-color: #1990D5;
}

.stSuccess {
    color: #17BF63;
}

.stWarning {
    color: #FF8800;
}

</style>
"""

# Function to apply custom CSS

def perform_sentiment_analysis(text):
    sia = SentimentIntensityAnalyzer()
    compound_score = sia.polarity_scores(text)['compound']
    sentiment_label = 1 if compound_score > 0 else 0
    return sentiment_label
def apply_custom_css():
    st.markdown(custom_css, unsafe_allow_html=True)

def main():
    apply_custom_css()
    st.title("Sentiment Analysis Web App")

    # Input Text
    user_input = st.text_area("What's happening?", height=200, key="input_text")

    # Predict Button
    if st.button("Tweet"):
        if not user_input.strip():
            st.warning("Please enter some text.")
        else:
            # Perform sentiment analysis using the imported function
            sentiment_label = perform_sentiment_analysis(user_input)

            # Display Result with enhanced styling
            result = "Positive" if sentiment_label == 1 else "Negative"
            st.success(f"The sentiment is: {result}")

if __name__ == "__main__":
    main()
