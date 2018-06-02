import discord, logging, json, asyncio, time, random, aiohttp, re, datetime, traceback, os, sys, math
from discord.ext import commands

#-------------------DATA---------------------
version = "0.6.1"
owner = ["361534796830081024"]
bot = commands.Bot(command_prefix='r-', description=None)
message = discord.Message
server = discord.Server
member = discord.Member
user = discord.User
Imox = ["365173881952272384"]
permissions = discord.Permissions
"""Registered : 452135771672018954"""
#--------------------------------------------

#--------------MODERATOR'S ID-----------------
"""                  Imox                  Rettend                PReiZ                 Lapras                Legends               sunrab                Spork"""
Moderators = ["365173881952272384", "361534796830081024", "407382812518383627", "323851553662566401", "386400236916047872", "366607123771293696", "375991973246533642"]
#--------------------------------------------

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print(discord.utils.oauth_url(bot.user.id))
    await bot.change_presence(game=discord.Game(name='Restarted 🤘'))

class NoPermError(Exception):
    pass

@bot.command(pass_context=True)
async def ping(ctx):
    before = time.monotonic()
    msg = await bot.say(":ping_pong: **...**")
    ping = (time.monotonic() - before) * 1000
    pinges = int(ping)
    if pinges > 1000:
        mesg = "Omg, we are really sloooooow...."
    elif pinges > 400:
        mesg = "Thats a lot!"
    elif pinges < 100:
        mesg = "Its Good, Boi ;)"
    await bot.edit_message(msg, f":ping_pong: **Seems like `{pinges}` MS\n{mesg}**")

@bot.command(pass_context=True)
async def clear(ctx, number : int):
    if ctx.message.author.id in Moderators:
        number += 1
        deleted = await bot.purge_from(ctx.message.channel, limit=number)
        num = number - 1
        msg = await bot.send_message(ctx.message.channel, f'**{ctx.message.author} deleted __{num}__ messages**')
        await asyncio.sleep(4)
        await bot.delete_message(msg)
    else:
        await bot.send_message(ctx.message.channel, f'**Boi, you cant use this command...*')
        raise NoPermError

@bot.command(pass_context=True)
async def roll(ctx, x : int, y : int):
    msg = random.randint(x, y)
    text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
    await asyncio.sleep(3)
    await bot.edit_message(text, f"**Oh, my choose: {msg}**")

@bot.command(pass_context=True)
async def sub(ctx, x : int, y : int):
    msg = x - y
    text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
    await asyncio.sleep(3)
    await bot.edit_message(text, f"**Oh, the result: {msg}**")
    
@bot.command(pass_context=True)
async def mul(ctx, x : int, y : int):
    msg = x * y
    text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
    await asyncio.sleep(3)
    await bot.edit_message(text, f"**Oh, the result: {msg}**")
    
@bot.command(pass_context=True)
async def div(ctx, x : int, y : int):
    msg = x / y
    text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
    await asyncio.sleep(3)
    await bot.edit_message(text, f"**Oh, the result: {msg}**")
    
@bot.command(pass_context=True)
async def exp(ctx, x : int, y : int):
    msg = x ** y
    text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
    await asyncio.sleep(3)
    await bot.edit_message(text, f"**Oh, the result: {msg}**")
    
@bot.command(pass_context=True)
async def add(ctx, x : int, y : int):
    msg = x + y
    text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
    await asyncio.sleep(3)
    await bot.edit_message(text, f"**Oh, the result: {msg}**")
    
@bot.command()
async def game(play):
    await bot.change_presence(game=discord.Game(name=play))
    em = discord.Embed(title="Game Status", description=f"Game status changed to __{play}__!", colour=0x3498db)
    await bot.say(embed=em)

@bot.command(pass_context=True)
async def nick(ctx, name):
    await bot.change_nickname(ctx.message.author, name)
    em = discord.Embed(title="Nickname", description=f"{ctx.message.author}'s nick set to __{name}__!", colour=0x3498db)
    await bot.say(embed=em)
    
@bot.command(pass_context=True)
async def suggest(ctx, pref, text):
    try:
        if pref is "S":
            msg = "𝓢𝓾𝓰𝓰𝒆𝓼𝓽𝓲𝓸𝓷"
        if pref is "Q":
            msg = "𝓠𝓾𝒆𝓼𝓽𝓲𝓸𝓷"
        if pref is "C":
            msg = "𝓒𝓸𝓶𝓶𝓪𝓷𝓭 𝓢𝓾𝓰𝓰𝒆𝓼𝓽𝓲𝓸𝓷"
        if pref is "B":
            msg = "𝓑𝓾𝓰𝓼"
        if pref is None:
            bot.say("**Please use a valid prefix! The available prefixes: __Q__, __S__, __C__, __B__**")
        if text is None:
            bot.say("**Please write a message!**")
        if text and pref is None:
            bot.say("**Usage:\n\tr-suggest {pref} \"{message}\"**")
    finally:
        colours = [0x11806a, 0x1abc9c, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e, 0xe67e22, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a]
        col = random.choice(colours)
        em = discord.Embed(title=f"{msg}", description=f"**From {ctx.message.author.mention}**\n⋙ {text}", colour=col)
        channel = bot.get_channel(id="444837114258128916")
        room = bot.get_channel(id="444837114258128916")
        await bot.send_message(ctx.message.channel, f"**:white_check_mark: Sent in {channel.mention}**")
        mesg = await bot.send_message(room, embed=em)
        if pref is "S":
            await bot.add_reaction(mesg, "👍")
            await bot.add_reaction(mesg, "👎")
        if pref is "C":
            await bot.add_reaction(mesg, "👍")
            await bot.add_reaction(mesg, "👎")
            
@bot.command(pass_context=True)
async def poll(ctx, question, options: str):
    if len(options) <= 1:
        await bot.say('You need more than one option to make a poll!')
        return
    if len(options) > 10:
        await bot.say('You cannot make a poll for more than 10 things!')
        return
    if len(options) == 2:
        reactions = ['👍', '👎']
    else:
        reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']
    description = []
    for x, option in enumerate(options):
        description += '\n {} {}'.format(reactions[x], option)
    embed = discord.Embed(title=question, description=''.join(description), colour=0x3498db)
    react_message = await bot.say(embed=embed)
    for reaction in reactions[:len(options)]:
        await bot.add_reaction(react_message, reaction)
    await bot.edit_message(react_message, embed=embed)

@bot.command(pass_context=True)
async def register(ctx):
    for server in bot.servers:
        roles = server.roles
        members = server.members
        member = None
        for mem in members:
            if mem.id == ctx.message.author.id:
                member = mem
                break
        for role in roles:
            if role.name == "Registered":
                await bot.add_roles(member, role)
                await bot.send_message(ctx.message.channel, "**Boi, you are already verified... Why are you want to?**")
                break
            elif role.name == "Unregistered":
                await bot.remover_roles(member, role)
                await bot.send_message(ctx.message.channel, f"**Congratulations {ctx.message.author}, you are verified!**")
                break
       
@bot.command(pass_context=True)
async def verify(ctx):
    room = bot.get_channel(id='420141568486408203')
    for server in bot.servers:
        roles = server.roles
        members = server.members
        member = None
        for mem in members:
            if mem.id == ctx.message.author.id:
                member = mem
                break
        for role in roles:
            if role.name == "Registered":
                await bot.send_message(ctx.message.channel, "**Boi, you are already verified... Why are you want to?**")
                break
            elif role.name == "Unregistered":
                em = discord.Embed(title='VERIFICATION', description='**Hey __' + ctx.message.author + '__, if you want to get verified, you need to answer 3 questions:\n'
                                        ':one: Do you play __.io games__?\n'
                                        ':two: What else games do you play? __Please enumerate some of them__\n'
                                        ':three: How did you get here?\n'
                                        '__Note__: if you play a game, and you want to get this game\'s special role, you need to ask it to an Admin (or higher), that game will be added to {0.mention}\n'
                                        '\n'
                                        '__Type `r-register` if you answered all of the questions above, and to finish the verification__**'.format(room), colour=0x3498db)
                em.set_thumbnail(url=message.author.avatar_url)
                await bot.send_message(ctx.message.channel, embed=em)
                break
    
@bot.listen()
async def on_member_join(member):
    room = bot.get_channel(id="381774233199443968")
    is_verified = False
    for role in member.roles:
        if role.name == "Registered":
            is_verified = True
            break
        if is_verified == False:
            await bot.send_message(room, f"**Welcome __{member.name}__, I will show you around, First, to __get permissions for all channels__, you need to type `r-verify` and __answer all of the questions!__\nThan type `r-register` ! __IMPORTANT: typing `r-register` without answering the questions, will unregister you!__**")

@bot.listen()
async def on_member_remove(member):
    room2 = bot.get_channel(id="370269066864361476")
    await bot.send_message(room2, f"**{member} left without saying anything...** <:thonkSad:421004865049985035>")

@bot.event
async def on_message(message):
    if message.content.startswith('r-lock'):
        if message.author.id in Moderators:
            room = message.channel
            Registered = discord.utils.get(message.server.roles, name="Registered")
            overwrite = discord.PermissionOverwrite()
            overwrite.send_messages = False
            await bot.edit_channel_permissions(room, Registered, overwrite)
            await bot.send_message(room, f"**{room.mention} is now locked! Ha ha**")
        else:
            await bot.send_message(ctx.message.channel, f'**Boi, you cant use this command...*')
            raise NoPermError
    if message.content.startswith('r-unlock'):
        if message.author.id in Moderators:
            room = message.channel
            Registered = discord.utils.get(message.server.roles, name="Registered")
            overwrite = discord.PermissionOverwrite()
            overwrite.send_messages = True
            await bot.edit_channel_permissions(room, Registered, overwrite)
            await bot.send_message(room, f"**{room.mention} is now unlocked, feel free to chat!**")
        else:
            await bot.send_message(ctx.message.channel, f'**Boi, you cant use this command...*')
            raise NoPermError
    if message.content.upper().startswith('R-AMIOWNER?'):
        if message.author.id in owner:
            await bot.send_message(message.channel, ':white_check_mark: **You are the Owner, Hey Rettend :D**')
        else:
            await bot.send_message(message.channel, ':negative_squared_cross_mark: **You aren\'t the Owner.**')
    if message.content.startswith('r-say'):
        args = message.content.split(' ')
        await bot.send_message(message.channel, '**%s**' % (' '.join(args[1:])))
    if message.content.startswith('r-bigdigits'):
        await bot.send_message(message.channel, ':globe_with_meridians: **DIGITS:\n'
                               '-Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine\n'
                               'Type `r-digits {0-9}` for the digits**')
    if message.content.startswith('r-digits 0'):
        await bot.send_message(message.channel, ':radio_button: **Zero:**')
        await bot.send_message(message.channel, ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n" 
                                    ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                                    ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                                    ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                                    ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                                    ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                                    ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:")
    if message.content.startswith('r-digits 1'):
        await bot.send_message(message.channel, ':radio_button: **One:**')
        await bot.send_message(message.channel, ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                                ":black_circle::large_blue_circle::large_blue_circle::black_circle::black_circle:\n"
                                ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                                ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                                ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                                ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                                ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n")
    if message.content.startswith('r-digits 2'):
        await bot.send_message(message.channel, ':radio_button: **Two:**')
        await bot.send_message(message.channel, ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                               ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                               ":black_circle::large_blue_circle::black_circle::black_circle::black_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::black_circle:\n"
                               ":large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle:")
    if message.content.startswith('r-digits 3'):
        await bot.send_message(message.channel, ':radio_button: **Three:**')
        await bot.send_message(message.channel, ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":black_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":black_circle::black_circle::large_blue_circle::large_blue_circle::large_blue_circle:\n"
                               ":black_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:")
    if message.content.startswith('r-digits 4'):
        await bot.send_message(message.channel, ':radio_button: **Four:**')
        await bot.send_message(message.channel, ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                               ":black_circle::black_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                               ":black_circle::large_blue_circle::black_circle::large_blue_circle::black_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                               ":large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle:\n"
                               ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:")
    if message.content.startswith('r-digits 5'):
        await bot.send_message(message.channel, ':radio_button: **Five:**')
        await bot.send_message(message.channel, ":large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::black_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::black_circle:\n"
                               ":large_blue_circle::large_blue_circle::large_blue_circle::black_circle::black_circle:\n"
                               ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:\n" 
                               ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                               ":large_blue_circle::large_blue_circle::large_blue_circle::black_circle::black_circle:")
    if message.content.startswith('r-digits 6'):
        await bot.send_message(message.channel, ':radio_button: **Six:**')
        await bot.send_message(message.channel, ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::black_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::black_circle:\n"
                               ":large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:")
    if message.content.startswith('r-digits 7'):
        await bot.send_message(message.channel, ':radio_button: **Seven:**')
        await bot.send_message(message.channel, ":black_circle::black_circle::black_circle::black_circle::black_circle:\n"
                               ":large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle:\n"
                               ":black_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                               ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                               ":black_circle::large_blue_circle::black_circle::black_circle::black_circle:\n"
                               ":black_circle::large_blue_circle::black_circle::black_circle::black_circle:")
    if message.content.startswith('r-digits 8'):
        await bot.send_message(message.channel, ':radio_button: **Eight:**')
        await bot.send_message(message.channel, ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:")
    if message.content.startswith('r-digits 9'):
        await bot.send_message(message.channel, ':radio_button: **Nine:**')
        await bot.send_message(message.channel, ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle:\n"
                               ":black_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":black_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:")
    if message.content.startswith('r-8ball'):
        await bot.send_message(message.channel, random.choice(['**It is certain :8ball:**',
                                                              '**It is decidedly so :8ball:**',
                                                              '**Without a doubt :8ball:**',
                                                              '**No U :8ball:**',
                                                              '**Boi, go sleep... :8ball:**',
                                                              '**As i see it, yes :8ball:**',
                                                              '**As i see it, *No U*   :8ball:**',
                                                              '**Most likely :8ball:**',
                                                              '**Outlook good :8ball:**',
                                                              '**Yes :8ball:**',
                                                              '**Signs point to yes :8ball:**',
                                                              '**Reply hazy try again :8ball:**',
                                                              '**Ask again later, nub :8ball:**',
                                                              '**Better not tell you :8ball:**',
                                                              '**Cannot predict now :8ball:**',
                                                              '**Concentrate and ask again :8ball:**',
                                                              '**8ball.exe not found :8ball:**',
                                                              '**Dont count on it :8ball:**',
                                                              '**My reply is no :8ball:**',
                                                              '**My sources say no :8ball:**',
                                                              '**Outloook not so good :8ball:**',
                                                              '**Very doubtful :8ball:**',
                                                              '**Ha! :8ball:**',
                                                              '**Ask it to ur mum :8ball:**',
                                                              ':feelsUltraREE: ***REEEE* :8ball:**',]))
    if message.content.startswith('r-lenny'):
        ears = ['q{}p', 'ʢ{}ʡ', '⸮{}?', 'ʕ{}ʔ', 'ᖗ{}ᖘ', 'ᕦ{}ᕥ', 'ᕦ({})ᕥ', 'ᕙ({})ᕗ', 'ᘳ{}ᘰ', 'ᕮ{}ᕭ', 'ᕳ{}ᕲ', '({})', '[{}]', '୧{}୨', '୨{}୧', '⤜({})⤏', '☞{}☞', 'ᑫ{}ᑷ', 'ᑴ{}ᑷ', 'ヽ({})ﾉ', '乁({})ㄏ', '└[{}]┘', '(づ{})づ', '(ง{})ง', '|{}|']
        eyes = ['⌐■{}■', ' ͠°{} °', '⇀{}↼', '´• {} •`', '´{}`', '`{}´', 'ó{}ò', 'ò{}ó', '>{}<', 'Ƹ̵̡ {}Ʒ', 'ᗒ{}ᗕ', '⪧{}⪦', '⪦{}⪧', '⪩{}⪨', '⪨{}⪩', '⪰{}⪯', '⫑{}⫒', '⨴{}⨵', "⩿{}⪀", "⩾{}⩽", "⩺{}⩹", "⩹{}⩺", "◥▶{}◀◤", "≋{}≋", "૦ઁ{}૦ઁ", "  ͯ{}  ͯ", "  ̿{}  ̿", "  ͌{}  ͌", "ළ{}ළ", "◉{}◉", "☉{}☉", "・{}・", "▰{}▰", "ᵔ{}ᵔ", "□{}□", "☼{}☼", "*{}*", "⚆{}⚆", "⊜{}⊜", ">{}>", "❍{}❍", "￣{}￣", "─{}─", "✿{}✿", "•{}•", "T{}T", "^{}^", "ⱺ{}ⱺ", "@{}@", "ȍ{}ȍ", "x{}x", "-{}-", "${}$", "Ȍ{}Ȍ", "ʘ{}ʘ", "Ꝋ{}Ꝋ", "๏{}๏", "■{}■", "◕{}◕", "◔{}◔", "✧{}✧", "♥{}♥", " ͡°{} ͡°", "¬{}¬", " º {} º ", "⍜{}⍜", "⍤{}⍤", "ᴗ{}ᴗ", "ಠ{}ಠ", "σ{}σ"]
        mouth = ['v', 'ᴥ', 'ᗝ', 'Ѡ', 'ᗜ', 'Ꮂ', 'ヮ', '╭͜ʖ╮', ' ͟ل͜', ' ͜ʖ', ' ͟ʖ', ' ʖ̯', 'ω', '³', ' ε ', '﹏', 'ل͜', '╭╮', '‿‿', '▾', '‸', 'Д', '∀', '!', '人', '.', 'ロ', '_', '෴', 'ѽ', 'ഌ', '⏏', 'ツ', '益']
        lenny = random.choice(ears).format(random.choice(eyes)).format(random.choice(mouth))
        await bot.send_message(message.channel, "**A wild Lenny has appeard:**\n\n\t" + lenny)
    if message.content.startswith('r-oof'):
        o = ['o00', 'oo', 'oO', 'o0', 'Oo', '0o', 'OOo', 'O0o', 'ooO', 'oo0', 'oo0oO', 'o0o', '0ooO', 'oo0oOO', 'ooo', '0oo', 'oooo', 'Ooo0', 'O0oo', 'ooo0', ]
        f = ['f', 'ff', 'fff']
        mark = ['!', '!!', '!!', '!1', '!!1', '!1!!', '1!!!', '!1!1!', '1!', '!!1!', '!!!1!', '!!!!', '!11!']
        msg1 = random.choice(o)
        msg2 = random.choice(f)
        msg3 = random.choice(mark)
        await bot.send_message(message.channel, msg1 + msg2 + msg3)
    if message.content.startswith('r-leavepls'):
        em5 = discord.Embed(title=":warning: WARNING :warning:", description="THE BOT WILL LEAVE THE SERVER IN:\n"
                            ":large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::black_circle:\n"
                            ":large_blue_circle::large_blue_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:\n" 
                            ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::large_blue_circle::large_blue_circle::black_circle::black_circle:", colour=0x3498db)
        msg = await bot.send_message(message.channel, embed=em5)
        await asyncio.sleep(1)
        em4 = discord.Embed(title=":warning: WARNING :warning:", description="THE BOT WILL LEAVE THE SERVER IN:\n"
                            ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                            ":black_circle::large_blue_circle::black_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle:\n"
                            ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:", colour=0x3498db)
        await bot.edit_message(msg,  embed=em4)
        await asyncio.sleep(1)
        em3 = discord.Embed(title=":warning: WARNING :warning:", description="THE BOT WILL LEAVE THE SERVER IN:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":black_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::large_blue_circle::large_blue_circle:\n"
                            ":black_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:", colour=0x3498db)
        await bot.edit_message(msg,  embed=em3)
        await asyncio.sleep(1)
        em2 = discord.Embed(title=":warning: WARNING :warning:", description="THE BOT WILL LEAVE THE SERVER IN:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::large_blue_circle::black_circle::black_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::black_circle:\n"
                            ":large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle:", colour=0x3498db)
        await bot.edit_message(msg,  embed=em2)
        await asyncio.sleep(1)
        em1 = discord.Embed(title=":warning: WARNING :warning:", description="THE BOT WILL LEAVE THE SERVER IN:\n"
                            ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n", colour=0x3498db)
        await bot.edit_message(msg,  embed=em1)
        await asyncio.sleep(1)
        em0 = discord.Embed(title=":warning: WARNING :warning:", description="THE BOT WILL LEAVE THE SERVER IN:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n" 
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:", colour=0x3498db)
        await bot.edit_message(msg,  embed=em0)
        await asyncio.sleep(1)
        em = discord.Embed(title="lol Joke", colour=0x3498db)
        em.set_thumbnail(url="https://cdn.discordapp.com/emojis/423864027610087426.png?v=1")
        await bot.edit_message(msg,  embed=em)
    if message.content.startswith('r-invite'):
        em = discord.Embed(title='MY LINKS:', description=':cyclone: PissRocket: https://discord.gg/Cf833k8\n'
                           ':link: Website: https://hegyiaron101.wixsite.com/pissrocket', colour=0x3498db)
        await bot.send_message(message.channel, embed=em)
    if message.content.startswith('r-list'):
        await bot.send_message(message.channel, "**Usage: `r-list 1` and `r-list 2`\nAlso `r-latest` for the latest commands**")
    if message.content.startswith('r-list 1'):
        emb = discord.Embed(title='MY COMMANDS:', description="Hey, check out my commands!", colour=0x3498db)
        emb.add_field(name='--------------------', value=':small_blue_diamond: r-bot\n'
                            ':white_small_square: r-game {game}\n'
                            ':small_blue_diamond: r-say {words}\n'
                            ':white_small_square: r-ping\n'
                            ':small_blue_diamond: r-AmiOwner?\n'
                            ':white_small_square: r-bigdigits\n'
                            ':small_blue_diamond: r-digits {0-9}\n'
                            ':white_small_square: r-help\n'
                            ':small_blue_diamond: r-leavepls\n'
                            ':white_small_square: r-poll {title} {options}\n'
                            ':small_blue_diamond: r-invite\n'
                            ':white_small_square: r-latest\n'
                            ':small_blue_diamond: r-lenny\n'
                            ':white_small_square: r-suggest {Q or S or C or B} "{message}"', inline=True)
        emb.set_thumbnail(url='https://cdn.discordapp.com/emojis/385152309090451467.png?v=1')
        emb.set_footer(text='The Official Bot of PissRocket, inviting and using the Bot in other servers breaks the Term of Use.\nType r-help 2 for more commands!!')
        await bot.send_message(message.channel, embed=emb)
    if message.content.startswith('r-list 2'):
        emb = discord.Embed(title='MY COMMANDS:', description="Hey, check out my commands!", colour=0x3498db)
        emb.add_field(name='--------------------', value=':white_small_square: r-add {number1} {number2}\n'
                        ':small_blue_diamond: r-sub {number1} {number2}\n'
                        ':white_small_square: r-mul {number1} {number2}\n'
                        ':small_blue_diamond: r-div {number1} {number2}\n'
                        ':white_small_square: r-exp {number1} {number2}\n'
                        ':small_blue_diamond: r-nick "{name}"\n'
                        ':white_small_square: r-verify\n'
                        ':small_blue_diamond: r-register\n'
                        ':white_small_square: r-clear {number}\n'
                        ':small_blue_diamond: r-oof\n'
                        ':white_small_square: r-8ball {Question}\n', inline=True)
        emb.set_thumbnail(url='https://cdn.discordapp.com/emojis/385152309090451467.png?v=1')
        emb.set_footer(text='The Official Bot of PissRocket, inviting and using the Bot in other servers breaks the Term of Use.\nType r-help for more commands!!')
        await bot.send_message(message.channel, embed=emb)
    if message.content.startswith('r-latest'):
        emb = discord.Embed(title="LATEST UPDATES", description=":high_brightness: The Currently version is __" + version + "__ :high_brightness:\n\n"
                            ":small_blue_diamond: r-suggest {Q or S or C or __B__} \"{message}\"\n"
                            "New prefix: __B__ for Command Bugs\n"
                            "\n"
                            ":white_small_square: r-oof\n"
                            "Fun\n"
                            "\n"
                            ":small_blue_diamond: r-nick \"{name}\"\n"
                            "Change your name\n"
                            "\n"
                            ":white_small_square: r-list\n"
                            "The commands list finnaly working", colour=0x3498db)
        emb.set_thumbnail(url="https://cdn.discordapp.com/emojis/438035428386275340.png?v=1")
        await bot.send_message(message.channel, embed=emb)
    if message.content.startswith('r-bot'):
        em = discord.Embed(description= "```md\n"
                                "<⊐______⊐______⊏THE-ROCKETER-BOT⊐______⊏______⊏>\n"
                                "<                                                >\n"
                                "<▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒>\n"
                                "<                                                >\n"
                                "<▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒>\n"
                                "<˙˙˙˙˙˙˙˙˙The-Official-Bot-of-PissRocket.˙˙˙˙˙˙˙˙>\n"
                                "<˙˙˙˙˙˙˙˙The-currently-version-is-{}-!˙˙˙˙˙˙˙˙>\n"
                                "<                                                >\n"
                                "<▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒>\n"
                                "<                                                >\n"
                                "<▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒>\n"
                                "\n"
                                "         for the commands, type: \"r-list\"```".format(version), colour=0x3498db)
        await bot.send_message(message.channel, embed=em)
    await bot.process_commands(message) #IMPORTANT



    
    
        













token = os.environ.get('DISCORD_TOKEN')
bot.run(token)
