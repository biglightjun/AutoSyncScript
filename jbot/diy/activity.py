from .. import jdbot, chat_id, _ConfigDir
from telethon import events
import re, json

with open(f"{_ConfigDir}/diybot.json", 'r', encoding='utf-8') as f:
    diybotset = json.load(f)
my_chat_id = int(diybotset['my_chat_id'])

@jdbot.on(events.NewMessage(from_users=chat_id, pattern=r'^activity.*|.*isv.isvj.*.com.*'))
async def activity(event):
    try:
        message = event.message.raw_text
        await jdbot.send_message(chat_id, '获取到activity地址，正在转换格式')
        id = re.findall(r'(?<=activityId.)[a-z0-9]*', message)[0]
        url = re.findall(r'https://.*isv.isvj.*.com', message)[0]
        end = ('export jd_zdjr_activityId="' + id + '"\n' + 'export jd_zdjr_activityUrl="' + url + '"')
        await jdbot.send_message(my_chat_id, end)
    except Exception as e:
        await jdbot.send_message(chat_id, 'something wrong,I\'m sorry\n' + str(e))
        logger.error('something wrong,I\'m sorry\n' + str(e))