import discord
from mcstatus import MinecraftServer
from discord.ext import tasks

client = discord.Client ( intents = discord.Intents.all () )
server = MinecraftServer.lookup ( "play.pixel-heim.com" )


@client.event
async def on_ready():
    print ( 'We have logged in as {0.user}'.format ( client ) )

    await client.change_presence (
        activity = discord.Activity ( type = discord.ActivityType.playing, name = "on play.pixel-heim.com" ) )


@client.event
async def on_member_join(member):
    channel = await client.fetch_channel ( 834516102649741349 )
    print ( "                {0} joined the server".format ( member.name ) )
    welcome = discord.Embed (
        title = '**We hope to meet you at play.pixel-heim.com**',
        description = 'Please check <#834687920211755049> and <#836172359446298674> before checking out the other channels to meet other players!',
        colour = discord.Colour.from_rgb ( 255, 0, 0 )
    )
    welcome.set_image ( url = 'https://i.imgur.com/AqxpDD2.png' )
    await channel.send ( "**Welcome to PixelHeim {0} !**".format ( member.mention ), embed = welcome )


@client.event
async def on_message(message):
    if message.channel.id == 848894973876764672:
        await message.add_reaction ( "a:checkmark:848898022921732166" )
        await message.add_reaction ( "a:cross:848897550610333737" )

    if ".ticket" in message.content:
        print ( ".ticket command was used by {0}".format ( message.author.name ) )
        await message.add_reaction ( "a:checkmark:848898022921732166" )
        ticket = discord.Embed (
            title = '**How to File a Ticket.**',
            description = 'Go to <#834520977694130226> and click on the :tickets: emoji.',
            colour = discord.Colour.from_rgb ( 255, 0, 0 )
        )
        ticket.set_image ( url = 'https://i.imgur.com/2nR55qk.png' )
        ticket.set_thumbnail ( url = "https://i.imgur.com/oPdS1DB.png" )
        await message.channel.send ( embed = ticket )

    if ".report" in message.content:
        print ( ".report command was used by {0}".format ( message.author.name ) )
        await message.add_reaction ( "a:checkmark:848898022921732166" )
        report = discord.Embed (
            title = '**Format For Reporting A Player:-**',
            description = 'Your Name:\nName of the player your reporting:\nReason:\nProof:',
            colour = discord.Colour.from_rgb ( 255, 0, 0 )
        )
        report.set_thumbnail ( url = "https://i.imgur.com/oPdS1DB.png" )
        await message.channel.send ( embed = report )

    if ".appeal" in message.content:
        print ( ".appeal command was used by {0}".format ( message.author.name ) )
        await message.add_reaction ( "a:checkmark:848898022921732166" )
        appeal = discord.Embed (
            title = '**Hello Pixels please follow the following format to appeal for your ban**',
            description = '1. Your Name in-game:\n2. Name of the staff who banned you:\n3.Reason for ban:\n4.Is your ban reasonable:\n5.How long is your ban:\n6.Why should we unban you:',
            colour = discord.Colour.from_rgb ( 255, 0, 0 )
        )
        appeal.set_thumbnail ( url = "https://i.imgur.com/oPdS1DB.png" )
        await message.channel.send ( embed = appeal )

    if ".format" in message.content:
        print ( ".format command was used by {0}".format ( message.author.name ) )
        await message.add_reaction ( "a:checkmark:848898022921732166" )
        format = discord.Embed (
            title = '**Hello Pixels our staff will be here soon to help you, In the meantime please follow the format and describe your concern:**',
            description = 'Your In Game Name :\nConcern :\nProof :',
            colour = discord.Colour.from_rgb ( 255, 0, 0 )
        )
        format.set_thumbnail ( url = "https://i.imgur.com/oPdS1DB.png" )
        await message.channel.send ( embed = format )

    if ".ip" in message.content:
        print ( ".ip command was used by {0}".format ( message.author.name ) )
        await message.add_reaction ( "a:checkmark:848898022921732166" )
        ip = discord.Embed (
            title = '**IP**',
            description = '**play.pixel-heim.com**',
            colour = discord.Colour.from_rgb ( 255, 0, 0 )
        )
        ip.set_thumbnail ( url = "https://i.imgur.com/oPdS1DB.png" )
        await message.channel.send ( embed = ip )

    if ".players" in message.content:

        try:
            temp1 = 1
            status = server.status ()
        except:
            await message.channel.send ( ":octagonal_sign: PixelHeim Server Is Offline" )
            print ( ".players command was used by {0} (Server was offline)".format ( message.author.name ) )
            temp1 = 0
        if temp1 == 1:
            await message.channel.send (
                "There are {0} Players currently playing on PixelHeim".format ( status.players.online ) )
            print ( ".players command was used by {0} ({1} Players were online)".format ( message.author.name,
                                                                                          status.players.online ) )

    if ".status" in message.content:

        try:
            temp2 = 1
            status = server.status ()
        except:
            await message.channel.send ( ":octagonal_sign: PixelHeim Server Is Offline" )
            print ( ".status was used by {0} (Server was offline)".format ( message.author.name ) )
            temp2 = 0
        if temp2 == 1:
            await message.channel.send ( ":white_check_mark: PixelHeim Server Is Online" )
            print ( ".status command was used by {0} (Server was online)".format ( message.author.name ) )


@tasks.loop ( minutes = 5 )
async def send():
    stagechannel = client.get_channel ( 841387979427545148 )

    try:
        temp3 = 1
        status = server.status ()
    except:
        print ( "Server is offline postponed channel update" )
        await stagechannel.edit ( name = "Server Status: Offline" )
        temp3 = 0
    if temp3 == 1:
        print ( "Updated Server Players: {0}".format ( status.players.online ) )
        await stagechannel.edit ( name = "Server Players: {0}".format ( status.players.online ) )


@send.before_loop
async def before():
    await client.wait_until_ready ()


send.start ()

client.run ( '' )
