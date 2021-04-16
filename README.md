
----

<div align="center">
  <img src="https://github.com/AkinYoungSoftware/TgEglenceBot/raw/master/logo.png" width="300" height="300">
  <h1>Telegram Doğruluk mu? Cesaret mi? Oyun Botu</h1>
</div>
<p align="center">
        <a href="https://telegram.dog/TgEglence_Bot">~Bot~</a>
</p>

----

# Bot Hakkında
**Pyrogram Bot Api Kullanılarak yazılmış basit telegram doğruluk mu? cesaret mi? oyun botu!**

# Heroku'da Clonlamak

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/AkinYoungSoftware/TgEglenceBot)

## Alanları Doldurma
* ``BOT_TOKEN``: Botunuzun tokeni t.me/botfather alınız!
* ``OWNER_API_ID``: Sizin api id'niz http://my.telegram.org/ alınız!
* ``OWNER_API_HASH``: Sizin api hash'ınız http://my.telegram.org/ alınız!


# Örnek Start Komutu
```python
from pyrogram import Client, filters

K_G = Client(
    "Pyrogram Bot",
    bot_token=YOUR_BOT_TOKEN,
    api_id=YOUR_API_ID,
    api_hash=YOUR_API_HASH
    )

@K_G.on_message(filters.command("start"))
async def _(client, message):
    await message.reply_text(text="Merhaba")
```

# İletişim
Şikayet, bağış v.b. için benim ile telegram'dan iletişime geç [@YoungSoftware](https://t.me/YoungSoftware)


# Credit
Thanks for;

[Akın](https://github.com/AkinYoungSoftware)

[Dan](https://telegram.dog/haskell) [Pyrogram Library](https://github.com/pyrogram/pyrogram) Kütüphanesi için
