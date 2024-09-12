import re
import argparse
import os


def parse_arguments():
    """
    Lesa inn argument frá skipanalínu
    :return: (ArgumentParser) parser með argumentunum
    """

    parser = argparse.ArgumentParser(description='Leita að netföngum úr skrá.')
    parser.add_argument('--file', required=True,
                        help='Slóð að inntaksskrá með netföngum.')
    return parser.parse_args()


def lesa_skra(file_path):
    """
    Lesa inntaksskrá og skila lista af línum
    :param file_path: (str) Slóð að skrá
    :return:          (list) Listi af línum
    """

    with open(file_path, 'r') as file:
        return file.readlines()


def finna_netfong(text): #Hér á ég að breyta einhverju.
    """
    Leita að netföngum í texta
    r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,3}(?:\.[a-zA-Z]{2,})?$'
    :param text: (list) Listi af línum
    :return:     (list) Listi af netföngum
    """

    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,3}(?:\.[a-zA-Z]{2,})?$' 
    # útilokar ólögleg netföng

    Cp = re.compile(pattern)
    matches_list = []

    for line in text:
        matches = Cp.finditer(line)
        #print(matches)
    
        for match in matches:
                matches_list.append(f"Match: {match.group(0)} @ {match.start()}: {match.end()}") #@
    return matches_list

    
    #raise NotImplementedError("Regluleg segð til að finna netföng hefur ekki verið útfærð.")
    


def prenta_nidurstodur(netfong_listi):
    """
    Prentar út niðurstöður í console
    :param netfong_listi: (list) Listi af netföngum
    :return:              None
    """

    if netfong_listi:
        print("Fundin netföng:")
        for email in netfong_listi:
            print(email)
    else:
        print("Engin netföng fundust.")


def main():
    """
    Keyrslufall sem les inn skrá, leitar að netföngum og prentar niðurstöður.
    :return: None
    """
    args = parse_arguments()

    # Athuga hvort uppgefin skrá sé til
    if not os.path.isfile(args.file):
        print(f"Skráin {args.file} er ekki til.")
        return

    # Lesa texta úr skránni
    text = lesa_skra(args.file)

    # Leita af netföngum með óútfærðri reglulegri segð
    netfong_listi = finna_netfong(text)
    prenta_nidurstodur(netfong_listi)


if __name__ == "__main__":
    main()