## CSV to Hexadecimal Converter

This Python script provides a user-friendly interface to convert data from a CSV file to hexadecimal format. It offers two conversion options:

* **Convert to hexadecimal (Single):** Converts the entire content of the CSV file into a single hexadecimal string.
* **Convert to hexadecimal (Each):** Converts each element within the CSV file (each cell) to a separate hexadecimal value.

## Features

- Graphical User Interface (GUI) for easy interaction.
- Handles UTF-8 encoding for broader CSV file compatibility.
- Saves the converted hexadecimal data to a new text file with a `.hex` extension.
- Displays a message box indicating the location of the saved file.

## Installation

1. Download or clone this repository.
2. Ensure you have Python 3 and `tkinter` installed (usually included with Python).

## Usage

1. Run the script using `python CSVtoHex.py` (replace `CSVtoHex.py` with your actual script filename if it's different).
2. The GUI window will appear.
3. Click the desired button:
    - "Convert to hexadecimal(Single)" to convert the entire CSV content.
    - "Convert to hexadecimal(Each)" to convert each element individually.
4. Select the CSV file you want to convert using the file selection dialog.
5. The converted data will be saved to a new `.hex` file in the same directory as your CSV file.
6. A message box will display the location of the saved file.

## Additional Notes

- This script assumes your CSV file uses UTF-8 encoding. If you're unsure about the encoding, you can try opening the file in a text editor that allows specifying encoding.
- The script can be further customized for specific needs, such as modifying the output format or adding error handling for invalid file types.
