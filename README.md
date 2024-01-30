# EZKeylogger

## Introduction
EZKeylogger is a simple, yet effective, keylogging tool developed by Yassin Habib. This tool is designed to record keystrokes on a computer for a set duration, capture system information, take screenshots, and then send this data via email. It's a comprehensive package for monitoring and logging system activity.

## Features
- **Keystroke Logging**: Records all keystrokes and saves them into a log file.
- **System Information Gathering**: Collects detailed system information including OS details, CPU usage, memory statistics, and clipboard content.
- **Screenshot Capturing**: Takes a screenshot at the end of the session for visual reference.
- **Email Integration**: Automatically sends the collected data (keystrokes, system information, and screenshot) to a specified email address.

## Usage
1. **Setup**: Clone the repository and install the required Python packages.
2. **Configuration**: Run the script and enter the sender's and receiver's email addresses, and the sender's email password.
3. **Execution**: The script will start collecting data, which includes logging keystrokes, gathering system information, and taking a screenshot.
4. **Email**: Upon completion, the data is compiled and sent to the specified email address.

## Requirements
- Python 3.x
- Necessary Python libraries: `keyboard`, `pyautogui`, `psutil`, `pyperclip`
- Email server credentials

## Disclaimer
This tool is intended for educational purposes only. Please ensure you have explicit authorization to use this tool on any system. Unauthorized keylogging is illegal and unethical.

## Future Improvements
The project is actively being improved. Currently, EZKeylogger requires `sudo` access to execute due to the `keyboard` library's requirements. However, future iterations are planned to remove this necessity, making the tool more accessible and user-friendly.

Stay tuned for more updates and enhancements!
