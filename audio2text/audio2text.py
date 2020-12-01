import torch
from utils.utils import read_batch, prepare_model_input, Decoder


class Audio2Text(object):
    def __init__(self, model_path='models/silero-models/en_v2_jit.model', device_type='cpu'):
        self.device = torch.device(device_type)
        self.model, self.decoder = self.init_jit_model(model_path, self.device)

    def init_jit_model(self, model_path: str, device: torch.device = torch.device('cpu')):
        torch.set_grad_enabled(False)
        model = torch.jit.load(model_path, map_location=device)
        model.eval()
        return model, Decoder(model.labels)

    def wav2text(self, audio_path):
        batch = read_batch([audio_path])
        input_ = prepare_model_input(batch, device=self.device)
        output = self.model(input_)
        return self.decoder(output[0].cpu())


if __name__ == "__main__":
    stt = Audio2Text("models/silero-models/en_v2_jit.model")
    print(stt.wav2text("notebooks/input/test_wav_data/speech_orig.wav"))