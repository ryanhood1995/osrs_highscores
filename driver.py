# ------------------------------------------------------------------------
# This is the main 'driver' code for the whole program.  It first finds all
# friends' old stats, and then it finds their new stats.  If any stats have
# changed, it figures out who has leveled.  Then it sends a text to the
# friend(s) who have leveled.  Laslty, it updated the old stats and cycles
# every minute.
#
# author: Ryan Hood
# email: ryanchristopherhood@gmail.com
# ------------------------------------------------------------------------

import boto3
import highscores_scraping
import detect_level_up
import time
import send_texts


# --------------------------------------------
# ------------------MAIN----------------------
# --------------------------------------------

# First, we get a list of the old total levels.
all_old_stats = highscores_scraping.generate_all_stats()

# This loop will repeatedly check for changes in total levels.
while True:
    # Get new total levels.  On first pass, the old levels will be identical to the new levels.
    all_new_stats = highscores_scraping.generate_all_stats()

    print("Checking Highscores...")
    print("The Old Stats: ", all_old_stats)
    print("The New Stats: ", all_new_stats)

    # Now, check to see if levels differ.
    if (all_old_stats != all_new_stats):
        # If they differ, then a friend has leveled up!
        print("A Friend has Leveled Up!")

        # Figure out who has leveled up, and store that in a list.
        friends_who_leveled = detect_level_up.who_leveled_up(all_old_stats, all_new_stats)

        print("Friend(s) who leveled: ", friends_who_leveled)
        print("Sending text(s)...")

        # Send SMS text messages to those who leveled up.
        send_texts.send_texts(friends_who_leveled)

        # Update 'old_stats', so we do not resend messages.
        all_old_stats = all_new_stats

    # This will cycle will repeat every so often.
    time.sleep(15)
