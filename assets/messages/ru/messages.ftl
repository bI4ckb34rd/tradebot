messages-start = 👋 Привет, { $name }! Добро пожаловать в Crypto Trading Bot!

    🚀 В данный момент этот бот всё ещё находится в разработке, и некоторые функции пока недоступны:
    - Take Profit / Stop Loss (TP/SL)
    - Лимитные ордера
    - Копирование торговли

    📌 Почему? Из-за нехватки времени эти функции ещё не реализованы. Следите за обновлениями!
messages-soon = скоро ❗️
messages-wallet_info = 👛 Информация о вашем кошельке:

    <b>Адрес:</b> <code>{ $address }</code>
    <b>Баланс:</b> { $ton_balance } TON
messages-language = 🌎 Выберите язык, нажав на кнопку ниже:
extra-language = 🇷🇺 Русский
extra-selectable = { $selected ->
    [true] [ {$value} ]
    *[other] { $value }
}

buttons-menu = 📚 Меню
buttons-back = 🔙 Назад
buttons-cancel = 🚫 Отмена
buttons-language = 🌎 Язык
buttons-wallet = 👛 Кошелек
buttons-buy = 📈 Купить
buttons-sell = 📉 Продать
buttons-token_info = ℹ️ Информация о токене
buttons-tp_sl_orders = 🎯 Ордера TP/SL
buttons-limit_order = 📊 Лимитные ордера
buttons-copy_trade = 🔄 Копировать торговлю
buttons-deposite = 📥 Пополнить
buttons-withdraw = 📤 Вывести