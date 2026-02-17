# Python data converter (JSON/CSV)

## Description
A simple CLI application that give the possibility to convert a JSON file in CSV
or vice versa.

## Features
- Class DataConverter with methods csv_to_json() and json_to_csv()
- Module function helper with functions to handle if the user want to quit the
app and if the filename is valid
- Main that is the main script to convert a file
- Handling errors like FileNotFound or filename invalid format
- Read/Write CSV file with csv module
- Read/Write JSON with json module
- While loop
- Handling user inputs

## Installation
Clone the repository:
```bash
git clone https://github.com/AlexandreCst/data-converter.git
cd data-converter
```

No additional dependencies required (uses Python standard library only).

## How to Use
Run the program:
```bash
python main.py
```

Follow the prompts:
- Enter your source filename
- Enter your source path
- Enter your new filename
- Enter your new path
- View result
- Type 'q' anytime to quit

## Supported Conversions
- JSON → CSV
- CSV → JSON

## Requirements
- Python 3.9 or above

## Author
Alexandre COSTE