import pyperclip, re

phone_regex = re.compile(r"""(
    (\d{3}|\(\d{3}\))?   #find areacode
    (\s|-|\.)?           #find seperator
    (\d{3})              # first 3 digits
    (\s|-|\.)            # another seperator
    (\d{4})              #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? #extension
)""", re.VERBOSE)

email_regex = re.compile(r"""(
    [a-zA-Z0-9_.+]+      #username part
    @                    # @ symbol
    [a-zA-Z0-9_.+]+      #domain name part
    (\.[a-zA-Z]{2,4})    #dot something
)""", re.VERBOSE)

#find matches in clipboard text
text = str(pyperclip.paste())

matches = []

for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])


#copy results to the clipboard
if len(matches) > 0:
    copied= pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
    # print(copied)
else:
    print('No phone numbers or email addresses found.')

