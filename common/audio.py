"""
The whole module is based off the following decode and data representation

Decode:
Use wave standard library to extract audio information per sample/frame per
channel.
Each data is represented as integer in byte form and can be normalized
based on the bit depth/sample width.

Representation:
- audio value are normalized from -1.0 to 1.0
- represented as nested list, outer list representing each sample, and inner
  list representing each channel
"""


import wave
import sys  # wave module uses sys.byteorder for byte order


def wav_to_floats(path):
    """
    Convert a .wav to audio stream data represented as nested list of floats,
    with audio value stored per channel per frame.

    Example:
    a stereo wav has two channels: left and right the output audio stream list
    is like such:
        [[-0.0371, -0.1289], [-0.0182, -0.1046], [0.0018, -0.0794], [...
    where each top element represent per frame data, and nested elements
    as data per channel

    :param path: str. .wav path
    :return: tuple.
             (the audio stream represented as nested list of floats,
              the audio sample rate)

             because it is always necessary to work with sample rate
             along with samples
    """
    with wave.open(path, "r") as wav:
        channel_count, sample_width, sample_rate, frame_count, _, _ \
            = wav.getparams()

        # 8-bit wav are unsigned
        signed = sample_width > 1
        byteorder = sys.byteorder

        sample_values = list()
        for _ in range(frame_count):
            # read next frame
            frame = wav.readframes(1)

            channel_vals = list()
            for channel in range(channel_count):
                audio_bytes = frame[channel * sample_width: (channel + 1) * sample_width]
                audio_int = int.from_bytes(audio_bytes, byteorder, signed=signed)
                normalized = round(audio_int/float(pow(2, sample_width*8-1)), 4)
                channel_vals.append(normalized)

            sample_values.append(channel_vals)

    return sample_values, sample_rate


def resample_wav_floats(values, original_rate, target_rate):
    """
    Re-sample the audio values to the target rate

    To sample our audio values based on animation framerate (e.g. 30fps)
    we down-sample by extract audio values from list with an fixed interval

    :param values: list. audio value lists
    :param original_rate: int. audio original sample rate (e.g. 44100)
    :param target_rate: int. audio target rate (e.g. 30)
    :return: list. audio values nested lists sampled
    """
    return values[::int(original_rate / target_rate)]


def get_wav_info(path):
    """
    Display .wav file basic properties

    :param path: str. path to the .wav file
    :return: str. debug information
    """
    with wave.open(path, "r") as wav:
        channel, sample_width, sample_rate, frame_count, _, _ = wav.getparams()
        length = frame_count/float(sample_rate)

    return (
        "Channel count: {}\n"
        "Sample width/bit depth: {}bits\n"
        "Sample rate: {}Hz\n"
        "Total samples/frames: {}\n"
        "Total length: {}s\n"
        ).format(channel, sample_width*8, sample_rate, frame_count, length)


def convert_wav_to_list(values):
    """
    Combine and average audio values from all channels to a single channel

    :param values: nested list. audio nested floats representation
    :return: list. averaged audio values in single-level list
    """
    return [sum(channel_vals)/len(channel_vals) for channel_vals in values]
