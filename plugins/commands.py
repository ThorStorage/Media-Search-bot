import os
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import START_MSG, CHANNELS, ADMINS
from utils import Media

logger = logging.getLogger(__name__)


@Client.on_message(filters.command('start'))
async def start(bot, message):
    """Start command handler"""
    buttons = [[
        InlineKeyboardButton('🔍 𝑺𝒆𝒂𝒓𝒄𝒉 𝑴𝒆𝒅𝒊𝒂', switch_inline_query_current_chat=''),
        InlineKeyboardButton('💡 𝑪𝒉𝒂𝒏𝒏𝒆𝒍', url='https://t.me/HindiMoviesDL')],
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(START_MSG, reply_markup=reply_markup)


@Client.on_message(filters.command('channel') & filters.user(ADMINS))
async def channel_info(bot, message):
    """Send basic information of channel"""
    if isinstance(CHANNELS, (int, str)):
        channels = [CHANNELS]
    elif isinstance(CHANNELS, list):
        channels = CHANNELS
    else:
        raise ValueError("Unexpected type of CHANNELS")

    for channel in channels:
        channel_info = await bot.get_chat(channel)
        string = str(channel_info)
        if len(string) > 4096:
            filename = (channel_info.title or channel_info.first_name) + ".txt"
            with open(filename, 'w') as f:
                f.write(string)
            await message.reply_document(filename)
            os.remove(filename)
        else:
            await message.reply(str(channel_info))


@Client.on_message(filters.command('total') & filters.user(ADMINS))
async def total(bot, message):
    """Show total files in database"""
    msg = await message.reply("Processing...⏳", quote=True)
    try:
        total = await Media.count_documents()
        await msg.edit(f'📁 𝐓𝐨𝐭𝐚𝐥 𝐅𝐢𝐥𝐞𝐬 𝐢𝐧 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞: {total}')
    except Exception as e:
        logger.exception('Failed to check total files')
        await msg.edit(f'Error: {e}')


@Client.on_message(filters.command('logger') & filters.user(ADMINS))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))


@Client.on_message(filters.command('delete') & filters.user(ADMINS))
async def delete(bot, message):
    """Delete file from database"""
    reply = message.reply_to_message
    if reply and reply.media:
        msg = await message.reply("Processing...⏳", quote=True)
    else:
        await message.reply('Reply to file with /delete which you want to delete', quote=True)
        return

    for file_type in ("document", "video", "audio"):
        media = getattr(reply, file_type, None)
        if media is not None:
            break
    else:
        await msg.edit('This is not supported file format')
        return

    result = await Media.collection.delete_one({
        'file_name': media.file_name,
        'file_size': media.file_size,
        'mime_type': media.mime_type,
        'caption': reply.caption
    })
    if result.deleted_count:
        await msg.edit('𝐹𝑖𝑙𝑒 𝑖𝑠 𝑠𝑢𝑐𝑐𝑒𝑠𝑠𝑓𝑢𝑙𝑙𝑦 𝑑𝑒𝑙𝑒𝑡𝑒𝑑 𝑓𝑟𝑜𝑚 𝑑𝑎𝑡𝑎𝑏𝑎𝑠𝑒 🙂')
    else:
        await msg.edit('File not found in database')
