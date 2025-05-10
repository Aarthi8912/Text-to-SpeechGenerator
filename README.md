# Text-to-SpeechGenerator


🔊 Text-to-Speech Generator Application


This is an AI-powered Text-to-Speech Generator that converts user-provided text into spoken audio. It uses Cohere for optional text enhancement, gTTS (Google Text-to-Speech) for audio generation, and Streamlit for a user-friendly web interface.

🔗 GitHub Repository:
https://github.com/<your-username>/Text-to-speechGenerator

----------------------------------------------------
📦 Requirements
----------------------------------------------------
- Python 3.8 or higher
- Streamlit
- Cohere
- LangChain
- gTTS (Google Text-to-Speech)

----------------------------------------------------
🚀 Setup Instructions
----------------------------------------------------

1. Clone the repository:
   git clone https://github.com/<your-username>/Text-to-speechGenerator.git
   cd Text-to-speechGenerator

2. Create and activate a virtual environment:
   python -m venv venv
   venv\Scripts\activate         (on Windows)
   source venv/bin/activate      (on macOS/Linux)

3. Install dependencies:
   pip install streamlit cohere langchain gTTS

4. (Optional) Set up Cohere API Key:
   - Open `app.py`
   - Replace `'your-api-key'` with your actual Cohere API key if you use Cohere

5. Run the Streamlit app:
   streamlit run app.py

----------------------------------------------------
🎤 How It Works
----------------------------------------------------
- User enters a message or text
- (Optional) Text is enhanced using Cohere or LangChain
- Text is converted into audio using gTTS
- Audio is played in the browser or downloaded as an MP3

----------------------------------------------------
📝 Example Usage
----------------------------------------------------
1. Launch the app:
   streamlit run app.py

2. In your browser:
   - Input: `Hello, welcome to AI-powered speech!`
   - Click “Generate Speech”
   - Listen to the audio or download the MP3 file

----------------------------------------------------
🛠 Sample `requirements.txt`
----------------------------------------------------
streamlit
cohere
langchain
gTTS

----------------------------------------------------
📄 License
----------------------------------------------------
MIT License – open-source and free to use!

----------------------------------------------------
🔉 Speak Your Words with AI! 🎙️
----------------------------------------------------
