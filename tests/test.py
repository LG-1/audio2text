import unittest
from audio2text.audio2text import Audio2Text


class Test_Audio2Text(unittest.TestCase):
    stt = Audio2Text("models/silero-models/en_v2_jit.model")

    def test_case1(self):
        assert self.stt.wav2text("tests/16-122828-0002.wav") == "i believe you're just talking nonsense"

    def test_case2(self):
        assert self.stt.wav2text("tests/speech_orig.wav") == """the birch canoe slit on the smooth planks blared the sheet to the dark blue background it's easy to tell a depth of a well four hours of steady work faced us"""


if __name__ == '__main__':
    unittest.main()