print('init')
import discord
import subprocess
print('stage0')
import asyncio 
print('stage1')
from discord.ext import commands
print('stage2')
client = commands.Bot(command_prefix = '.')
print('botStage')

tokenfile = open("/home/pi/Sans/recoverytoken", "r")
token = tokenfile.read()
tokenfile.close()

@client.event
async def on_ready():
    print('Ready.')

client.remove_command('help')

@commands.has_any_role('Owner')
@client.command()
async def recover(ctx):
    await ctx.send("Performing recovery. Please make sure the latest git commit is in a working state.")
    subprocess.run(['sudo', '/home/pi/duckdns/sans.sh'])
@commands.has_any_role('Owner')
@client.command()
async def showerr(ctx):
    await ctx.send("Please wait while the error status is obtained. This will take around 10 seconds.")
    cmd = "bash /home/pi/duckdns/err.sh"
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    err2 = p.stdout.read()
    errfile = open("/home/pi/ram/err", "r")
    err = errfile.read()
    errfile.close()
    cmd = "bash /home/pi/duckdns/del.sh"
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    err2 = p.stdout.read()
    err = "Error (or command output): \n" + "```" + err + "```"
    await ctx.send(err)

client.run(token)
