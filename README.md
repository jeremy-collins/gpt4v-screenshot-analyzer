
# GPT-4V Screenshot Analyzer

## Description

The GPT-4V Screenshot Analyzer is a tool that integrates the capabilities of OpenAI's GPT-4 Vision API into an interactive way to analyze and understand your screenshots. Screenshots are analyzed by GPT-4V to provide detailed descriptions. Additionally, this tool supports interactive dialogue, enabling users to ask follow-up questions about the screenshots for more in-depth information.

## Features

- **Image Analysis**: Utilize GPT-4 Vision API to analyze and describe screenshots.
- **Interactive Dialogue**: Engage in a chat with the AI about the screenshot for detailed insights and follow-up questions.
- **User-Friendly Interface**: Simple GUI for viewing screenshots and interacting with the AI.

## Installation (Tested on Ubuntu 20.04)

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
   - Set your OpenAI API key as an environment variable:
   ```
   echo 'export OPENAI_API_KEY=<put your key here>' >> ~/.bashrc
   ```
   - Alternatively, you can set the api_key variable inside gpt4v_screenshot_analyzer.py to your OpenAI key, but this is a security risk.

4. **Systemd Service Setup (Optional)**
   - First, make the gpt4_screenshot_analyzer.py file executable:
      ```
     sudo chmod +x gpt4_screenshot_analyzer.py
     ```
   - Then, customize the gpt4-screenshot.service file to your needs.
      - You will need to change the path to the gpt4_screenshot_analyzer.py file inside the ExecStart line.
      - You may also need to change the display number in the Environment line.
      - Lastly, you may want to change the User line.
   - To run the application as a service to be started on boot, follow these steps:
     ```
     sudo cp gpt4-screenshot.service /etc/systemd/system/
     sudo systemctl enable gpt4-screenshot
     sudo systemctl start gpt4-screenshot
     ```
   - If this doesn't work, you can debug the service by running:
     ```
     sudo systemctl status gpt4-screenshot
     ```
   - These commands may also be useful:
     ```
     sudo systemctl daemon-reload
     sudo systemctl stop gpt4-screenshot
     sudo systemctl restart gpt4-screenshot
     sudo systemctl disable gpt4-screenshot
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

Developed by [Jeremy A. Collins](https://jeremy-collins.github.io/). Special thanks to OpenAI for providing the GPT-4 Vision API.