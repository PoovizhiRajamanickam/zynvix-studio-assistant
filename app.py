import streamlit as st
from huggingface_hub import InferenceClient
import streamlit.components.v1 as components
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os

# Page Configuration & Sidebar-safe CSS (Arrow will NOT hide)
st.set_page_config(page_title="Zynvix Studio Assistant", page_icon="🤖", layout="wide")

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    /* Only hiding the deployment badge/crown, keeping the header & arrow safe */
    .viewerBadge_container__1QSob {display: none !important;}
    .stAppDeployButton {display: none !important;}
    header[data-testid="stHeader"] {background: transparent !important;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("🤖 Zynvix Studio Assistant")

# --- Helper Functions ---
def save_inquiry(name, phone, service, feedback="", rating=""):
    data = {
        "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "Name": [name],
        "Phone": [phone],
        "Service": [service],
        "Feedback": [feedback],
        "Rating": [rating]
    }
    df = pd.DataFrame(data)
    file_path = "inquiries.csv"
    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df.to_csv(file_path, mode='w', header=True, index=False)

def send_email_notification(subject, body):
    try:
        sender_email = st.secrets["email"]["sender_email"]
        sender_password = st.secrets["email"]["sender_password"]
        receiver_email = st.secrets["email"]["receiver_email"]

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
    except Exception as e:
        print("Email error:", e)

# --- Sidebar: Settings & Forms ---
st.sidebar.header("⚙️ Settings & Menu")

# Language Selection
selected_lang = st.sidebar.selectbox(
    "Choose Language:", 
    ["English", "Tamil"]
)

st.sidebar.markdown("---")

# Inquiry Form in Sidebar
st.sidebar.subheader("📋 Quick Service Inquiry")
with st.sidebar.form("inquiry_form"):
    client_name = st.text_input("Your Name")
    client_phone = st.text_input("Phone Number")
    selected_service = st.selectbox(
        "Service Required:",
        ["Resume Building", "Poster Making", "Portfolio Design", "Website Development"]
    )
    submit_inquiry = st.form_submit_button("Submit Inquiry")

    if submit_inquiry:
        if client_name and client_phone:
            save_inquiry(client_name, client_phone, selected_service)
            
            email_subject = f"🚀 New Inquiry from {client_name}"
            email_body = f"You received a new service inquiry:\n\nName: {client_name}\nPhone: {client_phone}\nService: {selected_service}\nTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            send_email_notification(email_subject, email_body)
            
            st.sidebar.success(f"Thank you {client_name}! We will contact you soon.")
        else:
            st.sidebar.error("Please fill in your name and phone number.")

st.sidebar.markdown("---")

# --- Feedback Form with Star Rating inside Sidebar ---
st.sidebar.subheader("💬 Feedback & Suggestions")

star_rating_html = """
<!DOCTYPE html>
<html>
<head>
<style>
  body { background-color: transparent; margin: 0; padding: 0; }
  .star-container { display: flex; gap: 6px; font-size: 24px; cursor: pointer; user-select: none; }
  .star { color: #555; transition: color 0.2s; }
  .star.active { color: #FFD700; }
  #rating-text { margin-top: 4px; font-family: sans-serif; font-size: 12px; font-weight: bold; color: #bbb; }
</style>
</head>
<body>
<div class="star-container" id="stars">
  <span class="star" data-value="1">&#9733;</span>
  <span class="star" data-value="2">&#9733;</span>
  <span class="star" data-value="3">&#9733;</span>
  <span class="star" data-value="4">&#9733;</span>
  <span class="star" data-value="5">&#9733;</span>
</div>
<div id="rating-text">Please select a rating</div>
<script>
  const stars = document.querySelectorAll('.star');
  const ratingText = document.getElementById('rating-text');
  const texts = { 1: "very poor", 2: "fair", 3: "good", 4: "very good", 5: "excellent" };
  stars.forEach((star, index) => {
    star.addEventListener('click', () => {
      const value = index + 1;
      stars.forEach((s, i) => {
        if (i < value) { s.classList.add('active'); } else { s.classList.remove('active'); }
      });
      ratingText.innerText = texts[value];
    });
  });
</script>
</body>
</html>
"""

with st.sidebar.form("feedback_form"):
    st.write("**Rate Your Experience:**")
    components.html(star_rating_html, height=65)
    
    improvement_text = st.text_area(
        "Any improvements or suggestions?",
        placeholder="Tell us what you can improve..."
    )
    submit_feedback = st.form_submit_button("Submit Feedback")

    if submit_feedback:
        save_inquiry("Anonymous", "N/A", "Feedback Only", feedback=improvement_text)
        
        email_subject = "⭐ New Feedback Received"
        email_body = f"New feedback/suggestion:\n\n{improvement_text}\nTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        send_email_notification(email_subject, email_body)
        
        st.sidebar.success("Thank you for your valuable feedback!")

# --- Admin Panel (Protected with password '1612', hidden securely) ---
st.sidebar.markdown("---")
st.sidebar.subheader("🔒 Admin Access")

admin_password_input = st.sidebar.text_input("Enter Admin Password", type="password")

if admin_password_input == "1612":
    st.sidebar.success("Welcome Admin! Access Granted.")
    
    st.markdown("---")
    st.subheader("📊 Zynvix Studio - Admin Control Panel (Private)")
    
    if os.path.exists("inquiries.csv"):
        df_inquiries = pd.read_csv("inquiries.csv")
        st.dataframe(df_inquiries, use_container_width=True)
        
        csv_data = df_inquiries.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download All Inquiries CSV",
            data=csv_data,
            file_name='zynvix_studio_inquiries.csv',
            mime='text/csv',
        )
    else:
        st.info("No inquiries or feedbacks recorded yet.")
    st.markdown("---")

# --- Main Chat Area (Fresh and Clean for Customers) ---
if selected_lang == "Tamil":
    st.write("வணக்கம்! Zynvix Studio சேவைகள், விலைகள் மற்றும் காண்டாக்ட் விபரங்களை என்னிடம் கேட்கலாம்.")
    input_placeholder = "உங்கள் கேள்வியை இங்கே தட்டச்சு செய்யவும்..."
else:
    st.write("Ask anything about our services, pricing, offers, and contact details!")
    input_placeholder = "Type your question here..."

# Hugging Face Client Setup using Streamlit Secrets or Environment Variables
hf_token = ""
try:
    if "HUGGINGFACE_API_KEY" in st.secrets:
        hf_token = st.secrets["HUGGINGFACE_API_KEY"]
except Exception:
    pass

if not hf_token:
    hf_token = os.environ.get("HUGGINGFACE_API_KEY", "")

client = InferenceClient(api_key=hf_token)

def get_notes():
    try:
        with open("notes.txt", "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        return ""

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_query := st.chat_input(input_placeholder):
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            notes_content = get_notes()
            
            if selected_lang == "Tamil":
                lang_instruction = "Respond politely and fluently in Tamil. Whenever listing services or pricing, you MUST present them vertically line-by-line using clear bullet points (-) or numbers (1., 2., 3., 4.). Never write services as a single paragraph sentence. Enthusiastically respond to casual greetings like 'Hi'."
            else:
                lang_instruction = "Respond clearly and warmly in English. Whenever a user says 'Hi', asks about services, or asks for pricing, you MUST present the 4 core services (Resume Building, Poster Making, Portfolio Design, Website Development) vertically line-by-line using clear bullet points (-) or numbered lists (1, 2, 3, 4). Never pack services inside a paragraph sentence."

            system_prompt = f"""
            You are a friendly and helpful assistant for Zynvix Studio. 
            When greeting the user or listing services/pricing, always display the options and services vertically one below the other using clean bullet points (-) or numbers. 
            
            {lang_instruction}
            
            STUDIO NOTES:
            {notes_content}
            """
            
            try:
                completion = client.chat.completions.create(
                    model="meta-llama/Llama-3.1-8B-Instruct",
                    messages=[
                        {
                            "role": "system",
                            "content": system_prompt
                        },
                        {
                            "role": "user",
                            "content": user_query,
                        }
                    ],
                    max_tokens=500
                )
                bot_reply = completion.choices[0].message.content
            except Exception as e:
                bot_reply = f"API Error: Please check if your HUGGINGFACE_API_KEY is correctly set. (Details: {e})"
            
            st.markdown(bot_reply)
            st.session_state.messages.append({"role": "assistant", "content": bot_reply})