from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

reply_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="1 - Ryad. Tugma 1"
        ),
        KeyboardButton(
            text="1 - Ryad. Tugma 2"
        ),
        KeyboardButton(
            text="1 - Ryad. Tugma 3"
        )
    ],
    [
        KeyboardButton(
            text="2 - Ryad. Tugma 1"
        ),
        KeyboardButton(
            text="2 - Ryad. Tugma 2"
        ),
        KeyboardButton(
            text="2 - Ryad. Tugma 3"
        ),
        KeyboardButton(
            text="2 - Ryad. Tugma 4"
        )
    ],
    [
        KeyboardButton(
            text="3 - Ryad. Tugma 1"
        ),
        KeyboardButton(
            text="3 - Ryad. Tugma 2"
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Tugmani tanlang ⬇️", selective=True)

loc_tel_poll_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Manzilingni yubor",
            request_location=True
        )
    ],
    [
        KeyboardButton(
            text="Nomeringni yubor",
            request_contact=True
        )
    ],
    [
        KeyboardButton(
            text="O'yin taxla",
            request_poll=KeyboardButtonPollType()
        )
    ]
], resize_keyboard=True, one_time_keyboard=False,
    input_field_placeholder="Manzil , Telefon Nomer yoki O'yin taxla/tadqiqot ⬇️")



























