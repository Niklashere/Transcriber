# Audio Transcriber

[![GitHub licence](https://img.shields.io/github/license/Niklashere/Transcriber)](LICENSE)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](.github/CODE_OF_CONDUCT.md)

## 📜 Description

Audio Transcriber is a tool that allows users to upload audio files via a custom API platform. The backend processes the audio files, converting them to WAV format, and then performs a transcription in text form. Users can select different language models for precise transcriptions, and the transcribed text is further processed by a language model (e.g., ChatGPT) to generate an accurate summary. Both the transcribed text and the summary are provided via the API.

## 💫 Features

- [X] Development of a custom API platform
- [X] Users can upload audio files via the API
- [X] The backend receives the audio files and converts them to WAV format
- [X] Subsequently, a transcription is performed in text form
- [X] Integration of speech recognition and/or language selection for different languages
- [X] Option to select different language models (e.g., Whisper) for precise transcriptions
- [X] The transcribed text is sent to a language model (e.g., ChatGPT) to generate an accurate summary
- [X] The transcribed text and summary are provided via the API.


## 📝 TODO

Planned features and enhancements can be found on the project's board. Check out the board for updates and future developments.

## 📩 Installation

1. Ensure Python 3.8 or later and NodeJS is installed.
2. Clone the repository.
3. Navigate in the console to the root folder of the repository.
4. **OPTIONAL:** Create a virtual environment with `python -m venv .venv` if needed. Otherwise, proceed to step 6.
5. **OPTIONAL:** Activate the virtual environment.
6. Install all required Python packages by running `pip install -r requirements.txt`.
7. Install PyTorch from [here](https://pytorch.org/get-started/locally/).
8. **OPTIONAL:** When using a supported OS, install Accelerate to benefit from performance gains. Check [here](https://huggingface.co/docs/accelerate/basic_tutorials/install) for instructions.
9. **OPTIONAL:** Install Deepspeed to benefit from additional performance gains. Instructions can be found [here](https://github.com/microsoft/DeepSpeed?tab=readme-ov-file#installation).
10. Start the backend by executing `main.py` in the backend folder.
11. Start the frontend by typing `ng serve` into the console inside the frontend folder.

## 💾 Contributing

For more information on how to contribute, please visit the [Contributing](https://github.com/Niklashere/Transcriber/wiki/Contributing) page.
