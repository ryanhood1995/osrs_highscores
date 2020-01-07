# ------------------------------------------------------------------------
# This file is the file that needs to be run to start the program.
# It's purpose is to restart the script when it crashes, so I don't
# have to keep restarting the script.
#
# author: Ryan Hood
# email: ryanchristopherhood@gmail.com
# ------------------------------------------------------------------------

from subprocess import Popen

filename = r'C:\Users\User\Data_Science_Projects\osrs_scraping\driver.py'
while True:
    print("\nStarting " + filename)
    p = Popen("python " + filename, shell=True)
    p.wait()
