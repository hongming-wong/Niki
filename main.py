import discord 
import os
from discord.ext import commands
from discord.ext.forms import Form
from replit import db
client = commands.Bot(command_prefix='!')

@client.command()
async def active(ctx):
	await ctx.send("Active! Ready to plan your trip!")


def validateMsg(message):
    if message.content == "Y" or message.content == "N":
        return True
    return False

def addToDB(name, count, dest, budget):
    dest_parsed = dest.split(',');
    dest = [i.strip() for i in dest_parsed]
    
    if len(db.keys()) == 0:
        db['trips'] = [name]
    else:
        temp = db['trips']
        temp.append(name)
        db['trips'] = temp
        
    db[f'{name}-count'] = count
    db[f'{name}-dest'] = dest
    db[f'{name}-budget'] = budget
    
    pass
    
@client.command()
async def plan(ctx, name):
    form = Form(ctx, f'Details for {name}')
    form.add_question('How many people are going?', 'people')
    form.add_question('Which destinations are you considering? (Add a "," between each destination)', 'destinations')
    form.add_question('Budget Range?', 'budget')
    result = await form.start()
    description = f"""Number of people: {result.people}\n
    Destinations: {result.destinations}\n
    Minimum Budget: {result.budget}
    """
    embed=discord.Embed(title="Type Y to confirm, Type N to cancel",description=description )
    await ctx.send(embed=embed)
    msg = await client.wait_for("message", check = validateMsg)
    if msg.content == 'Y':
        await ctx.send(f"Trip {name} is confirmed!")
        addToDB(name, result.people, result.destinations, result.budget)
    else:
        await ctx.send(f"Cancelled :(")
	
client.run(os.environ['Token'])