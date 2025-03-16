messages-start = 👋 Hi, { $name }! Welcome to Crypto Trading Bot!

    🚀 Currently, this bot is still under development, and some features are not yet available:
    - Take Profit / Stop Loss (TP/SL)
    - Limit Orders
    - Copy Trading

    📌 Why? Due to time constraints, these features are not yet implemented. Stay tuned for updates!
messages-soon = 🔜 soon ❗️
messages-wallet_info = 👛 Your Wallet Information:

    <b>Address:</b> <code>{ $address }</code>
    <b>Balance:</b> { $ton_balance } TON
messages-ask_symbol = Please enter a token symbol (e.g., NOT) or contract address:
messages-token_info = 🚀 <b>{ $name } ({ $symbol })</b> 🚀
    💰 Price: ${ $price } 📉 { $price_change }% (24h)
    📊 TVL: ${ $tvl }
    👥 Holders: { $holders }
    ✨ Trust Score: { $trust_score }/100
    🔗 Address: <code>{ $address }</code>
messages-token_not_found = ❗️ Could not find information for token: { $symbol }
messages-token_error = ❌ Sorry, there was an error fetching the token information.

messages-buy-ask_address = 🎯 What's the token address you'd like to buy?
messages-buy-ask_amount = 🔢 Awesome! How much of this token do you want to purchase?
messages-buy-confirm = ✅ Just to confirm, you're buying <b>{ $amount }</b> of the token at <b>{ $address }</b>. Ready to go?
messages-buy-result = 🎉 You've successfully bought the token! ✅\n\n📄 Transaction Hash: <code>{ $tx_hash }</code>

messages-sell-ask_address = 🎯 What's the token address you'd like to sell?
messages-sell-ask_amount = 🔢 Awesome! How much of this token do you want to sell?
messages-sell-confirm = ✅ Just to confirm, you're selling <b>{ $amount }</b> of the token at <b>{ $address }</b>. Ready to go?
messages-sell-result = 🎉 You've successfully sold the token! ✅\n\n📄 Transaction Hash: <code>{ $tx_hash }</code>

messages-withdraw-ask_address = 🎯 Please enter the token address you want to withdraw. Enter 'ton' if you want to withdraw TON.
messages-withdraw-ask_amount = 🔢 Great! How much would you like to withdraw?
messages-withdraw-ask_destination = 📬 Please enter the destination wallet address where you want to send the funds:
messages-withdraw-confirm = ✅ Just to confirm, you're withdrawing <b>{ $amount }</b> { $token_type ->
    [ton] TON
    *[other] tokens from <b>{ $address }</b>
} to <b>{ $destination }</b>. Ready to proceed?
messages-withdraw-result = 🎉 Withdrawal successful! ✅\n\n📄 Transaction Hash: <code>{ $tx_hash }</code>

messages-language = 🌎 Select your preferred language by clicking button below:

extra-language = 🇬🇧 English
extra-selectable = { $selected ->
    [true] [ {$value} ]
    *[other] { $value }
}

buttons-menu = 📚 Menu
buttons-back = 🔙 Back
buttons-cancel = 🚫 Cancel
buttons-language = 🌎 Language
buttons-wallet = 👛 Wallet
buttons-buy = 📈 Buy
buttons-sell = 📉 Sell
buttons-token_info = ℹ️ Token Info
buttons-tp_sl_orders = 🎯 TP/SL Orders
buttons-limit_order = 📊 Limit Orders
buttons-copy_trade = 🔄 Copy Trade
buttons-deposite = 📥 Deposite
buttons-withdraw = 📤 Withdraw
buttons-confirm = ✅ Yes, I'm sure