import re
import argparse

def find_kennitolur(file_path, types):
    with open(file_path, 'r') as file:
        text = file.read()

    einstaklingskenn = r'\b[0-3]\d(0\d|1[0-2])\d{2}-[2-9]\d{2}[8,9,0]'
    fyrirtaekjakenn = r'\b[4-9]\d{5}-\d{4}\b'    
    if 'einstaklingar' in types:
        print("Einstaklingar:")
        for match in re.finditer(einstaklingskenn, text):
            print(match.group())
    
    if 'fyrirtaeki' in types:
        print("Fyrirtæki:")
        for match in re.finditer(fyrirtaekjakenn, text):
            print(match.group())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Leita að kennitölum")
    parser.add_argument('--file', type=str, required=True, help='Skrá með texta til að leita í')
    parser.add_argument('--einstaklingar', action='store_true', help='Leita að kennitölum einstaklinga')
    parser.add_argument('--fyrirtaeki', action='store_true', help='Leita að kennitölum fyrirtækja')
    args = parser.parse_args()
    
    types = []
    if args.einstaklingar:
        types.append('einstaklingar')
    if args.fyrirtaeki:
        types.append('fyrirtaeki')
    
    find_kennitolur(args.file, types)
