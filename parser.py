import json, re
from datetime import datetime

with open("Google Chat/Groups/DM uZ8_QQAAAAE/messages.json", "r") as d:
    dict = json.load(d)
    
    messages = dict['messages']

    dates = []

    for message in messages:
        try:
            sender = message['creator']['name']
            date = message['created_date']
            text = message['text']
            
            # parse created_date string to datetime
            date_time_obj = datetime.strptime(date, '%A, %B %d, %Y at %X %p UTC')
            
            dates.append(date_time_obj.date())

            print(sender, ' - ' , date, '\n', text, '\n\n --- \n')
        except KeyError:
            continue

# firstDate = dates[0].__str__()
# lastDate = dates[-1].__str__()
# chat_date_duration = firstDate + ' - ' + lastDate

# print(chat_date_duration)
