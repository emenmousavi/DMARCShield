#!/usr/bin/env python3

import os
import smtplib
import dns.resolver
import email.mime.text
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def dmarc_checker():
    domain = input("Enter a domain to check for DMARC record: ")
    try:
        answers = dns.resolver.query('_dmarc.' + domain, 'TXT')
        for rdata in answers:
            if "v=DMARC1" in rdata.strings:
                print("The domain {} is secure by email authentication with DMARC record.".format(domain))
                return
        print("The domain {} does not have a DMARC record.".format(domain))
        print("Please configure DMARC for your domain by following the instructions in the article below:")
        print("https://easydmarc.com/blog/dmarc-step-by-step-guide/")
    except:
        print("The domain {} does not exist or is invalid.".format(domain))

def send_email():
    domain = input("Enter your domain name: ")
    header = input("Enter email header: ")
    body = input("Enter email body: ")
    recipient = input("Enter recipient email address: ")
    sender = input("Enter sender email address: ")

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = header
    message.attach(MIMEApplication(body, 'html'))

    try:
        server = smtplib.SMTP('localhost')
        server.sendmail(sender, recipient, message.as_string())
        print("Email has been sent successfully.")
    except:
        print("Failed to send email.")

if __name__ == '__main__':
    print("Welcome to DMARCSheild, created by Emen Mousavi.")
    while True:
        print("Enter 1 for DMARC Checker")
        print("Enter 2 for Spoofing Email")
        choice = input("Enter your choice (1 or 2): ")
        if choice == '1':
            dmarc_checker()
            break
        elif choice == '2':
            send_email()
            break
        else:
            print("Invalid input, please try again.")
