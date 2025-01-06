# Chicago Police Radio Communications Automation

This project automates the real-time extraction of audio files from the Chicago Police Department’s radio communications using data provided by OpenMHz. The workflow leverages Python and Selenium to ensure timely data capture and efficient processing for further analysis.

## Features

- **Real-Time Monitoring**: Tracks newly posted audio files on OpenMHz for immediate detection.
- **Automated Downloads**: Automatically captures audio files as they are uploaded to the platform.
- **Error Handling**: Includes robust mechanisms to handle interruptions and ensure workflow continuity.

## Requirements

- Python 3.x
- Selenium WebDriver
- Google Chrome or compatible browser
- ChromeDriver (matching the browser version)



1. Download the appropriate version of [ChromeDriver](https://sites.google.com/chromium.org/driver/) and place it in the project directory.

2. Configure the script:
   - Update the OpenMHz URL and any necessary parameters in the configuration file.

3. Run the script:
   ```bash
   python main.py
   ```

## Future Enhancements

- **Audio-to-Text Conversion**: Implement Natural Language Processing (NLP) techniques to transcribe audio files into text for actionable insights.
- **Real-Time Notifications**: Develop a system to send real-time alerts to people in the surrounding areas based on analyzed content.
