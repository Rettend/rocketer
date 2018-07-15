import discord, logging, json, asyncio, time, random, aiohttp, re, datetime, traceback, os, sys, math, asyncpg
from time import gmtime
from discord.ext import commands
from functions import edit_json,read_json
#-------------------DATA---------------------

version = "0.9.0"
owner = ["361534796830081024"]
bot = commands.Bot(command_prefix='r-', description=None)
bot.remove_command("help")
startup_extensions = ["YouTube"]
message = discord.Message
server = discord.Server
member = discord.Member
user = discord.User
Imox = ["365173881952272384"]
permissions = discord.Permissions
PRserver = "PissRocket"
underworking = ":warning: **Meh Boi, this command hasn't finished. Please wait until it's got.** :warning:"
"""timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())"""
#--------------------------------------------

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

"""@bot.command()
async def load(extension_name : str):
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))

@bot.command()
async def unload(extension_name : str):
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))"""

#--------------------------------------------

#----------------COMMANDS--------------------
@bot.command(pass_context=True)
async def selfrole(ctx, role : discord.Role=None):
    dj_role = discord.utils.get(ctx.message.server.roles, id="403594320634052610")
    radish_role = discord.utils.get(ctx.message.server.roles, id="380764242757943326")
    thonker_role =discord.utils.get(ctx.message.server.roles, id="381139610924875787")
    noe_role = discord.utils.get(ctx.message.server.roles, id="435090845960634378")
    selfroles = [dj_role, radish_role, thonker_role, noe_role]
    global color
    if selfrole is radish_role:
        color = 0xe74c3c
    elif selfrole is dj_role:
        color = 0x3498db
    elif selfrole is thonker_role:
        color = 0x206694
    elif selfrole is noe_role:
        color = 0x95a5a6
    if role is None:
        e = discord.Embed(title="Selfroles", description="The usage is `r-selfrole {selfrole}`," + f" the available Selfroles are:\n{dj_role.mention}\n{radish_role.mention}\n{thonker_role.mention}\n{noe_role.mention}", colour=0x3498db)
        e.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        e.set_footer(text=timer)
    elif role not in selfroles:
        e = discord.Embed(title="Selfroles", description=f"That role isnt a Selfrole! The available Selfroles are:\n{dj_role.mention}\n{radish_role.mention}\n{thonker_role.mention}\n{noe_role.mention}", colour=0x3498db)
        e.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        e.set_footer(text=timer)
    else:
        if role not in ctx.message.author.roles:
            await bot.add_roles(ctx.message.author, role)
            e = discord.Embed(title="Selfroles", description=f"Selfrole found!\nSelfrole ({role.mention}) added succesfuly!", colour=color)
            e.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            e.set_footer(text=timer)
        else:
            await bot.remove_roles(ctx.message.author, role)
            e = discord.Embed(title="Selfroles", description=f"Selfrole found!\nSelfrole ({role.mention}) removed succesfuly!", colour=color)
            e.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            e.set_footer(text=timer)
    await bot.say(embed=e)

@bot.command(pass_context=True)
async def fight(ctx, member : discord.Member=None):
    if member is None:
       await bot.reply("**The usage is `r-fight {member}` ty.**")
    else: 
        e = discord.Embed(title="Lets Fight!", description=f"{ctx.message.author} and {member.mention} ready?\n\n**Write the correct answers in the chat!**", colour=0xe74c3c)
        e.set_thumbnail(url="https://png.pngtree.com/element_pic/19/03/20/1656ed1ca75411c.jpg")
        msg = await bot.say(embed=e)
        question = ["thonk", "pissrocket", "taxi", "brawlhalla", "lin fei", "lapras", "imox", "rettend", "spork", "youtube", "pc", "no u"]
        question = random.choice(question)
        random.shuffle(question)
        em = discord.Embed(title="Lets Fight!", description=f'The word is "{word}"\n\nYou have 20 seconds to find the word.', colour=0x3498db)
        await bot.edit_message(embed=em)
        try:
            await bot.wait_for_message(content=question, timeout=20)
            await bot.say("**Congratulation! You won the game!**")
        except TimeoutError:
            await bot.say("**Time is over!**")
            
        

@bot.command(pass_context=True)
async def typing(ctx):
    await bot.say("**Im typing something** <:think:385152309090451467>")
    await bot.send_typing(ctx.message.channel)

@bot.command(pass_context=True)
async def whoami(ctx):
    LemonRoom = bot.get_channel(id="435081405899210754")
    msg = [" the Captain, aye aye! <:blobSalute:402168383556157442>", " Sir Lancelot", " gay :couple_mm:", " :regional_indicator_y: :regional_indicator_o: :regional_indicator_u:", " banned <:pepeBanhammer:423892407650877442>", "John Dick", " the Terminator!!", f" nothing, so go to {LemonRoom.mention} and farm lemons", " me", " a Bot", "... aaaaaaaaa!! A SPIDER!!!", " SuperMario", "... Its Raining Man!", " the Deathhh", " a dancing skeleton", " your mom's child", " ( ͡° ͜ʖ ͡°) <- this guy", " your mom and your sister is your dad", " a chicken", " a rabbit xd", " a fucking chicken", " _nothing_  hehe", ", wait, who you?", " a giant penis", " the devil >:)", " Donald Trump", " an Alien", " scared as hell... (ha ha)", " somebody, idk u Lol.", " a fat mouse.", " the Sup-sup-super Grandma!", " uhm, Should i know you??", ", ahhhhhh", " You."]
    smsg = random.choice(msg)
    colours = [0x11806a, 0x1abc9c, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e, 0xe67e22, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a]
    col = random.choice(colours)
    em = discord.Embed(title="WHO AM I?", description=f"**\n{ctx.message.author}, You are{smsg}**", colour=col)
    em.set_thumbnail(url=ctx.message.author.avatar_url)
    await bot.send_message(ctx.message.channel, embed=em)

@bot.command(pass_context=True)
async def slap(ctx, member : discord.Member=None, *, Reason=None):
    if member is None:
        await bot.reply("**The usage is `r-slap {member} {Reason}` ty.**")
    else:
        await bot.say(f"**{ctx.message.author} slaped {member.mention} for __{Reason}__**")

@bot.command(pass_context=True)
async def kill(ctx, user : discord.User=None):
    if user is None:
        await bot.reply("**The usage is `r-kill {member}` ty.**")
    else:
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
@commands.has_permissions(ban_members=True)
async def unban(ctx, user : discord.User=None, *, Reason=None):
    if user is None:
        await bot.reply("**The usage is `r-unban {member} {Reason}` ty.**")
    elif Reason is None:
        await bot.reply("**The usage is `r-slap {member} {Reason}` ty.**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**I won't let you moderate yourself xD**")
        else:
            banneds = await bot.get_bans(ctx.message.server)
            if user not in banneds:
                bot.say("**Plz mention a banned user!**")
            else:
                room = ctx.message.channel
                await bot.unban(ctx.message.server, user)
                LogRoom = bot.get_channel(id="401752340366884885")
                await bot.say(f"**{user.mention} got unbanned by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
                em = discord.Embed(title="╲⎝⧹𝓤𝓝𝓑𝓐𝓝⧸⎠╱", description=None, colour=0xe91e63)
                em.add_field(name="User", value=f"{user.mention}")
                em.add_field(name="Moderator", value=f"{ctx.message.author}")
                em.add_field(name="Reason", value=f"{Reason}")
                em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
                timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
                em.set_footer(text=timer)
                await bot.send_message(LogRoom, embed=em)
                Private = await bot.start_private_message(user)
                await bot.send_message(Private, f"**`Server: {PRserver}`\nHey! You got unbanned from {PRserver}, Ready to join back?\nhttps://discord.gg/Cf833k8**")

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, user : discord.User=None, Day : int=None, *, Reason=None):
    if user is None:
        await bot.reply("**The usage is `r-ban {member} {0 - 7 amount of days to delete his messages} {Reason}` ty.**")
    elif Reason is None:
        await bot.reply("**The usage is `r-ban {member} {0 - 7 amount of days to delete his messages} {Reason}` ty.**")
    elif Day is None:
        await bot.reply("**The usage is `r-ban {member} {0 - 7 amount of days to delete his messages} {Reason}` ty.**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**I won't let you moderate yourself xD**")
        else:
            room = ctx.message.channel
            await bot.ban(user, delete_message_days=Day)
            LogRoom = bot.get_channel(id="401752340366884885")
            await bot.say(f"**{user.mention} got banned by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
            em = discord.Embed(title="╲⎝⧹𝓑𝓐𝓝⧸⎠╱", description=None, colour=0xad1457)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value=f"{Reason}")
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/388945761611808769/453211671935057920/banned.gif")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)
            Private = await bot.start_private_message(user)
            await bot.send_message(Private, f"**`Server: {PRserver}`\nBAMM!! You got banned from {PRserver}, bai bai!**\n*Thor made hes best...*")

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user : discord.User=None, *, Reason=None):
    if user is None:
        await bot.reply("**The usage is `r-kick {member} {Reason}` ty.**")
    elif Reason is None:
        await bot.reply("**The usage is `r-kick {member} {Reason}` ty.**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**I won't let you moderate yourself xD**")
        else:
            room = ctx.message.channel
            await bot.kick(user)
            LogRoom = bot.get_channel(id="401752340366884885")
            await bot.say(f"**{user.mention} got Kicked by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
            em = discord.Embed(title="╲⎝⧹𝓚𝓘𝓒𝓚⧸⎠╱", description=None, colour=0xe74c3c)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value=f"{Reason}")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)
            Private = await bot.start_private_message(user)
            await bot.send_message(Private, f"**`Server: {PRserver}`\nHey! You got kicked from {PRserver}, bai bai!**")

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def mute(ctx, user : discord.User=None, duration : int=None, *, Reason=None):
    if user is None:
        await bot.reply("**The usage is `r-mute {member} {duration(in sec)} {Reason}` ty.**")
    elif Reason is None:
        await bot.reply("**The usage is `r-mute {member} {duration(in sec)} {Reason}` ty.**")
    elif duration is None:
        await bot.reply("**The usage is `r-mute {member} {duration(in sec)} {Reason}` ty.**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**I won't let you moderate yourself xD**")
        else:
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
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)
            Private = await bot.start_private_message(user)
            await bot.send_message(Private, f"**`Server: {PRserver}`\nRoses are red, violets are blue and {user.mention} is muted!**")
            await asyncio.sleep(duration)
            await bot.remove_roles(user, MutedRole)
            em = discord.Embed(title="╲⎝⧹𝓤𝓝𝓜𝓤𝓣𝓔⧸⎠╱", description=None, colour=0x1abc9c)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value="Time is up...")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)
            Private = await bot.start_private_message(user)
            await bot.send_message(Private, f"**`Server: {PRserver}`\nHey! You got unmuted, dont get too excited..**")

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, user : discord.User=None, *, Reason=None):
    if user is None:
        await bot.reply("**The usage is `r-unmute {member} {Reason}` ty.**")
    elif Reason is None:
        await bot.reply("**The usage is `r-unmute {member} {Reason}` ty.**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**I won't let you moderate yourself xD**")
        else:
            LogRoom = bot.get_channel(id="401752340366884885")
            room = ctx.message.channel
            MutedRole = discord.utils.get(ctx.message.server.roles, name="Muted")
            await bot.remove_roles(user, MutedRole)
            await bot.say(f"**{user.mention} got UnMuted (he he) by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
            em = discord.Embed(title="╲⎝⧹𝓤𝓝𝓜𝓤𝓣𝓔⧸⎠╱", description=None, colour=0x1abc9c)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value=f"{Reason}")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)
            Private = await bot.start_private_message(user)
            await bot.send_message(Private, f"**`Server: {PRserver}`\nHey! You got unmuted, dont get too excited..**")
        
@bot.command(pass_context=True)
async def ping(ctx):
    before = time.monotonic()
    embed = discord.Embed(description=":ping_pong: **...**", colour=0x3498db)
    msg = await bot.say(embed=embed)
    ping = (time.monotonic() - before) * 1000
    pinges = int(ping)
    if 999 > pinges > 400:
        mesg = "Thats a lot!"
    elif pinges > 1000:
        mesg = "Omg, really sloooooow...."
    elif 399 > pinges > 141:
        mesg = "Ahhh, not good!"
    elif pinges < 140:
        mesg = "Its Good, Boi ;)"
    em = discord.Embed(title=None, description=f":ping_pong: Seems like `{pinges}` MS\n{mesg}", colour=0x3498db)
    em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    em.set_footer(text=timer)
    await bot.edit_message(msg, embed=em)

@bot.command(pass_context=True)
@commands.has_permissions(manage_channels=True)
async def lock(ctx, duration : int=None, *, Reason=None):
    if Reason is None:
        await bot.reply("**The usage is `r-lock {duration (in sec)} {Reason}` ty.**")
    elif duration is None:
        await bot.reply("**The usage is `r-lock {duration (in sec)} {Reason}` ty.**")
    else:
        Registered = discord.utils.get(ctx.message.server.roles, name="Registered")
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        await bot.edit_channel_permissions(ctx.message.channel, Registered, overwrite)
        await bot.send_message(ctx.message.channel, f"**{ctx.message.channel.mention} is now locked for __{Reason}__**")
        LogRoom = bot.get_channel(id="401752340366884885")
        em = discord.Embed(title="╲⎝⧹𝓛𝓞𝓒𝓚⧸⎠╱", description=None, colour=0x1f8b4c)
        em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.add_field(name="Duration", value=f"{duration} sec")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(LogRoom, embed=em)
        await asyncio.sleep(duration)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = True
        await bot.edit_channel_permissions(ctx.message.channel, Registered, overwrite)
        await bot.send_message(ctx.message.channel, f"**{ctx.message.channel.mention} is now unlocked for __{Reason}__**")
        LogRoom = bot.get_channel(id="401752340366884885")
        em = discord.Embed(title="╲⎝⧹𝓤𝓝𝓛𝓞𝓒𝓚⧸⎠╱", description=None, colour=0x2ecc71)
        em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(LogRoom, embed=em)

@bot.command(pass_context=True)
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, *, Reason=None):
    if Reason is None:
        await bot.reply("**The usage is `r-unlock {Reason}` ty.**")
    else:
        Registered = discord.utils.get(ctx.message.server.roles, name="Registered")
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = True
        await bot.edit_channel_permissions(ctx.message.channel, Registered, overwrite)
        await bot.send_message(ctx.message.channel, f"**{ctx.message.channel.mention} is now unlocked for __{Reason}__**")
        LogRoom = bot.get_channel(id="401752340366884885")
        em = discord.Embed(title="╲⎝⧹𝓤𝓝𝓛𝓞𝓒𝓚⧸⎠╱", description=None, colour=0x2ecc71)
        em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(LogRoom, embed=em)
    
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, number : int=None):
    if number is None:
        await bot.reply("**The usage is `r-clear {number of messages to delete}` ty.**")
    else:
        number += 1
        deleted = await bot.purge_from(ctx.message.channel, limit=number)
        num = number - 1
        LogRoom = bot.get_channel(id="401752340366884885")
        em = discord.Embed(title=None, description=f'{ctx.message.author} deleted __{num}__ messages', colour=0x3498db)
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        msg = await bot.send_message(ctx.message.channel, embed=em)
        await bot.send_message(LogRoom, embed=em)
        await asyncio.sleep(4)
        await bot.delete_message(msg)

@bot.command(pass_context=True)
async def roll(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**The usage is `r-roll {number} {number}` ty.**")
    elif y is None:
        await bot.reply("**The usage is `r-roll {number} {number}` ty.**")
    else:
        msg = random.randint(x, y)
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**Oh, my choose: {msg}**")

@bot.command(pass_context=True)
async def sub(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**The usage is `r-sub {number} {number}` ty.**")
    elif y is None:
        await bot.reply("**The usage is `r-sub {number} {number}` ty.**")
    else:
        msg = x - y
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**Oh, the result: {msg}**")
    
@bot.command(pass_context=True)
async def mul(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**The usage is `r-mul {number} {number}` ty.**")
    elif y is None:
        await bot.reply("**The usage is `r-mul {number} {number}` ty.**")
    else:
        msg = x * y
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**Oh, the result: {msg}**")
    
@bot.command(pass_context=True)
async def div(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**The usage is `r-div {number} {number}` ty.**")
    elif y is None:
        await bot.reply("**The usage is `r-div {number} {number}` ty.**")
    else:
        msg = x / y
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**Oh, the result: {msg}**")
    
@bot.command(pass_context=True)
async def exp(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**The usage is `r-exp {number} {number}` ty.**")
    elif y is None:
        await bot.reply("**The usage is `r-exp {number} {number}` ty.**")
    else:
        msg = x ** y
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**Oh, the result: {msg}**")
    
@bot.command(pass_context=True)
async def add(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**The usage is `r-add {number} {number}` ty.**")
    elif y is None:
        await bot.reply("**The usage is `r-add {number} {number}` ty.**")
    else:
        msg = x + y
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**Oh, the result: {msg}**")
    
@bot.command()
async def game(*, play=None):
    if play is None:
        await bot.reply("**The usage is `r-game {Something to set as a game}` ty.**")
    else:
        await bot.change_presence(game=discord.Game(name=play))
        em = discord.Embed(title="Game Status", description=f"Game status changed to __{play}__!", colour=0x3498db)
        await bot.say(embed=em)

@bot.command(pass_context=True)
async def nick(ctx, *, name=None):
    if name is None:
        await bot.reply("**The usage is `r-name {Something to set as your name}` ty.**")
    else:
        await bot.change_nickname(ctx.message.author, name)
        em = discord.Embed(title="Nickname", description=f"{ctx.message.author}'s nick set to __{name}__!", colour=0x3498db)
        await bot.say(embed=em)
    
@bot.command(pass_context=True)
async def suggest(ctx, pref=None, *, text=None):
    if pref is None:
        await bot.reply("**The usage is `r-suggest {prefix (Q, S, C, B)} {text}` ty.**")
    elif text is None:
        await bot.reply("**The usage is `r-suggest {prefix (Q, S, C, B)} {text}` ty.**")
    else:
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
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
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
async def poll(ctx, options: str=None, *, question=None):
    if options is None:
        await bot.reply("**The usage is `r-poll {options (2-10)} {Question or Suggestion}` ty.**")
    elif question is None:
        await bot.reply("**The usage is `r-poll {options (2-10)} {Question or Suggestion}` ty.**")
    else:
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

@bot.listen()
async def on_member_join(member):
    botserver = bot.get_server(id="370269066864361472")
    membersroom = bot.get_channel(id="460397271788421120")
    await bot.edit_channel(membersroom, name=f"👥Members: {len(botserver.members)}")
    room = bot.get_channel(id="370269066864361476")
    em = discord.Embed(title=f"__{member.name}__ Joined!", description=f"**Welcome {member.mention}, have a great time here! Chat, Search for playing-mates, farm lemons :lemon:, or just listen to music ;)**", colour=0x3498db)
    em.set_thumbnail(url="https://cdn.discordapp.com/emojis/391322023739129856.png?v=1")
    await bot.send_message(room, embed=em)

@bot.event
async def on_server_role_create(role):
    botserver = bot.get_server(id="370269066864361472")
    rolesroom = bot.get_channel(id="460457033129263145")
    await bot.edit_channel(rolesroom, name=f"🌵Roles: {len(botserver.roles)}")  

@bot.event
async def on_server_role_delete(role):
    botserver = bot.get_server(id="370269066864361472")
    rolesroom = bot.get_channel(id="460457033129263145")
    await bot.edit_channel(rolesroom, name=f"🌵Roles: {len(botserver.roles)}")  

@bot.event
async def on_channel_create(channel):
    botserver = bot.get_server(id="370269066864361472")
    channelsroom = bot.get_channel(id="460397552379101184")
    await bot.edit_channel(channelsroom, name=f"🌐Channels: {len(botserver.channels)}")

@bot.event
async def on_channel_delete(channel):
    botserver = bot.get_server(id="370269066864361472")
    channelsroom = bot.get_channel(id="460397552379101184")
    await bot.edit_channel(channelsroom, name=f"🌐Channels: {len(botserver.channels)}")
    
@bot.listen()
async def on_member_remove(member):
    botserver = bot.get_server(id="370269066864361472")
    membersroom = bot.get_channel(id="460397271788421120")
    await bot.edit_channel(membersroom, name=f"👥Members: {len(botserver.members)}")
    room2 = bot.get_channel(id="453598661306482688")
    await bot.send_message(room2, f"**{member} left without saying anything...** <:thonkSad:421004865049985035>")

@bot.command(pass_context=True)
async def say(ctx, *, words=None):
    if words is None:
        await bot.reply("**The usage is `r-say {Something}` ty.**")
    else:
        await bot.say(f"**{words}**")
#-----------------------------------------------

reaction_roles=read_json('reaction_roles')
active_messages=[]

@bot.command(pass_context=True)
async def add_er(ctx, emoji : str=None, role : discord.Role=None):
    if ctx.message.author.id not in owner:
        await bot.say('**I only let my owner use this command...**')
    else:
        if (emoji or role) is None:
            await bot.say('**Missing arguments `Emoji` or `@Role`**')
            return
        bot_member=discord.utils.get(ctx.message.server.members, id=bot.user.id)
        if role.position >= bot_member.top_role.position:
            await bot.say("**Can't assign that role, bot role needs to be raised.**")
            return
        reaction_roles[emoji] = role.id
        edit_json('reaction_roles', reaction_roles)
        await bot.say('**{} will assign members to {}**'.format(emoji, role.mention))

@bot.command(pass_context=True)
async def remove_er(ctx, emoji):
    if ctx.message.author.id not in owner:
        await bot.say('**I only let my owner use this command...**')
    else:
        role = discord.utils.get(ctx.message.server.roles, id=reaction_roles[emoji])
        await bot.say('**{} will no longer assign {}**'.format(emoji, role.mention))
        del reaction_roles[emoji]
        edit_json('reaction_roles', reaction_roles)

@bot.command(pass_context=True)
async def er(ctx):
    if ctx.message.author.id not in owner:
        await bot.say('**I only let my owner use this command...**')
    else:
        if len(reaction_roles) == 0:
            await bot.say("**No emojis have been assigned to roles**")
            return
        global active_messages
        server = ctx.message.server
        message = ''
        for emoji, role in reaction_roles.items():
            role = discord.utils.get(server.roles, id=role)
            message += '{} will assign {}\n'.format(emoji, role.mention)
        msg = await bot.say(f"**__Click on the Reactions to get Roles!__\n{message}**")
        for emoji in reaction_roles.keys():
            await bot.add_reaction(msg, emoji)
        active_messages.append(msg.id)

@bot.event
async def on_reaction_add(reaction, user):
    if reaction.message.id in active_messages and reaction.emoji in reaction_roles and user != bot.user:
        role = discord.utils.get(reaction.message.server.roles, id=reaction_roles[reaction.emoji])
        for r_id in reaction_roles.values():
            e_role = discord.utils.get(reaction.message.server.roles, id=r_id)
        await bot.add_roles(user, role)

@bot.event
async def on_reaction_remove(reaction, user):
    if reaction.message.id in active_messages and reaction.emoji in reaction_roles and user != bot.user:
        role = discord.utils.get(reaction.message.server.roles, id=reaction_roles[reaction.emoji])
        for r_id in reaction_roles.values():
            e_role = discord.utils.get(reaction.message.server.roles, id=r_id)
        await bot.remove_roles(user, role)
#-----------------------------------------------

@bot.event
async def on_message(message):
    if message.content.startswith("r-time"):
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        await bot.send_message(message.channel, f"**{message.author.mention}, the time is __{timer}__**")
    if message.content.startswith("r-mod"):
        em = discord.Embed(title="MODERATION COMMANDS", description=None, colour=0x3498db)
        em.add_field(name="Admin commands", value=":small_blue_diamond: r-ban {member} {0 - 7 amount of days to delete his messages} {Reason}\n"
                     ":black_small_square: Kicks the user and removes his messages for the given days, the user can't rejoin, until he gots unbanned\n"
                     "\n"
                     ":small_orange_diamond: r-unban {member} \"{Reason}\"\n"
                     ":black_small_square: UnBans the Banned user, the user now can rejoin by instant-invite links\n\n\n")
        em.add_field(name="Mod commands", value=":small_blue_diamond: r-kick {member} {Reason}\n"
                     ":black_small_square: Kicks the user from the server, the user can rejoin by instant-invite links\n"
                     "\n"
                     ":small_orange_diamond: r-mute {member} {duration(in sec)} {Reason}\n"
                     ":black_small_square: Mutes the user, this user can't send messages for the given duration, if the _time is up,_ he will auto get unmuted\n"
                     "\n"
                     ":small_blue_diamond: r-unmute {member} {Reason}\n"
                     ":black_small_square: UnMutes the Muted user, this user now allowed to send messages\n"
                     "\n"
                     ":small_orange_diamond: r-lock {Reason}\n"
                     ":black_small_square: Locks down the currently channel, only Admins can send messages until an unlock\n"
                     "\n"
                     ":small_blue_diamond: r-unlock {Reason}\n"
                     ":black_small_square: Unlocks the currently locked channel, now everyone can send messages there\n"
                     "\n"
                     ":small_orange_diamond: r-clear {number of messages to delete}\n"
                     ":black_small_square: Deletes a specific amount of messages")
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
    if message.content.upper().startswith('R-AMIOWNER?'):
        if message.author.id in owner:
            await bot.send_message(message.channel, ':white_check_mark: **You are the Owner, Hey Rettend :D**')
        else:
            await bot.send_message(message.channel, ':negative_squared_cross_mark: **You aren\'t the Owner.**')
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
        emb.add_field(name='--------------------', value=':small_blue_diamond: r-typing\n'
                            ':white_small_square: r-whoami\n'
                            ':small_blue_diamond: r-slap\n'
                            ':white_small_square: r-kill\n'
                            ':small_blue_diamond: r-ping\n'
                            ':white_small_square: r-roll\n'
                            ':small_blue_diamond: r-add\n'
                            ':white_small_square: r-suv\n'
                            ':small_blue_diamond: r-mul\n'
                            ':white_small_square: r-div\n'
                            ':small_blue_diamond: r-exp\n'
                            ':white_small_square: r-game\n'
                            ':small_blue_diamond: r-nick\n'
                            ':white_small_square: r-suggest\n'
                            ':small_blue_diamond: r-poll\n'
                            ':white_small_square: r-say\n', inline=False)
        emb.set_thumbnail(url='https://cdn.discordapp.com/emojis/385152309090451467.png?v=1')
        emb.set_footer(text='The Official Bot of PissRocket, inviting and using the Bot in other servers breaks the Term of Use.\nType r-help 2 for more commands!!')
        await bot.send_message(message.channel, embed=emb)
    if message.content.startswith('r-list 2'):
        emb = discord.Embed(title='MY COMMANDS:', description="Hey, check out my commands!", colour=0x3498db)
        emb.add_field(name='--------------------', value=':small_blue_diamond: r-time\n'
                            ':white_small_square: r-mod\n'
                            ':small_blue_diamond: r-help\n'
                            ':white_small_square: r-AmIOwner?\n'
                            ':small_blue_diamond: r-bigdigits\n'
                            ':white_small_square: r-8ball\n'
                            ':small_blue_diamond: r-lenny\n'
                            ':white_small_square: r-oof\n'
                            ':small_blue_diamond: r-leavepls\n'
                            ':white_small_square: r-invite\n'
                            ':small_blue_diamond: r-list\n'
                            ':white_small_square: r-latest\n'
                            ':small_blue_diamond: r-bot\n', inline=False)
        emb.set_thumbnail(url='https://cdn.discordapp.com/emojis/385152309090451467.png?v=1')
        emb.set_footer(text='The Official Bot of PissRocket, inviting and using the Bot in other servers breaks the Term of Use.\nType r-help for more commands!!')
        await bot.send_message(message.channel, embed=emb)
    if message.content.startswith('r-latest'):
        emb = discord.Embed(title="LATEST UPDATES", description=":high_brightness: The Currently version is __" + version + "__ :high_brightness:\n\n"
                            ":white_small_square: r-typing\n"
                            "Sends a weird typing\n"
                            "\n"
                            ":small_blue_diamond: r-whoami\n"
                            "Who am I?\n"
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
