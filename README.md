# KrishiMitra: Your AI Agricultural Advisor 🌾
KrishiMitra is an AI-powered agricultural advisory application built with Streamlit. It aims to assist Indian farmers by providing relevant and actionable advice on various farming topics, leveraging the power of Google's Gemini model and web search capabilities.

Features
AI-Powered Advice: Get intelligent answers to your farming questions, powered by the Gemini 2.0 Flash model.

Contextual Information: Utilizes web search (via SerpAPI) to fetch up-to-date and location-specific information based on your queries and pincode.

User-Friendly Interface: A simple and intuitive Streamlit interface makes it easy for farmers to ask questions and receive advice.

Demographic Relevance: Advice is tailored by incorporating demographic details like pincode, ensuring more accurate and relevant suggestions.

Project Structure
krishimitra/
├── config/
│   ├── __init__.py
│   └── config.py          # Loads API keys from .env
├── pages/
│   ├── __init__.py
│   └── 1_Crop_Page.py     # Streamlit page for crop-related queries
├── services/
│   └── gemini_client.py   # Handles Gemini API calls and SerpAPI integration
├── app.py                 # Main Streamlit application entry point
├── poetry.lock            # Poetry lock file for dependency management
├── pyproject.toml         # Poetry project configuration
└── README.md              # This README file

Setup and Installation
Follow these steps to set up and run the KrishiMitra application locally.

1. Prerequisites
Python 3.8+

pip (Python package installer) or poetry (if you prefer using it for dependency management)

2. Clone the Repository (if applicable)
If your project is in a Git repository, clone it:

git clone <your-repository-url>
cd krishimitra

3. Install Dependencies
It's recommended to use a virtual environment.

Using pip:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt # You might need to create this from pyproject.toml
# Or manually install:
pip install streamlit langchain langchain-google-genai python-dotenv google-search-results

Using Poetry (if pyproject.toml is configured for it):

poetry install
poetry shell

4. Obtain API Keys
KrishiMitra requires API keys for the following services:

Google Gemini API Key: For accessing the Gemini model. You can get this from Google AI Studio.

SerpAPI API Key: For performing web searches. Obtain this from SerpAPI.

5. Configure Environment Variables
Create a directory named config at the root of your project if it doesn't exist. Inside the config directory, create a file named .env and add your API keys as follows:

# config/.env
GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY_HERE"
SERPAPI_API_KEY="YOUR_SERPAPI_API_KEY_HERE"

Replace "YOUR_GOOGLE_API_KEY_HERE" and "YOUR_SERPAPI_API_KEY_HERE" with your actual keys.

6. Run the Application
Navigate to the root directory of your project (where app.py is located) in your terminal and run the Streamlit application:

streamlit run app.py

This command will open the KrishiMitra application in your default web browser.

How to Use
Welcome Page: When you open the app, you'll land on the welcome page (app.py).

Navigation: Use the sidebar on the left to navigate to different sections of the application. Currently, you'll find the "Crop Page".

Ask Questions: On the "Crop Page", enter your agricultural question and your pincode.

Get Answer: Click the "Get Answer" button to receive AI-generated advice.

Contributing
(Optional section - if you plan to allow contributions)
If you'd like to contribute to KrishiMitra, please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/your-feature-name).

Make your changes and commit them (git commit -m 'Add new feature').

Push to the branch (git push origin feature/your-feature-name).

Open a Pull Request.

License
(Optional section - specify your project's license)
This project is licensed under the MIT License - see the LICENSE file for details.

Thank you for using KrishiMitra! We hope it helps farmers thrive.