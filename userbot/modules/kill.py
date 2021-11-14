#Ported from userge by @PrajjuS
import asyncio
from asyncio import sleep
from userbot.events import register
from userbot import CMD_HELP, trgg

@register(outgoing=True, pattern="^\{trg}kill$".format(trg=trgg))
async def kill_func(message):
    animation_chars = [
        "F U C K I N G...",
        "C u m m i n g g g g g",
        "(　･ิω･ิ)︻デ═一-->",
        "------>_____________",
        "--------->___⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠_______",
        "-------------->_____",
        "------------------->",
        "------>;(^。^)ノ",
        "(￣ー￣) cummed",
        "<b>Target got pregnant sucessfully (´°̥̥̥̥̥̥̥̥ω°̥̥̥̥̥̥̥̥｀)</b>",
    ]
    for i in range(10):
        await sleep(0.6)
        await message.edit(animation_chars[i % 10], parse_mode="html")

CMD_HELP.update({
    "kill":
    "'.kill'"
    "\nUsage: Kill Meme"
    })
