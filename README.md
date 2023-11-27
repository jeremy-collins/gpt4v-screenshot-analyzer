
# GPT-4V Screenshot Analyzer

## Description

The GPT-4V Screenshot Analyzer is a tool that integrates the capabilities of OpenAI's GPT-4 Vision API into an interactive way to analyze and understand your screenshots. Screenshots are analyzed by GPT-4V to provide detailed descriptions. Additionally, this tool supports interactive dialogue, enabling users to ask follow-up questions about the screenshots for more in-depth information.

## Features

- **Image Analysis**: Utilize GPT-4 Vision API to analyze and describe screenshots.
- **Interactive Dialogue**: Engage in a chat with the AI about the screenshot for detailed insights and follow-up questions.
- **User-Friendly Interface**: Simple GUI for viewing screenshots and interacting with the AI.

## Installation

1. **Clone the Repository**
   ```
   git clone https://github.com/jeremy-collins/gpt4v-screenshot-analyzer.git
   ```

2. **Install Dependencies**
   - Ensure Python 3 is installed.
   - Install required Python libraries:
     ```
     pip install -r requirements.txt
     ```

3. **Set Up OpenAI API Key**
   - Obtain an API key from OpenAI.
   - Replace `your-api-key-here` in `gpt4_screenshot_analyzer.py` with your actual API key.

4. **Systemd Service Setup (Optional)**
   - To run the application as a service to be started on boot, follow these steps:
     ```
     sudo cp gpt4-screenshot.service /etc/systemd/system/
     sudo systemctl enable gpt4-screenshot
     sudo systemctl start gpt4-screenshot
     ```

## Usage

- Start the application:
  ```
  python3 gpt4_screenshot_analyzer.py
  ```
- Use the `Ctrl+Alt+S` hotkey to start a screenshot capture.
- Drag to select the area you want to capture.
- GPT-4V will analyze the screenshot and display the results in a GUI window.
- Use the text box in the GUI to ask follow-up questions.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.

## Credits

Developed by [Jeremy A. Collins](jeremy-collins.github.io). Special thanks to OpenAI for providing the GPT-4 Vision API.