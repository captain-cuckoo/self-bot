import discord
from discord.ext import commands
from meme import GetMeme,SearchEmoji,generateUwU,bunny
import time
import random
from animals import Animals
import asyncio
#config
token = "ACCOUNT_TOKEN"
prefix = "~" 


print ("starting")

bot = commands.Bot(command_prefix=prefix, self_bot=True)



@bot.event
async def on_ready():
    print ("Ready to be MEME.")
# Prints when the bot is ready to be used.

try:
    async def self_check(ctx):
        if bot.user.id == ctx.message.author.id:
            return True
        else:
            return False
    # A secondary check to ensure nobody but the owner can run these commands.

    #MEME

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def emb(ctx,title,desc=None):
        await ctx.message.delete()
        embed = discord.Embed(
                title = title,
                description=desc,
                colour = discord.Colour.blue())
        await ctx.send(embed = embed)
        

    
    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def meme(ctx,*args):

        await ctx.message.delete()
        try:
            link = GetMeme(*args)
            embed = discord.Embed(
                title = None,
                colour = discord.Colour.blue())
            embed.set_image(url = link)
            await ctx.send(embed = embed)
            
        except:
            await ctx.send("```template not found :(```")
            

    #random lmgtfy implementation cause why not
    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def search(ctx,*args):
        await ctx.message.delete()
        link = "https://lmgtfy.com/?q="
        x = args
        for i in range(len(x)):
            if i == 0:
                link = link + x[i]
            else:
                link = link + '+' + x[i]

        
        await ctx.send(link)

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def emoji(ctx,emoji):
        await ctx.message.delete()
        x = SearchEmoji(emoji)
        
        await ctx.send(x)

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def animal(ctx,name):
        await ctx.message.delete()
        animal = Animals(name)
        
        await ctx.send(animal.image())

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def spread(ctx,*args):
        await ctx.message.delete()
        x = args
        text = ''
        for i in x:
            for j in i:
                text = text + " " + j
        
        await ctx.send(text)

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def caps(ctx,*args):
        await ctx.message.delete()
        x = args
        text = ''
        final = ''
        for i in x:
            text = text+ " " +i

        for i in text:
            if random.randrange(0,2) == 0:
                final = final + i.upper()
            else:
                final = final + i.lower()
        
        await ctx.send(final)

    #uwu command
    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def uwu(ctx,*args):
        await ctx.message.delete()
        x = args
        text = ''
        for i in x:
            text = text+ " " +i

        final = generateUwU(text)
        
        await ctx.send(final)

    #sign command
    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def sign(ctx,*args):
        await ctx.message.delete()
        x = args
        text = ''
        for i in x:
            text = text+ " " +i
        text = text[1:]
        final = bunny(text)
        fuck = "```" + final +"```"
        await ctx.send(fuck)


    #B command
    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def b(ctx,*args):
        await ctx.message.delete()
        x = args
        text = ''
        final = ''
        for i in x:
            text = text+ " " +i
        for i in text:
            if i == "b":
                final = final+":b:"
            else:
                final = final + i

        await ctx.send(final)

    #ping command
    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def ping(ctx):
        """ Pong! """
        await ctx.message.delete()
        before = time.monotonic()
        message = await ctx.send("Pong!")
        ping = (((time.monotonic() - before))/2) * 1000
        await message.edit(content=f"Pong! :ping_pong: `{int(ping)}ms`")


    @bot.command()
    async def gay(ctx,text='so are any of you **NOT** gay?',time=5):
        await ctx.message.delete()
        message1 = await ctx.send(text)
        await asyncio.sleep(time)
        msg1 = await bot.wait_for('message')

        
        # OR `check=lambda m: m.author == ctx.author`
        await message1.edit(content="https://cdn.discordapp.com/attachments/691681269167161354/746351444810006679/eemxonrxj9151.png")
        message2 = await ctx.send('https://cdn.discordapp.com/attachments/691681269167161354/746351506936168458/1ly9dyy0k9151.png')
        
except:
    pass

bot.run(token, bot=False)
# Starts the bot by passing it a token and telling it it isn't really a bot.

