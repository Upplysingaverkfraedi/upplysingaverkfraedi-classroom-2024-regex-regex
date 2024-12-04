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
    1) heimilisfang, 2) símanúmer, 3) kenninafn, eiginnafn millinafn.
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
    """
    Endurraðar línum úr csv skrá í tsv skrá í réttri röð:
    Heimilisfang, Símanúmer, Kenninafn, Eiginnafn Millinafn.
    :param linur: (list) Listi af línum úr inntaksskrá
    :return:      (list) Listi af endurröðuðum línum
    """
    nytt_linuformat = []

    for lina in linur:
        # Nota reglulega segð til að finna nafn, heimilisfang og símanúmer
        # Hér virka einfaldar stafarhúgur aðskildar af kommum
        pattern = r"^(.*?),\s*(.*\s+\d{3}\s+[^\s]+),\s*(\d{3}-\d{4})$"
        match = re.match(pattern, lina.strip())
        
        if match:
            nafn, heimilisfang, simanumer = match.groups()

            heimilisfang = heimilisfang.replace(",", "")
            
            # Skipta nafni í eiginnafn, millinafn og kenninafn
            nafn_partar = nafn.split()
            if len(nafn_partar) == 2:  # Bara eiginnafn og kenninafn
                eiginnafn = nafn_partar[0]
                kenninafn = nafn_partar[1]
                millinafn = ""
            elif len(nafn_partar) == 3:  # Eiginnafn, millinafn og kenninafn
                eiginnafn = nafn_partar[0]
                millinafn = nafn_partar[1]
                kenninafn = nafn_partar[2]
            else:
                raise ValueError("Óvæntur fjöldi nafna")

            fullt_nafn = f"{kenninafn}, {eiginnafn} {millinafn}".strip()
            
            # Búa til nýja línu með tab (\t) í stað kommu nema fyrir kenninafn
            ny_lina = f"{heimilisfang}\t\t{simanumer}\t{fullt_nafn}"
            nytt_linuformat.append(ny_lina)

    return nytt_linuformat


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
