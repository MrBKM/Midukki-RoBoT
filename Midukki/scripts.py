START_TXT = """<i><b>Hello 👋 {mention},</i></b>

<i><b>I Am Not Only {bot} To Assist You But Also Employed At <a href="https://t.me/Tk_movies_adda">Movie Time</a> Group By <a href="https://t.me/BIKASH_9999">Bikash</a> So You Can't Get My Service By Adding Me To Your Group So Don't Waste Your Time & Data  😉</i></b>

<i><b>Better You Click Below & Join <a href="https://t.me/Tk_movies_adda">Movie Time</a> & Feel The Experience Of Downloading Unlimited Movies/Series ✅</i></b>

<i><b>For More Information Click ℹ️ Help</i></b>"""


HELP_TXT = """<i><b>Hello 👋 {mention},</i></b>

<i><b>I can Guide You Through All Of {bot}'s Cool Features & How To Properly Use Them. Use The Buttons Below To Navigate Through All Of The Modules.</i></b>

ABOUT_TXT = """<b>
[{name}] Was created on December 8, 2022

➾ Developers : Mr.BKM
➾ Language : Python3
➾ Framework : Pyrogram
➾ Database : MongoDB
</b>"""

DONATE_TXT = """<i><b>Hello 👋 {mention}</i></b>

<i><b>Thank You For Showing Interest In My Works 🙏

To Support My Works, Please Feel Free To Donate Any Amount You Like 💸</i></b>

<b>UPI 🆔

Google Pay 📲</b> `joynathnet4@oksbi`
"""

STATUS_TXT = """
**--{bot}'s STATUS--**

📡 __--Server Status--__
◉ Uptime: `{a}`
◉ CPU Usage: `{b}%`
◉ RAM Usage: `{c}%`
◉ Total Disk Space: `{d}`
◉ Used Space: `{e} ({f}%)`
◉ Free Space: `{g}`

🗃️ __--Database Status--__
◉ Tota Files: `{h}`
◉ Tota Users: `{i}`
◉ Tota Chats: `{j}`
◉ Used Storage: `{k}` 
◉ Free Storage: `{l}`
◉ Total Storage: `{m}` 
"""

AUTO_TXT = """
**--MODULE OF AUTOFILTER--**

● I Can Provide Files In Your Group, It Very Easy Way Just Add Me Ro Your Group And Make Me Admin In Your Group, Thats All.. I Will Provide Files From Your Group 
      
🔋 **--Usage & Commands--** :

◉ /autofilter : use to turn on & off
◉ /set_temp : set new result temp
◉ /del_temp : del seted result temp
◉ /settings : use to modify autofilter settings

🔋 **--Supporting Vars--** :

 • `{mention}` : user profile link
 • `{query}` : request text
 • `{group_name}` : group name
"""

MANUAL_TXT = """
**--MODULE OF MANUALFILTER--**

● Filter Is The Feature Were Users Can Set Automated Replies For A Particular Keyword And Bot Will Respond Whenever A Keyword Is Found The Message

🔋 **--Note--** :

1. This bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

🔋 **--Commands and Usage--** :

◉ /add : add a filter in chat
◉ /filters : list all the filters of a chat
◉ /del : delete a specific filter in chat
◉ /delall : delete the whole filters in a chat (chat owner only)
"""

CONNECTION_TXT = """
**--MODULE OF CONNECTIONS**--

● Used to connect bot to PM for managing filters 
● it helps to avoid spamming in groups.

🔋 **--NOTE--** :

1. Only admins an add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

🔋 **--Commands and Usage--** :

◉ /connect : connect a particular chat to your PM
◉ /disconnect : disconnect from a chat
◉ /connections : list all your connections
"""

INFO_TXT = """
**--MODULE OF INFO--**

● Hese are the extra features of this bot

🔋 **--Commands and Usage--** :

◉ /id : get id of a specifed user.
◉ /info : get information about a user.
"""

SPELL_TXT = """
**--MODULE OF SPELLCHECK--**

● Everything Related To The Spell Check Module When No AutoFilter Result Are Found 

🔋 **--Commands & Usage--** :

◉ /set_spell : Set A New SpellCheck Text
◉ /del_spell : restart Spell Check Message

🔋 **--Supporting Vars--** :

 • `{mention}` : user profile link
 • `{query}` : request text 
 • `{title}` : get chat title

> Eg:- /setspell Check Your Spelling {query}
"""

CAP_TXT = """
**--MODULE OF CUSTOM CAPTION--**

● Use This Feature To Add A Custom Caption To File

🔋 **--Commands & Usage--** :

◉ /set_cap : set new file caption 
◉ /del_cap : restart file caption

🔋 **--Supporting Vars--** :

 • {mention} : user profile link
 • {file_name} : file name
 • {size} : file size 
 • {caption} : get original caption
"""

MUTE_TXT = """
**--MODULE OF MUTE--** 🤐

● some people need to be publicly muted: spammers, annkyances, or just trolls...! this module allows you to do that easily by exposing same commo actions, so everyone will see..!

🔋 **--Commands and Usage**-- :

◉ /mute : Mute a user
◉ /unmute : Unmute a user
◉ /tmute : Temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days
"""

BAN_TXT = """
**--MODULE OF BAN--** 🚫

● some people need to be publicly banned: spammers, annkyances, or just trolls...! this module allows you to do that easily by exposing same commo actions, so everyone will see..!

🔋 **--Commands and Usage**-- :

◉ /ban : ban a user 
◉ /unban : unban the user
◉ /tban : Temporarily ban a user. Example time values: 30s = 30 seconds, 4m = 4 minutes, 3h = 3 hours
"""

PIN_TXT = """
**--MODULE OF PIN--** 📌

● all the pin related commands can be found here; keep your chat up to date on the latest news with a simple pinned message!

🔋 **--Commands and Usage**-- :

◉ /pin : Pin the message you replied to message to send a notification to group members
◉ /unpin : Unpin the current pinned message. if used as a reply, unpins the replied to message
"""

ADMIN_PANEL = """
📤 **Admin Only**

- /channel : total channels
- /total : total files
- /delfile : del single files
- /delallfile : del all files
- /skip : skip index file
- /logs : bot logs
- /broadcast : broadcast message
"""

FILE_CAPTION_TXT = """{file_name}"""

SPELLCHECK_TXT = """<b>Hello</b> 👋 {mention}

<b>I Couldn't 🔍 Find</b> {query} <b>You Asked For 🤷</b>

<b>Search In GOOGLE And Find The Correct Movie/Series Name And Enter It Here ⤵️</b>

<b>If You Do Not Receive The Movie/Series Even After Entering The Correct Name Then Your Requested Movie/Series Does Not Exit In My Database 🗄</b>"""

IMDB_TEMPLATE_TXT = """
🙋‍♂️ Hey {mention} Your Requested {query} is ready 👍
"""

WELCOME_TXT = """⁣👋 Hello {mention},
 
Wᴇʟᴄᴏᴍᴇ ᴛᴏ {chat} 💐

Gʟᴀᴅ ʏᴏᴜ ғᴏᴜɴᴅ ᴜs !! 
Pʟᴇᴀsᴇ ᴛᴀᴋᴇ ᴀ ᴍᴏᴍᴇɴᴛ ᴛᴏ ʀᴇᴀᴅ 
ᴛʜᴇ Gʀᴏᴜᴘ Rᴜʟᴇs. Iᴛ's sʜᴏʀᴛ I ᴘʀᴏᴍɪsᴇ.
Yᴏᴜʀ ᴘᴏsᴛɪɴɢ ʜᴇʀᴇ ɪs ᴀᴄᴄᴇᴘᴛɪɴɢ ᴛʜᴀᴛ ʏᴏᴜ'ᴠᴇ ʀᴇᴀᴅ ᴛʜᴇᴍ ᴀɴᴅ ᴡɪʟʟ ᴀʙɪᴅᴇ ʙʏ ᴛʜᴇᴍ. Jᴜᴍᴘ ɪɴ !!"""

SEND_LOGS_A = """
#BOT_STARTED"""

class Txt(object):
    START_TXT = START_TXT
    HELP_TXT = HELP_TXT
    ABOUT_TXT = ABOUT_TXT
    STATUS_TXT = STATUS_TXT
    AUTO_TXT = AUTO_TXT
    MANUAL_TXT = MANUAL_TXT
    INFO_TXT = INFO_TXT
    CONNECTION_TXT = CONNECTION_TXT
    CAP_TXT = CAP_TXT
    SPELL_TXT = SPELL_TXT
    MUTE_TXT = MUTE_TXT
    BAN_TXT = BAN_TXT
    PIN_TXT = PIN_TXT
    ADMIN_PANEL = ADMIN_PANEL
