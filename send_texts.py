# ------------------------------------------------------------------------
# This code will use boto3 to send SMS text messages to all friends who
# have leveled up.
#
# author: Ryan Hood
# email: ryanchristopherhood@gmail.com
# ------------------------------------------------------------------------

import boto3
import phone_numbers

MESSAGE = 'Congratulations On Leveling Your Runescape Character!!  Keep Making Big Gains!'

def send_texts(friends_who_leveled):
    for friend in friends_who_leveled:
        # We need to get the correct phone number from the 'phone_numbers' file.
        phone_number = phone_numbers.get_phone_number(friend)

        # Now, we simply send that friend the message.
        client = boto3.client('sns')
        client.publish(PhoneNumber=phone_number, Message=MESSAGE)
