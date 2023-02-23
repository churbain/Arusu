from redbot.core import commands
import discord
import re
from redbot.core.commands import Cog

list = ["Quoi", "quoi"]
activate = 1

class Feur(commands.Cog):
    """Quoi ? Feur"""

    def __init__(self, bot):
        self.bot = bot
    @commands.group(name = "feur", invoque_without_command = True)
    async def feurmain(self, ctx) :
        pass
    @feurmain.command(name = "activate")
    async def actimain(self, ctx) :
        if activate == 1 : 
            activate = 2
            await ctx.send("Feur désactivé")
        else :
            activate = 1
            await ctx.send("Feur activé")
     
    @Cog.listener()
    async def on_message(message : discord.Message):
        if activate == 1 :
            for l in list :
                if re.search(l, message.content) :
                    await ctx.send("Feur")
                else : 
                    pass
        else :
            pass
    
    
