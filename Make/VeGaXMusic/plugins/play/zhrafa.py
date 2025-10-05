import random
import re
from pyrogram import filters, Client
from pyrogram.types import Message
from VeGaXMusic import app

@app.on_message(filters.command(["زخرفه", "زخرفة"], ""), group=838)
async def zahrafa_handler(client: Client, message: Message):
    ask = await app.ask(
        message.chat.id,
        "📝 **أرسل لي النص الذي تريد زخرفته (عربي/إنجليزي):**",
        reply_to_message_id=message.id,
        timeout=300
    )    
    text = ask.text
    if len(text) > 200:
        await message.reply_text("⚠️ **عذرًا! لا يمكن زخرفة أكثر من 200 حرف.**")
        return
    if "\n" in text:
        await message.reply_text("⚠️ **عذرًا! لا يمكن زخرفة نصوص متعددة الأسطر.**")
        return
    DECORATIONS = [
        ' ✧ ', ' ✦ ', ' ❀ ', ' ❁ ', ' ✿ ', ' ❃ ', ' ❊ ', ' ❄ ', 
        ' ⚘ ', ' ♕ ', ' ♛ ', ' ✪ ', ' ✵ ', ' ✺ ', ' ❖ ', ' ✼ ',
        ' ✨ ', ' ⭐ ', ' 🌟 ', ' 💫 ', ' 🌠 ', ' 🎀 ', ' 🎇 ', ' 🎆 '
    ]
    ARABIC_STYLES = [
        lambda t: re.sub('[ضصثقفغعهخحجشسيبلاتنمكطئؤرلاىةوزظ]', lambda x: x.group() + 'ـٌـ', t),
        lambda t: re.sub('[ضصثقفغعهخحجشسيبلاتنمكطئؤرلاىةوزظ]', lambda x: x.group() + 'ِٰـِۢ', t),
        lambda t: re.sub('[ضصثقفغعهخحجشسيبلاتنمكطئؤرلاىةوزظ]', lambda x: x.group() + 'ۜہٰٰ', t),
        lambda t: re.sub('[ضصثقفغعهخحجشسيبلاتنمكطئؤرلاىةوزظ]', lambda x: x.group() + 'ـ❤ـ', t),
        lambda t: re.sub('[ضصثقفغعهخحجشسيبلاتنمكطئؤرلاىةوزظ]', lambda x: x.group() + 'ـ✧ـ', t),
        lambda t: re.sub('[ضصثقفغعهخحجشسيبلاتنمكطئؤرلاىةوزظ]', lambda x: x.group() + 'ـ☁ـ', t),
        lambda t: re.sub('[ضصثقفغعهخحجشسيبلاتنمكطئؤرلاىةوزظ]', lambda x: x.group() + 'ـ🔥ـ', t),
        lambda t: re.sub('[ضصثقفغعهخحجشسيبلاتنمكطئؤرلاىةوزظ]', lambda x: x.group() + 'ـ💧ـ', t)
    ]
    ENGLISH_STYLES = [
        lambda t: ''.join([chr(ord(c) + 119743) if c.isalpha() else c for c in t]),
        lambda t: ''.join([chr(ord(c) + 119795) if c.isalpha() else c for c in t]),
        lambda t: ''.join([chr(ord(c) + 119835) if c.isalpha() else c for c in t]),
        lambda t: ''.join([chr(ord(c.upper()) + 127135) if c.isalpha() else c for c in t]),
        lambda t: ''.join([chr(ord(c.upper()) + 127280) if c.isalpha() else c for c in t]),
        lambda t: ''.join([f'🌈{c}🌈' for c in t]),
        lambda t: ''.join([chr(ord(c) + 120094) if c.isalpha() else c for c in t]),
        lambda t: ''.join([chr(ord(c) + 120146) if c.isalpha() else c for c in t])
    ]
    decorated_texts = []
    for i in range(8):
        arabic_text = ARABIC_STYLES[i](text) if any(char in 'ضصثقفغعهخحجشسيبلاتنمكطئؤرلاىةوزظ' for char in text) else text
        english_text = ENGLISH_STYLES[i](text) if any(char.isalpha() and char not in 'ضصثقفغعهخحجشسيبلاتنمكطئؤرلاىةوزظ' for char in text) else text
        final_text = arabic_text if arabic_text != text else english_text
        decorated_texts.append(f"{i+1}. {final_text} {random.choice(DECORATIONS)}")
    result_message = "🎨 **إليك نصوصك المزخرفة:**\n\n" + "\n\n".join(decorated_texts)
    result_message += "\n\n🔸 **اضغط على أي نص لنسخه**"    
    await message.reply_text(result_message)