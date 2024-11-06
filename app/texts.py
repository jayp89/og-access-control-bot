from aiogram.utils.markdown import hide_link

# Add other languages and their corresponding codes as needed.
SUPPORTED_LANGUAGES = {
    "ru": "🇪🇹 Amharic",
    "en": "🇬🇧 English",
}

TEXT_BUTTONS = {
    "ru": {
        "add": "﹢ አክል",
        "back": "‹ ወደ ኋላ",
        "main": "≡ ዋና",
        "retry": "↻ እንደገና ሞክር",
        "delete": "× ሰርዝ",
        "confirm": "✓ አረጋግጥ",
        "connect_wallet": "{wallet_name} አገናኝ",
        "open_wallet": "{wallet_name} ክፈት",
        "disconnect_wallet": "× አቋርጥ",
        "change_language": "↻ ቋንቋ ቀይር",
        "get_access": "🔍 መዳረሻ አረጋግጥ",
        "newsletter": "📰 የዜና መልእክት",
        "admins_menu": "👥 አስተዳዳሪዎች",
        "chats_menu": "💬 ውይይቶች",
        "tokens_menu": "💎 ቶከኖች",
        "edit_min_amount": "✎ የዝቅተኛውን መጠን ቀይር"
    },
    "en": {
        "add": "﹢ Add",
        "back": "‹ Back",
        "main": "≡ Main",
        "retry": "↻ Retry",
        "delete": "× Delete",
        "confirm": "✓ Confirm",

        "connect_wallet": "Connect {wallet_name}",
        "open_wallet": "Go to {wallet_name}",
        "disconnect_wallet": "× Disconnect",

        "change_language": "↻ Change Language",
        "get_access": "🔍 Check access availability",

        "newsletter": "📰 Newsletter",
        "admins_menu": "👥 Admins",
        "chats_menu": "💬 Chats",
        "tokens_menu": "💎 Tokens",
        "edit_min_amount": "✎ Edit minimum amount",
    }
}

TEXT_MESSAGES = {
    "ru": {
        "loader_text": "⏳",
        "outdated_text": "...",

         "main_menu": (
            f"{hide_link('https://etneco.ethio-tech.com/security/db9c5c3febe75811e41af.jpg')}"
            "🤖 <b>እንኳን ደህና መጡ!</b>\n\n"
            "እኔ የ ETN ደህንነት ነኝ። መቀላቀል እንደምትችል ወይም አለመቻልህን እወስናለሁ። እና የት መቀላቀል እንደምትችል እነግርሃለሁ። "
            "ለመቀላቀል የ ETN ማህደሮች እና NFTs ወይም SBTs ሊኖርህ ይገባል። "
            "በ NFT አይነት ላይ በመመስረት በምክር ቤቱ ውስጥ የምታገኘው የድምጽ መብት ሊለያይ ይችላል።\n\n"
            "<blockquote><b>የግል ውይይቶች:</b>\n{chats}\n"
            "<b>አስፈላጊ ቶከኖች:</b>\n{tokens}</blockquote>\n\n"
            "<b>መዳረሻ አረጋግጥ</b> ላይ ጠቅ ያድርጉ ፣ መዳረሻ እንደሚሰጥዎት ለማወቅ!"
            "<b>የተገናኘ ወደ:</b> {wallet}"
        ),
        "select_language": (
            f"{hide_link('https://etneco.ethio-tech.com/security/aaba319da09f60e6def03.jpg')}"
            "👋 <b>ሰላም!</b>\n\n"
            "ቋንቋ ይምረጡ:"
        ),
        "change_language": (
            f"{hide_link('https://etneco.ethio-tech.com/security/aaba319da09f60e6def03.jpg')}"
            "<b>ቋንቋ ይምረጡ:</b>"
        ),
        "deny_access": (
            f"{hide_link('https://etneco.ethio-tech.com/security/ceec89ba75c903210411c.jpg')}"
            "🚫 <b>መዳረሻ የተከለከለ ነው</b>\n\n"
            "በሚያሳዝን ሁኔታ በኪስ ቦርሳዎ ውስጥ አስፈላጊ ቶከኖች አልተገኙም።\n\n"
            "አትበሳጭ፣ <b>ከታች ያሉትን አዝራሮች ጠቅ በማድረግ ቶከኖችን መግዛት ትችላለህ</b> እና እንደገና ሞክር።"
        ),
        "allow_access": (
            f"{hide_link('https://etneco.ethio-tech.com/security/6b03c59182d959cddeb02.jpg')}"
            "🎉 <b>እንኳን ደስ አላችሁ!</b>\n\n"
            "ወደ የግል ውይይቶቻችን መዳረሻ ተሰጥቶዎታል።\n\n"
            "<b>ከታች ያሉትን አዝራሮች ጠቅ ያድርጉ</b> እና ለመቀላቀል ማመልከቻ ያስገቡ፣ ወዲያውኑ እቀበላለሁ!"
        ),
        "user_kicked": (
            "ተጠቃሚ {user} [{wallet}] ከውይይቱ ተወግዷል!"
        ),

        "connect_wallet": (
            f"<a href='https://ton.org/ru/wallets?locale=ru&filters[wallet_features][slug][$in]=dapp-auth&pagination[limit]=-1'>የኪስ ቦርሳ ጫን</a>\n\n"
            "<b>የእርስዎን {wallet_name} ያገናኙ!</b>\n\n"
            "በሞባይል ኪስ ቦርሳ ይቃኙ:"
        ),
        "connect_wallet_proof_wrong": (
            f"{hide_link('https://telegra.ph//file/a4ddc111ff41692ad5200.jpg')}"
            "<b>ማስጠንቀቂያ</b>\n\n"
            "የኪስ ቦርሳ ፊርማ ውሸት ነው ወይም የግንኙነት ጊዜው አልቋል።"
        ),
        "connect_wallet_timeout": (
            f"{hide_link('https://telegra.ph//file/a4ddc111ff41692ad5200.jpg')}"
            "<b>ማስጠንቀቂያ</b>\n\n"
            "የግንኙነት ጊዜው አልቋል።"
        ),

        "admin_menu": (
            f"{hide_link('https://etneco.ethio-tech.com/security/aaba319da09f60e6def03.jpg')}"
            "<b>የአስተዳዳሪ ፓነል</b>\n\nተግባር ይምረጡ:"
        ),
        "chats_menu": (
            f"{hide_link('https://etneco.ethio-tech.com/security/aaba319da09f60e6def03.jpg')}"
            "<b>የግል ውይይቶች ምናሌ</b>\n\nተግባር ይምረጡ:"
        ),
        "chat_info": (
            f"{hide_link('https://etneco.ethio-tech.com/security/aaba319da09f60e6def03.jpg')}"
            "• <b>የግል ውይይት መረጃ</b>\n\n"
            "• <b>ID:</b>\n"
            "<blockquote>{chat_id}</blockquote>\n"
            "• <b>አይነት:</b>\n"
            "<blockquote>{chat_type}</blockquote>\n"
            "• <b>ስም:</b>\n"
            "<blockquote>{chat_name}</blockquote>\n"
            "• <b>የግብዣ አገናኝ:</b>\n"
            "<blockquote>{chat_invite_link}</blockquote>\n"
            "• <b>የተፈጠረበት ቀን:</b>\n"
            "<blockquote>{chat_created_at}</blockquote>"
        ),
       "token_send_address": "<b>የቶከን አድራሻ ያስገቡ</b>\n\nየ NFT ስብስቦች እና የ Jetton ጌቶች አድራሻዎች ብቻ ይፈቀዳሉ፡",
        "token_send_address_error": "የማይቻል የቶከን አድራሻ፡\n{}",
        "token_send_address_error_already_exist": "በአድራሻ {address} ላይ ቶከን ቀድሞውኑ አለ!",
        "token_send_address_error_not_supported": "ኮንትራት {interfaces} አይደገፍም።\n{supported_interfaces} ብቻ ይደገፋሉ።",
        "token_send_amount": (
            "<b>የቶከን መረጃ</b>:\n\n"
            "• <b>አይነት:</b>\n{token_type}\n"
            "• <b>ስም:</b>\n{token_name}\n\n"
            "<b>ለግል ውይይት መዳረሻ የሚያስፈልገውን የቶከን ዝቅተኛ መጠን ያስገቡ፡</b>"
        ),
        "token_edit_amount": "<b>ለግል ውይይት መዳረሻ የሚያስፈልገውን አዲስ የቶከን መጠን ያስገቡ፡</b>",
        "token_send_amount_error": "የተሳሳተ የቶከን መጠን!",
        "admins_menu": (
            f"{hide_link('https://etneco.ethio-tech.com/security/aaba319da09f60e6def03.jpg')}"
            "<b>የአስተዳዳሪዎች ምናሌ</b>\n\nተግባር ይምረጡ:"
        ),
        "admin_info": (
            f"{hide_link('https://etneco.ethio-tech.com/security/aaba319da09f60e6def03.jpg')}"
            "• <b>የአስተዳዳሪ መረጃ</b>\n\n"
            "• <b>ID:</b>\n"
            "<blockquote>{admin_id}</blockquote>\n"
            "• <b>ስም:</b>\n"
            "<blockquote>{admin_full_name}</blockquote>\n"
            "• <b>የተጠቃሚ ስም:</b>\n"
            "<blockquote>{admin_username}</blockquote>\n"
            "• <b>የተፈጠረበት ቀን:</b>\n"
            "<blockquote>{admin_created_at}</blockquote>"
        ),
        "admin_send_id": "<b>የአስተዳዳሪ ID ያስገቡ:</b>",
        "admin_send_id_error": "የማይቻል ID:\n{}",
        "admin_send_id_error_not_found": "አስተዳዳሪው አልተገኘም። ተጠቃሚው በመጀመሪያ ከቦቱ ጋር ውይይት መጀመር አለበት።",
        "admin_send_id_error_not_member": "የአስተዳዳሪ ID ቁጥር መሆን አለበት።",
        "confirm_item_add": "<b>አረጋግጥ</b> {item} ወደ {table} ማከል?",
        "item_added": "{item} ወደ {table} ተጨምሯል!",
        "confirm_item_delete": "<b>አረጋግጥ</b> {item} ከ {table} መሰረዝ?",
        "item_deleted": "{item} ከ {table} ተሰርዟል!"
    },
    "en": {
        "loader_text": "⏳",
        "outdated_text": "...",

        "main_menu": (
            f"{hide_link('https://etneco.ethio-tech.com/security/db9c5c3febe75811e41af.jpg')}"
            "🤖 <b>Welcome!</b>\n\n"
            " I am the ETN Security. I will decide whether or not you can join. and where you can join "
            " In order to join you need to possess one of the ETN archives and NFT's, or SBT's "
            "depending on the type of NFT you have The amount of voting power you will have on the council may defer.\n\n"
            "<blockquote><b>Private Chats:</b>\n{chats}\n"
            "<b>Required Tokens:</b>\n{tokens}</blockquote>\n\n"
            "Click on <b>Check access availability</b> to find out if you'll be admitted!\n\n"
            "<b>Connected to:</b> {wallet}"
        ),
        "select_language": (
            f"{hide_link('https://etneco.ethio-tech.com/security/aaba319da09f60e6def03.jpg')}"
            "👋 <b>Hello!</b>\n\n"
            "Choose a language:"
        ),
        "change_language": (
            f"{hide_link('https://etneco.ethio-tech.com/security/aaba319da09f60e6def03.jpg')}"
            "<b>Choose a language:</b>"
        ),
        "deny_access": (
            f"{hide_link('https://etneco.ethio-tech.com/security/ceec89ba75c903210411c.jpg')}"
            "🚫 <b>Access Denied</b>\n\n"
            "Unfortunately, I did not detect the required tokens in your wallet.\n\n"
            "Don't worry, you can <b>purchase tokens by clicking the buttons</b> below and try again."
        ),
        "allow_access": (
            f"{hide_link('https://etneco.ethio-tech.com/security/6b03c59182d959cddeb02.jpg')}"
            "🎉 <b>Congratulations!</b>\n\n"
            "You have access to our private chats.\n\n"
            "<b>Click on the buttons</b> below and submit an application to join, "
            "I will approve them immediately!"
        ),
        "user_kicked": (
            "User {user} [{wallet}] was kicked from chat!"
        ),

        "connect_wallet": (
            f"<a href='https://ton.org/wallets?locale=en&filters[wallet_features][slug][$in]=dapp-auth&pagination[limit]=-1'>Get a Wallet</a>\n\n"
            "<b>Connect your {wallet_name}!</b>\n\n"
            "Scan with your mobile app wallet:"
        ),
        "connect_wallet_proof_wrong": (
            f"{hide_link('https://telegra.ph//file/a4ddc111ff41692ad5200.jpg')}"
            "<b>Warning</b>\n\n"
            "The wallet signature is wrong or the connection timeout has expired."
        ),
        "connect_wallet_timeout": (
            f"{hide_link('https://telegra.ph//file/a4ddc111ff41692ad5200.jpg')}"
            "<b>Warning</b>\n\n"
            "The connection timeout has expired."
        ),

        "admin_menu": (
            f"{hide_link('https://etneco.ethio-tech.com/security/aaba319da09f60e6def03.jpg')}"
            "<b>Administrator Panel</b>\n\nSelect action:"
        ),
        "chats_menu": (
            f"{hide_link('https://etneco.ethio-tech.com/security/aaba319da09f60e6def03.jpg')}"
            "<b>Private Chats Menu</b>\n\nSelect action:"
        ),
        "chat_info": (
            f"{hide_link('https://etneco.ethio-tech.com/security/aaba319da09f60e6def03.jpg')}"
            "• <b>Private Chat Information</b>\n\n"
            "• <b>ID:</b>\n"
            "<blockquote>{chat_id}</blockquote>\n"
            "• <b>Type:</b>\n"
            "<blockquote>{chat_type}</blockquote>\n"
            "• <b>Name:</b>\n"
            "<blockquote>{chat_name}</blockquote>\n"
            "• <b>Invite Link:</b>\n"
            "<blockquote>{chat_invite_link}</blockquote>\n"
            "• <b>Creation Date:</b>\n"
            "<blockquote>{chat_created_at}</blockquote>"
        ),
        "tokens_menu": (
            f"{hide_link('https://etneco.ethio-tech.com/security/aaba319da09f60e6def03.jpg')}"
            "<b>Tokens Menu</b>\n\nSelect action:"
        ),
        "token_info": (
            f"{hide_link('https://etneco.ethio-tech.com/security/aaba319da09f60e6def03.jpg')}"
            "• <b>Token Information</b>\n\n"
            "• <b>Type:</b>\n"
            "<blockquote>{token_type}</blockquote>\n"
            "• <b>Name:</b>\n"
            "<blockquote>{token_name}</blockquote>\n"
            "• <b>Address:</b>\n"
            "<blockquote>{token_address}</blockquote>\n"
            "• <b>Minimum Amount:</b>\n"
            "<blockquote>{token_min_amount}</blockquote>\n"
            "• <b>Creation Date:</b>\n"
            "<blockquote>{token_created_at}</blockquote>"
        ),
        "token_send_address": "<b>Enter Token Address</b>\n\nOnly NFT collection and Jetton master addresses are allowed:",
        "token_send_address_error": "Invalid token address:\n{}",
        "token_send_address_error_already_exist": "Token with address {address} already exists!",
        "token_send_address_error_not_supported": "Contract {interfaces} is not supported.\nOnly {supported_interfaces} are supported.",
        "token_send_amount": (
            "<b>Token Information</b>:\n\n"
            "• <b>Type:</b>\n"
            "<blockquote>{token_type}</blockquote>\n"
            "• <b>Name:</b>\n"
            "<blockquote>{token_name}</blockquote>\n\n"
            "<b>Enter the minimum token amount</b> to access the private chat:"
        ),
        "token_edit_amount": "<b>Enter the new token amount</b> to access the private chat:",
        "token_send_amount_error": "Invalid token amount!",
        "admins_menu": (
            f"{hide_link('https://etneco.ethio-tech.com/security/aaba319da09f60e6def03.jpg')}"
            "<b>Administrators Menu</b>\n\nSelect action:"
        ),
        "admin_info": (
            f"{hide_link('https://etneco.ethio-tech.com/security/aaba319da09f60e6def03.jpg')}"
            "• <b>Administrator Information</b>\n\n"
            "• <b>ID:</b>\n"
            "<blockquote>{admin_id}</blockquote>\n"
            "• <b>Name:</b>\n"
            "<blockquote>{admin_full_name}</blockquote>\n"
            "• <b>Username:</b>\n"
            "<blockquote>{admin_username}</blockquote>\n"
            "• <b>Creation Date:</b>\n"
            "<blockquote>{admin_created_at}</blockquote>"
        ),
        "admin_send_id": "<b>Enter Administrator ID:</b>",
        "admin_send_id_error": "Invalid ID:\n{}",
        "admin_send_id_error_not_found": "Administrator not found. First, the user needs to start a conversation with the bot.",
        "admin_send_id_error_not_member": "Administrator ID must be a number.",
        "confirm_item_add": "<b>Confirm</b> adding {item} to {table}?",
        "item_added": "{item} added to {table}!",
        "confirm_item_delete": "<b>Confirm</b> deleting {item} from {table}?",
        "item_deleted": "{item} deleted from {table}!"
    }
}
