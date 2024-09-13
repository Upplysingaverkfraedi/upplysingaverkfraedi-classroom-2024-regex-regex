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


def finna_netfong(text):
    """
    Leita að netföngum í texta
    :param text: (list) Listi af línum
    :return:     (list) Listi af netföngum
    """
    # Regluleg segð fyrir netföng, fyrst kemur texti af óþekktri lengd sem er stoppaður af "@", svo meiri texti stoppaður af punkti
    # og loks domain textinn sem getur innihaldið aukapunkt og aukatexta
    email_pattern = r'[a-zA-Z0-9þæð_.+-]+@[a-zA-Z0-9þæð-]{1,63}\.[a-zA-Z]{2,6}(?:\.[a-zA-Z]{2,6})?$'


    # Listi til að geyma öll fundin netföng
    netfong_listi = []
    
    for line in text:
        # Finna öll netföng í hverri línu og bæta þeim við lista
        found_emails = re.findall(email_pattern, line)
        netfong_listi.extend(found_emails)
    
    return netfong_listi


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

    # Leita af netföngum með reglulegri segð
    netfong_listi = finna_netfong(text)
    prenta_nidurstodur(netfong_listi)


if __name__ == "__main__":
    main()
