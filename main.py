import discord 
import os
from discord.ext import commands
#run pip install discord-ext-forms
from discord.ext.forms import Form
import time
from rec import getRec

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
        
    db[name] = []
    db[f'{name}-count'] = int(count)
    db[f'{name}-counting'] = 0
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
    if arg not in db['trips']:
        await ctx.send("This trip doesn't exist!")
        return 
    count = db[f"{arg}-count"]
    counting = db[f"{arg}-counting"]
    des = db[f'{arg}-dest'].value
    budget = db[f'{arg}-budget']
    part = ""
    for i in db[arg].value:
        part += i + "\n"

    description = f"""Number of people invited: {count}\n
    Destinations: {des}\n
    Minimum Budget: {budget}\n\n
    People who have registered: {counting}\n 
    {part}\n\n
    Link to form: https://Niki-Cathay.hongmingwong.repl.co?trip={arg} 
    """
    embed=discord.Embed(title="Summary",description=description )
    await ctx.send(embed=embed)
    


@client.command()
async def assist(ctx, arg):
    if arg not in db['trips']:
        await ctx.send("This trip doesn't exist!")
        return 
    
    if f"{arg}-count" not in db.keys():
        await ctx.send("Nobody has registered yet!")
        return

    count = int(db[f"{arg}-count"])
    counting = int(db[f"{arg}-counting"])

    if counting < count:
        await ctx.send(f"Pending requests: {count - counting}")
        await ctx.send("Not everyone has signed up yet, you sure you want to proceed? (Y/N)")
        msg = await client.wait_for("message", check = validateMsg)
        if msg == "N":
            await ctx.send("Noted!")
            return
    
    await ctx.send("Please for a moment for me to create recommendations...")

    budgetList = []
    rec = getRec(budgetList, int(db[f"{arg}-budget"]))
    await ctx.send("Here are my recommendations:")
    await ctx.send(rec)
    

        

    
    
    
client.run(os.environ['Token'])