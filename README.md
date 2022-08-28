# GoogleTakeout
Python for parsing Google Takeout json

Currently only handles Google Chat, not Hangout.

##### reads json formatted as such
```
{
  "messages": [
    {
      "creator": {
        "name": "firstname lastname",
        "email": "name@gmail.com",
        "user_type": "Human"
      },
      "created_date": "Tuesday, September 15, 2020 at 11:19:21 PM UTC",
      "text": "Hello beautiful",
      "topic_id": "ovpt6yptqo4"
    },
```

##### outputs in the following format:
```
Alice  -  Wednesday, September 16, 2020 at 12:35:38 AM UTC 
 How was your trip? 

 --- 

Bob  -  Wednesday, September 16, 2020 at 12:36:54 AM UTC 
 Really nice. 

 --- 
```

datetime is configured for precise readings, but currently commented out.

##### TODO
output to other formats
support images?
generate graphs?
