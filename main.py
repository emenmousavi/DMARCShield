#!/usr/bin/env python3

import os
import smtplib
import dns.resolver
import socket
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import pydmarc


def check_dmarc():
    """Checks if a domain has a DMARC record."""
    domain = input("Enter a domain to check for DMARC record: ")
    try:
        answers = dns.resolver.query('_dmarc.' + domain, 'TXT')
        for rdata in answers:
            if "v=DMARC1" in rdata.strings:
                dmarc_record = pydmarc.DmarcRecord(rdata.strings[0])
                policy = dmarc_record.policy
                reporting_options = dmarc_record.reporting_options
                print(f"The domain {domain} has a DMARC record with policy {policy} and reporting options {reporting_options}.")
                return
        print(f"The domain {domain} does not have a DMARC record.")
        print("Please configure DMARC for your domain by following the instructions in the article below:")
        print("https://easydmarc.com/blog/dmarc-step-by-step-guide/")
    except dns.resolver.NXDOMAIN:
        print(f"The domain {domain} does not exist.")
    except dns.resolver.NoAnswer:
        print(f"The domain {domain} does not have a DMARC record.")
    except Exception as e:
        print(f"Failed to check DMARC record for {domain}: {e}")


def send_email():
    """Sends an email from a given domain."""
    domain = input("Enter your domain name: ")
    header = input("Enter email header: ")
    body = input("Enter email body: ")
    recipient = input("Enter recipient email address: ")
    sender = input("Enter sender email address: ")

    try:
        # Validate domain name
        domain_parts = domain.split('.')
        if len(domain_parts) < 2:
            raise ValueError("Invalid domain name")
        
        # Validate email addresses
        if not recipient or not sender:
            raise ValueError("Invalid email address")
        
        # Check if domain has DMARC record
        answers = dns.resolver.query('_dmarc.' + domain, 'TXT')
        for rdata in answers:
            if "v=DMARC1" not in rdata.strings:
                raise ValueError("DMARC record not found")
        
        # Check SPF and DKIM records
        # ...
        
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = recipient
        message['Subject'] = header
        message.attach(MIMEApplication(body, 'html'))

        server = smtplib.SMTP('localhost')
        server.sendmail(sender, recipient, message.as_string())
        print("
