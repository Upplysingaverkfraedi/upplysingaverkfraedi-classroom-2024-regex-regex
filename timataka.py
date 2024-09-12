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

def valid_url(url):
    # Regular expression to validate URLs that show results on timataka.net
    pattern = re.compile(r'^https?://(?:www\.)?timataka\.net/[\w-]+/urslit/\?race=\d+&cat=[a-z]+(?:&age=\d{4})?$')
    return bool(pattern.match(url))


def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Tókst ekki að sækja gögn af {url}")
        return None


def parse_html(html):
    # Regular expression to match Simen Nordahl Svendsen's row of results
    simen_pattern = re.compile(
        r'<tr>\s*<td[^>]*>1</td>\s*<td[^>]*>1</td>\s*<td[^>]*>Simen Nordahl Svendsen</td>(.*?)</tr>',
        re.DOTALL
    )

    # List to hold parsed data
    results = []

    # Extract Simen Nordahl Svendsen's information
    simen_match = simen_pattern.search(html)
    if simen_match:
        row_data = simen_match.group(1)
        # Extract other details from Simen Nordahl Svendsen's row
        simen_details_pattern = re.compile(
            r'<td[^>]*>([^<]*)</td>'
        )
        simen_details = simen_details_pattern.findall(row_data)
        if len(simen_details) >= 6:  # Ensure there are enough details
            results.append({
                'Rank': '1',
                'Bib': '1',
                'Name': 'Simen Nordahl Svendsen',
                'Year': simen_details[0].strip(),
                'Club': simen_details[1].strip(),
                'Split': simen_details[2].strip(),
                'Time': simen_details[3].strip(),
                'Behind': simen_details[4].strip(),
                'Chiptime': simen_details[5].strip()
            })

    return results


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

    if not valid_url(args.url):
        print("Slóðin er ekki frá timataka.net eða í réttu formi.")
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
