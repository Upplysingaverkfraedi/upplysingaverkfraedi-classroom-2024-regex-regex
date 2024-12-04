import re
import requests
import pandas as pd
import argparse


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


def parse_html(html):
    # Notum reglulega segð til að sækja niðurstöður.
    # Það er mögulegt að dálkar eins og Club og Behind séu tómar.
    pattern = r'<tr>\s*<td class="hidden-xs">\s*(\d+)\s*</td>\s*<td>\s*(\d+)\s*</td>\s*<td>\s*([^<]+?)\s*</td>\s*<td class="hidden-xs">\s*(\d+)\s*</td>\s*<td class="hidden-xs">\s*([^<]*)\s*</td>\s*<td>\s*([\d:]+)\s*</td>\s*<td>\s*([^<]*)\s*</td>'

    # Leitum að samsvörun í HTML-inu
    matches = re.findall(pattern, html)

    # Breytum niðurstöðum í lista af orðum
    data = []
    for match in matches:
        rank, bib, name, year, club, time, behind = match
        data.append({
            "Rank": rank,
            " BIB": bib,
            " Name": name,
            " Year": year,
            " Club": club.strip(),
            " Time": time.strip(),
            " Behind": behind.strip() if behind else "N/A"
        })

    return data


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

    html = fetch_html(args.url)
    if not html:
        raise Exception("Ekki tókst að sækja HTML gögn, athugið URL.")

    # Regluleg segð til að tryggja rétt form á slóðinni
        url_pattern = re.compile(r'^https:\/\/(www\.)?timataka\.net\/.+\/urslit\/\?race=\d+&cat=[a-zA-Z]+')
        if not url_pattern.match(args.url):
            print("Slóðin er ekki í réttu formi fyrir timataka.net úrslit.")
            return

    if args.debug:
        html_file = args.output.replace('.csv', '.html')
        with open(html_file, 'w') as file:
            file.write(html)
        print(f"HTML fyrir {args.url} vistað í {html_file}")

    results = parse_html(html)
    skrifa_nidurstodur(results, args.output)


if __name__ == "__main__":
    main()
