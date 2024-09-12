import os
import argparse
import re


def parse_arguments():
    """
    Lesa inn argument frá skipanalínu
    :return: (ArgumentParser) parser með argumentunum
    """

    parser = argparse.ArgumentParser(description="""Endurraða csv-skrá sem hefur röðunina: 
    1) eiginnafn millinafn kenninafn, 2) heimilisfang, 3) símanúmer.    
    Úttaksskráin verður endurröðuð í tsv röð:
    1) heimilisfang, 2) símanúmer, 3) kenninafn, eigninnafn millinafn.
    """)
    parser.add_argument('--infile', required=True,
                        help='Slóð að inntaksskrá með upplýsingum.')
    parser.add_argument('--outfile', required=True,
                        help='Slóð að úttaksskrá með endurröðuðum upplýsingum.')
    return parser.parse_args()


def lesa_skra(file_path):
    """
    Lesa inntaksskrá og skila lista af línum
    :param file_path: (str) Slóð að skrá
    :return:          (list) Listi af línum
    """

    with open(file_path, 'r') as file:
        return file.readlines()


def endurraða_skra(linur):
    endurröðuðar_linur = []
    for lina in linur:
        # Notum reglulega segð til þess að skipta línunum upp í parta
        pattern = r'([^,]+)\s([^,]+),\s([^,]+),\s([^,]+),\s(.+)'
        match = re.match(pattern, lina.strip())
        if match:
            ## print(len(match.groups()))
            name, last_name, address, address1, phone_number = match.groups()
            ## print(f"{name}, {last_name}, {address}, {phone_number}")

            
            # Sameinum partana í réttri röð
            endurröðuð_lina = '\t'.join([address, address1, phone_number, f'{last_name}, {name}'])
            endurröðuðar_linur.append(endurröðuð_lina)

    return endurröðuðar_linur

def skrifa_nidurstodur(output_file, linur):
    """
    Skrifar niðurstöður í úttaksskrá
    :param output_file: (str) Slóð að úttaksskrá
    :param linur:       (list) Listi af línum
    :return:            None
    """
    with open(output_file, 'w') as file:
        for lina in linur:
            file.write(lina + '\n')


def main():
    """
    Keyrslufall sem les inn skrá, endurraðar henni og skrifar niðurstöður í nýja skrá.
    :return: None
    """

    args = parse_arguments()

    # Athuga hvort skráar endingar séu réttar
    if not args.infile.endswith('.csv'):
        print('Inntaksskrá þarf að vera csv skrá.')
        return
    if not args.outfile.endswith('.tsv'):
        print('Úttaksskrá þarf að vera tsv skrá.')
        return
    # Athuga hvort inntaksskrá sé til
    if not os.path.exists(args.infile):
        print('Inntaksskrá fannst ekki.')
        return

    # Lesa línur úr skránni
    linur = lesa_skra(args.infile)

    # Endurraða hverri línu í skránni
    linur = endurraða_skra(linur)

    # Skrifa niðurstöðurnar í nýja skrá
    skrifa_nidurstodur(args.outfile, linur)


if __name__ == "__main__":
    main()