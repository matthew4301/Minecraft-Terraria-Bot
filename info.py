import discord
from discord.ext import commands


class MinecraftInfo(commands.Cog, name="Minecraft Info"):
    """Contains commands about minecraft info."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def blocks(self, ctx):
        """Get the amount of blocks in Minecraft."""
        print(ctx.message.content)
        print(ctx.message.author)
        print(ctx.message.guild)
        print("--------------------------------")
        await ctx.channel.send("There are more than 150 blocks in minecraft!")

    @commands.command()
    async def snapshots(self, ctx):
        """Get info about the current snapshots."""
        print(ctx.message.content)
        print(ctx.message.author)
        print(ctx.message.guild)
        await ctx.channel.trigger_typing()
        embed = discord.Embed(
            title="Minecraft Snapshots",
            colour=discord.Colour.green(),
            description="""
            __Minecraft Java:__
**Snapshot 20w15a**
https://www.minecraft.net/en-us/article/minecraft-snapshot-20w15a
• Added a Piglin banner pattern
• Added Basalt Deltas biome to the Nether
• Added three new tracks of Nether music
• Added a new set of stone blocks called Blackstone, and Gilded Blackstone
• Added line spacing and chat delay accessibility options

            __Minecraft Bedrock:__
            **Beta 1.16.0.55**
            https://feedback.minecraft.net/hc/en-us/articles/360041294872
             • Carrot on a stick, Shield, and Shovel now lose durability consistently
             • Light propagation now works correctly, fixing hostile mob spawning
             • Water can now be collected from Bubble Columns using a bucket 
             • Creepers no longer lose aggro immediately after losing sight of its target
             • Technical changes and bug fixes
            """)
        await ctx.send(embed=embed)

    @commands.command()
    async def wiki(self, ctx):
        """Get the link to the Minecraft Wiki."""
        print(ctx.message.content)
        print(ctx.message.author)
        print(ctx.message.guild)
        print("--------------------------------")
        embed = discord.Embed(
            title="Minecraft Wiki",
            description="https://minecraft.gamepedia.com/Minecraft_Wiki",
            color=discord.Colour.blue())
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def bedrock(self, ctx):
        """Get info about Minecraft Bedrock edition."""
        print(ctx.message.content)
        print(ctx.message.author)
        print(ctx.message.guild)
        print("--------------------------------")
        await ctx.channel.trigger_typing()
        embed = discord.Embed(
            title="Bedrock is available on:",
            description="Phone and Tablet (Android, IOS, Fire OS, Windows Mobile), Windows 10, Nintendo Switch, Xbox One, PS4, Fire TV and Gear VR. Learn more about Bedrock  at https://minecraft.gamepedia.com/Bedrock_Edition",
            colour=discord.Colour.green())
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def java(self, ctx):
        """Get info about Minecraft Java edition."""
        print(ctx.message.content)
        print(ctx.message.author)
        print(ctx.message.guild)
        print("--------------------------------")
        await ctx.channel.trigger_typing()
        embed = discord.Embed(
            title="Java Edition is available on:",
            description="Linux, MacOS and Windows. Learn more about Java Edition  at https://minecraft.gamepedia.com/Java_Edition",
            colour=discord.Colour.green())
        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(MinecraftInfo(bot))
