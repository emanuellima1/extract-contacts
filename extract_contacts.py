#!/usr/bin/env python3

import pandas as pd
import sys
import re

def main():
    if len(sys.argv) != 3:
        print("Aborting due to incorrect usage!")
        print("Use: extract_contacts.py [FILE] [STRING]")
        sys.exit(1)

    contacts_file = sys.argv[1]
    string = sys.argv[2]
    telephone = ""
    results = {}

    with open(contacts_file, "r") as file:
        for line in file:
            match = re.match(f"^FN:{string}(.*)SP$", line)
            if match:
                dirty_telephone = next(file)
                telephone = clean_string(dirty_telephone)
                results[line[3:].strip("\n")] = telephone

    data = pd.DataFrame(results.items(), columns=["Arquitetos", "Telefone"])
    data.to_excel("arquitetos.xlsx") 

def clean_string(dirty_string):
    """
    (str) -> str
    Removes all non-numeric characters from a string.
    """
    clean = ""

    for char in dirty_string:
        if char.isdigit():
            clean += char
    
    if clean[:2] == "55":
        return clean[2:]
    elif clean[:3] == "041":
        return clean[3:]
    else:
        return clean

if __name__ == "__main__":
    main()
