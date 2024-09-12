[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/CMNHJo7M)
# Reglulegar segðir (Regular Expressions)

Þetta verkefni inniheldur fjögur mismunandi Python forrit sem framkvæma sérhæfðar aðgerðir með gagnasettum, nota reglulegar segðir og mismunandi skráarform.

## Lausn 1: Leita að kennitölum einstaklinga eða fyrirtækja

Þetta forrit tekur við inntaksskrá og leitar að kennitölum einstaklinga eða fyrirtækja. Það styður eftirfarandi valkosti:
- `--file`: Slóð að inntaksskrá sem inniheldur kennitölur.
- `--einstaklingar`: Leita að kennitölum einstaklinga.
- `--fyrirtaeki`: Leita að kennitölum fyrirtækja.

Keyrsla forrits:
```bash
python3 code/regex_kt.py --file data/kt.txt --einstaklingar
python3 code/regex_kt.py --file data/kt.txt --fyrirtaeki 
python3 code/regex_kt.py --file data/kt.txt --fyrirtaeki --einstaklingar
```
---

## Lausn 2: Leita að netföngum úr skrá

Þetta forrit les inntaksskrá með textagögnum og leitar að netföngum í textanum. Forritið styður eftirfarandi valkost:
- `--file`: Slóð að inntaksskrá með netföngum.

Keyrsla forrits:

```bash
python3 code/regex_email.py --file data/email.txt
```
---

## Lausn 3: Endurraða upplýsingum úr CSV í TSV

Þetta forrit tekur inn CSV skrá sem inniheldur nöfn, heimilisföng og símanúmer. Það endurraðar gögnunum í tsv-skrá með reglulegri segð í eftirfarandi röð:
- Heimilisfang
- Staður og póstnúmer
- Símanúmer
- Kenninafn, eiginnafn og millinafn
- Til þess að keyra forritið má notast við þessa skipun í terminal: 
```bash
python3 code/regex_reorder.py --infile data/nafn_heimilisfang_simanumer.csv --outfile data/heimilisfang_simanumer_nafn.tsv  
```

---

## Lausn 4: Greina keppnisúrslit af tímataka.net

Þetta forrit sækir keppnisúrslit frá tímataka.net, vinnur úr HTML gögnunum og vistar niðurstöðurnar í CSV formi. Það styður eftirfarandi valkosti:
- `--url`: Slóð að vefsíðu með keppnisúrslitum.
- `--output`: Slóð að útgangsskrá til að vista niðurstöðurnar (CSV format).
- `--metadata_output`: (Optional) Slóð til að vista metadata um keppnina í CSV eða JSON formi.

### Lýsing
Forritið sækir HTML gögn frá uppgefnum vefslóð, notar reglulegar segðir til að vinna úr keppnisgögnum og vistar niðurstöðurnar í CSV skrá. Ef beðið er um, skilar það einnig metadata um keppnina í sérstaka skrá.

```bash
python3 code/timataka.py --url "https://timataka.net/jokulsarhlaup2024/urslit/?race=2&cat=m" --output data/hlaup.csv --debug
```
---


