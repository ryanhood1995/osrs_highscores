# ------------------------------------------------------------------------
# A very simple file containing just one method.  Given a list of old stats
# and new stats, this method will return a list of names who have leveled
# up their runescape accounts.
#
# author: Ryan Hood
# email: ryanchristopherhood@gmail.com
# ------------------------------------------------------------------------

def who_leveled_up(old_stats, new_stats):
    # The code is self-explanatory...
    # Each firend corresponds to an entry in the stats lists.
    friends_who_leveled = []
    if old_stats[0] != new_stats[0]:
        friends_who_leveled.append('ryan')
    if old_stats[1] != new_stats[1]:
        friends_who_leveled.append('kevin')
    if old_stats[2] != new_stats[2]:
        friends_who_leveled.append('brevin')
    if old_stats[3] != new_stats[3]:
        friends_who_leveled.append('isaac')
    if old_stats[4] != new_stats[4]:
        friends_who_leveled.append('alex')
    if old_stats[5] != new_stats[5]:
        friends_who_leveled.append('aaron')
    return friends_who_leveled
