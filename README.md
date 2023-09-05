# PythonBookReader - An Audiobook Creator

This repository contains the code for the Audiobook Creator, a Python script designed to convert text-based PDF books into audio versions.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributions](#contributions)
- [License](#license)

## Introduction

Utilizing the PyPDF3 library to extract text from a PDF file and the Python Text-To-Speech library to convert this text into audio. You can use this script to create audiobooks from your favorite PDF books, making it easier to enjoy literature on the go or for those with visual impairments.

## Requirements

To use this script, you need the following:

- Python 3.x
- The `PyPDF2` library, which can be installed using pip:
  
  ```bash
   pip install pypdf2
   ```
  
- The `pyttsx3` module, which can be installed using pip:
  
  ```bash
   pip install pyttsx3
   ```
  
- The `threading` module (usually included in Python standard library)

## Installation

1. Clone this repository to to both the camera and remote devices or download it as a ZIP file:

   ```bash
   git clone https://github.com/elcruzo/camera-chat.git
   ```
2. Navigate to the project directory:

   ```bash
   cd camera-chat
   ```
3. Ensure you have Python 3.x installed. You can check by running:

   ```bash
   python3 --version
   ```
   If Python is not installed, you can download it from the official [Python website](https://www.python.org/downloads/).
4. Install the Vidstream Library using pip:

   ```bash
   pip install vidstream
   ```

5. Update the IP addresses and port numbers in the `index.py` file to match your network setup. Modify the following lines to match your network setup:

   ```bash
    receiving = StreamingServer('192.168.0.68', 9999)
    sending = CameraClient('192.168.0.172', 9999)
   ```
6. Replace the IP addresses and port numbers with the appropriate values for your devices.


## Usage

1. Start the server on the receiving device by running the following command:
   ```bash
   python index.py
   ```
2. Wait for a moment to allow the server to initialize.
3. Start the client on the sending device by running the following command:
   ```bash
   python index.py
   ```
4. The video stream should now start, and you can see live video from the sending device on the receiving device.
5. To end the chat, simply press Enter (or any key) in the terminal where the server is running. This will stop the video stream on both devices.

## Contributions

Contributions to this repository are welcome! If you have any improvements or feature suggestions, feel free to fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.

---

Have fun exploring my Camera Chat Application! If you have any questions or run into issues, don't hesitate to ask for help.

   
