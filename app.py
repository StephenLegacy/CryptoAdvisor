import streamlit as st
from streamlit_chat import message
from data.crypto_db import CRYPTO_DB, get_all_coins, get_coin_data
from utils.helpers import analyze_profitability, analyze_sustainability, generate_recommendation
from config.styles import apply_styles
from config.settings import APP_NAME, DISCLAIMER
from typing import List, Dict, Optional

# Initialize session state
def init_session_state():
    if 'generated' not in st.session_state:
        st.session_state['generated'] = []
    if 'past' not in st.session_state:
        st.session_state['past'] = []
    if 'input' not in st.session_state:
        st.session_state['input'] = ""

# Response generation functions
def generate_coin_response(coin: str) -> str:
    data = get_coin_data(coin)
    if not data:
        return f"Sorry, I don't have data for {coin}."
    
    response = f"📊 **{coin} Analysis**\n\n"
    response += f"📈 Price Trend: {data['price_trend'].capitalize()}\n"
    response += f"🏦 Market Cap: {data['market_cap'].capitalize()}\n"
    response += f"⚡ Energy Use: {data['energy_use'].capitalize()}\n"
    response += f"🌱 Sustainability: {data['sustainability_score']}/10\n"
    response += f"⚠️ Risk Level: {data['risk_level'].capitalize()}\n\n"
    response += f"📝 Description: {data['description']}\n\n"
    response += f"Last updated: {data.get('last_updated', 'N/A')}"
    return response

def generate_trending_response() -> str:
    trending = [coin for coin in CRYPTO_DB if CRYPTO_DB[coin]["price_trend"] == "rising"]
    if not trending:
        return "No cryptocurrencies are currently showing strong upward trends."
    
    response = "📈 Currently trending up:\n"
    for coin in trending:
        response += f"\n- **{coin}**: {CRYPTO_DB[coin]['description']}"
    return response

def generate_sustainability_response() -> str:
    sustainable = sorted(CRYPTO_DB.keys(), 
                        key=lambda x: CRYPTO_DB[x]["sustainability_score"], 
                        reverse=True)[:3]
    response = "🌱 Top sustainable cryptocurrencies:\n"
    for coin in sustainable:
        score = CRYPTO_DB[coin]["sustainability_score"]
        response += f"\n- **{coin}** (Score: {score}/10): {CRYPTO_DB[coin]['description']}"
    return response

def generate_recommendation_response() -> str:
    coin, score, data = generate_recommendation()
    response = f"💡 Recommended investment: **{coin}**\n\n"
    response += f"⭐ Overall score: {score:.1f}/10\n"
    response += f"📈 Price trend: {data['price_trend'].capitalize()}\n"
    response += f"🏦 Market cap: {data['market_cap'].capitalize()}\n"
    response += f"🌱 Sustainability: {data['sustainability_score']}/10\n"
    response += f"⚠️ Risk level: {data['risk_level'].capitalize()}\n\n"
    response += f"{data['description']}\n\n"
    response += DISCLAIMER
    return response

def generate_risk_response() -> str:
    response = "⚠️ Risk levels of major cryptocurrencies:\n"
    for coin in CRYPTO_DB:
        response += f"\n- **{coin}**: {CRYPTO_DB[coin]['risk_level'].capitalize()} risk"
    response += "\n\nGenerally, higher market cap coins tend to be less volatile."
    return response

def generate_list_response() -> str:
    response = "💰 Available cryptocurrencies:\n"
    for coin in get_all_coins():
        response += f"\n- {coin}"
    response += "\n\nAsk me about any of them for detailed analysis!"
    return response

# UI Components
def display_chat_interface():
    """Display the main chat interface"""
    st.markdown("### 💬 Chat with CryptoAdvisor")
    
    # Chat container
    chat_container = st.container()
    
    # Input area
    with st.form(key='chat_form', clear_on_submit=True):
        user_input = st.text_input("Ask me about cryptocurrencies...", key="input")
        submit_button = st.form_submit_button(label='Send')
    
    if submit_button and user_input:
        # Add user message to chat history
        st.session_state.past.append(user_input)
        
        # Get bot response
        bot_response = get_response(user_input)
        st.session_state.generated.append(bot_response)
    
    # Display chat messages
    if st.session_state['generated']:
        with chat_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state['past'][i], is_user=True, key=f"{i}_user")
                message(st.session_state['generated'][i], key=str(i))

def display_sidebar():
    """Display the sidebar content"""
    with st.sidebar:
        st.markdown(f"## 🔍 {APP_NAME} Insights")
        
        # Quick stats
        st.markdown("### 📈 Quick Stats")
        rising = [coin for coin in CRYPTO_DB if CRYPTO_DB[coin]["price_trend"] == "rising"]
        if rising:
            st.markdown(f"**Trending Up:** {', '.join(rising)}")
        
        # Sustainability leaders
        st.markdown("### 🌱 Sustainability Leaders")
        sustainable = sorted(CRYPTO_DB.keys(), 
                           key=lambda x: CRYPTO_DB[x]["sustainability_score"], 
                           reverse=True)[:3]
        for coin in sustainable:
            score = CRYPTO_DB[coin]["sustainability_score"]
            st.markdown(f"- **{coin}** ({score}/10)")
        
        # Disclaimer
        st.markdown(f"## ⚠️ Disclaimer")
        st.markdown(DISCLAIMER)

# Main processing function
def get_response(user_input: str) -> str:
    user_input = user_input.lower()
    
    # Check for greetings
    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return "Hello! I'm CryptoAdvisor. How can I help you with cryptocurrency investments today?"
    
    # Check for specific coin queries
    for coin in get_all_coins():
        if coin.lower() in user_input:
            return generate_coin_response(coin)
    
    # Process other intents
    if any(word in user_input for word in ["trend", "rising", "going up"]):
        return generate_trending_response()
    elif any(word in user_input for word in ["sustainable", "eco", "green"]):
        return generate_sustainability_response()
    elif any(word in user_input for word in ["invest", "buy", "recommend"]):
        return generate_recommendation_response()
    elif "risk" in user_input:
        return generate_risk_response()
    elif any(word in user_input for word in ["list", "all", "options"]):
        return generate_list_response()
    
    return "I'm not sure I understand. Try asking about:\n- Trending cryptocurrencies\n- Sustainable crypto options\n- Investment recommendations\n- Specific coin information"

def main():
    # App configuration
    st.set_page_config(
        page_title=APP_NAME,
        page_icon="💰",
        layout="wide"
    )
    
    # Apply custom styles
    st.markdown(apply_styles(), unsafe_allow_html=True)
    
    # Initialize session
    init_session_state()
    
    # Header
    st.title(APP_NAME)
    st.markdown("AI-powered cryptocurrency investment analysis")
    
    # Chat interface
    display_chat_interface()
    
    # Sidebar
    display_sidebar()

if __name__ == "__main__":
    main()