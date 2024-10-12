import discord
import random
import asyncio
from discord.ext import commands
import os 
from sett_tok import BOT_TOKEN


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def start(ctx):
    await ctx.send('Приветствую, я эколог Джим, Сегодня я проведу небольшую экскурсию :sunglasses:')

@bot.command()
async def hlp(ctx):
    await ctx.send('Список доступных команд: $theo, $game, $end')

@bot.command()
async def theo(ctx):
    await ctx.send('С чего же нам начать.....')
    await asyncio.sleep(1.0)
    await ctx.send('Начнём пожалуй с основ, что же такое экология?')
    await asyncio.sleep(3.0)
    await ctx.send('Экология - наука изучающая взаимодействие живых организмов в окружающей среде')
    await asyncio.sleep(5.0)
    await ctx.send('К сожалению множество людей в наше время совсем не озабочены проблемой загрязнения окружающей среды :(')
    await asyncio.sleep(1.0)
#Тут я решил воспользоваться другим, более простым методом отправки изображений, через непосредственно отправку ссылки на изображение
    await ctx.send("https://static.tildacdn.com/tild3031-3939-4536-b837-316630613636/_.jpg")
    await asyncio.sleep(2.0)
    await ctx.send('И таких случаев миллионы...(')
    await asyncio.sleep(3.0)
    await ctx.send('Именно поэтому важно поддерживать экологию, ведь представьте какая бы была планета, если бы люди не разбрасывали мусор где попало!')
    await ctx.send('https://img.freepik.com/premium-photo/illustration-earth-globe-surrounded-by-vibrant-plants_92152-71124.jpg?semt=ais_hybrid-rr-similar')

#отсутствуют какие либо 
@bot.command()
async def game(ctx):
    await ctx.send('Добро пожаловать в мою игру!:partying_face:, здесь тебе будут попадаться отрывки из которых нужно будет собрать целую фразу! Данная мини-игра важна для общего понимания')
    await asyncio.sleep(6.0)
    rand_num = random.randint(1,6)
    if rand_num == 1:
        await ctx.send('Не природе нужна наша защита....')
    elif rand_num == 2:
        await ctx.send('....это нам необходимо ее покровительство....')
    elif rand_num == 3:
        await ctx.send('.....чистый воздух, чтобы дышать,....')
    elif rand_num == 4:
        await ctx.send('.....кристальная вода, чтобы пить,.....')
    elif rand_num == 5:
        await ctx.send('.....вся природа, чтобы жить.....') 

@bot.command()
async def end(ctx):
    await ctx.send('Итак, подитожим...')
    await asyncio.sleep(2.0)
    await ctx.send('Сегодня мы узнали что же такое экология и зачем она вообще нужна, так же сегодня мы познакомились с великой цитатой не менее великого человека - Николая Фёдоровича Реймерса')
bot.run(BOT_TOKEN)
