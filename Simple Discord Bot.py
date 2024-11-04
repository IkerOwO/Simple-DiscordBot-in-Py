import discord
from discord.ext import commands

intents = discord.Intent.default()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())

#Bot Ready Comment
@bot.event
async def on_ready()     #Syncs the bot
    print("Bot is ready")
    try:
        synced = await bot.tree.sync()          #Syncs the Commands to the bot
        print(f"{len(synced)} commands synchronized)
    except Exception as e:
        print(e)
        
        
#Messages
@bot.event
async def on_message(msg):
    if msg.author == bot.user
        return
    if msg.content.lower() == "Hello":           #content.lower = It registers the message even if it starts with a capital letter
        await msg.reply("Hello :3")


        
        
#Commands
@bot.tree.command(name="hello", description= "say hello to the bot")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello! {interaction.user.mention},
    ephemeral= True)
#{interaction.user.mention} = Mentions the User |  ephemeral= True = Only the User that used the command can see the message
        


#Use your API KEY :3 | I recommend putting the API KEY on another .py and importing it to this one
bot.run('YOUR API KEY')
