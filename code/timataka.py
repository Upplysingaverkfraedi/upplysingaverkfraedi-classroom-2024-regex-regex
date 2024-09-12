import re
import requests
import pandas as pd
import argparse
import json
from datetime import datetime

# Skilgreining á parse_arguments fallinu til að sækja valmöguleika
def parse_arguments():
    parser = argparse.ArgumentParser(description='Vinna með úrslit af tímataka.net.')
    parser.add_argument('--url', help='Slóð að vefsíðu með úrslitum.')
    parser.add_argument('--output', required=True,
                        help='Slóð að útgangsskrá til að vista niðurstöðurnar (CSV format).')
    parser.add_argument('--debug', action='store_true',
                        help='Vistar html í skrá til að skoða.')
    parser.add_argument('--metadata_output', required=False,
                        help='Slóð til að vista metadata í CSV eða JSON formi.')
    return parser.parse_args()


# Fall sem sækir HTML frá tilgreindri slóð
def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Tókst ekki að sækja gögn af {url}")
        return None


# Reglulegar segðir til að vinna úr HTML og sækja keppendagögn
def parse_html(html):
    # Regluleg segð sem vinnur úr stöðu, BIB-númeri, nafni og tíma keppenda
    pattern = re.compile(
        r'<tr.*?>.*?<td.*?>(\d+)</td>.*?<td.*?>(\d+)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(\d{2}:\d{2}:\d{2})</td>', re.S)

    results = []
    for match in pattern.finditer(html):
        place = match.group(1).strip()  # Staða keppanda
        bib = match.group(2).strip()  # BIB-númer keppanda
        name = match.group(3).strip()  # Nafn keppanda
        time = match.group(4).strip()  # Tími keppanda
        results.append([place, bib, name, time])

    return results


# Fall til að skrifa niðurstöður í CSV-skrá
def skrifa_nidurstodur(data, output_file):
    """
    Skrifar niðurstöður í úttaksskrá.
    :param data:        (list) Listi af línum
    :param output_file: (str) Slóð að úttaksskrá
    :return:            None
    """
    if not data:
        print("Engar niðurstöður til að skrifa.")
        return


    df = pd.DataFrame(data, columns=['Place', 'BIB', 'Name', 'Time'])
    df.to_csv(output_file, sep=',', index=False)
    print(f"Niðurstöður vistaðar í '{output_file}'.")


# Fall til að skrifa metadata í CSV eða JSON
def skrifa_metadata(output_file, url):
    """
    Skrifar metadata fyrir keppnina.
    :param output_file: Slóð að metadata skrá (JSON eða CSV).
    :param url: Slóðin sem gögnin voru sótt af.
    :return: None
    """
    metadata = {
        'Race Name': 'Brúarhlaupið 2024',
        'Date': '2024-09-01',  # Þú getur uppfært þetta með raunverulegri dagsetningu ef hún er í gögnunum
        'Category': 'Male, Age 18-39',
        'URL': url,
        'Downloaded At': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    # Ákveða hvort metadata skráin á að vera CSV eða JSON út frá endingunni
    if output_file.endswith('.json'):
        with open(output_file, 'w') as f:
            json.dump(metadata, f, indent=4)
    elif output_file.endswith('.csv'):
        df = pd.DataFrame([metadata])
        df.to_csv(output_file, index=False)
    else:
        print("Óþekkt skráarsnið fyrir metadata. Vinsamlega notið .json eða .csv.")
        return

    print(f"Metadata vistað í '{output_file}'.")


# Aðalfallið sem keyrir ferlið
def main():
    args = parse_arguments()

    if not args.output.endswith('.csv'):
        print(f"Inntaksskráin {args.output} þarf að vera csv skrá.")
        return

    if not 'timataka.net' in args.url:
        print("Slóðin er ekki frá timataka.net")
        return

    html = fetch_html(args.url)
    if not html:
        raise Exception("Ekki tókst að sækja HTML gögn, athugið URL.")

    if args.debug:
        html_file = args.output.replace('.csv', '.html')
        with open(html_file, 'w') as file:
            file.write(html)
        print(f"HTML fyrir {args.url} vistað í {html_file}")

    # Vinna úr HTML gögnunum og skila niðurstöðum
    results = parse_html(html)

    # Skrifa niðurstöðurnar í CSV skrá
    skrifa_nidurstodur(results, args.output)

    # Skrifa metadata skrá ef slóð er gefin upp
    if args.metadata_output:
        skrifa_metadata(args.metadata_output, args.url)


if __name__ == "__main__":
    main()

# python timataka.py --url 'https://timataka.net/bruarhlaupid2024/urslit/?race=2&cat=m&age_from=18&age_to=39' --output results.csv --metadata_output metadata.json
