import hashlib
import telegram
from telegram.ext import Updater, CommandHandler

# Initialize blockchain as a list of blocks
blockchain = []

# Define the function to calculate the hash of a block
def calculate_hash(index, previous_hash, data, timestamp):
    block_string = str(index) + previous_hash + data + str(timestamp)
    return hashlib.sha256(block_string.encode()).hexdigest()

# Define the function to create a new block
def create_block(index, previous_hash, data):
    timestamp = time.time()
    hash = calculate_hash(index, previous_hash, data, timestamp)
    block = {
        'index': index,
        'previous_hash': previous_hash,
        'data': data,
        'timestamp': timestamp,
        'hash': hash
    }
    return block

# Define the function to add a block to the blockchain
def add_block(block, blockchain):
    previous_hash = blockchain[-1]['hash']
    if block['previous_hash'] == previous_hash:
        blockchain.append(block)
        return True
    else:
        return False

# Define the /add_data command to add data to the blockchain
def add_data(update, context):
    data = update.message.text.split(" ", 1)[1]
    index = len(blockchain)
    previous_hash = blockchain[-1]['hash']
    block = create_block(index, previous_hash, data)
    if add_block(block, blockchain):
        update.message.reply_text("Block added to the blockchain!")
    else:
        update.message.reply_text("Error adding block to the blockchain.")

# Set up the Telegram bot
updater = Updater(token='YOUR_TELEGRAM_BOT_TOKEN', use_context=True)
dispatcher = updater.dispatcher

# Add the /add_data command handler
add_data_handler = CommandHandler('add_data', add_data)
dispatcher.add_handler(add_data_handler)

# Start the bot
updater.start_polling()
