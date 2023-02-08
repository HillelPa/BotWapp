from alright import WhatsApp
import time
import csv
import os


if __name__ == "__main__":

    invites = []

    with open('invites.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader) # skip the header row
        for row in reader:
            invite = {
                'nom': row[0].strip(),
                'tel': row[1].strip()
            }
            invites.append(invite)

    messenger = WhatsApp()

    for invite in invites:
        try:
            messenger.find_user(invite['tel'])
            messenger.send_file("Cartes/Carte-" + invite['nom'] + ".pdf")
            time.sleep(5)
            messenger.send_message("Blablabla " + invite['nom'] + " blablabla")
            time.sleep(1)
        except Exception as e:
            print("Error for user " + invite['nom'] + " with number " + invite['tel'] + ": " + str(e))
            continue
