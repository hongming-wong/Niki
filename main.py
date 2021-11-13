import discord 
import os
from discord.ext import commands
from discord.ext.forms import Form
client = commands.Bot(command_prefix='!')

@client.command()
async def active(ctx):
	await ctx.send("Active! Ready to plan your trip!")


@client.command()
async def plan(ctx, name):
	form = Form(ctx, f'Details for {name}')
	form.add_question('How many people are going?', 'people')
	form.add_question('Which destinations are you considering?', 'destinations')
	form.add_question('Budget Range?', 'budget')
	result = await form.start()
	embed=discord.Embed(title="Type Y to confirm, Type N to cancel",description=f"Number of people: {result.people}\nDestinations: {result.destinations}" )
	await ctx.send(embed=embed)
	msg = await client.wait_for("message")
    while msg != "Y" and msg != "N":
        ctx.send("Please Type Y or N")
        msg = await client.wait_for("message")
       
	
	
client.run(os.environ['Token'])