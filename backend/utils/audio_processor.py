import io
import numpy as np
import soundfile as sf
from fastapi import UploadFile
from scipy.signal import resample

def get_processed_audio(audio: UploadFile, target_sample_rate: int = 16000) -> np.ndarray:
    """
    Process the uploaded audio file and convert it to a numpy array with the target sample rate.
    
    :param audio: The uploaded audio file.
    :param target_sample_rate: The sample rate to which the audio will be resampled.
    :return: Processed audio as a numpy array.
    """
    wav_bytes = audio.file.read()
    wav_stream = io.BytesIO(wav_bytes)
    audio_array, sample_rate = sf.read(wav_stream)
    
    # Resample if necessary
    if sample_rate != target_sample_rate:
        num_samples = int(len(audio_array) * target_sample_rate / sample_rate)
        audio_array = resample(audio_array, num_samples)
    
    audio_array = audio_array.astype(np.float32)

    # Normalize audio
    audio_array = audio_array / np.max(np.abs(audio_array))

    return audio_array
