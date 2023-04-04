# DMARCShield
![Logo](https://github.com/emenmousavi/DMARCShield/blob/main/logo.png)

DMARCShield is a Python program for email authentication and security. It offers a DMARC checker to ensure domain security, and a spoofing email sender to test for vulnerabilities. Protect your email communication and keep your domain safe with DMARCShield.


## Description
This is a Python program that allows the user to choose between two options:

1. DMARC Checker - the user enters a domain and the program checks if it has a DMARC record. If it does, it outputs that the domain is secure by email. If not, it provides instructions on how to configure DMARC for the domain.
2. Spoofing Email Sender - the user enters a domain, email header, email body text, recipient email, and sender email. The program attempts to send a spoofed email using the inputted domain. If successful, it outputs that the email has been sent. If not, it outputs that it was unable to send the email.


## Getting Started
### Dependencies
- Python 3.x
- pip
- The following packages: dns.resolver, smtplib, email, and argparse.


### Installing
- Clone the repository to your local machine.
- Install Python 3.x.
- Install pip.
- Run the following command to install the required packages:
```sh
pip install -r requirements.txt
```

### Executing program
- Navigate to the project directory.
- Run the following command to start the program:
```sh
python main.py
```
- Choose between option 1 (DMARC Checker) and option 2 (Spoofing Email Sender).
- Follow the prompts to enter the required information for the chosen option.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/emenmousavi/DMARCShield/blob/main/LICENSE) file for details.

## Output Example
- Screenshot of a DMARC Checker

![Screenshot of a DMARC Checker](https://github.com/emenmousavi/DMARCShield/blob/main/1.png)


- Screenshot of Spoofing Email

![Screenshot of Spoofing Email](https://github.com/emenmousavi/DMARCShield/blob/main/2.png)
