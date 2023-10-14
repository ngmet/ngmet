import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('$hello'):
        await message.channel.send(f'Привет Я бот  я покажу   тибе примери что делали с бутулками вот комади 1 $heh 2 $tam 3 $hek{client.user}!')
    elif message.content.startswith('$heh'):
        await message.channel.send(f'hehehehehehehehehehehehehehehehe{client.user}!')
    elif message.content.startswith('$tam'):
        await message.channel.send(f'https://youtu.be/mSmqsl0TadQ?si=GOygrfdE80-PiQLA{client.user}!')
    elif  message.content.startswith('$hek'):
        if len(message.content) > 4:
            count_heh = int(message.content[4:])
        else:
            count_heh = 5
        await message.channel.send("he" * count_heh)

client.run("MTE1Mjk2MjA2MTYzNTE3ODYwNg.GSlDeG.iQbcTbauSOAwwCVnQH6csx69v0fSxm9oHOFSCo")
