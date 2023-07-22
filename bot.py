# 導入Discord.py模組
import discord
from discord.ext import commands, tasks
import json
import datetime
import aiohttp
from searchweather import status

with open('TOKEN.json',"r",encoding="utf8") as jsonf:
    jdata=json.load(jsonf)

# client是跟discord連接，intents是要求機器人的權限
intents = discord.Intents.all()  # 創建預設的意圖對象
bot = commands.Bot(command_prefix='!', intents=intents)

testchannel= 1129593537105760409
slepychannel = 1130499450142478458
is_task_started = False

# 調用event函式庫
@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")
    print('Bot 已經上線！')
    print("working")
    print(status)
    bot.session = aiohttp.ClientSession()
    global is_task_started
    if not is_task_started:
        # send_message.start()
        is_task_started = True
        scheduled_task.start()
        my_task.start()
        autoslepy.start()

@bot.event
async def on_disconnect():
    await bot.session.close()

@bot.event
async def on_resumed():
    print('Bot 已經重新連接！')

@tasks.loop(seconds=60)
async def autoslepy():
    global slepychannel
    now = datetime.datetime.now().strftime('%H%M')
    thetime = '1213'
    if now == thetime:
        print('autoslepycheck')
        tag_.start(slepychannel)


@bot.command()
async def slepy(ctx):
    if not tag_.is_running():
        tag_.start(ctx)




@tasks.loop(seconds=5)
async def tag_(ctx):
    global slepychannel
    ronid=691162367886622730
    user = bot.get_user(ronid)
    user_mention = user.mention
    if ctx == slepychannel:
        channel = bot.get_channel(slepychannel)
        await channel.send(f"{user_mention} 快去睡覺！！！")
        await channel.send('如需暫停請輸入 !gotobed')
    else:
        await ctx.send(f"{user_mention} 快去睡覺！！！")
        await ctx.send('如需暫停請輸入 !gotobed')





@bot.command()
async def gotobed(ctx):
    gotobedloop.start(ctx)
    gotobedloop1.start(ctx)
    tag_.cancel()


@tasks.loop(seconds=2)
async def gotobedloop(ctx):
    await ctx.send('請去睡覺！！！ 請去睡覺！！！ 請去睡覺！！！')

@tasks.loop(seconds=4)
async def gotobedloop1(ctx):
    await ctx.send('若需支援請輸入 !Imafool')

@bot.command()
async def Imafool(ctx):
    gotobedloop.cancel()
    gotobedloop1.cancel()
    gotobedloop2.start(ctx)

gotobedloop2bool=False

@tasks.loop(seconds=2)
async def gotobedloop2(ctx):
    global gotobedloop2bool
    await ctx.send('到底要睡覺了沒')
    gotobedloop2bool=True





@bot.command()
async def ping(ctx):
    await ctx.send(round(bot.latency*1000)+"(ms)")

@bot.command()
async def youreafool(ctx):
    await ctx.send('真的')

@bot.command()
async def f(ctx,message):
    await ctx.send(str(message))

@bot.event
# 當頻道有新訊息
async def on_message(message):
    global gotobedloop2bool
    # 排除機器人本身的訊息，避免無限循環
    if message.author == bot.user:
        return
    
    if message.content.startswith('!'):
        await bot.process_commands(message)
    # 新訊息包含Hello，回覆Hello, world!
    elif message.content == '到底誰笨':
        await message.channel.send('Ron!')
    elif gotobedloop2bool:
        if message.content.startswith('要') :
            gotobedloop2.cancel()
            gotobedloop2bool=False
            await message.channel.send("終於要去睡覺了，晚安")
        else:
            await message.channel.send("輸入錯誤，請重新回答")

    else:
        if message.content == "Hello":
            await message.channel.send("Hello, world!")



@tasks.loop(seconds=60)  # 每分鐘執行一次任務
async def scheduled_task():
    now = datetime.datetime.now().strftime("%H:%M")  # 獲取當前時間
    specified_time = "10:04"  # 指定時間為每天的 10 點 30 分
    print(now)
    
    if now == specified_time:
        channel = bot.get_channel(testchannel)
        await channel.send('test')   # 執行功能



utc = datetime.timezone.utc
# If no tzinfo is given then UTC is assumed.
thetime = datetime.time(hour=8, minute=30, tzinfo=utc)
@tasks.loop(time=thetime)
async def my_task():
    print("My task is running!")

#天氣
@tasks.loop(time=thetime)
async def getweather():
    infweather = status



# @tasks.loop(minutes = 5)  # 每 24 小時執行一次任務
# async def send_message():
#     print('ok')
#     channel = bot.get_channel(testchannel)  # 替換成你想要發送訊息的頻道 ID
#     await channel.send("這是每日騷擾訊息！"+"每隔五分鐘為您服務 " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))




bot.run(jdata['token'])