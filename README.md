# PythonBookReader - An Audiobook Creator

Welcome to my repository containing the code for the Audiobook Creator, a Python script designed to convert text-based PDF books into audio versions.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Contributions](#contributions)
- [License](#license)
- [Acknowledgments](#acknowledgements)

## Introduction

Utilizing the PyPDF3 library to extract text from a PDF file and the Python Text-To-Speech library to convert this text into audio. You can use this script to create audiobooks from your favorite PDF books, making it easier to enjoy literature on the go or for those with visual impairments.

## Requirements

To use this script, you need the following:

- Python 3.x
- The `PyPDF3` library, which can be installed using pip:
  
  ```bash
   pip install pypdf3
   ```
  
- The `pyttsx3` module, which can be installed using pip:
  
  ```bash
   pip install pyttsx3
   ```

## Installation

1. Clone this repository to to both the camera and remote devices or download it as a ZIP file:

   ```bash
   git clone https://github.com/elcruzo/audiobook-script.git
   ```
   
2. Navigate to the project directory:

   ```bash
   cd audiobook-script
   ```
   
3. Ensure you have Python 3.x installed. You can check by running:

   ```bash
   python3 --version
   ```
   If Python is not installed, you can download it from the official [Python website](https://www.python.org/downloads/).

## Usage
   
1. Place Your PDF File in the project directory. Make sure to rename the PDF file to `book.pdf` or modify the script to specify the correct file path.

2. Run the Script:

   ```bash
   python index.py
   ```
   
3. The script will process the PDF file and create an audiobook in MP3 format named `myaudiobook.mp3` in the same directory.

## Customization

You can customize the script by adjusting the following parameters:

- `rate` : You can change the reading speed by modifying the rate property. The current rate is set to 100, but you can increase or decrease it as needed for a comfortable listening experience.

## Contributions

Contributions to this repository are welcome! If you have any improvements or feature suggestions, feel free to fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project is based on the PyPDF3 and pyttsx3 libraries. Special thanks to the developers of these libraries for their contributions.

---

Enjoy your newly created audiobook with PythonBookReader! If you have any questions or encounter any issues, please feel free to open an issue in the project's GitHub repository.

   
