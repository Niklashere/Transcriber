"""
Interface for transcription services.
"""
import numpy as np

from transcribers.whisper_offline import get_offline_whisper
from transcribers.whisper_online import get_online_whisper
from utils.audio_processor import get_processed_audio

def get_transcribed_text(audiofile: np.ndarray, language: str, model: str = "whisper_offline/whisper-medium") -> str:
    """
    Transcribe the given audio using specified model.
    
    :param audio_array: The audio data to transcribe.
    :param language: The language for transcription.
    :param model: The transcription model to use.
    :return: Transcribed text.
    """
    model = "whisper_offline/whisper-medium" if model == None else model
    transcriber_family, transcriber_model = model.split("/")

    if transcriber_family == "whisper_offline":
        audio_array = get_processed_audio(audiofile)
        return get_offline_whisper(audio_array, language, transcriber_model)
    if transcriber_family == "whisper_online":
        return get_online_whisper(audiofile, language, transcriber_model)
    raise ValueError(f"Unsupported transcriber family: {transcriber_family}")
