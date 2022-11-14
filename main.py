import os
import bot
import sqlite3
import time

print('''
##MADE BY Buxx0-github.com/Buxx0###
###################################
###____####################___#####
##|  _ \                  / _ \ ###
##| |_) |_   ___  ____  _| | | |###
##|  _ <| | | \ \/ /\ \/ / | | |###
##| |_) | |_| |>  <  >  <| |_| |###
##|____/ \__,_/_/\_\/_/\_\\___/####
###################################
###################################
''')
time.sleep(2)

con = sqlite3.connect("config.db")
cur = con.cursor()

def setup():
    for row in cur.execute("SELECT setupdone FROM config"):
        if row[0] == 1:
            print("Setup already done!")
            return
    requirements = ["hikari", "hikari-lightbulb", "asyncio"]
    for requirement in requirements:
        print(f"Installing requirement {requirement}...")
        os.system(f"pip install {requirement}")
        print(f"{requirement}: requirement met!")
    print("All requirements met!")
    cur.execute("UPDATE config SET setupdone = 1")
    con.commit()

def start_main():
    token = 0
    for row in cur.execute("SELECT token FROM config"):
        if row[0] == 0:
            token = input("Please input your bot token: ")
            cur.execute(f"UPDATE config SET token = '{token}'")
            con.commit()
        else:
            token = row[0]
    bot.main(token)

setup()
start_main()

