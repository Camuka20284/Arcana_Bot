import discord
from discord.ext import commands
from config import token

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='*', intents=intents)

class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def info(self):
        return f"Aracın markası: {self.brand}, rengi: {self.color}"

@client.event
async def on_ready():
    print(f'Giriş yapıldı: {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.attachments:
        await message.channel.send("📷 Güzel bir resim göndermişsin!")

    if message.content.startswith(client.command_prefix):
        await client.process_commands(message)
    else:
        await message.channel.send(message.content)

@client.command()
async def about(ctx):
    await ctx.send('Ben discord.py ile oluşturulmuş basit bir botum! Adım Arcana.')

@client.command()
async def info(ctx):
    await ctx.send("Ben bir Echo Bot’um! discord.py ile yapıldım.")

@client.command()
async def repeat(ctx, times: int, *, message: str):
    for _ in range(times):
        await ctx.send(message)

@client.command()
async def car(ctx, color: str, brand: str):
    my_car = Car(color, brand)
    await ctx.send(my_car.info())

client.run(token)
