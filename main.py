import dns.resolver

def has_dkim_record(domain):
    try:
        dns.resolver.query(f"_adsp._domainkey.{domain}", 'TXT')
        return True
    except dns.resolver.NoAnswer:
        return False
    except Exception as e:
        print(f"An unexpected error occurred while checking for DKIM record: {e}")
        return False

def is_domain_secure(domain):
    resolver = dns.resolver.Resolver()
    resolver.timeout = 1
    resolver.lifetime = 1

    try:
        spf_found = False
        spf_record = resolver.query(domain, 'TXT')
        for rdata in spf_record:
            if 'v=spf1' in rdata.strings:
                spf_found = True
                break
        dmarc_found = False
        dmarc_record = resolver.query(f"_dmarc.{domain}", 'TXT')
        for rdata in dmarc_record:
            if 'v=DMARC1' in rdata.strings:
                dmarc_found = True
                break
        return spf_found and has_dkim_record(domain) and dmarc_found
    except dns.resolver.NXDOMAIN:
        print(f"The domain {domain} does not exist.")
        return False
    except dns.resolver.NoAnswer:
        print(f"No TXT record found for {domain}.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred while checking domain security: {e}")
        return False

def check_domain_security(domain):
    if is_domain_secure(domain):
        print(f"{domain} is secured properly with SPF, DKIM, and DMARC.")
    else:
        print(f"{domain} is not secured properly with SPF, DKIM, and DMARC.")

domain = input("Enter a domain to check: ")
if domain:
    check_domain_security(domain.strip())
else:
    print("Please enter a valid domain.")
