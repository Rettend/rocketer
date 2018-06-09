import discord, logging, json, asyncio, time, random, aiohttp, re, datetime, traceback, os, sys, math
from discord.ext import commands

#-------------------DATA---------------------
version = "0.8.6"
owner = ["361534796830081024"]
bot = commands.Bot(command_prefix='r-', description=None)
bot.remove_command("help")
message = discord.Message
server = discord.Server
member = discord.Member
user = discord.User
Imox = ["365173881952272384"]
permissions = discord.Permissions
underworking = ":warning: **Meh Boi, this command hasn't finished. Please wait until it's got.** :warning:"
#--------------------------------------------


#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-ID-MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

#-----------------ADMIN'S ID-----------------\|/-ban, -lock, -unlock
"""               Imox                 Rettend               Lapras               Legends                Spork                  Hman"""
Admins = ["365173881952272384", "361534796830081024", "323851553662566401", "386400236916047872", "375991973246533642", "392039138179940362"]

#--------------MODERATOR'S ID----------------\|/-mute, -kick, -unmute
"""                 PReiZ                 sunrab"""
Moderators = ["407382812518383627", "366607123771293696"]

#--------------------------------------------

#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM


#-----------------SETUP----------------------
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name='Restarted 🤘'))

class NoPermError(Exception):
    pass
#--------------------------------------------

#----------------COMMANDS--------------------
@bot.command(pass_context=True)
async def whoami(ctx):
    msg = [" a chicken", " a rabbit xd", " a fucking chicken", " _nothing_  hehe", ", wait, who you?", " a giant penis", " the devil >:)", " Donald Trump", " an Alien", " scared as hell... (ha ha)", " somebody, idk u Lol.", " a fat mouse.", " the Sup-sup-super Grandma!", " uhm, Should i know you??", ", ahhhhhh", " You."]
    smsg = random.choice(msg)
    colours = [0x11806a, 0x1abc9c, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e, 0xe67e22, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a]
    col = random.choice(colours)
    em = discord.Embed(title="WHO AM I?", description=f"**\n{ctx.message.author}, You are{smsg}**", colour=col)
    em.set_thumbnail(url=ctx.message.author.avatar_url)
    await bot.send_message(ctx.message.channel, embed=em)

@bot.command(pass_context=True)
async def slap(ctx, member : discord.Member, Reason):
    await bot.say(f"**{ctx.message.author} slaped {member.mention} for {Reason}**")

@bot.command(pass_context=True)
async def kill(ctx, user : discord.User):
    life = ["Yes", "Yes2" "No", "No2"]
    yourlife = random.choice(life)
    if yourlife == "Yes":
        await bot.say(f"**{user.mention} got killed by {ctx.message.author}** <:rip:449949312508493834>")
    elif yourlife == "Yes2":
        await bot.say(f"**{ctx.message.author} shoot down {user.mention}**")
    elif yourlife == "No":
        await bot.say(f"**Ha ha {ctx.message.author}, really funny xd**")
    else:
        await bot.say(f"**No u, {ctx.message.author}**")

@bot.command(pass_context=True)
async def unban(ctx, user : discord.User, Reason):
    if ctx.message.author.id in Admins:
        room = ctx.message.channel
        await bot.unban(ctx.message.server, user)
        LogRoom = bot.get_channel(id="401752340366884885")
        await bot.say(f"**{user.mention} got unbanned by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
        em = discord.Embed(title="╲⎝⧹𝓤𝓝𝓑𝓐𝓝⧸⎠╱", description=None, colour=0xe91e63)
        em.add_field(name="User", value=f"{user.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        await bot.send_message(LogRoom, embed=em)
    else:
        await bot.send_message(ctx.message.channel, f'*Boi, you cant use this command...*')
        raise NoPermError

@bot.command(pass_context=True)
async def ban(ctx, user : discord.User, Day : int, Reason):
    if ctx.message.author.id in Admins:
        room = ctx.message.channel
        await bot.ban(user, delete_message_days=Day)
        LogRoom = bot.get_channel(id="401752340366884885")
        await bot.say(f"**{user.mention} got banned by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
        em = discord.Embed(title="╲⎝⧹𝓑𝓐𝓝⧸⎠╱", description=None, colour=0xad1457)
        em.add_field(name="User", value=f"{user.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/388945761611808769/453211671935057920/banned.gif")
        await bot.send_message(LogRoom, embed=em)
    else:
        await bot.send_message(ctx.message.channel, f'*Boi, you cant use this command...*')
        raise NoPermError

@bot.command(pass_context=True)
async def kick(ctx, user : discord.User, Reason):
    if ctx.message.author.id in Moderators or Admins:
        room = ctx.message.channel
        await bot.kick(user)
        LogRoom = bot.get_channel(id="401752340366884885")
        await bot.say(f"**{user.mention} got Kicked by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
        em = discord.Embed(title="╲⎝⧹𝓚𝓘𝓒𝓚⧸⎠╱", description=None, colour=0xe74c3c)
        em.add_field(name="User", value=f"{user.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        await bot.send_message(LogRoom, embed=em)
    else:
        await bot.send_message(ctx.message.channel, f'*Boi, you cant use this command...*')
        raise NoPermError

@bot.command(pass_context=True)
async def mute(ctx, user : discord.User, duration : int, Reason):
    if ctx.message.author.id in Moderators or Admins:
        LogRoom = bot.get_channel(id="401752340366884885")
        room = ctx.message.channel
        MutedRole = discord.utils.get(ctx.message.server.roles, name="Muted")
        await bot.add_roles(user, MutedRole)
        await bot.say(f"**{user.mention} got Muted (for {duration} sec) by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
        em = discord.Embed(title="╲⎝⧹𝓜𝓤𝓣𝓔⧸⎠╱", description=None, colour=0x11806a)
        em.add_field(name="User", value=f"{user.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.add_field(name="Duration", value=f"{duration} sec")
        await bot.send_message(LogRoom, embed=em)
        await asyncio.sleep(duration)
        await bot.remove_roles(user, MutedRole)
        em = discord.Embed(title="╲⎝⧹𝓤𝓝𝓜𝓤𝓣𝓔⧸⎠╱", description=None, colour=0x1abc9c)
        em.add_field(name="User", value=f"{user.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value="Time is up...")
        await bot.send_message(LogRoom, embed=em)
    else:
        await bot.send_message(ctx.message.channel, f'*Boi, you cant use this command...*')
        raise NoPermError

@bot.command(pass_context=True)
async def unmute(ctx, user : discord.User, Reason):
    if ctx.message.author.id in Moderators or Admins:
        LogRoom = bot.get_channel(id="401752340366884885")
        room = ctx.message.channel
        MutedRole = discord.utils.get(ctx.message.server.roles, name="Muted")
        await bot.remove_roles(user, MutedRole)
        await bot.say(f"**{user.mention} got UnMuted (he he) by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
        em = discord.Embed(title="╲⎝⧹𝓤𝓝𝓜𝓤𝓣𝓔⧸⎠╱", description=None, colour=0x1abc9c)
        em.add_field(name="User", value=f"{user.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        await bot.send_message(LogRoom, embed=em)
    else:
        await bot.send_message(ctx.message.channel, f'*Boi, you cant use this command...*')
        raise NoPermError
        
@bot.command(pass_context=True)
async def ping(ctx):
    before = time.monotonic()
    msg = await bot.say(":ping_pong: **...**")
    ping = (time.monotonic() - before) * 1000
    pinges = int(ping)
    if 999 > pinges > 400:
        mesg = "Thats a lot!"
    elif pinges > 1000:
        mesg = "Omg, really sloooooow...."
    elif 399 > pinges > 101:
        mesg = "Ahhh, not good!"
    elif pinges < 100:
        mesg = "Its Good, Boi ;)"
    await bot.edit_message(msg, f":ping_pong: **Seems like `{pinges}` MS\n{mesg}**")

@bot.command(pass_context=True)
async def clear(ctx, number : int):
    if ctx.message.author.id in Moderators or Admins:
        number += 1
        deleted = await bot.purge_from(ctx.message.channel, limit=number)
        num = number - 1
        msg = await bot.send_message(ctx.message.channel, f'**{ctx.message.author} deleted __{num}__ messages**')
        await asyncio.sleep(4)
        await bot.delete_message(msg)
    else:
        await bot.send_message(ctx.message.channel, f'*Boi, you cant use this command...*')
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
        else:
            bot.say("**Please use a valid prefix! The available prefixes: __Q__, __S__, __C__, __B__**")
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
    room2 = bot.get_channel(id="370269066864361476")
    room = bot.get_channel(id="381774233199443968")
    is_verified = False
    for role in member.roles:
        if role.name == "Registered":
            is_verified = True
            break
        if is_verified == False:
            em = discord.Embed(title=f"__{member.name}__ Joined!", description=None, colour=0x3498db)
            em.add_field(name=None, value=f"\n**Welcome __{member.mention}__,**\n\nI will show you around, First, to __get permissions for all channels__, you need to type `r-verify` and __answer all of the questions!__\nThan type `r-register`!\n\n**__IMPORTANT__: typing `r-register` without answering the questions, will unregister you!**")
            em.set_thumbnail(url="https://cdn.discordapp.com/emojis/391322023739129856.png?v=1")
            await bot.send_message(room, embed=em)
    await bot.send_message(room2, f"**Welcome {member.mention}, have a great time here! btw go to {room.mention} and verify yourself ;)**")

@bot.listen()
async def on_member_remove(member):
    room2 = bot.get_channel(id="453598661306482688")
    await bot.send_message(room2, f"**{member} left without saying anything...** <:thonkSad:421004865049985035>")

@bot.event
async def on_message(message):
    if message.content.startswith("r-mod"):
        em = discord.Embed(title="MODERATION COMMANDS", description=None, colour=0x3498db)
        em.add_field(name="Admin commands", value=":small_blue_diamond: r-ban {member} {0 - 7 amount of days to delete his messages} \"{Reason}\"\n"
                     ":black_small_square: Kicks the user and removes his messages for the given days, the user can't rejoin, until he gots unbanned\n"
                     "\n"
                     ":small_orange_diamond: r-unban {member} \"{Reason}\"\n"
                     ":black_small_square: UnBans the Banned user, the user now can rejoin by instant-invite links\n\n\n")
        em.add_field(name="Mod commands", value=":small_blue_diamond: r-kick {member} \"{Reason}\"\n"
                     ":black_small_square: Kicks the user from the server, the user can rejoin by instant-invite links\n"
                     "\n"
                     ":small_orange_diamond: r-mute {member} {duration(in sec)} \"{Reason}\"\n"
                     ":black_small_square: Mutes the user, this user can't send messages for the given duration, if the _time is up,_ he will auto get unmuted\n"
                     "\n"
                     ":small_blue_diamond: r-unmute {member} \"{Reason}\"\n"
                     ":black_small_square: UnMutes the Muted user, this user now allowed to send messages\n"
                     "\n"
                     ":small_orange_diamond: r-lock\n"
                     ":black_small_square: Locks down the currently channel, only Admins can send messages until an unlock\n"
                     "\n"
                     ":small_blue_diamond: r-unlock\n"
                     ":black_small_square: Unlocks the currently locked channel, now everyone can send messages there")
        await bot.send_message(message.channel, embed=em)
    if message.content.startswith("r-help"):
        Rettend = discord.utils.get(message.server.members, id="361534796830081024")
        em = discord.Embed(title="HELP", description="__Hey! Dont get Scared, Ask for help!__\n"
                           "\n"
                           ":small_blue_diamond: Try `r-mod` to get the moderator commands, but you need to be Staff to use them!\n"
                           ":white_small_square: Use the `r-list` command to get all of the commands!\n"
                           ":small_blue_diamond: Type `r-latest` to get the latest updates!\n"
                           f":white_small_square: If you have any questions, ask it to {Rettend.mention}", colour=0x3498db)
        em.set_thumbnail(url="https://cdn.discordapp.com/emojis/430347128100093962.gif?v=1")
        await bot.send_message(message.channel, embed=em)
    if message.content.startswith('r-lock'):
        if message.author.id in Admins:
            room = message.channel
            Registered = discord.utils.get(message.server.roles, name="Registered")
            overwrite = discord.PermissionOverwrite()
            overwrite.send_messages = False
            await bot.edit_channel_permissions(room, Registered, overwrite)
            await bot.send_message(room, f"**{room.mention} is now locked! Ha ha**")
        else:
            await bot.send_message(ctx.message.channel, f'*Boi, you cant use this command...*')
            raise NoPermError
    if message.content.startswith('r-unlock'):
        if message.author.id in Admins:
            room = message.channel
            Registered = discord.utils.get(message.server.roles, name="Registered")
            overwrite = discord.PermissionOverwrite()
            overwrite.send_messages = True
            await bot.edit_channel_permissions(room, Registered, overwrite)
            await bot.send_message(room, f"**{room.mention} is now unlocked, feel free to chat!**")
        else:
            await bot.send_message(ctx.message.channel, f'*Boi, you cant use this command...*')
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
                        ':white_small_square: r-8ball {Question}\n'
                        ':small_blue_diamond: r-help\n'
                        ':white_small_square: r-kill {user}\n'
                        ':small_blue_diamond: r-slap {user} "{Reason}"'
                        ':white_small_square: r-whoami', inline=True)
        emb.set_thumbnail(url='https://cdn.discordapp.com/emojis/385152309090451467.png?v=1')
        emb.set_footer(text='The Official Bot of PissRocket, inviting and using the Bot in other servers breaks the Term of Use.\nType r-help for more commands!!')
        await bot.send_message(message.channel, embed=emb)
    if message.content.startswith('r-latest'):
        emb = discord.Embed(title="LATEST UPDATES", description=":high_brightness: The Currently version is __" + version + "__ :high_brightness:\n\n"
                            ":small_blue_diamond: Moderator Commands are here!!\n"
                            "Type `r-mod` for the commands\n"
                            "\n"
                            ":white_small_square: r-kill {user}\n"
                            "Dont ab00se.\n"
                            "\n"
                            ":small_blue_diamond: r-whoami\n"
                            "Shows your ping! Finally its working!!\n"
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

# define database
conn = bot.connect("my_database.db")
cursor = conn.cursor()
# get stored object from database
sql = "SELECT * FROM my_table WHERE field_1=?"
cursor.execute(sql, [(value_1)])
data = cursor.fetchall()
# if object does not exist, create it
if len(data) == 0:
    sql = "INSERT INTO my_table VALUES (?, ?)"
    cursor.execute(sql, [(value_1), (value_2)])
# if stored object exist and we need update it
elif ...:
    sql = "UPDATE my_table SET field_2 = ? WHERE field_1 = ?"
    cursor.execute(sql, [(value_2), (value_1)])
else:
    # get data from first object
    value_of_field_1 = data[0][0]
    # get data from third object
    value_of_field_2 = data[2][1]
# close database connection
conn.commit()
conn.close()

    
    
        













token = os.environ.get('DISCORD_TOKEN')
bot.run(token)
