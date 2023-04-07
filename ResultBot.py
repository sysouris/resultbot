from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, InputMediaPhoto
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
TOKEN = f"6009163802:AAHxItimxRZmeJCfi9VbO3IoTkvlKFoWWGc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:   
    keyboard = [
        [InlineKeyboardButton("IIM-B Final Result Status", callback_data=getResultDeclaredStatus(link, holyword))],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    img = open('Statpic.png', 'rb')
    stxt = "Click below to get the status"
    chatID = update.effective_chat.id
    await context.bot.send_photo(chat_id=chatID,photo=img, caption=stxt, reply_markup=reply_markup)

    return COUNTER

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    try:
        query = update.callback_query
        await query.answer()
        now = datetime.now()
        strnow = now.strftime(f"%B %d, %H:%M")
        bimg = open('Statpic.png', 'rb')
        btext = f"{query.data}"+" as of "+ strnow
        await query.edit_message_media(media=InputMediaPhoto(media=bimg))
        await query.edit_message_caption(caption = btext)
        time.sleep(120)
    except:
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=1862428631&text={ErrorMessage1}")
        await query.edit_message_caption(caption="Please start again: type /start")
        return ConversationHandler.END

    try:
        keyboard = [
            [InlineKeyboardButton("IIM-B Final Result Status", callback_data=getResultDeclaredStatus(link, holyword))],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        beimg = open('Statpic.png', 'rb')
        btxt = f"{query.data}"+" as of "+ strnow
        await query.edit_message_media(media=InputMediaPhoto(media=beimg))
        await query.edit_message_caption(caption=btxt, reply_markup = reply_markup)
            
    except:
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=1862428631&text={ErrorMessage2}")
        await query.edit_message_caption(caption="Please start again: type /start")
        return ConversationHandler.END
    
    return COUNTER

app = Application.builder().token(TOKEN).build()
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
