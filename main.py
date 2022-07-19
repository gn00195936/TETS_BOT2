# 導入Discord.py


import ast
import random
import discord
from discord.ext import commands
import json
# client是我們與Discord連結的橋樑
client = discord.Client()

client = commands.Bot(command_prefix='&')


@client.event
# 當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)


@client.command()
# 當有訊息時
async def 決戰香腸伯(ctx):
    client.channel = client.get_channel(998867242513084487)

    pic = ['6',
           '15',
           '14',
           '15',
           '9',
           '11',
           '13',
           '19',
           '19',
           '18',
           '13',
           '14',
           '15',
           '16',
           '17',
           '18',
           '19',
           '20',
           '21', ]
    random_pic = random.choice(pic)
    pic2 = ['3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '10',
            '11',
            '12',
            '13',
            '14',
            '15',
            '16',
            '17',
            '18',
            '19',
            '20',
            '21', ]
    random_pi2 = random.choice(pic2)
    pic3 = ['偷拿一顆骰子,跨山小',
            '拉起胳膊用力一骰',
            '左手偷偷替換骰子',
            '笑連 偶飛碟',
            '靠邀 手抽筋',
            '賽厲鬼哩',
            '阿喜巴拉',
            '挖嘎利貢 挖ㄟ我手氣很好',
            '沖啊!!!',
            '塞利鬼 開BTC合約蹦倉 幹',
            '贏後利宋歪歪',
            '妹啊美賣',
            '閃妮妹ㄟ來啊 緊緊跨',
            '笑連ㄟ 糾顏捯唷', ]

    pic4 = ["https://upload.cc/i1/2022/07/19/bSXODC.png",
            "https://upload.cc/i1/2022/07/19/bSXODC.png",
            "https://upload.cc/i1/2022/07/19/21uKEM.png",
            "https://upload.cc/i1/2022/07/19/bSXODC.png",
            "https://upload.cc/i1/2022/07/19/bSXODC.png",
            "https://upload.cc/i1/2022/07/19/bSXODC.png", ]
    pic5 = ['0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '1',
            '2',
            '3',
            '4',
            '5',
            '99',
            '0',
            '0',
            '0', ]
    pic6 = ['今天運勢平平,猛力一骰裂成兩半',
            '轟嘛利鬨!!!!',
            '我出運啦',
            '出來吧 皮卡丘',
            '九天玄女在此降靈',
            '阿密坨丸IN村羽',
            '那又怎麼樣呢?出來吧神之卡!',
            '嗯嗯嗯 哈哈哈哈哈!!!',
            '沖啊!!!',
            '大吉大利!',
            '閃妮Do Re Mi',
            '瓦甘達Forever', ]

    random_pi3 = random.choice(pic3)
    random_pi4 = random.choice(pic4)
    random_pi5 = random.choice(pic5)
    random_pi6 = random.choice(pic6)
    BOSS = int(random_pic)
    YOU = int(random_pi2)+int(random_pi5)
    random_pi7 = str(YOU)
    await client.channel.send("【香腸伯】:拚輸贏啦~~~"+"【"+random_pi3+"】"+"     【你】:.......")
    await client.channel.send("【香腸伯】:"+random_pic+"    【你】:"+"骰出"+random_pi2+"點"+"此時雙手合併用力吶喊說道"+"【"+random_pi6+"】"+"恭喜獲得:"+random_pi5+"點加成,"+"總計骰出:"+random_pi7)

    if BOSS >= YOU:
        await client.channel.send("【香腸伯】: 笑連ㄟ 咖嘎U,貪財貪財啦")
    else:
        await client.channel.send("【香腸伯】: 靠杯 輸棄,來啦貼棄")
        await client.channel.send(random_pi4)


# TOKEN在剛剛Discord Developer那邊「BOT」頁面裡面
client.run('OTk4Nzg3MDkyNjIyNjEwNDcy.Gp-Qng.KI_bpsyoZORwi7d09Yc5RCdZaVKxH5Qj8LcONU')
