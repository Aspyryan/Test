import discord

from discord.ext import commands

TOKEN = "NTA4NjIyODc4NzkxNTY1MzMz.XmzvYw.bHethCui2OxHLMYJg5lMDEhRXLQ"
client = commands.Bot(description="Baguette", command_prefix="*")

@client.event
async def on_ready():
    print("[BOT] I'm ready")

RoleReaction = {'514810473267331083': '👀', '398389102485045248': '👍'}
FinalMessages = {}
Emojis = []
removeMessages = []
watchFinalMessage = None
finalMessage = ""

# # For linking role and emoji
# watchMessage = None
# watchMessageRole = ""
# #############################


# @client.command(pass_context=True)
# async def setrank(ctx, RoleId):
#     global watchMessage, watchMessageRole
#     watchMessageRole = RoleId
#     watchMessage = await ctx.message.channel.send("Give this message the reaction you want to add %s to" %RoleId)

@client.event
async def on_reaction_add(reaction, User):
    global watchMessage, removeMessages, Emojis
    if not reaction.me:

        # # Dit is de code om een directory aan te maken van ranks met emoji // DONE
        # if reaction.message.id == watchMessage.id:
        #     RoleReaction[watchMessageRole] = reaction.emoji
        #     roles = await reaction.message.author.guild.fetch_roles()
        #     role = ""
        #     for item in roles:
        #         if item.id == int(watchMessageRole):
        #             role = item.name
        #     await reaction.message.delete()
        #     await reaction.message.channel.send("%s has been assigned to the rank: %s" %(reaction.emoji, role))
        #     watchMessage = None
        #     print(RoleReaction)

        # Dit is de code om te kijken of er een reactie is toegevoeg aan

        if reaction.message.id == watchFinalMessage.id:
            if reaction.emoji in RoleReaction.values():
                if reaction.emoji not in Emojis:
                    Emojis.append(reaction.emoji)
                    await reaction.message.add_reaction(reaction.emoji)
            else:
                remove = await reaction.message.channel.send("This emoji is not yet registrated")
                removeMessages.append(remove)
        elif reaction.message.id in FinalMessages:
            roles = await reaction.message.author.guild.fetch_roles()

            for item in RoleReaction:
                if RoleReaction[item] == reaction.emoji:
                    for role in roles:
                        if int(role.id) == int(item):
                            await User.add_roles(role)


@client.command(pass_context=True)
async def SetMessage(ctx, *, Message):
    global finalMessage, watchFinalMessage, removeMessages
    finalMessage = Message
    watchFinalMessage = await ctx.message.channel.send("Add the reactions to this message to watch them")

    removeMessages.append(ctx.message)
    removeMessages.append(watchFinalMessage)

@client.command(pass_context=True)
async def done(ctx):
    global watchFinalMessage, finalMessage, removeMessages

    removeMessages.append(ctx.message)

    for item in removeMessages:
        await item.delete()
    addReactions = await ctx.message.channel.send(finalMessage)

    FinalMessages[addReactions.id] = Emojis
    print(FinalMessages)

    for item in FinalMessages[addReactions.id]:
        await addReactions.add_reaction(item)
client.run(TOKEN)