import discord
from discord.ext import commands

from . import constants as c


class Misc(commands.Cog, name="Miscellaneous"):
    """Miscellaneous commands, includes Ping, Vote and the Support server."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, *, cog=None):
        """This command!"""
        if cog is None:
            embed = discord.Embed(
                title="Category Listing and Uncatergorized Commands",
                description="""Use `m!help *category*` to find out more about them!""",
                colour=discord.Colour.green()
            )
            cogs_desc = ""
            for cog in self.bot.cogs:
                if cog != "Non-Prefix":
                    cogs_desc += f"`{cog}` - **{self.bot.cogs[cog].__doc__}**\n"
            embed.add_field(
                name="Categories",
                value=cogs_desc[:len(cogs_desc) - 1],
                inline=False
            )
            commands = [
                cmd for cmd in self.bot.walk_commands() if 
                not (cmd.cog_name or cmd.hidden)
            ]
            if len(commands) > 0:
                cmds_desc = ""
                for cmd in commands:
                    cmds_desc += f"`{cmd.name}` - **{cmd.help}**\n"
                embed.add_field(
                    name="Uncatergorized Commands",
                    value=cmds_desc[0:len(cmds_desc) - 1],
                    inline=False
                )
            # await ctx.message.add_reaction(emoji="✉")
            # await ctx.message.author.send(embed=embed)
            await ctx.send(embed=embed)
        else:
            bot_cogs = {name.lower(): cog for name, cog in self.bot.cogs.items()}
            if cog.lower() in bot_cogs.keys() and cog.lower() != "non-prefix":
                embed = discord.Embed(
                    title=f"{list(self.bot.cogs.keys())[list(self.bot.cogs.values()).index(bot_cogs[cog.lower()])]} Command Listing",
                    description=f"__{bot_cogs[cog.lower()].__doc__}__",
                    colour=discord.Colour.green()
                )
                for command in bot_cogs[cog.lower()].get_commands():
                    if not command.hidden:
                        embed.add_field(
                            name=command.name,
                            value=f"**{command.help}**",
                            inline=False
                        )
                # await ctx.message.add_reaction(emoji='✉')
                # await ctx.message.author.send(embed=embed)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title='Error!',
                    description=f"The category `{cog}` doesn't even exist!",
                    color=discord.Color.green()
                )
                await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        """Get the bot's latency."""
        print(ctx.message.content)
        print(ctx.message.author)
        print(ctx.message.guild)
        print('--------------------------------')
        embed = discord.Embed(
            title='Bot Latency',
            description=f'**{int(self.bot.latency * 100)}**ms',
            colour=discord.Colour.green())
        return await ctx.send(embed=embed)

    @commands.command()
    async def server(self, ctx):
        """Get an invite link to the support server."""
        print(ctx.message.content)
        print(ctx.message.author)
        print(ctx.message.guild)
        print('--------------------------------')
        await ctx.channel.trigger_typing()
        if ctx.guild.id == c.SERVER_ID:
            embed = discord.Embed(
                title='You are already in this server',
                description=
                f'However, you can still invite your friends with this link: {c.SERVER_INVITE}',
                colour=discord.Colour.green())
        else:
            embed = discord.Embed(
                title='--> Terraria Bot Official Server <--',
                colour=discord.Colour.green(),
                url=c.SERVER_INVITE)
        embed.set_image(url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def vote(self, ctx):
        """Get the vote link to the bot on top.gg."""
        print(ctx.message.content)
        print(ctx.message.author)
        print(ctx.message.guild)
        print('--------------------------------')
        await ctx.channel.trigger_typing()
        embed = discord.Embed(
            title='--> Vote for Terraria Bot <--',
            colour=discord.Colour.green(),
            url='https://google.com')
        embed.set_image(url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def wiki(self, ctx):
        """Get a link to the Terraria wiki."""
        print(ctx.message.content)
        print(ctx.message.author)
        print(ctx.message.guild)
        print("--------------------------------")
        embed = discord.Embed(
            title="Terraria Wiki",
            description="https://terraria.gamepedia.com/Terraria_Wiki",
            color=discord.Colour.blue())
        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Misc(bot))
