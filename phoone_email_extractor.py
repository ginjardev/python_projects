import pyperclip, re

phone_regex = re.compile(r"""(
    (\d{3}|\(\d{3}\))?   #find areacode
    (\s|-|\.)?           #find seperator
    (\d{3})              # first 3 digits
    (\s|-|\.)            # another seperator
    (\d{4})              #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? #extension
)""", re.VERBOSE)

email_regex = re.compile(r"""
    [a-zA-Z0-9_.+]+      #username part
    @                    # @ symbol
    [a-zA-Z0-9_.+]+      #domain name part
    (\.[a-zA-Z]{2,4})    #dot something

""", re.VERBOSE)