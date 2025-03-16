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
messages-ask_symbol = Пожалуйста, введите символ токена (например, NOT) или адрес контракта:
messages-token_info = 🚀 <b>{ $name } ({ $symbol })</b> 🚀
    💰 Цена: ${ $price } 📉 { $price_change }% (24ч)
    📊 TVL: ${ $tvl }
    👥 Владельцев: { $holders }
    ✨ Доверие: { $trust_score }/100
    🔗 Адрес: <code>{ $address }</code>
messages-token_not_found = ❗️ Не удалось найти информацию о токене: { $symbol }
messages-token_error = ❌ Извините, произошла ошибка при получении информации о токене.

messages-deposit-info = 📥 Чтобы пополнить ваш кошелек, отправьте TON или любые другие активы на этот адрес:

    <code>{ $address }</code>

    ⚠️ Важно:
    • Убедитесь, что отправляете только активы в блокчейне TON
    • Перепроверьте адрес перед отправкой
    • Депозит будет зачислен после подтверждения сети

messages-buy-ask_address = 🎯 Какой адрес токена вы хотите купить?
messages-buy-ask_amount = 🔢 Отлично! Какое количество этого токена вы хотите приобрести?
messages-buy-confirm = ✅ Просто для подтверждения: вы покупаете <b>{ $amount }</b> токенов по адресу <b>{ $address }</b>. Готовы продолжить?
messages-buy-result = 🎉 Вы успешно купили токен! ✅\n\n📄 Хэш транзакции: <code>{ $tx_hash }</code>

messages-sell-ask_address = 🎯 Какой адрес токена вы хотите продать?
messages-sell-ask_amount = 🔢 Отлично! Какое количество этого токена вы хотите продать?
messages-sell-confirm = ✅ Просто для подтверждения: вы продаёте <b>{ $amount }</b> токенов по адресу <b>{ $address }</b>. Готовы продолжить?
messages-sell-result = 🎉 Вы успешно продали токен! ✅\n\n📄 Хэш транзакции: <code>{ $tx_hash }</code>

messages-withdraw-ask_address = 🎯 Пожалуйста, введите адрес токена, который вы хотите вывести. Введите 'ton' если хотите вывести TON.
messages-withdraw-ask_amount = 🔢 Отлично! Какую сумму вы хотите вывести?
messages-withdraw-ask_destination = 📬 Пожалуйста, введите адрес кошелька, на который вы хотите отправить средства:
messages-withdraw-confirm = ✅ Для подтверждения: вы выводите <b>{ $amount }</b> { $token_type ->
    [ton] TON
    *[other] токенов с адреса <b>{ $address }</b>
} на <b>{ $destination }</b>. Готовы продолжить?
messages-withdraw-result = 🎉 Вывод успешно выполнен! ✅\n\n📄 Хэш транзакции: <code>{ $tx_hash }</code>

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
buttons-confirm = ✅ Да, я уверен