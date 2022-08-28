import os
from io import BytesIO
from random import normalvariate

import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
from loguru import logger
import asyncio
from thefuzz import fuzz

from .whataweek import whataweek
from .rainbow import colorgen
from .mangetamain import jai_faim
from .bientotle import bientot_l_apero, bientot_le_weekend

load_dotenv()


class PoutouBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=["!", "☭"])

        @self.command(name="whataweek")
        async def watch_whataweek(ctx: commands.Context):
            io_img = BytesIO()
            whataweek().save(io_img, format="png")
            io_img.seek(0)
            await ctx.send(file=discord.File(io_img, filename="whataweek_captain.png"))

        @self.command(name="bientot_apero")
        async def bientot_apero(ctx: commands.Context):
            await ctx.reply(bientot_l_apero())

        @self.command(name="bientot_weekend")
        async def bientot_weekend(ctx: commands.Context):
            await ctx.reply(bientot_le_weekend())

        @self.command(name="wololo")
        async def on_demand_wololo(ctx: commands.Context):
            await self.change_role_color()
        self.periodic_wololo.start()

    async def get_role(self, name):
        logger.info("get guild")
        try:
            guild = await self.fetch_guild(os.environ["GUILD_UID"])
        except KeyError:
            raise ValueError("$GUILD_UID not set")
        logger.info(guild)
        role = discord.utils.get(guild.roles, name=name)
        logger.info(role)
        return role

    async def change_role_color(self):
        logger.info("wololo?")
        wololo = await self.get_role("wololo")
        colour = colorgen()
        logger.info(colour)
        await wololo.edit(colour=colour)
        logger.info("wololo!")

    @tasks.loop(minutes=30)
    async def periodic_wololo(self):
        await self.change_role_color()

    @periodic_wololo.before_loop
    async def before_periodic_wololo(self):
        print("waiting...")
        await self.wait_until_ready()

    async def on_ready(self):
        print("Poutou is watching.")

    async def on_message(self, message:discord.Message):
        if message.author == self.user:
            return
        score = fuzz.partial_ratio(message.content, "j'ai faim")
        print(message.content, score)
        if score > 70 and "faim" in message.content.lower():
            with message.channel.typing():
                await asyncio.sleep(max(0, normalvariate(2, 0.5)))
                response = jai_faim()
                await message.reply(response)
        await bot.process_commands(message)


if __name__ == "__main__":
    bot = PoutouBot()
    bot.run(os.environ["TOKEN"])
