# Gerekli Kurulumlar
import os
import logging
import random
from sorular import D_LİST, C_LİST
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# ============================ #

# stats komutumuz icin kullanicilarin idlerinin depolanacagi liste
USERS=[]
# stats komutumuz icin chat idlerinin depolanacagi liste
CHATS=[]


B_TOKEN = os.getenv("BOT_TOKEN") # Kullanıcı'nın Bot Tokeni
API_ID = os.getenv("OWNER_API_ID") # Kullanıcı'nın Apı Id'si
API_HASH = os.getenv("OWNER_API_HASH") # Kullanıcı'nın Apı Hash'ı

# Log Kaydı Alalım
logging.basicConfig(level=logging.INFO)

# Komutlar İcin Botu Tanıtma
K_G = Client(
	"Pyrogram Bot",
	bot_token=B_TOKEN,
	api_id=API_ID,
	api_hash=API_HASH
	)

# Start Buttonu İcin Def Oluşturalım :)
def button():
	BUTTON=[[InlineKeyboardButton(text="👨🏻‍💻 Sahibim ",url="t.me/YoungSoftware")]]
	BUTTON+=[[InlineKeyboardButton(text="🌱 Open Source 🌱",url="https://github.com/AkinYoungSoftware/TgEglenceBot")]]
	return InlineKeyboardMarkup(BUTTON)

# Kullanıcı Start Komutunu Kullanınca Selam'layalım :)
@K_G.on_message(filters.command("start"))
async def _(client, message):
	user = message.from_user # Kullanıcın Kimliğini Alalım

	await message.reply_text(text="**Merhaba {}!**\n\n__Ben Pyrogram Api İle Yazılmış Eğlence Botuyum :)__\n\n**Repom =>** [Open Source](https://github.com/AkinYoungSoftware/TgEglenceBot)\nDoğruluk mu? Cesaret mi? Oyun Komutu => /dc".format(
		user.mention, # Kullanıcı'nın Adı
		),
	disable_web_page_preview=True, # Etiketin Önizlemesi Olmaması İcin Kullanıyoruz
	reply_markup=button() # Buttonlarımızı Ekleyelim
	)
	kullanici_stats(chat_id=message.chat.id, user_id=user.id)

# Dc Komutu İcin Olan Buttonlar
def d_or_c(user_id):
	BUTTON = [[InlineKeyboardButton(text="✅ Doğruluk", callback_data = " ".join(["d_data",str(user_id)]))]]
	BUTTON += [[InlineKeyboardButton(text="💪 Cesaret", callback_data = " ".join(["c_data",str(user_id)]))]]
	return InlineKeyboardMarkup(BUTTON)

# Dc Komutunu Oluşturalım
@K_G.on_message(filters.command("dc"))
async def _(client, message):
	user = message.from_user

	await message.reply_text(text="{} İstediğin Soru Tipini Seç!".format(user.mention),
		reply_markup=d_or_c(user.id)
		)
	kullanici_stats(chat_id=message.chat.id, user_id=user.id)

# Buttonlarımızı Yetkilendirelim
@K_G.on_callback_query()
async def _(client, callback_query):
	d_soru=random.choice(D_LİST) # Random Bir Doğruluk Sorusu Seçelim
	c_soru=random.choice(C_LİST) # Random Bir Cesaret Sorusu Seçelim
	user = callback_query.from_user # Kullanıcın Kimliğini Alalım

	c_q_d, user_id = callback_query.data.split() # Buttonlarımızın Komutlarını Alalım

	# Sorunun Sorulmasını İsteyen Kişinin Komutu Kullanan Kullanıcı Olup Olmadığını Kontrol Edelim
	if str(user.id) == str(user_id):
		# Kullanıcının Doğruluk Sorusu İstemiş İse Bu Kısım Calışır
		if c_q_d == "d_data":
			await callback_query.answer(text="Doğruluk Sorusu İstediniz", show_alert=False) # İlk Ekranda Uyarı Olarak Gösterelim
			await client.delete_messages(
				chat_id=callback_query.message.chat.id,
				message_ids=callback_query.message.message_id) # Eski Mesajı Silelim

			await callback_query.message.reply_text("**{user} Doğruluk Sorusu İstedi:** __{d_soru}__".format(user=user.mention, d_soru=d_soru)) # Sonra Kullanıcıyı Etiketleyerek Sorusunu Gönderelim
			return

		if c_q_d == "c_data":
			await callback_query.answer(text="Cesaret Sorusu İstediniz", show_alert=False)
			await client.delete_messages(
				chat_id=callback_query.message.chat.id,
				message_ids=callback_query.message.message_id)
			await callback_query.message.reply_text("**{user} Cesaret Sorusu İstedi:** __{c_soru}__".format(user=user.mention, c_soru=c_soru))
			return


	# Buttonumuza Tıklayan Kisi Komut Calıştıran Kişi Değil İse Uyarı Gösterelim
	else:
		await callback_query.answer(text="Komutu Kullanan Kişi Sen Değilsin!!", show_alert=False)
		return

# kullanicinin idsi nin listede olup olmadigini kontrol edip ekliyelim
def kullanici_stats(chat_id, user_id):
    if user_id not in USERS and user_id != None:
        USERS.append(user_id)
    
    if chat_id not in CHATS and chat_id != None and user_id != chat_id:
        CHATS.append(chat_id)


@K_G.on_message(filters.command("stats"))
async def _(client, message):
    if message.from_user.id != 818300528:
        return
    
    await message.reply_text(f"Chat Sayisi: {len(CHATS)}\nUser Sayisi: {len(USERS)}")

K_G.run() # Botumuzu Calıştıralım :)
