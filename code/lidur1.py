import re
import argparse

# Regular expressions for Icelandic IDs
regex_einstaklingar = r'\b[0-3]\d(?:0[1-9]|1[0-2])\d{2}-[2-9]\d{2}[089]\b'
regex_fyrirtaeki = r'\b[4-9]\d{5}-\d{4}\b'

def lesa_skra(skra_nafn):
    with open(skra_nafn, 'r', encoding='utf-8') as file:
        return file.read()

def finna_kt(texti, regex):
    return re.findall(regex, texti)

def prenta_nidurstodur(nidurstodur, lysing):
    if nidurstodur:
        print(f"{lysing}:")
        for kt in nidurstodur:
            print(kt)
    else:
        print(f"Engar {lysing.lower()} fundust.")

def main():
    parser = argparse.ArgumentParser(description="Leita að kennitölum.")
    parser.add_argument("--file", required=True, help="Skrá til að lesa texta úr.")
    parser.add_argument("--einstaklingar", action="store_true", help="Leita að kennitölum einstaklinga.")
    parser.add_argument("--fyrirtaeki", action="store_true", help="Leita að kennitölum fyrirtækja.")
    
    args = parser.parse_args()

    texti = lesa_skra(args.file)

    if args.einstaklingar:
        einstaklinga_kt = finna_kt(texti, regex_einstaklingar)
        prenta_nidurstodur(einstaklinga_kt, "Kennitölur einstaklinga")

    if args.fyrirtaeki:
        fyrirtækja_kt = finna_kt(texti, regex_fyrirtaeki)
        prenta_nidurstodur(fyrirtækja_kt, "Kennitölur fyrirtækja")

if __name__ == "__main__":
    main()













