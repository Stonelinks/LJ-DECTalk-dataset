# LJ-DECTalk-dataset

A tacotron compatible version of https://keithito.com/LJ-Speech-Dataset/ using DECTalk for the voice data instead of a human's voice.

Use this with https://github.com/keithito/tacotron in the place of the LJ dataset to get a modern version of an terrible text to speech engine


## Requirements

- wine
- python3

## Usage

making the dataset:

```
python3 process.py
```

zipping it:

```
tar -cvjSf ljdectalk.tar.bz2 dataset
```