```markdown
# Tímataka keppnisgögn - Vinna úr úrslitum með Python

Þessi forritsverkefni sækir og vinnur úr keppnisgögnum af vefsíðunni **tímataka.net**. Það notar reglulegar segðir til að vinna úr staðsetningu, BIB-númeri, nafni og keppnistíma keppenda og vistar þau í CSV-skrá.

## Kröfur

Til að keyra þetta verkefni þarftu:
- **Python 3**
- Nokkrir Python pakkar (tilgreindir í skrefunum hér fyrir neðan)

## Skref 1: Setja upp sýndarumhverfi (virtual environment)

1. **Búðu til nýtt Python sýndarumhverfi**. Þetta gerir þér kleift að halda öllum ósamræmdum pakkaversjónum á hreinu.

```bash
python3 -m venv venv
```

2. **Virkjaðu sýndarumhverfið**:

Á macOS/Linux:

```bash
source venv/bin/activate
```

Á Windows:

```bash
venv\Scripts\activate
```

## Skref 2: Setja upp nauðsynlega pakka

Núna þarftu að setja upp alla nauðsynlega pakka, sem eru tilgreindir hér:

```bash
pip install requests pandas
```

## Skref 3: Keyra kóðann

Forritið notar **argparse** til að taka á móti slóð (URL) að vefsíðu með úrslitum, og staðsetningu til að vista CSV-skrána með niðurstöðum. Einnig geturðu valfrjálst gefið upp slóð til að vista metadata og stillt forritið á debug-ham.

### Dæmi um keyrslu

```bash
python script.py --url 'https://timataka.net/bruarhlaupid2024/urslit/?race=2&cat=m&age_from=18&age_to=39' --output results.csv
```

Þetta dæmi sækir gögnin fyrir keppnina **Brúarhlaupið 2024** og vistar keppnisniðurstöður í CSV-skránni **`results.csv`**.

### Valfrjálst: Notkun debug-hams

Ef þú vilt vista HTML-skrána til frekari skoðunar, geturðu keyrt forritið með **--debug**:

```bash
python script.py --url 'https://timataka.net/bruarhlaupid2024/urslit/?race=2&cat=m&age_from=18&age_to=39' --output results.csv --debug
```

Þetta mun einnig vista HTML-skrána sem **`results.html`**.

### Valfrjálst: Vistun metadata

Ef þú vilt vista metadata fyrir keppnina í JSON eða CSV formi, geturðu notað **--metadata_output**:

```bash
python script.py --url 'https://timataka.net/bruarhlaupid2024/urslit/?race=2&cat=m&age_from=18&age_to=39' --output results.csv --metadata_output metadata.json
```

Þetta mun vista metadata eins og keppnisnafn, dagsetningu, keppnisflokk, og slóð á niðurstöður í **`metadata.json`**.

### Nauðsynlegir pakkar:

- **requests**: Notað til að sækja HTML frá vefsíðum.
- **pandas**: Notað til að vista niðurstöður í CSV-skrá.

## Skref 4: Útskráning úr sýndarumhverfi

Eftir að þú hefur keyrt kóðann og unnið úr niðurstöðunum, geturðu útskráð þig úr sýndarumhverfinu með:

```bash
deactivate
```



### Skýringar á skrefunum í **README.md**:
1. **Skref 1:** Býr til nýtt sýndarumhverfi til að einangra pakkauppsetningar.
2. **Skref 2:** Setur upp **`requests`** og **`pandas`**, sem eru nauðsynlegir pakkar til að sækja gögn og vinna úr þeim í CSV-formi.
3. **Skref 3:** Útskýrir hvernig á að keyra forritið með slóð að keppninni og vista niðurstöður. Býður einnig upp á möguleika til að vista HTML og metadata.
4. **Skref 4:** Útskráning úr sýndarumhverfinu eftir notkun.