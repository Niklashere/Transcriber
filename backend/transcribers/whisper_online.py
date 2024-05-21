"""
Transcription using Whisper model online through OpenAI.
"""
import io

from openai import OpenAI

def get_online_whisper(audio: bytes, language: str = None, model_id: str = "whisper-1") -> str:
    """
    Get transcription from Whisper model online.
    
    :param audio: The audio data to transcribe.
    :param language: The language for transcription.
    :param model_id: The Whisper model ID to use.
    :return: Transcribed text.
    """
    wav_bytes = audio.file.read()
    buffer = io.BytesIO(wav_bytes)
    buffer.name = "audio.wav"  # Set a dummy filename with the appropriate extension

    client = OpenAI()

    try:
        if language is None:
            transcription = client.audio.transcriptions.create(model=model_id, file=buffer)
        else:
            transcription = client.audio.translations.create(model=model_id, file=buffer)
        return transcription.text
    except Exception as e:
        raise RuntimeError("Online Whisper transcription failed", e) from e
