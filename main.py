from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Your bot token
token = "BOT_TOKEN"

# Calculation function     
def calculate_position(...):
   ...

def start(update, context):
    keyboard = [
       [
           InlineKeyboardButton("Calculate", callback_data="calculate")
       ]    
    ]
    
    update.message.reply_text("Hi! I can help calculate your position size.", 
                              reply_markup=InlineKeyboardMarkup(keyboard))

def button_clicked(update, context):      
    query = update.callback_query   
    update.message.reply_text("Please send me the following:\n"
                              "- Contact size\n"
                              "- Entry price\n"                  
                              "- Stop loss price\n"
                              "- Risk %", 
                              reply_markup=ReplyKeyboardRemove())

def get_inputs(update, context):
    contact_size = update.message.text      
    ... 
    # Get the 3 other inputs               
    position_size = calculate_position(contact_size, ...)
    
    update.message.reply_text(f"Your position size is {position_size}")
    
    # Show keyboard again      
    update.message.reply_text("Hi! I can help calculate...",  
                              reply_markup=keyboard)

def main():
    ...
    
    dp.add_handler(CallbackQueryHandler(button_clicked, pattern='calculate'))
    
    dp.add_handler(MessageHandler(Filters.text, get_inputs))

if __name__ == '__main__':
    main()
