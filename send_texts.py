# ------------------------------------------------------------------------
# This code will use boto3 to send SMS text messages to all friends who
# have leveled up.
#
# author: Ryan Hood
# email: ryanchristopherhood@gmail.com
# ------------------------------------------------------------------------

import boto3
import private

MESSAGE = 'Congratulations On Leveling Your Runescape Character!!  Keep Making Big Gains!'

def get_phone_number(first_name):
    if (first_name == 'ryan'):
        return private.RYAN_PHONE_NUMBER
    if (first_name == 'kevin'):
        return private.KEVIN_PHONE_NUMBER
    if (first_name == 'brevin'):
        return private.BREVIN_PHONE_NUMBER
    if (first_name == 'isaac'):
        return private.ISAAC_PHONE_NUMBER
    if (first_name == 'alex'):
        return private.ALEX_PHONE_NUMBER
    if (first_name == 'aaron'):
        return private.AARON_PHONE_NUMBER

def send_texts(friends_who_leveled):
    for first_name in friends_who_leveled:
        # We need to get the correct phone number from the 'phone_numbers' file.
        phone_number = get_phone_number(first_name)

        # Now, we simply send that friend the message.
        client = boto3.client('sns')
        client.publish(PhoneNumber=phone_number, Message=MESSAGE)
