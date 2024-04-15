#!/usr/bin/env python3

import argparse

import numpy as np
from scipy import signal
from pydub import AudioSegment

from main import num_tags, prediction_to_str
from morse import ALPHABET, SAMPLE_FREQ, get_spectrogram

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    args = parser.parse_args()

    audio = AudioSegment.from_file(args.input, format="ogg")
    data = np.array(audio.get_array_of_samples())
    rate = audio.frame_rate

    # Resample and rescale
    length = len(data) / rate
    new_length = int(length * SAMPLE_FREQ)

    data = signal.resample(data, new_length)
    data = data.astype(np.float32)
    data /= np.max(np.abs(data))

    # Create spectrogram
    spec = get_spectrogram(data)
    spec_orig = spec.copy()
    spectrogram_size = spec.shape[0]

    spec = spec.transpose(1,0)
    spec = np.expand_dims(spec, axis=0)

    import onnxruntime as ort

    sess = ort.InferenceSession('nn-morse.onnx')
    output = sess.run(['output'], {'input': spec})

    output1 = np.array(output[0][0])
    y_pred_l = np.exp(output1.tolist())

    # Convert prediction into string
    # TODO: proper beam search
    m = np.argmax(output1, 1)
    print(prediction_to_str(m))
