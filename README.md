# data_generator
This program generates fictional data about person.
Use method generate from class Generator, if you want import it into your module
or run 'python main.py' in terminal, if u want to use it like script.

# Usage
Example: ~ python main.py person ru m 17658 57
This command generates data about 17658 russian men 57 years old
Use python main.py person -h for more information or python main.py password -h (generate passwords)

# Add new localization
If u want to share this code and add new localization you need:
1) add package with localization to data-package
Structure of loc-package: !PLEASE KEEP THIS STRUCTURE!
----loc
--------address (city_names, street_titles)
--------job (jobs)
--------person (first_names_fe/male, last_names_fe/male)
2) add loc into dictionary of data (generator.py ---> pds)