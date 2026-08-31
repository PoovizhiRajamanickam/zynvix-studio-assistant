# 🚀 Zynvix Studio Assistant

An intelligent **AI-powered virtual assistant** built for **Zynvix Studio** to help customers explore creative and development services, understand pricing, ask questions, and submit their project requirements.

The assistant uses **Hugging Face's Meta Llama model**, **Python**, and **Streamlit** to provide an interactive conversational experience while capturing customer inquiries for easy follow-up.

---

## ✨ Features

### 🤖 AI-Powered Chatbot

* Conversational AI assistant for customer queries
* Powered by **Meta Llama** through the Hugging Face Inference API
* Uses `huggingface_hub` and `InferenceClient`
* Answers questions using Zynvix Studio's business information
* Provides service details and pricing information
* Generates clean, conversational responses

### 🎨 Service Catalog

Customers can explore Zynvix Studio's services, including:

* 📄 **Resume Building**
* 🎨 **Poster Design**
* 💻 **Portfolio Design**
* 🌐 **Website Development**

Service descriptions and pricing are provided based on the business information configured in the project.

### 📩 Lead Generation

* Collects customer inquiries
* Stores customer requirements and feedback
* Maintains inquiry records in CSV format
* Makes client follow-up easier
* Supports automated email notifications for new inquiries

### 🔐 Admin Control Panel

* Secure password-protected admin panel
* View stored customer inquiries
* Review customer feedback and ratings
* Manage and monitor submitted leads

### 💬 Modern Web Interface

* Interactive chat-based interface
* Built with **Streamlit**
* Simple and user-friendly design
* Responsive interface for different screen sizes
* Designed for quick customer interactions

---

## 🛠️ Tech Stack

| Technology              | Purpose                                       |
| ----------------------- | --------------------------------------------- |
| 🐍 **Python**           | Core programming language                     |
| 🎈 **Streamlit**        | Web application and user interface            |
| 🤖 **Hugging Face Hub** | Llama model integration                       |
| 🦙 **Meta Llama**       | AI language model                             |
| 🔌 **InferenceClient**  | Communication with Hugging Face Inference API |
| 📊 **Pandas**           | Data processing and management                |
| 📁 **CSV**              | Customer inquiry and feedback storage         |

---

## 📂 Project Structure

```text
zynvix-studio-assistant/
│
├── app.py
│   └── Main Streamlit application
│       ├── AI Chat Interface
│       ├── Service Information
│       ├── Lead Collection
│       └── Admin Control Panel
│
├── notes.txt
│   └── Business information, services,
│       pricing, and AI assistant knowledge
│
├── inquiries.csv
│   └── Customer inquiries, feedback,
│       ratings, and lead information
│
├── requirements.txt
│   └── Python dependencies
│
└── README.md
    └── Project documentation
```

---

## ⚙️ How It Works

```text
              👤 Customer
                   │
                   ▼
          💬 Streamlit Chat UI
                   │
                   ▼
            🤖 AI Assistant
                   │
          ┌────────┴────────┐
          ▼                 ▼
   📚 Business Notes    🦙 Llama Model
      notes.txt         Hugging Face
          │                 │
          └────────┬────────┘
                   ▼
             💡 AI Response
                   │
                   ▼
             📩 Lead Capture
                   │
          ┌────────┴────────┐
          ▼                 ▼
    📁 inquiries.csv    📧 Email Alert
          │
          ▼
     🔐 Admin Panel
```

The assistant uses `notes.txt` as its business knowledge source.

When a customer asks a question:

1. The question is received through the Streamlit chat interface.
2. Business information is loaded from `notes.txt`.
3. The conversation context is sent to the **Meta Llama model** through the Hugging Face Inference API.
4. `InferenceClient` handles communication with the Hugging Face model.
5. The AI generates a relevant response.
6. Customer inquiries and feedback can be stored in `inquiries.csv`.
7. Administrators can review submitted inquiries through the protected Admin Panel.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/zynvix-studio-assistant.git
```

### 2. Navigate to the Project

```bash
cd zynvix-studio-assistant
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Hugging Face API Key

Create a **Hugging Face Access Token** and set it as an environment variable.

**Windows PowerShell**

```powershell
$env:HUGGINGFACE_API_KEY="your-api-key"
```

**macOS / Linux**

```bash
export HUGGINGFACE_API_KEY="your-api-key"
```

> ⚠️ **Security:** Never hard-code your API key or commit it to GitHub.

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## 💼 Services

| Service                    | Description                                                   |
| -------------------------- | ------------------------------------------------------------- |
| 📄 **Resume Building**     | Professional and customized resume creation                   |
| 🎨 **Poster Making**       | Creative posters for events, promotions, and social media     |
| 💻 **Portfolio Design**    | Personal portfolio websites for students and professionals    |
| 🌐 **Website Development** | Modern and responsive websites for businesses and individuals |

---

## 🎯 Project Goals

The main goals of the **Zynvix Studio Assistant** are to:

* 🤖 Automate basic customer support
* 💬 Provide instant responses to customer queries
* 🎨 Showcase design and development services
* 💰 Make pricing information easily accessible
* 📩 Capture potential client leads
* 📊 Organize customer inquiries and feedback
* 🔐 Provide secure admin access
* 📧 Support automated inquiry notifications
* 🚀 Create a scalable AI-powered business assistant

---

## 🔮 Future Enhancements

Planned improvements may include:

* 💳 Online payment integration
* 🧠 Improved conversational memory
* 📈 Advanced customer analytics
* 🔔 Automated customer follow-ups
* 🗄️ Database integration
* 📱 WhatsApp integration
* 🌐 Multi-language support
* 👤 Customer account management

---

## 👨‍💻 Built By

### **Zynvix Studio**

Creative solutions for **Design, Development & Digital Services**.

---

## 📜 License

This project is created for **Zynvix Studio** and is intended for business and portfolio use.
