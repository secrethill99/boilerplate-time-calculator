import re

# I create a numeric code for each day of the week by associating each day with an array position:
dayoftheweek_pos = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}
dayoftheweek_calculated = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",]

def add_time(starttime, duration, startday = "Monday"):
    
    startday = startday.lower()
    
    # I'll assume that start time and duration are entered correctly in the required format.
    # My approch is to convert everything to minutes in a first step and then convert the end point back.

    # I start by converting the duration to minutes:
    durationstr = re.search("[1-9]*[0-9]+:", duration).group()
    durationhours = durationstr[:-1]
    durationstr2 = re.search(":[0-5]*[0-9]", duration).group()
    durationminutes = durationstr2[1:]
    durationhh = int(durationhours)
    
    durationmm = int(durationminutes)
    
    totalduration = durationhh*60 + durationmm
    
    
    # I convert the start time to minutes:
    starthourstr = re.search("[1-9]*[0-9]+?:", starttime).group()
    starthour = starthourstr[:-1]
    startminstr = re.search(":[0-9][0-9]", starttime).group()
    startminutes = startminstr[1:3]
    starthh = int(starthour)
    if "PM" in starttime:
        starthh += 12 
        
    startmm = int(startminutes)
    
    convertedstarttime = starthh*60 + startmm

    # I calculate the end time in minutes starting from midnight of the start day:
    convertedendtime = convertedstarttime + totalduration
    
    
    if convertedendtime < 24*60:
        # I convert the convertedendtime back to hours and minutes:
        numberofhrs = int(convertedendtime/60)
        numberofmins = convertedendtime - numberofhrs*60 
        ampmtext = "AM"
                    
        if numberofhrs >= 12:
            ampmtext = "PM"
            if numberofhrs > 12:
                numberofhrs -= 12
        
        new_time = str(numberofhrs)+ ":"+ f'{numberofmins:02d}'+ " " +ampmtext
        print(new_time)
        
    if convertedendtime > 24*60:
        ampmtext = "AM"

        # I convert the convertedendtime back to days, hours and minutes:
        numberofdays = int(convertedendtime/(24*60)) 
        numberofhrs = int(convertedendtime%(24*60)/60)
        numberofmins = convertedendtime - numberofdays*24*60 - numberofhrs*60
        
        # I calculate the end day:
        enddayindex = (dayoftheweek_pos[startday] + numberofdays)%7
        endday = dayoftheweek_calculated[enddayindex] 
        
        # I print the result:
        if numberofdays == 1:
             
            if numberofhrs > 12:
                numberofhrs -= 12
                ampmtext = "PM"
            new_time = str(numberofhrs) + ":"+ f'{numberofmins:02d}'+ " " + ampmtext+ ", " + endday+ " (next day)"
            print(new_time)

        else:
            if numberofhrs == 0:
                str(numberofhrs) == f'{numberofhrs:02d}'
            if numberofhrs > 12:
                numberofhrs -= 12
                ampmtext = "PM"
            new_time = str(numberofhrs) + ":"+ f'{numberofmins:02d}' + " " + ampmtext+ ", " + endday +" ("+ str(numberofdays) + " days later)"
            print(new_time)
            
add_time("8:16 PM", "466:02", "tuesday")
