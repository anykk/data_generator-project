# data_generator
This program generates fictional data about person.
Use method generate from class Generator, if you want import it into your module
or run 'python main.py' in terminal, if u want to use it like script.

# Usage
Example: ~ python main.py person ru male 17658 57
This command generates data about 17658 russian men 57 years old
Use python main.py person -h for more information or python main.py password -h (generate passwords)

# Add new localization
If u want to share this code and add new localization you need:
add json with localization to "data" folder
Structure of loc-package: !PLEASE KEEP THIS STRUCTURE!
{'address':
    {'city': '(...)',
    'street': '(...)'},
'job': '(...)',
'person':
    {'m':
        {'first_name': '(...)',
        'last_name': '(...)'},
    'f':
    {'first_name': '(...)',
    'last_name': '(...)'}}}

