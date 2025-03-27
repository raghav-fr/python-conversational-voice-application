# Python Voice Assistant

- This is a Python-based voice assistant that uses speech recognition and text-to-speech capabilities to interact with users.
- It integrates with the Google GenAI API to generate responses based on user input.

## Features

- Speech recognition using `speech_recognition` library.
- Text-to-speech functionality using `pyttsx3`.
- Integration with Google GenAI for intelligent responses.

## Prerequisites

- Ensure you have Python 3.7 or later installed.
- Required Python libraries:
    - `speech_recognition`
    - `pyttsx3`
    - `google-genai`

### Installation

- Install the required libraries using pip:

    ```bash
    pip install speechrecognition pyttsx3 google-genai
    ```

### Getting Started

- Clone the repository:

    ```bash
    git clone https://github.com/your-username/python-voice-assistant.git
    cd python-voice-assistant
    ```

- Obtain a Google GenAI API key:
    - Visit the [Google GenAI API documentation](https://ai.google.dev/gemini-api/docs/api-key).
    - Click on the "Get a Gemini API Key" button.
    - Generate an API key.
    - Replace the placeholder API key in the `pyConversation.py` file with your actual API key:
        ```python
        client = genai.Client(api_key="YOUR_API_KEY_HERE")
        ```

- Run the project:

    ```bash
    python pyConversation.py
    ```

- The voice assistant will start listening for your commands. You can ask questions or give commands, and it will respond accordingly.

## Usage

- The voice assistant will start listening for your input.
- Say "exit" to terminate the program.

## License

- This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Google GenAI for the AI-powered responses.
- SpeechRecognition for speech-to-text functionality.
- pyttsx3 for text-to-speech capabilities.