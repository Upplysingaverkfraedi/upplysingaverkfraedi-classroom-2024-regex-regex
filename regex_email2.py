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

      # Regluleg segð til að finna lögleg netföng
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]{1,63}\.[a-zA-Z]{2,6}(?:\.[a-zA-Z]{2,6})*$'

    """
    [a-zA-Z0-9_.+-]: Notendanafnið (fyrir @). Leyfir litla og stóra stafi, tölur frá 0-9, undirstrik, punkt og plús og mínus

    +: Táknar að einn eða fleiri stafir eru aðeins leyfilegar (þannig að þetta sé ekki tómt)

    @[a-zA-Z0-9-]: leyfir litla og stóra stafi í domain, tölustafi frá 0-9 og bandstrik. En bandstrik er ekki leyft fyrst eða seinast.

    {1,63}: Domainið getur innihaldið 1-63 stafi samkv standard emaili

    \.: Setur punkt þarna á milli (t.d hi.is)

    [a-zA-Z]{2,6}: Leyfir bara stóra og litla bókstafi og passar að það séu 2-6 stafir. 
    
    (?: ..): Þetta er optional eins og email getur verið xx@hi.is eða xx@explorer.co.uk

    
    """


    # Listi til að geyma fundin netföng
    fundin_netfong = []
    
    # Leita að netföngum í hverri línu
    for line in text:
        line = line.strip()  # Fjarlægjum óþarfa bil
        if re.match(pattern, line):
            fundin_netfong.append(line)

    return fundin_netfong


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