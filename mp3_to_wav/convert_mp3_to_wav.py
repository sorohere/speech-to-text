import os
import argparse
import librosa
import soundfile as sf

def convert_mp3_to_wav(mp3_file, wav_file):
    """Convert a single MP3 file to WAV format."""
    try:
        audio, sr = librosa.load(mp3_file, sr=None)
        sf.write(wav_file, audio, sr)
        print(f"Converted: {mp3_file} -> {wav_file}")
    except Exception as e:
        print(f"Error converting {mp3_file}: {e}")

def process_files(input_path, output_path=None):
    """Handle both single file and directory conversions."""
    if os.path.isfile(input_path):  # Single file case
        if output_path is None:
            output_path = os.path.splitext(input_path)[0] + ".wav"
        convert_mp3_to_wav(input_path, output_path)

    elif os.path.isdir(input_path):  # Directory case
        output_dir = output_path if output_path else "audios"
        os.makedirs(output_dir, exist_ok=True)

        mp3_files = [f for f in os.listdir(input_path) if f.endswith(".mp3")]
        if not mp3_files:
            print("No MP3 files found in the directory.")
            return

        for mp3_file in mp3_files:
            input_file = os.path.join(input_path, mp3_file)
            output_file = os.path.join(output_dir, os.path.splitext(mp3_file)[0] + ".wav")
            convert_mp3_to_wav(input_file, output_file)

    else:
        print("Invalid path provided. Please check the input.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert MP3 files to WAV format.")
    parser.add_argument("block1", help="MP3 file path or directory containing MP3 files.")
    parser.add_argument("block2", nargs="?", default=None, help="Output WAV file name or output directory.")

    args = parser.parse_args()
    process_files(args.block1, args.block2)
