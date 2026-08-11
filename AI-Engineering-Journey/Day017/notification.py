
# 🛠️ Mini Project 3 — Notification System
# Parent:
# Notification

# Abstract method:
# send()

# Children:
# EmailNotification
# SMSNotification
# PushNotification

# Each implements send() differently.

# Then:
# notifications = [
#     EmailNotification(),
#     SMSNotification(),
#     PushNotification()
# ]

# Loop through them.




from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self):
        pass

class EmailNotification(Notification):

    def send(self):
        print("Email sent")

class SMSNotification(Notification):

    def send(self):
        print("SMS sent")

class PushNotification(Notification):

    def send(self):
        print("Push sent")


notifications = [EmailNotification(), SMSNotification(), PushNotification()]
for notification in notifications:
    notification.send()