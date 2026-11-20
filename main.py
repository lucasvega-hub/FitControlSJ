
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
import responses

# Token del bot
API_KEY = "9035539051:AAEjZd3MU-0CmmiK-MRi-V0MGGKHXKjOhvg"

# Configuración de registros
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logging.info("Iniciando FitControl Bot...")


# Comando de inicio
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "¡Hola! Soy FitControl Bot 🤖\n\n"
        "Tu asistente de hábitos saludables.\n"
        "Puedo ayudarte con:\n"
        "Alimentación\n"
        "Actividad física\n"
        "Seguimiento del peso\n"
        "Objetivos\n"
        "Progreso\n\n"
        "¿En qué puedo ayudarte?"
    )


# Comando de ayuda
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Puedo responder consultas sobre:\n"
        "- Comidas y alimentación\n"
        "- Ejercicio y actividad física\n"
        "- Peso actual\n"
        "- Objetivos personales\n"
        "- Progreso en FitControl\n\n"
        "¡Escribime tu consulta!"
    )


# Comando personalizado
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "¡Bienvenido a FitControl! "
        "Registrá tus hábitos y trabajá en tus objetivos."
    )


# Procesar mensajes
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    logging.info(f'Usuario ({update.effective_chat.id}): {text}')

    response = responses.get_response(text)

    await update.message.reply_text(response)


# Manejo de errores
async def error(update: object, context: ContextTypes.DEFAULT_TYPE):
    logging.error(f'Error: {context.error}')


# Ejecutar bot
if __name__ == '__main__':
    application = ApplicationBuilder().token(API_KEY).build()

    # Comandos
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("custom", custom_command))

    # Mensajes de texto
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    # Errores
    application.add_error_handler(error)

    logging.info("FitControl Bot está funcionando...")

    application.run_polling()
