from random import randint
import telebot 
from telebot import types
from khayyam import JalaliDate
from datetime import date
import gtts
from io import BytesIO
import qrcode

bot = telebot.TeleBot("6697657651:AAG8QRxXib_gQWnqEHuv4BF0q4t30cmNySI", parse_mode=None)
@bot.message_handler(commands=['start'])
def send_welcome(message):
	username = message.from_user.username
	bot.reply_to(message, f"سلام {username}، به ربات من خوش اومدی! 👾")
# random ____________________________________________________________________________________________
key_markup=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
key_markup.add("new game")# commands start
@bot.message_handler(commands=['game'])
def game(message):
    global computer_number
    global num_of_guesses
    computer_number = randint(0, 20)
    num_of_guesses = 0
    bot.send_message(message.chat.id, "Welcome! Can you guess a number between 0 and 20? You have 5 chances.")
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    global num_of_guesses
    user_number = int(message.text)
    num_of_guesses += 1
    if num_of_guesses >= 5:
        bot.reply_to(message, "☠️ Your chance is over! The number was {}.".format(computer_number),reply_markup=key_markup)
    else:
        if user_number == computer_number:
            bot.reply_to(message, "🎉 you won. The number was {}.".format(computer_number))
        elif user_number < computer_number:
            bot.reply_to(message, "🔼 Go higher! Opportunity {}".format(num_of_guesses))
        else:
            bot.reply_to(message, "🔽 Go lower! Opportunity {} ".format(num_of_guesses))
@bot.message_handler()
def keyboard(message):
    if message.text=="new game":
        game()
# age _____________________________________________________________________________________
@bot.message_handler(commands=['age'])
def jalali_date(message):
    msg=bot.send_message(message.chat.id,"لطفا سال تولد خود را وارد کنید")
    bot.register_next_step_handler(msg,year)
def year(message):
    global user_year
    user_year=message.text
    msg=bot.send_message(message.chat.id,"لطفا ماه تولد خود را وارد کنید")
    bot.register_next_step_handler(msg,month)
def month(message):
    global user_month
    user_month=message.text
    msg=bot.send_message(message.chat.id,"لطفا روز تولد خود را وارد کنید")
    bot.register_next_step_handler(msg,day)    
def day(message):
    user_day=message.text
    birthday = JalaliDate(user_year, user_month, user_day)
    today = JalaliDate(date.today())
    # محاسبه سن
    global age 
    age= today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    bot.send_message(message.chat.id,f"سن شما {age} سال است.") 
# max ______________________________________________________________________________________________
@bot.message_handler(commands=['max'])
def find_max(message):
    msg = bot.send_message(message.chat.id, "لطفا اعداد مورد نظر را با کاما جدا کنید (برای مثال: 3,7,12):")
    bot.register_next_step_handler(msg, process_numbers)
def process_numbers(message):
    numbers_list = [int(num.strip()) for num in message.text.split(',')]
    max_num = numbers_list[0]
    for i in range(1, len(numbers_list)):
          if numbers_list[i] > max_num:
                max_num = numbers_list[i]
                print(max_num)
    bot.send_message(message.chat.id, f"بزرگترین عدد: {max_num}")
# argmax ______________________________________________________________________________________________
@bot.message_handler(commands=['argmax'])
def find_index(message):
    msg = bot.send_message(message.chat.id, "لطفا اعداد مورد نظر را با کاما جدا کنید (برای مثال: 3,7,12):")
    bot.register_next_step_handler(msg, process_index)
def process_index(message):
    numbers_list = [int(num.strip()) for num in message.text.split(',')]
    max_num = numbers_list[0]
    for i in range(1, len(numbers_list)):
          if numbers_list[i] > max_num:
                max_num = numbers_list[i]
                print(max_num)
    max_index = numbers_list.index(max_num)	
    bot.send_message(message.chat.id, f"بزرگترین عدد: {max_num} و ایندکس عدد: {max_index}")
# voice ______________________________________________________________________________________________
@bot.message_handler(commands=['voice'])
def voice(message):
    msg=bot.send_message(message.chat.id, "لطفا متن خود را برای تبدیل به ویس بنویسید.")
    bot.register_next_step_handler(msg, voice_convert)
def voice_convert(message):
    my_text = message.text
    tts = gtts.gTTS(text=my_text, lang='en')
    voice_buffer = BytesIO()
    tts.write_to_fp(voice_buffer)
    voice_buffer.seek(0)
    bot.send_voice(message.chat.id, voice_buffer)
# qrcode _____________________________________________________________________________________________
@bot.message_handler(commands=['qrcode'])
def qrcode_generate(message):
    msg = bot.send_message(message.chat.id, "لطفا متن یا لینک خود را برای تولید کد QR وارد کنید.")
    bot.register_next_step_handler(msg, generate_qrcode)
def generate_qrcode(message):
    # دریافت داده ورودی از پیام کاربر
    data = message.text
    # ایجاد یک شیء QRCode  تعیین نسخه، تصحیح خطا، اندازه جعبه و حاشیه
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    # تولید تصویر کد QR با تعیین رنگ پر و رنگ پس زمینه
    img = qr.make_image(fill_color="black", back_color="white")
    # ایجاد یک بوفر BytesIO برای ذخیره تصویر
    img_buffer = BytesIO()
    img.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    # ارسال تصویر کد QR به کاربر از طریق ربات تلگرام
    bot.send_photo(message.chat.id, photo=img_buffer) 
# qrcode _____________________________________________________________________________________________
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "/start خوش آمد گویی\n/game حدس عدد\n/age تشخیص سن با تاریخ شمسی\n/max عدد بزرگتر\n/argmax ایندکس عدد\nvoice تبدیل متن به ویس\nqrcode تبدیل متن به بارکد\n/help راهنما")
bot.infinity_polling()