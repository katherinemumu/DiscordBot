# bot.py

import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@bot.command()
async def info(ctx):
    """
    !info
    ctx - context
    """
    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)

@bot.command()
async def add(ctx, *items):
    """
    !add item
    add an item to the grocery list
    """
    # if they send nothing, tell them then return
    if len(items) == 0:
        await ctx.send("yo add something.")
        return

    # since each command only adds one item, we need to join in one string
    item = ' '.join(items)

    embed = discord.Embed(
        title=f'Adding {item} To Grocery List'
    )

    msg = await ctx.send(embed=embed)
    await msg.add_reaction("⚪")
    await msg.add_reaction("👲")
    await msg.add_reaction("🛒")


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    # await message.channel.send("hi from bot :)")
    await bot.process_commands(message)

@bot.event
async def on_reaction_add(reaction, user):
    print(f'{user} reacted with {reaction.emoji}')
    # await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')

bot.run(TOKEN)