import re
import pandas as pd
import requests
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Vinna með úrslit af tímataka.net.')
    parser.add_argument('--url', required=True, help='Slóð að vefsíðu með úrslitum.')
    parser.add_argument('--output', required=True, help='Slóð að útgangsskrá til að vista niðurstöðurnar (CSV format).')
    parser.add_argument('--debug', action='store_true', help='Vistar html í skrá til að skoða.')
    return parser.parse_args()

# Sækir HTML efni frá gefnu URL
def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Tókst ekki að sækja gögn af {url}")
        return None

# Greinir út hvort taflan sé einstaklings-, liðakeppni eða hraðatafla út frá höfuðgögnum

def detect_format(html):
    if re.search(r'\bTeam\b', html, re.IGNORECASE):
        return 'team'
    elif re.search(r'\bPace\b', html, re.IGNORECASE):
        return 'pace'
    elif re.search(r'\bBehind\b', html, re.IGNORECASE):
        return 'individual'
    else:
        return 'unknown'

# Parsear niðurstöður fyrir einstaklingskeppni
def parse_individual_results(html):
    names = re.findall(r'<td[^>]*class="name"[^>]*>(.*?)<\/td>', html)
    years = re.findall(r'<td[^>]*class="year"[^>]*>(.*?)<\/td>', html)
    clubs = re.findall(r'<td[^>]*class="club"[^>]*>(.*?)<\/td>', html)
    times = re.findall(r'<td[^>]*class="time"[^>]*>(.*?)<\/td>', html)
    behind = re.findall(r'<td[^>]*class="behind"[^>]*>(.*?)<\/td>', html)

    results = []
    for i in range(len(names)):
        results.append({
            'Keppandi': names[i].strip(),
            'Ár': years[i].strip(),
            'Klúbbur': clubs[i].strip(),
            'Tími': times[i].strip(),
            'Á eftir': behind[i].strip() if i < len(behind) else 'N/A'
        })
    return results

# Parsear niðurstöður fyrir liðakeppni
def parse_team_results(html):
    teams = re.findall(r'<td[^>]*class="team"[^>]*>(.*?)<\/td>', html)
    members = re.findall(r'<td[^>]*class="members"[^>]*>(.*?)<\/td>', html, re.DOTALL)
    splits = re.findall(r'<td[^>]*class="split"[^>]*>(.*?)<\/td>', html, re.DOTALL)
    times = re.findall(r'<td[^>]*class="time"[^>]*>(.*?)<\/td>', html)

    results = []
    for i in range(len(teams)):
        split_time = splits[i] if i < len(splits) else 'N/A'
        results.append({
            'Lið': teams[i].strip(),
            'Meðlimir': re.sub(r'\s+', ' ', members[i].strip()),
            'Splits': split_time.strip(),
            'Tími': times[i].strip(),
        })
    return results

# Parsear niðurstöður þar sem hraði er notaður (pace results)
def parse_pace_results(html):
    names = re.findall(r'<td[^>]*class="name"[^>]*>(.*?)<\/td>', html)
    ages = re.findall(r'<td[^>]*class="age"[^>]*>(.*?)<\/td>', html)
    final_times = re.findall(r'<td[^>]*class="final"[^>]*>(.*?)<\/td>', html)
    paces = re.findall(r'<td[^>]*class="pace"[^>]*>(.*?)<\/td>', html)

    results = []
    for i in range(len(names)):
        results.append({
            'Keppandi': names[i].strip(),
            'Aldur': ages[i].strip(),
            'Lokastaða': final_times[i].strip(),
            'Hraði': paces[i].strip()
        })
    return results

# Velur rétta aðferð til að parsea HTML út frá því hvaða gögn eru til staðar
def parse_html(html):
    format_type = detect_format(html)
    
    if format_type == 'individual':
        return parse_individual_results(html)
    elif format_type == 'team':
        return parse_team_results(html)
    elif format_type == 'pace':
        return parse_pace_results(html)
    else:
        raise ValueError("Óþekkt form gagna.")

# Skrifar niðurstöður í CSV skrá
def skrifa_nidurstodur(data, output_file):
    if not data:
        print("Engar niðurstöður til að skrifa.")
        return

    df = pd.DataFrame(data)
    df.to_csv(output_file, sep=',', index=False)
    print(f"Niðurstöður vistaðar í '{output_file}'.")

# Aðalforritið sem tengir saman alla aðgerðina
def main():
    args = parse_arguments()

    if not args.output.endswith('.csv'):
        print(f"Inntaksskráin {args.output} þarf að vera csv skrá.")
        return

    # Sækir HTML efni
    html = fetch_html(args.url)
    if not html:
        raise Exception("Ekki tókst að sækja HTML gögn, athugið URL.")

    if args.debug:
        html_file = args.output.replace('.csv', '.html')
        with open(html_file, 'w') as file:
            file.write(html)
        print(f"HTML fyrir {args.url} vistað í {html_file}")

    # Parsear HTML út frá því hvaða gögn eru til staðar
    results = parse_html(html)

    # Skrifar niðurstöður í CSV skrá
    skrifa_nidurstodur(results, args.output)

if __name__ == "__main__":
    main()