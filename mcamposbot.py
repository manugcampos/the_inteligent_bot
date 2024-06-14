from typing import final
from telegram import Update, Document
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, ConversationHandler
import fitz  # PyMuPDF
import os
from gtts import gTTS

TOKEN: final = '7385014817:AAH2GHV4d-zJzMem1oVGBymEWnQhSACCOxo'
BOT_USERNAME: final = '@el_inteligente_bot'

TEXT_TO_AUDIO = range(1)

async def start_command(update: Update, context: CallbackContext):
    await update.message.reply_text(
        'Si quieres convertir un archivo PDF en audio, solo tienes que enviármelo sin usar ningún comando. Si por el contrario, quieres pasar de un mensaje de texto a audio, usa el comando /texttoaudio y escríbeme lo que desees. 📚🔊. \n\n'
        'Si tienes algún problema, duda o sugerencia, por favor, contáctame por Telegram a @manuelgutierrezc14. \n'
        'Recuerda que iré mejorando con el tiempo, ¡gracias por tu Feedback! 😊'
    )

async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text('De momento, solo puedo crear audios a partir de archivos PDF y mensajes. Si quieres un audio a partir de un PDF, solo adjúntalo sin usar ningún comando. Para convertir un mensaje a audio, selecciona /texttoaudio en el menú y envíame el texto en el siguiente mensaje 🙂.\n\nEn las siguientes actualizaciones, podré hacer más cosas interesantes como sacar las ideas principales de tu PDF gracias a la IA, traducir texto, responderte a preguntas sobre el PDF, etc..\n\nSi tienes alguna sugerencia para actualizaciones futuras, por favor, contáctame por Telegram a @manuelgutierrezc14.\n\n😊')

async def text_to_mp3_command(update: Update, context: CallbackContext):
    await update.message.reply_text('Por favor, proporciona el texto que quieres convertir a audio en el siguiente mensaje.')
    return TEXT_TO_AUDIO

async def convert_text_to_audio(update: Update, context: CallbackContext):
    message = update.message.text

    # Convertir el texto a voz
    tts = gTTS(message, lang='es', tld='es')
    audio_path = 'text_to_audio.mp3'
    tts.save(audio_path)

    # Enviar el archivo de audio al usuario
    await update.message.reply_audio(audio=open(audio_path, 'rb'))

    # Eliminar el archivo de audio después de procesarlo
    os.remove(audio_path)
    return ConversationHandler.END

def handle_responses(text: str) -> str:
    return 'De momento solo puedo convertir archivos PDF a audio. \n\n Adjunta en el siguiente mensaje tu archivo PDF y te responderé con un archivo de audio con el contenido del PDF en los siguientes minutos (mientras más grande sea el PDF, más tiempo tardaré en procesarlo)📚🔊. \n\n Si tienes algún problema, duda o sugerencia, por favor, contáctame por Telegram a @manuelgutierrezc14.'

async def message_handler(update: Update, context: CallbackContext):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'Usuario: ({update.message.chat.id}) in {message_type}: {text}')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_responses(new_text)
        else:
             return

    else:
        response: str = handle_responses(text)

    print(f'Bot: {response}')
    await update.message.reply_text(response)

async def pdf_handler(update: Update, context: CallbackContext):
    document: Document = update.message.document
    if document.mime_type == 'application/pdf':
        file = await context.bot.get_file(document.file_id)
        file_path = f'downloads/{document.file_name}'

        # Asegúrate de que el directorio de descargas existe
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        await file.download_to_drive(file_path)
        text = extract_text_from_pdf(file_path)

        # Convertir el texto a voz
        tts = gTTS(text, lang='es')
        audio_path = f'{file_path}.mp3'
        tts.save(audio_path)

        # Enviar el archivo de audio al usuario
        await update.message.reply_audio(audio=open(audio_path, 'rb'))

        # Eliminar el archivo descargado y el archivo de audio después de procesarlo
        os.remove(file_path)
        os.remove(audio_path)
    else:
        await update.message.reply_text('Por favor, adjunta un archivo PDF.')

def extract_text_from_pdf(file_path: str) -> str:
    doc = fitz.open(file_path)
    text = ''
    for page in doc:
        text += page.get_text()
    return text

async def error_handler(update: Update, context: CallbackContext):
    print(f'Update: {update} caused error: {context.error}')

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    # Conversation handler for text to audio conversion
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('texttoaudio', text_to_mp3_command)],
        states={
            TEXT_TO_AUDIO: [MessageHandler(filters.TEXT & ~filters.COMMAND, convert_text_to_audio)]
        },
        fallbacks=[],
    )
    app.add_handler(conv_handler)

    # Messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    app.add_handler(MessageHandler(filters.Document.PDF, pdf_handler))

    # Errors
    app.add_error_handler(error_handler)

    # polls the bot
    app.run_polling(poll_interval=3)
