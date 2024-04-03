import asyncio

from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import run_async, run_js

# Global variables to store chat messages and online users
chat_msgs = []
online_users = set()

# Maximum number of messages to keep in the chat history
MAX_MESSAGES_COUNT = 100


async def main():
    global chat_msgs

    # Display welcome message
    put_markdown("## 💬 Welcome to online chat!\n")

    # Output box to display chat messages
    msg_box = output()
    put_scrollable(msg_box, height=300, keep_bottom=True)

    # Input field to get user's nickname
    nickname = await input("Enter the chat", required=True, placeholder="What's your name?",
                           validate=lambda
                               n: "This nickname is already in use!" if n in online_users or n == '👥' else None)
    online_users.add(nickname)

    # Notify all users about new user joining the chat
    chat_msgs.append(('👤', f'`{nickname}` joined the chat!'))
    msg_box.append(put_markdown(f'👤 `{nickname}` joined the chat'))

    # Start asynchronous task to refresh chat messages
    refresh_task = run_async(refresh_msg(nickname, msg_box))

    # Main loop to handle user interaction
    while True:
        # Get input from the user (message or leave chat)
        data = await input_group("💭 A new message", [
            input(placeholder="Message text ...", name="msg"),
            actions(name="cmd", buttons=["Send", {'label': "Leave chat", 'type': 'cancel'}])
        ], validate=lambda m: ('msg', "Enter message text!") if m["cmd"] == "Send" and not m['msg'] else None)

        # If user leaves the chat, break the loop
        if data is None:
            break

        # Display user's message in the chat
        msg_box.append(put_markdown(f"`{nickname}`: {data['msg']}"))
        chat_msgs.append((nickname, data['msg']))

    # Exit chat
    refresh_task.close()

    # Remove user from online users
    online_users.remove(nickname)
    # Notify all users about user leaving the chat
    toast("You have left the chat!")
    msg_box.append(put_markdown(f'👤 User `{nickname}` left the chat!'))
    chat_msgs.append(('👤', f'User `{nickname}` left the chat!'))

    # Button to refresh the page for re-entering the chat
    put_buttons(['Re-Enter'], onclick=lambda btn: run_js('window.location.reload()'))


async def refresh_msg(nickname, msg_box):
    global chat_msgs
    last_idx = len(chat_msgs)

    # Continuously refresh the chat messages
    while True:
        await asyncio.sleep(1)

        # Display new messages in the chat
        for m in chat_msgs[last_idx:]:
            if m[0] != nickname:  # if not a message from current user
                msg_box.append(put_markdown(f"`{m[0]}`: {m[1]}"))

        # Remove expired messages to control the chat history size
        if len(chat_msgs) > MAX_MESSAGES_COUNT:
            chat_msgs = chat_msgs[len(chat_msgs) // 2:]

        last_idx = len(chat_msgs)


if __name__ == "__main__":
    # Start the chat server
    start_server(main, debug=True, port=8080, cdn=False)
