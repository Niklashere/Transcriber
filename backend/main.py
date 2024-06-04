"""
Main entry point for the FastAPI application.
Handles audio file upload and processing.
"""

import os

from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from config import *
from llm.llm import get_llm_text
from transcribers.transcriber import get_transcribed_text

app = FastAPI()

# Allow CORS for all origins (you can restrict this to specific domains if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/upload-audio/")
async def upload_audio(
    audiofile: UploadFile = File(...),
    language: str = Form(None),
    whisper_model: str = Form(None),
    chatgpt_model: str = Form(None)
):
    """
    Endpoint to upload audio file and receive transcribed and summarized text.
    
    :param audiofile: The audio file to be uploaded.
    :param language: The language for transcription.
    :param whisper_model: The Whisper model to use.
    :param chatgpt_model: The ChatGPT model to use for summarization.
    :return: JSONResponse containing transcribed and summarized text.
    """
    try:
        print(language)
        transcribed_text = get_transcribed_text(audiofile, language, whisper_model)
        summarized_text = get_llm_text(PROMPT, transcribed_text, chatgpt_model)
        print(summarized_text)

        return JSONResponse(content={
            "Transcribed Text": transcribed_text,
            "Summarized Text": summarized_text
        })
    except Exception as e: # pylint: disable=broad-exception-caught
        print(e)
        return JSONResponse(content={"error": f"An error occurred: {str(e)}"}, status_code=500)

def on_startup():
    """
    Set up environment variables on startup.
    """
    os.environ["OPENAI_API_KEY"] = API_KEY

if __name__ == "__main__":
    on_startup()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
