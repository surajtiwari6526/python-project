# Installed Libraries
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Twilio credentials
account_sid = 'AC9c1bc307e6c2d6a71a53881876774aa5'
account_token = '3a97702c48758ac415de5d47edae0349'
client = Client(account_sid, account_token)

# Function to send WhatsApp message
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID: {message.sid}')
    except Exception as e:
        print(f'An error occurred: {e}')

# User Input
name = input("Enter the name of recipient: ")
recipient_number = input("Enter the recipient number with country code (e.g., +91 1234456789): ")
message_body = input(f"Enter the message body you want to send to {name}: ")

# Parse Date/Time and Calculate Delay
date_str = input("Enter the date to send the message (YYYY-MM-DD): ")
time_str = input("Enter the time to send the message (HH:MM in 24-hour format): ")

# Date-time processing
scheduled_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

# Time difference calculation
time_difference = scheduled_datetime - current_datetime
delay_scheduled = time_difference.total_seconds()

if delay_scheduled <= 0:
    print("The specified time is in the past. Please enter a valid time.")
else:
    print(f'Message scheduled to be sent to {name} at {scheduled_datetime}')

    # Wait until the scheduled time
    time.sleep(delay_scheduled)

    # Send the message
    send_whatsapp_message(recipient_number, message_body)
