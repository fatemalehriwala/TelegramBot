from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler,filters, ContextTypes
TOKEN: Final='token'
bot_username: Final = '@Jspm_college_bot' 
#commands
async def start_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('hello, welcome to JSPM telegram bot')

async def view_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('view')

async def admission_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('admission')

async def fees_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('fees')

#responses will be handled here
def handle_response(text: str) -> str:

    processed: str = text.lower()#handles the upper lower case enter by making everything in lower

    if'hello'in processed:
        return 'hey there!'
    if'how are you' in processed:
        return'I am good!'
    return 'i dont know what it is !'

#this will inform us wheather it is a group chat or private chat
async def handle_message(update:Update, context: ContextTypes.DEFAULT_TYPE):
    message_type:str =update.message.chat.type
    text: str = update.message.text
    
    # shows user id,and shows either it is from groupchat or private
    print(f'User({update.message.chat.id}) in {message_type}:"{text}')

    #for group chats
    if message_type == 'group':
        if bot_username in text:
            new_text: str = text.replace(bot_username,'').strip()
            response: str = handle_response(new_text)
        else:
            return
        #for private chat
    else:
        response: str = handle_response(text)

    print('bot: ',response)
    await update.message.reply_text(response)

#logs error
async def error(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

#joins everything together
if __name__=='__main__':
    print('Starting bot....') #indicates the initiation of program
    app = Application.builder().token(TOKEN).build()
    #Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('view', view_command))
    app.add_handler(CommandHandler('Admission', admission_command))
    app.add_handler(CommandHandler('fees', fees_command))
    #Messages
    app.add_handler(MessageHandler(filters.TEXT,handle_message))
    #Errors
    app.add_error_handler(error)
    #checks every 3 secs for new messages
    print('Polling...') #indicates waits for the user inputs and return values
    app.run_polling(poll_interval=3)
