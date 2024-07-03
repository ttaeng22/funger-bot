import discord
from discord.ext import commands

discord_bot_token = 'MTI1Nzg4NjE4Mjc1OTQ2NDk5Mg.GClC7o.UZkPcTNjJXhFaoZd00wu38E6IjDTX9OqvnhT5U'
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="%", intents=intents)

#봇 로그인
@bot.event
async def on_ready():
    print(f'{bot.user} 에 로그인하였습니다!')

#봇 명령어
@bot.command()
async def 안녕(ctx):
    await ctx.send("안녕하세요! 무엇을 도와드릴까요?")

#봇 실행
bot.run(discord_bot_token)