"""This program finds domain's registration expiration date at https://who.is
with the help of urllib library. User is asked to enter root domain. RegEx is
used to match the date. Expiration date is being displayed.

Input:
    root_domain (str)

Output:
    expiration (str)

Example:
    Enter root domain:
    sav.com

    Registrar Registration Expiration Date:
    2021-08-10.

References:
    * regex module documentation:
        https://docs.python.org/3/library/re.html

"""
from urllib.request import urlopen
import re


def get_root_domain():
    """Get root domain from the user.

    Args: none
    Returns: root_domain (str)

    """
    print("Enter root domain:")
    root_domain = input()
    return root_domain


def create_lookup_url(root_domain):
    """Concatenate root domain to who.is.

    Args: root_domain (str)
    Returns: lookup_url (str)

    """
    whois = "https://who.is/whois/"
    lookup_url = whois + root_domain
    return lookup_url


def read_webpage(lookup_url):
    """Read webpage and convert it to string using utf-8 encoding.

    Args: lookup_url (str)
    Returns: html (str)

    """
    with urlopen(lookup_url) as site_info:
        html = site_info.read()
        html = str(html, 'utf-8')
    return html


def find_expiration(html):
    """Use RegEx pattern to find expiration date on the page.

    Args: html (str)
    Returns: expiration (str)

    """
    expiration = re.findall(r'.*<div .*>Expires On<\/div>\n.*<div .*>' +
                            r'(\d{4}-\d{2}-\d{2})<\/div>', html)
    expiration = expiration[0]
    return expiration


def display_expiration(expiration):
    """Display expiration date.

    Args: expiration (str)
    Returns: none

    """
    print(f"\nRegistrar Registration Expiration Date:\n{expiration}.")


def main():
    root_domain = get_root_domain()
    lookup_url = create_lookup_url(root_domain)
    html = read_webpage(lookup_url)
    expiration = find_expiration(html)
    display_expiration(expiration)


main()
