import streamlit as st

# Page config
st.set_page_config(page_title="Neural Volts AI Chatbot", page_icon="🤖")

# Title
st.title("🤖 Neural Volts AI Chatbot")
st.write("Smart Customer Support Assistant (Demo)")

# Sample knowledge base
responses = {
    "price": "Our chatbot solutions start from Rs. 15,000 depending on features.",
    "services": "We offer AI Chatbots, Energy Optimization, Predictive Maintenance, and Smart Dashboards.",
    "contact": "You can contact us via LinkedIn or WhatsApp for a free demo.",
    "demo": "Yes! We offer a FREE demo for all our AI solutions.",
    "ai": "We use AI to automate customer interactions and improve efficiency.",
    "default": "I'm sorry, I didn't understand that. Can you please rephrase?"
}

# Function to get response
def get_response(user_input):
    user_input = user_input.lower()
    
    for keyword in responses:
        if keyword in user_input:
            return responses[keyword]
    
    return responses["default"]

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input("Ask something about our services...")

if user_input:
    # User message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.write(user_input)
    
    # Bot response
    response = get_response(user_input)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    with st.chat_message("assistant"):
        st.write(response)
