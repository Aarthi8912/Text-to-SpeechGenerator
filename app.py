import streamlit as st
import cohere
from gtts import gTTS
import os
from langchain.llms.base import LLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from typing import Optional, List
import uuid


# Custom LLM for Cohere
class CohereLLM(LLM):
    def __init__(self, api_key: str):
        super().__init__()
        self._client = cohere.Client(api_key)

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        response = self._client.generate(
            model="command",
            prompt=prompt,
            max_tokens=100,
            temperature=0.7
        )
        return response.generations[0].text.strip()

    @property
    def _llm_type(self) -> str:
        return "cohere"


# === SETUP ===
COHERE_API_KEY = "your-cohere-api-key"  # 🔐 Replace with your actual API key
llm = CohereLLM(api_key=COHERE_API_KEY)

prompt_template = PromptTemplate(
    input_variables=["input_text"],
    template="Paraphrase the following sentence:\n\n{input_text}"
)
chain = LLMChain(llm=llm, prompt=prompt_template)

# === Streamlit App ===
st.set_page_config(page_title="Text-to-Speech Generator")
st.title("🗣️ Cohere + LangChain Text-to-Speech App")

input_text = st.text_area("Enter your text to paraphrase and speak:")

if st.button("Generate and Speak"):
    if not input_text.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Generating..."):
            result_text = chain.run({"input_text": input_text})
            st.success("Generated Text:")
            st.write(result_text)

            # Convert to speech using gTTS
            tts = gTTS(result_text)
            audio_path = f"output_{uuid.uuid4().hex}.mp3"
            tts.save(audio_path)

            # Play audio
            audio_file = open(audio_path, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3')

            # Cleanup after playing
            audio_file.close()
            os.remove(audio_path)
