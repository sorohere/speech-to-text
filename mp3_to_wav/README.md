# Convert from mp3 to wav 

This script converts mp3 files to wav format using `librosa` and `soundfile`. 
It supports both **single file conversion** and **batch conversion** for an entire directory.

## Features 
- Convert a single mp3 file to wav.
- Convert all mp3 files in a directory to wav.
- Specify a custom output filename or directory.
- Automatically creates the output directory if it doesn’t exist.

## Requirements
Make sure you have Python installed (>=3.10) and install the required dependencies:
```
pip install librosa soundfile
```


  ## Usage 
1. Convert a single mp3 file to wav : `python convert_mp3_to_wav.py input.mp3`
2. Convert a single mp3 file to wav with custom output name : `python convert_mp3_to_wav.py input.mp3 output.wav`
3. Convert All mp3 file in a directory : `python convert_mp3_to_wav.py input_directory/`
4. Convert All mp3 file and save to a custom directory : `python convert_mp3_to_wav.py input_directory/ output_directory/`

