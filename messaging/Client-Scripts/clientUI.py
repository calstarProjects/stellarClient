# WIP
# this is a terminal based UI
# to make this universal we use a basic UI
# if you have this in a controlable enviroment, then we use rich
# for user input we use a seperate script
import datetime
try:
    from rich.console import Console
    from rich.table import Table
    usingRich = True
except:
    print("Rich not installed, using basic UI")
    usingRich = False
    
class UI:
    def __init__(self, GCs, Friends):
        self.ActiveChatters = 10
        self.ActiveFriends = 11
        self.TotalFriends = 30
        self.TotalChatters = 15
        if usingRich == True:
            # start rich table and console
            MainTable = Table()
            MainConsole = Console()
            # add stuff to rich and the table
            MainTable.add_column(self.getTopText())
            MainTable.add_column("   Chats:     ")
            # output to rich console
            MainConsole.print(MainTable)
        else:
            pass
    def getTopText(self):
        now = datetime.datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%b")
        day = now.strftime("%d")
        daystr = now.strftime("%a")
        hour = int(now.strftime("%H"))
        minute = int(now.strftime("%M"))
        second = now.strftime("%S")
        ap = now.strftime("%p")
        # there are 2 main modes, break and not break (and a special end state)
        # if the month is not june or july
        onBreak = None
        if month != "Jun" and month != "Jul":
            # and is not before the 15 of august
            if not (month == "Aug" and day < 15):
                # or after the 22 of december
                if not (month == "Dec" and day > 22):
                    # is not the 1st,2nd, or 19th of january
                    if not (month == "Jan" and (day in [1,2,19])):
                        # not the fisrt of september or 16th of febuary
                        if ((month == "Sep" and day == 1) != True) and ((month == "Feb" and day == 16) != True):
                            # is not the 24th to 28th of november
                            if not (month == "Nov" and (day in [24,25,26,27,28])):
                                # is not the 22nd to 31st of december
                                if not (month == "Dec" and (day in [22,23,24,25,26,27,28,29,30,31])):
                                    # not the 16th of febuary 30th of march
                                    if (not (month == "Feb" and day == 16)) and (not (month == "Mar" and day == 30)):
                                        # not the 31st of march
                                        if not (month == "March" and day == "31"):
                                            # not the 1-3 of april
                                            if not (month == "April" and (day in [1,2,3])):
                                                # nor the 25th of may
                                                if not (month == "May" and day == 25):
                                                    # nor a saturday, or sunday
                                                    if daystr != "Sat" and daystr != "Sun":
                                                        # then set to off break
                                                        onBreak = "nu"
        # but if it is the 29th of may
        if month == "May" and day == 29:
            # set to special condition
            onBreak = "LastDay"
        if onBreak == None:
            # otherwise we are on a break
            onBreak = "ye"
        # if the mode is special set everything to gold
        if onBreak == "LastDay":
            finalStr = f"[gold3]{month}, {daystr} {day} {year}@{hour}:{minute}:{second} {ap} Active in GC: {self.ActiveChatters}/{self.TotalChatters} Active Friends: {self.ActiveFriends}/{self.TotalFriends}[/gold3]"
        else:
            # if the mode is set to break set date to green
            if onBreak == "ye":
                datetext = f"[green]{month}, {daystr} {day} {year}[/green]"
            else:
                # if mode is not on break set date to red
                datetext = f"[red]{month}, {daystr} {day} {year}[/red]"
            # if the time is 7:11 set to 7-Eleven colors
            if hour == 7 and minute == 11:
                timeText = f"[dark_green]{hour}[/dark_green]:[indian_red1]{minute}[/indian_red1]:[orange3]{second}[/orange3] {ap}"
                # if it is later than 9:30 PM then set the clock color to orange
            elif (hour == 9 and minute > 29 and minute < 60) or hour == 10 or hour == 11 and ap == "PM":
                timeText = f"[orange3]{hour}:{minute}:{second} {ap}[/orange3]"
                # if it is later than 12:00 AM then set the clock color to dark orange
            elif (hour == 11 and ap == "PM") or (hour == 1 and ap == "AM"):
                timeText = f"[dark_orange]{hour}:{minute}:{second} {ap}[/dark_orange]"
                # if it is later than 2:00 AM and before 5:00 set clock color to red
            elif hour > 1 and hour < 6 and ap == "AM":
                timeText = f"[red]{hour}:{minute}:{second} {ap}[/red]"
                # if it is after 5:00 but before 6:30 then set to orange
            elif (hour == 5 or (hour == 6 and minute < 31)) and ap == "AM":
                timeText = f"[orange3]{hour}:{minute}:{second} {ap}[/orange3]"
                # otherwise set it to green
            else:
                timeText = f"[green]{hour}:{minute}:{second} {ap}[/green]"
            OCP = (self.ActiveChatters/self.TotalChatters)*100
            OFP = (self.ActiveFriends/self.TotalFriends)*100
            if OCP >= 0 and OCP < 5:
                # if the percentage of online users is 0-4% set fraction to red
                
                pass
            elif OCP > 4 and OCP < 36:
               # if the percentage of online users is 5-35% set fraction to orange
               pass
            elif OCP > 35 and OCP > 66:
                # if the percentage of online users is 35-65% set fraction to yellow
                pass
            elif OCP > 64 and OCP < 80:
                # if the percentage of online users is 65-80% set fraction to light yellow
                pass
            else:
                # if the percentage of online users is 80-100% set fraction to green
                pass
            # all of that also goes for the amount of active friends
            finalStr = datetext+"@"+timeText
        return finalStr
    
UI([],[])
