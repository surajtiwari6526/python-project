#installed liberary
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# twilio credentials
account_sid ='AC9c1bc307e6c2d6a71a53881876774aa5'
account_token='3a97702c48758ac415de5d47edae0349'
client =Client(account_sid,account_token)

# design and send message
def send_whatsapp_number(receipetent_number,message_body):
   try:
    message = client.message.Create(
          from_='whatsapp:+14155238886',
          body = message_body,
          to = 'whatsapp:{recreceipetent_number}'
     )
    print(f'Message sent successfully! Message Sid(message.sid)')
   except Exception as e:
     print('an error occured')

    # user input
name = input("Enter the name of reciptent:")
receipetent_number = input("Enter the reciptent number with country code with country code eg(+91 1234456789)")
message_body = input("Enter the message body you want to send to {name}")

   #parase date/time and calculate dealy
date_str =input("Enter the date to send the message in (YYYY-MM-DD)")
time_str = input("Enter the time to send the message(HH:MM in 24 hour format):")

#date times
scheduled_datetime = datetime.strptime(f'{date_str}{time_str}',"%H-%m-%d %H:%M")
current_datetime = datetime.now()

#time difference
time_difference = scheduled_datetime - current_datetime
dealy_scheduled = time_difference.total_seconds

if dealy_scheduled<=0:
  print("The specified is in the past. please enter valid time..")
else:
  print(f'Message scheduled to be sent to{name} at {scheduled_datetime}')

#wait until the scheduled time
time.sleep(dealy_scheduled)

#send the message
send_whatsapp_number(receipetent_number,message_body)