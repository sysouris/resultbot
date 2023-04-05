from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes, ConversationHandler
from resultmonitor import *
from datetime import datetime

link = 'https://www.iimb.ac.in/pgp-admissions'
holyword1 = 'admission'
holyword = 'pgp 2023 offer'
current_count = 0
COUNTER, = range(1)
ErrorMessage1 = 'Error in 1st stage button press'
ErrorMessage2 = 'Error in 2nd stage button press'
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    keyboard = [
        [InlineKeyboardButton("IIM-B Final Result Status", callback_data=getResultDeclaredStatus(link, holyword))],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Click on the tab", reply_markup=reply_markup)
    return COUNTER

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    try:
        query = update.callback_query
        await query.answer()
        now = datetime.now()
        strnow = now.strftime(f"%B %d, %H:%M")
        await query.edit_message_text(text=f"{query.data}"+" as of "+ strnow)
        time.sleep(120)
    except:
        requests.get("https://api.telegram.org/bot6009163802:AAHxItimxRZmeJCfi9VbO3IoTkvlKFoWWGc/sendMessage?chat_id=1862428631&text={}".format(ErrorMessage1))
        await query.edit_message_text(text="Please start again: type /start")
        return ConversationHandler.END
    try:
        keyboard = [
            [InlineKeyboardButton("IIM-B Final Result Status", callback_data=getResultDeclaredStatus(link, holyword))],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=f"{query.data}"+" as of "+ strnow, reply_markup = reply_markup)
            
    except:
        requests.get("https://api.telegram.org/bot6009163802:AAHxItimxRZmeJCfi9VbO3IoTkvlKFoWWGc/sendMessage?chat_id=1862428631&text={}".format(ErrorMessage2))
        await query.edit_message_text(text="Please start again: type /start")
        return ConversationHandler.END
    
    return COUNTER

app = Application.builder().token("6009163802:AAHxItimxRZmeJCfi9VbO3IoTkvlKFoWWGc").build()
conv_handler = ConversationHandler(
    entry_points = [(CommandHandler("start", start))],
    states = {
        COUNTER: [CallbackQueryHandler(button)]
    },
    fallbacks=[],
    per_user = False
)
app.add_handler(conv_handler)
app.run_polling()
