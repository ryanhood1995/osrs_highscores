# ------------------------------------------------------------------------
# Uses the RoboBrowser and BeautifulSoup modules to scrape the Old School
# Runescape highscores for a particular player name and return their
# total level found
#
# author: Ryan Hood
# email: ryanchristopherhood@gmail.com
# ------------------------------------------------------------------------

from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
import private

def get_username(first_name):
    if (first_name == 'ryan'):
        return private.RYAN_USERNAME
    if (first_name == 'kevin'):
        return private.KEVIN_USERNAME
    if (first_name == 'brevin'):
        return private.BREVIN_USERNAME
    if (first_name == 'isaac'):
        return private.ISAAC_USERNAME
    if (first_name == 'alex'):
        return private.ALEX_USERNAME
    if (first_name == 'aaron'):
        return private.AARON_USERNAME

def fetch_highscores(first_name):
    # First, a RoboBrowser opens the highscores list.
    br = RoboBrowser()
    br.open('https://secure.runescape.com/m=hiscore_oldschool/hiscorepersonal')

    # To access a player's highscores, we must have RoboBrowser enter their username in the
    # 'search player' form.  There are multiple forms on the page, but the 'search player'
    # form is the first one.
    form = br.get_forms()[0]

    # 'user1' is the name attribute of the form.  We get the username from the first name using
    # the file 'usernames'.  The purpose of a separate file for usernames is so I can present
    # this code but keep my friends and my usernames a secret.
    form.fields['user1'].value = get_username(first_name)

    # Sumbit the form.  We are now in first_name's highscores page.
    br.submit_form(form)

    # src is a long HTML string which we will look through for the total level.
    src = str(br.parsed())

    # Here is use BeautifulSoup.  It's probably not necessary to switch from RoboBrowser, but
    # it was easier for me to get the code working.
    soup = BeautifulSoup(src, features='html.parser')

    # At the time of writing this code, 'class_ = centerDiv' is the closest location for the
    # total level.
    posts = soup.find_all(class_ = 'centerDiv')
    player_string = posts[0].get_text()

    # 'player_string' has a lot of new line characters, and I only want one piece of the string.
    # So, I turn the string into a list using newline characters as the break points.
    player_list = player_string.splitlines()

    # The total level is at index number 47, so extract it.
    total_level = player_list[47]
    return total_level

def generate_all_stats():
    # This method simply calls the above method for all friends, adding their total levels to a list.
    list = []
    list.append(fetch_highscores('ryan'))
    list.append(fetch_highscores('kevin'))
    list.append(fetch_highscores('brevin'))
    list.append(fetch_highscores('isaac'))
    list.append(fetch_highscores('alex'))
    list.append(fetch_highscores('aaron'))
    return list
