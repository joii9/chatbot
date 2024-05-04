from typing import Final


from telegram import *
from telegram.ext import *

from requests import *

TOKEN: Final = "6925512151:AAEOIiBflpRfK2FKmugSCRqDvv4httVCEFA"
BOT_USERNAME: Final = "@hello_world_test0_bot"

user=""
evento=""
sat=""
ind=[]


#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bienvenido. Te voy a ayudar a registrar un evento en la bitacora de sistemas.")
    await update.message.reply_text("Primeramente indicame quien eres?")
    #buttons = [[KeyboardButton("Coordinador")], [KeyboardButton("Analista")], [KeyboardButton ("Invitado")]]
    

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Soy un bot")
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Aun no se que personalizar en este comando")


#Handle responses
def handle_responses(text: str) -> str:
    #users=["Jorge, Joel, Invitado"]
    global user,evento
    processed: str= text[0].upper()+text[1:].lower()
    print(text)
    if processed in ["Jorge", "Joel", "Invitado"]:
        user=processed
        return "Hola "+user+" Ahora indicame ¿Cual es el evento?"
    if user in ["Jorge", "Joel", "Invitado"]:
        evento=text
        return "Listo carnal"
    
    if "how are you" in processed:
        return "I am good"

    if "i love python" in processed:
        return "Me too. It is great!"
    
    if "que wey" in processed:
        return "Que hijo de tu pinche madre"
    
    return "No te entiendo, pero tal vez mas adelante lo haga 🖕🏼"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    print(message_type)

    if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_responses(new_text)
        else:
            return
    else:
        response: str = handle_responses(text)
    
    print("Bot: ", response)
    await update.message.reply_text(response)
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")



if __name__ == "__main__":
    print("Starting bot...")
    app= Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    #Mesages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Errors
    app.add_error_handler(error)

    #Polls the bot
    print("Polling...")
    app.run_polling(poll_interval=3)




