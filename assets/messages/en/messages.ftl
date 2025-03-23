messages-start = 👋 Hi, { $name }! Welcome to Crypto Trading Bot!

    🚀 Currently, this bot is still under development, and some features are not yet available:
    - Take Profit / Stop Loss (TP/SL)
    - Limit Orders
    - Copy Trading

    📌 Why? Due to time constraints, these features are not yet implemented. Stay tuned for updates!

messages-wallet-setup = 👛 <b>Welcome to the Wallet Setup!</b>

    To get started, you need to set up your wallet. You have two options:

    1️⃣ Create a new wallet
    • Generates a new wallet with a unique seed phrase
    • You'll need to securely store the recovery phrase
    • Perfect for new users

    2️⃣ Import an existing wallet
    • Use your existing wallet by entering the seed phrase
    • Make sure you have your 24-word recovery phrase ready
    • For users who already have a wallet

    Please choose an option below:

messages-wallet-created = ✅ <b>Your new wallet has been created!</b>

    <b>Wallet Address:</b>
    <code>{ $address }</code>

    <b>Recovery Phrase:</b>
    <code>{ $mnemonic }</code>

    ⚠️ <b>IMPORTANT:</b>
    • Save your recovery phrase in a secure place
    • Never share it with anyone
    • You'll need it to recover your wallet

messages-wallet-import_ask = 🔐 Please enter your 24-word recovery phrase:

    • Enter all 24 words separated by spaces
    • Words should be in English
    • Double-check for typos

messages-wallet-import_success = ✅ <b>Wallet successfully imported!</b>

    <b>Wallet Address:</b>
    <code>{ $address }</code>

messages-wallet-import_error = ❌ <b>Error importing wallet</b>

    The recovery phrase you entered is invalid. Please make sure:
    • You entered all 24 words
    • Words are spelled correctly
    • Words are in English
    • Words are separated by spaces

    Try again or press 'Cancel' to go back.

messages-wallet-unlink_confirm = ⚠️ <b>Are you sure you want to unlink your wallet?</b>

    This action will:
    • Remove your wallet from the bot
    • You'll need to create or import a wallet again to use wallet features
    • Your funds will remain safe in your wallet
    • You can always import the same wallet back using your recovery phrase

messages-wallet-unlinked = ✅ <b>Wallet successfully unlinked!</b>

    You can now:
    • Create a new wallet
    • Import an existing wallet

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

messages-deposit-info = 📥 To deposit funds to your wallet, send TON or any other assets to this address:

    <code>{ $address }</code>

    ⚠️ Important:
    • Ensure that you send only assets on the TON blockchain
    • Double-check the address before sending
    • The deposit will be credited after network confirmation

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

messages-backup-warning = 🔐 <b>Your Wallet Recovery Phrase:</b>

    <code>{ $mnemonic }</code>

    ⚠️ <b>IMPORTANT SECURITY WARNING:</b>
    • This is your wallet's secret recovery phrase
    • Anyone with these words can access your funds
    • Never share these words with anyone
    • Never enter these words on any website
    • Store them in a safe place offline

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
buttons-backup = 🔐 Backup
buttons-confirm = ✅ Yes, I'm sure
buttons-create_wallet = 🔑 Create New Wallet
buttons-import_wallet = 📝 Import Existing Wallet
buttons-unlink_wallet = 🔓 Unlink Wallet
