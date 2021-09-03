# Documentation can be found at https://nighty.one/docs/#customscripts #

import asyncio

@bot.command(usage='mping <argument>', description='Mass pings everybody')
async def mping(nighty, arg):
    msg = nighty.message
    messagePing = ""
    for user in nighty.message.guild.members:
        messagePing += "<@" +str(user.id) + "> "
    lists = [messagePing[i:i+1900] for i in range(0, len(messagePing), 1900)]
    print("Mass pinging a total of " + str(len(nighty.message.guild.members)) + " members")
    
    for string in lists:
        try:
            messagePing = string[:1900] + "> " + arg
            newMsg = await msg.channel.send(messagePing)
            await asyncio.sleep(1)
            await newMsg.delete()
        except:
            print("An error occured idk.")