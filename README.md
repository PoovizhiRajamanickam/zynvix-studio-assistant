# 🚀 Zynvix Studio Assistant

An intelligent **AI-powered virtual assistant** built for **Zynvix Studio** to help customers instantly explore services, understand pricing, ask questions, and submit their project requirements.

The assistant combines **Google GenAI, Python, and Streamlit** to provide a simple conversational experience while automatically collecting potential client leads.

---

## ✨ Features

### 🤖 AI-Powered Chatbot

* Conversational AI assistant for customer queries
* Powered by Google's GenAI model
* Answers questions using Zynvix Studio's custom business information
* Provides relevant service and pricing details

### 🎨 Service Catalog

Customers can quickly explore available services, including:

* 📄 Resume Building
* 🎨 Poster Design
* 💻 Portfolio Design
* 🌐 Website Development

The assistant provides service descriptions and pricing information based on the configured business notes.

### 📩 Automated Lead Generation

* Collects customer inquiries
* Captures potential client requirements
* Stores lead information systematically
* Makes it easier to follow up with interested customers

### 💬 Conversational Interface

* Simple and interactive chat experience
* Built with Streamlit
* Responsive and easy to use
* Designed for quick customer interactions

---

## 🛠️ Tech Stack

| Technology              | Purpose                      |
| ----------------------- | ---------------------------- |
| 🐍 **Python**           | Core programming language    |
| 🎈 **Streamlit**        | Web application interface    |
| 🤖 **Google GenAI SDK** | AI-powered conversations     |
| 📊 **Pandas**           | Data handling and management |

---

## 📂 Project Structure

```text
zynvix-studio-assistant/
│
├── app.py
│   └── Main Streamlit web application
│
├── agent.py
│   └── AI agent logic, session management,
│      and Google GenAI integration
│
├── notes.txt
│   └── Business information, services,
│      pricing, and assistant knowledge
│
├── requirements.txt
│   └── Project dependencies
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
       ┌─────┴─────┐
       ▼           ▼
  📚 Business    🧠 Google
     Notes          GenAI
       │           │
       └─────┬─────┘
             ▼
      💡 AI Response
             │
             ▼
       📩 Lead Capture
```

The assistant uses the information stored in `notes.txt` as its business knowledge source. When a customer asks a question, the application sends the relevant context to the Google GenAI model and generates a suitable response.

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

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API Key

Create a Google GenAI API key and configure it as an environment variable.

**Windows PowerShell:**

```powershell
$env:GEMINI_API_KEY="your-api-key"
```

**macOS / Linux:**

```bash
export GEMINI_API_KEY="your-api-key"
```

> ⚠️ Never commit your API key directly to GitHub.

---

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💼 Services

| Service                | Description                                                   |
| ---------------------- | ------------------------------------------------------------- |
| 📄 Resume Building     | Professional and customized resume creation                   |
| 🎨 Poster Making       | Creative posters for events, promotions, and social media     |
| 💻 Portfolio Design    | Personal portfolio websites for students and professionals    |
| 🌐 Website Development | Modern and responsive websites for businesses and individuals |

---

## 🎯 Project Goals

The main goals of the Zynvix Studio Assistant are to:

* Automate basic customer support
* Provide instant service information
* Make pricing information easily accessible
* Reduce repetitive customer inquiries
* Capture potential client leads
* Improve customer engagement
* Provide a scalable AI-based business assistant

---

## 🔮 Future Enhancements

Planned improvements may include:

* 📧 Email notifications for new leads
* 🗄️ Database integration for lead management
* 📊 Admin dashboard
* 💳 Online payment integration
* 🌐 Multi-language support
* 🧠 Improved conversational memory
* 📈 Customer analytics
* 🔔 Automated follow-up messages

---

## 👨‍💻 Built By

**Zynvix Studio**

Creative solutions for **Design, Development & Digital Services**.

---

## 📜 License

This project is created for **Zynvix Studio** and is intended for business and portfolio use.
