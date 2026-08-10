# Parent:
# Notification

# Method:
# send()

# Children:
# EmailNotification
# SMSNotification
# PushNotification

# Store all notification objects in a list.
# Loop through them.

# Call:
# notification.send()


class Notification:

    def send(self):
        pass

class EmailNotification(Notification):

    def send(self):
        print("Email Sent Successfully")



class SMSNotification(Notification):


    def send(self):
        print("SMS Sent Successfully")



class PushNotification(Notification):

    def send(self):
        print("PUSH Sent Successfully")


notifications = [EmailNotification(), SMSNotification(), PushNotification()]

for notification in notifications:
    notification.send()