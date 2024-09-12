import requests
import pandas as pd
import argparse
import re


def parse_arguments():
    parser = argparse.ArgumentParser(description='Vinna með úrslit af tímataka.net.')
    parser.add_argument('--url', help='Slóð að vefsíðu með úrslitum.')
    parser.add_argument('--output', required=True,
                        help='Slóð að útgangsskrá til að vista niðurstöðurnar (CSV format).')
    parser.add_argument('--debug', action='store_true',
                        help='Vistar html í skrá til að skoða.')
    return parser.parse_args()


def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Tókst ekki að sækja gögn af {url}")
        return None

def is_valid_url(url):
    pattern = re.compile(r'https://(www\.)?timataka\.net/.+?/urslit/\?race=\d+&cat=[a-z]+(&age=\d+)?')
    return re.match(pattern, url) is not None


def parse_html(html):
    """
    Vinnur úr HTML með reglulegri segð og finnur keppnisnúmer, nöfn keppenda og tíma
    """
    pattern = re.compile(r'<tr>\s*<td>(?P<rank>\d+)</td>\s*<td>(?P<name>.+?)</td>\s*<td>(?P<ime>\d{1,2}:\d{2}:\d{2})</td>\s*<td>(?P<category>.+?)</td>', re.DOTALL)

    results = []
    for match in re.finditer(pattern, html):
        results.append(match.groupdict())

    return results

    raise NotImplementedError("Eftir að útfæra reglulega segð sem vinnur úr HTML gögnum.")


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

    df = pd.DataFrame(data)
    df.to_csv(output_file, sep=',', index=False)
    print(f"Niðurstöður vistaðar í '{output_file}'.")


def main():
    args = parse_arguments()

    if not args.output.endswith('.csv'):
        print(f"Inntaksskráin {args.output} þarf að vera csv skrá.")
        return

    if not is_valid_url(args.url):
        print("Slóðin er ekki frá tímataka.net eða er ekki í réttu formi.")
        return
    
    html = fetch_html(args.url)
    if not html:
        raise Exception("Ekki tókst að sækja HTML gögn, athugið URL.")

    if args.debug:
        html_file = args.output.replace('.csv', '.html')
        with open(html_file, 'w') as file:
            file.write(html)
        print(f"HTML fyrir {args.url} vistað í {html_file}")

    results = parse_html(html)
    skrifa_nidurstodur(results, args.output)


if __name__ == "__main__":
    main()
