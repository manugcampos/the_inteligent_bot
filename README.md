
# el_inteligente_bot README

## Overview
`el_inteligente_bot` is a Telegram bot designed to convert PDF documents and text messages into audio files using the Google Text-to-Speech (gTTS) library. The bot offers users the convenience of listening to the contents of their documents and messages instead of reading them, making information more accessible on the go.

## Features
- **PDF to Audio Conversion:** Users can send PDF documents to the bot, which will convert the content into an audio file and send it back.
- **Text to Audio Conversion:** Users can send text messages to the bot, which will convert the text into an audio file and send it back.
- **Command-based Interaction:** The bot supports various commands to guide users through its functionalities.

## Commands
- **/start:** Provides a welcome message and instructions on how to use the bot.
- **/help:** Gives detailed information on the bot’s capabilities and future updates.
- **/texttoaudio:** Initiates the process to convert a text message into an audio file.

## Installation
To run `el_inteligente_bot` locally, follow these steps:

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/yourusername/el_inteligente_bot.git
   cd el_inteligente_bot
   ```

2. **Install Dependencies:**
   ```sh
   pip install python-telegram-bot
   pip install PyMuPDF
   pip install gtts
   ```

3. **Set Up Environment Variables:**
   Ensure you have your Telegram bot token ready. Replace the `TOKEN` variable in the script with your bot token.

4. **Run the Bot:**
   ```sh
   python bot.py
   ```

## Usage
1. **Starting the Bot:**
   - Start a conversation with your bot on Telegram.
   - Send the `/start` command to see the welcome message and instructions.

2. **Converting PDF to Audio:**
   - Send a PDF file to the bot directly.
   - The bot will process the PDF and send back an audio file of the content.

3. **Converting Text to Audio:**
   - Send the `/texttoaudio` command followed by the text message you want to convert.
   - The bot will process the text and send back an audio file of the content.

## Code Structure
- **`main.py:`** The main script to run the bot.
- **Handlers:**
  - `start_command`: Handles the `/start` command.
  - `help_command`: Handles the `/help` command.
  - `text_to_mp3_command`: Initiates text to audio conversion.
  - `convert_text_to_audio`: Converts text messages to audio.
  - `message_handler`: Processes text messages.
  - `pdf_handler`: Processes PDF files.
  - `error_handler`: Handles errors.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests on GitHub.

## Future Improvements
- **Main Idea Extraction:** Automatically summarize the main ideas of a PDF.
- **Translation Services:** Translate text before converting it to audio.
- **PDF Question Answering:** Respond to questions about the PDF content.

## Contact
If you have any problems, questions, or suggestions, please contact me on Telegram: [@manuelgutierrezc14](https://t.me/manuelgutierrezc14).

---

Thank you for using `el_inteligente_bot`! Your feedback is greatly appreciated and helps in improving the bot. 😊
