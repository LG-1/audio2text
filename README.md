# speech2text
Ease of use for Speech to Text

# Example
    stt = Audio2Text("models/silero-models/en_v2_jit.model")
    print(stt.wav2text("tests/speech_orig.wav"))

# Unittest
    python -m unittest tests.test