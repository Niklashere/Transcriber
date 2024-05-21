import logging
import numpy as np
import torch
import sys
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

def get_offline_whisper(audio: np.ndarray, language: str = None,
                        model_id: str = "whisper-medium") -> str:
    """
    Get transcription from Whisper model offline.
    
    :param audio: The audio data to transcribe.
    :param language: The language for transcription.
    :param model_id: The Whisper model ID to use.
    :return: Transcribed text.
    """
    model_id = "openai/" + model_id

    if 'accelerate' in sys.modules:
        model = AutoModelForSpeechSeq2Seq.from_pretrained(
            model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
        )
    else:
        model = AutoModelForSpeechSeq2Seq.from_pretrained(
            model_id, torch_dtype=torch_dtype, use_safetensors=True
        )

    model.to(device)
    processor = AutoProcessor.from_pretrained(model_id)

    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        chunk_length_s=30,
        batch_size=16,
        torch_dtype=torch_dtype,
        device=device,
    )

    try:
        if language is None:
            return pipe(audio)["text"]
        else:
            return pipe(audio, generate_kwargs={"language": language})["text"]
    except Exception as e:
        logger.error("Error during offline Whisper transcription: %s", str(e))
        raise RuntimeError("Offline Whisper transcription failed: %s" % str(e)) from e
