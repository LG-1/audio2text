# audio2text
Ease of use for audio to Text

# Example
    from audio2text.audio2text import Audio2Text
    stt = Audio2Text("models/silero-models/en_v2_jit.model")
    print(stt.wav2text("tests/speech_orig.wav"))

# Unittest
    python -m unittest tests.test