import discord 
import os
from discord.ext import commands
#run pip install discord-ext-forms
from discord.ext.forms import Form
import time

from replit import db

client = commands.Bot(command_prefix='!')

print("bot server is running")

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
    
@client.command()
async def plan(ctx, name):
    form = Form(ctx, f'Details for {name}')
    form.add_question('How many people are going?', 'people')
    form.add_question('Which destinations are you considering? (Add a "," between each destination)', 'destinations')
    form.add_question('Minimum budget?', 'budget')
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
        link = f"https://Niki-Cathay.hongmingwong.repl.co?trip={name}" 
        addToDB(name, result.people, result.destinations, result.budget)
        await ctx.send(f"Send this form to your friends: {link}")
    else:
        await ctx.send(f"Cancelled :(")

@client.command()
async def TIP(ctx):
    if 'trips' not in db.keys():
        await ctx.send("No trips in progress. Use the command !plan to start one!")
    trips = db['trips'].value
    if len(trips) == 0:
        await ctx.send("No trips in progress. Use the command !plan to start one!")
    else:
        await ctx.send(f"{len(trips)} trip(s) in progress")   
        s = ""
        for i, v in enumerate(trips):
            s += f"{i + 1}. {v}\n"
        await ctx.send(s)

@client.command()
async def info(ctx, arg):
    pass

@client.command()
async def assist(ctx, arg):
    if arg not in db['trips']:
        await ctx.send("This trip doesn't exist!")
        return 
    
    if db[f"{arg}-count"] not in db.keys():
        await ctx.send("Nobody has registered yet!")
        return

    counting = db[f"{arg}-count"]
    count = db[f"{arg}-counting"]

    if count != counting:
        await ctx.send("Not everyone has signed up yet, you sure you want to proceed? (Y/N)")
        msg = await client.wait_for("message", check = validateMsg)
        if msg == "N":
            await ctx.send("Noted!")
            return
    
    await ctx.send("Please for a moment for me to create recommendations...")
    time.sleep(2)
    await ctx.send("Here are my recommendations:")
    #do something

        

    
    
    
client.run(os.environ['Token'])