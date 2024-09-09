import re
import argparse

def find_kennitolur(file_path, types):
    with open(file_path, 'r') as file:
        text = file.read()

    einstaklingskenn = r'\b[0-3]\d(0\d|1[0-2])\d{2}-[2-9]\d{2}[8,9,0]'
    """
    [0-3] velur fyrsta tölustaf sem getur bara verið á bilinu 0 upp í 3
    \d{5} sex tölustafir á bilinu 0-9
    - strik milli fyrstu 6 og seinni 4 tölustöfum

    """
    fyrirtaekjakenn = r'\b[4-9]\d{5}-\d{4}\b'

    """
    Útskýring fyrir reglulega segð (fyrirtækja):
    \b þýðir byrjun á orði
    \d[4-9] velur tölustaf á bilinu 4 upp í 9
    \d{5} velur 5 tölustafi á bilinu 0-9
    - strik milli fyrstu 6 og seinni 4 tölustafa í kennitölu
    \d{4} velur 4 tölustafi á bilinu 0-9
    \b táknar svo enda orðs (eða talnaröð í þessu tilfelli)
    """
    
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
