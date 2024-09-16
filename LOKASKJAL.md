# *Spurning 1: Leita af kennitölu:*

    I. Skrifið tvær reglulegar segðir til að finna kennitölur einstaklinga og   fyrirtækja í texta.

    II. Skrifið Python kóða sem leitar að kennitölum samkvæmt reglulegu segðunum og prentar niðurstöðurnar.
    
    III. Keyrið kóðann með valmöguleikum til að leita annað hvort af einstaklinga, fyrirtækja eða báðum í einu.

## *LAUSN:*
Byrjum á að svara fyrstu spurningunni þar sem við eigum að skrifa tvær reglulegar segðir til að finna kennitölur einstaklinga og á hinn bóginn kennitölur fyrirtækja í texta:

**Forsendur: Samkvæmt Þjóðskrá Íslands** 
Form einstaklings kennitalna á Íslandi er alltaf það sama þ.e. Kennitalann er í heildina 10 tölustafir þar sem fyrstu 6 eru myndaðir af fæðingardagsetningu einstaklingsins.  
Næstu tveir tölustafir hafa í raun enga merkingu og er þeim alla jafna úthlutað í röð frá og með 20, t.d. 120160-33.   
Því næst er svokölluð öryggistalan reiknuð út en hún má vera á bilinu 0 til 9. Aftasti stafur í kennitölu er 8, 9 eða 0 og merkir hann öldina sem viðkomandi er fæddur á. Kt. gæti verið t.d. 129160-3359

Form fyrirtækis kennitalna á Íslandi er þó aðeins frábrugðið. Kennitalan er í heild sinni 10 tölustafir myndaðir af stofnunardagsetningu fyrirtækisins en fyrsta talan er hækkuð um 4. Sem dæmi segjum að fyrirtæki sé stofnað 05.11.2005 þá yrði fyrstu 6 tölustafirnir án upphækkunarinnar 051105 en á réttu formi yrði fyrsta talan hækkuð um 4 og því yrði kt. 451105. Því getur fyrsta talann einungis verið 4, 5, 6 eða 7. Vegna 0+4, 1+4, 2+4, 3+4. Enginn mánuður hefur 40 daga. Síðustu 4 virka þannig að tölustafirnir 7. og 8. geta verið hvaða tala frá 01-99, 9. talan getur verið hvaða tala frá 0-9 og 10. talann er ein af þremur tölum 8,9 eða 0. Kt. gæti verið t.d. 660487-3459

Því getum við byrjað að skrifa reglulega segð sem finnur kennitölu einstaklings og svo fyrirtækis.  

**Einstaklings regluleg segð gæti litið svona út:**
```regex
\b(?:0[1-9]|[1-2][0-9]|3[0-1])(?:0[1-9]|1[0-2])\d{2}-(?:2[0-9]|[3-9]\d)\d[890]\b
```

Þar sem, 
```regex
\b: Segða eða orðaamörk
```
Þetta merkir „mörk“ segðar og tryggir að leitun byrji á stöðum þar sem orð endar eða byrjar. 

```regex
(0[1-9]|[1-2][0-9]|3[0-1]): Dagur í Mánuði
```
Hér er notað hópur með „valkostum“ (|), sem merkir að það passar eitt af eftirfarandi:  
**Valkostur 1** - 0[1-9]: Passar að á eftir 0 fylgir tölustafur frá 1 til 9, sem gefur til kynna dagana 01 til 09.  
**Valkostur 2** - [1-2][0-9]: Passar að tölustafur á eftir 1 eða 2 kemur tala frá 0 til 9, sem gefur til kynna dagana 10 til 29.  
**Valkostur 3** - 3[0-1]: Passar að ef fyrsta tala er 3 þá fylgir annaðhvort 0 eða 1 á eftir, sem gefur til kynna dagana 30 og 31.
```regex
(0[1-9]|1[0-2]): Mánuður
```
Þetta er hópur með „valkostum“ (|), sem merkir að það passar eitt af eftirfarandi:
**Valkostur 1** - 0[1-9]: Passar að ef 0 þá fylgir eftir tölustafur frá 1 til 9, sem gefur til kynna mánuðina 01 til 09.  
**Valkostur 2** - 1[0-2]: Passar að ef 1 þá fylgir eftir tölustafurinn 0, 1, eða 2, sem gefur til kynna mánuðina 10 til 12.
```regex
(\d{2}): Ár
```
Þetta passar að hafa nákvæmlega tvo tölustafi *(\d* stendur fyrir hvaða tölustaf sem er, og {2} krefst að þeir séu einmitt nákvæmlega tveir). Þetta táknar síðustu tvo tölustafir af fyrstu 6 þ.e. árið svo sem 87 (1987), 04 (2004), osfrv.

```regex
-(2[0-9]|[3-9]\d): Talan í sæti 8 og 9
```
Þetta er hópur með „valkostum“ (|), sem merkir að það passar eitt af eftirfarandi:
**Valkostur 1** - 2[0-9]: Passar að ef 2 þá fylgir eftir tölustafur frá 0 til 9, sem gefur til kynna talnaraðir frá 20 til 29.
**Valkostur 2** - [3-9]\d: Passar að ef 3 til 9, getur fylgt eftir hvaða tölustaf sem er *(\d)*, sem gefur til kynna talnaraðir frá 30 til 99.
```regex
(\d): Eitt Tölustaf
```
Þetta passar að hafa nákvæmlega einn tölustaf (*\d* stendur fyrir hvaða tölustaf sem er). Þ.e. hvaða tölustafur sem er frá 0 til 9.
```regex
([890]): Lokastafur
```

Þetta er úrtak sem leyfir aðeins einn af tölustöfunum 8, 9, eða 0 að gilda. Þetta táknar lokastaf sem getur verið 8, 9, eða 0.

```regex
(?: ...) 
```
Merkir í reglulegum segðum hópun án upptöku (e. non-capturing group). Dæmi: (?:abc) passar við abc í streng en fanga það ekki. Þetta þýðir að það verður ekki hluti af niðurstöðum sem findall() skilar eða annarra aðgerða sem geyma upptökur úr regex.

```regex
\b: Orðamörk
```
Eins og fyrri *\b* þýðir þetta mörk. En þetta *\b* tryggir að leitin endar hér. 

**Dæmi**
Hér er dæmi um kennitölu: 160405-2650

160405: Fæðingardagsetning (16. apríl 2005).
26: Random talan frá og með 20.
5: Öryggistalan (0-9).
0: Táknar árin frá 2000-2100 

**Fyrirtækis regluleg segð:**
```regex
\b[4-7][0-9](?:0[1-9]|1[0-2])\d{2}-[0-9]{2}[0-9][890]\b
```
Þar sem,
```regex
\b: Segðamörk
```
Þetta er „orðamörk“ (e. boundaries) sem tryggir að leitunin verði aðeins frá byrjun til enda á orði.
```regex
[4-7]: Fyrsta tala
```
Þetta er „stafasett“ sem leyfir aðeins eina tölustaf úr bili 4 til 7. Þetta þýðir að fyrsta talan í 6-stafa númerinu getur aðeins verið 4, 5, 6, eða 7.
```regex
[0-9]: Önnur tala
```
Þetta er „stafasett“ sem leyfir hvaða tölustaf sem er frá 0 til 9. Þetta þýðir að önnur talan getur verið hvaða tölustafur sem er.
```regex
(?:0[1-9]|1[0-2]): Þriðja og fjórða talan
```
Þetta er hópur með „valkostum“ (|), sem þýðir að það mun passa annað hvort af tveimur valkostum gildi.  
**Valkostur 1 - 0[1-9]:**   
Passar að á eftir 0 fylgir tölustafur frá 1 til 9. Þetta tryggir að ef þriðja talan er 0, þá getur fjórða talan verið frá 1 til 9. Til dæmis vegna þess að mánuður getur ekki verið 00.  
**Valkostur 2 - 1[0-2]:** 
Passar að á eftir 1 fylgir tölustafur frá 0 til 2. Þetta tryggir að ef þriðja talan er 1, þá getur fjórða talan aðeins verið 0, 1, eða 2. Til dæmis vegna þess að mánuður getur ekki verið 13 eða 14.
```regex
\d{2}: Fimmta og sjötta talan
```
Þetta passar að nákvæmlega tveir tölustafir séu (*\d* stendur fyrir hvaða tölustaf sem er, og *{2}* krefst að það séu nákvæmlega tveir tölustafir). Þetta þýðir að fimmta og sjötta talan geta verið hvaða tölustafir sem er frá 0 til 9.

```regex
(?: ...) 
```
Sama útskýring og áðan... En þetta merkir í reglulegum segðum hópun án upptöku (e. non-capturing group). Dæmi: (?:abc) passar við abc í streng en fangar það ekki. Þetta þýðir að það verður ekki hluti af niðurstöðum sem findall() skilar eða annarra aðgerða sem geyma upptökur úr regex.

```regex
-:
```
Strik (hyphen) sem aðskilur dagsetningu frá eftirfarandi hluta kennitölunnar.

```regex
[0-9]{2}: 7-8 tala
```
Þetta eru tveir tölustafir sem getur verið hvaða tveir tölustafir sem er (01 til 99).

```regex
[0-9]:
```
Þetta er einn tölustafur sem getur verið hvaða tala sem er frá 0 til 9.

```regex
[890]:
```
Þetta er síðasti tölustafur sem merkir öldina og getur verið 8, 9 eða 0.

```regex
\b: Segðamörk
```
Líkt og áðan var sagt þá merkir *\b* mörk segðar. Þetta *\b* tryggir að leitin endar á orðamörk. 


**Dæmi**
Hér er dæmi um kennitölu fyrirtækis: 560787-2009

560787: Fæðingardagsetning (16. Júlí 1987). Búið að uppfæra fyrsta staf um +4 Sjáum að tölurnar tvær í miðjunni geta ekki verið 00 eða 13,14,15... o.s.frv og fyrsta talan getur einungis verið 4,5,6 eða 7. 
Tala 7-8 er frá 01-99 (20) 
Tala 9 er frá 0-9 og (0) 
Tala 10 er annaðhvort 8,9, eða 0 (9)


Til þess að geta keyrt kóðann þarftu fyrst að gera "cd code" skipunina og til að leita eftir einstaklings kennitölum skrifaru einfaldlega skipunina: 

```regex
python regex_kt.py --file inntaksskra.txt --einstaklingar
```

Þar sem regex_kt.py er python skjalið með kóðanum og inntaksskra.txt er textaskjal í tölvunni þinni með ýmsum kennitölum. Í okkar tilfelli notuðum við textaskjal sem lítur svona út: 


Kennitala Haskola Islands: 600169-2039
Vigdis Finnbogadottur: 150430-2329 
Guðni Th. Johannessonar: 260668-4719. 
Halla Tomasdóttir: 111068-4379
Kennitala Auður Capital: 640507-0390. 
Ekki logleg kennitala: 151617-1819.


og --einstaklingar vísar í kóðann til að leita eftir löglegum kennitölum sem uppfyllir reglulegu segðina sem við gerðum í byrjun. Með þessari skipun á forritið að lesa út löglegar kennitölur og einungis prenta þær þ.e. til dæmis fyrsta kennitalan í texta skjalinu má sjá að fylgir ekki reglum íslensku kennitalnanna og er því ekki prentuð.

Á hinn bóginn til að finna löglega kennitölu fyrirtækja skaltu keyra þessa skipun:

```regex
python regex_kt.py --file inntaksskra.txt --fyrirtaeki
```

og að lokum ef þú vilt fá bæði einstaklings og fyrirtækja kennitölur skaltu keyra:

```regex
python regex_kt.py --file inntaksskra.txt --einstaklingar --fyrirtaeki
```
# KÓÐI SPURNING 1:

import argparse


def parse_arguments():
    """
    Lesa inn argument frá skipanalínu
    :return: (ArgumentParser) parser með argumentunum
    """

    parser = argparse.ArgumentParser(description='Leita að kennitölum einstaklinga eða fyrirtækja.')
    parser.add_argument('--file', required=True,
                        help='Slóð að inntaksskrá með kennitölum.')
    parser.add_argument('--einstaklingar', action='store_true',
                        help='Leita að kennitölum einstaklinga.')
    parser.add_argument('--fyrirtaeki', action='store_true',
                        help='Leita að kennitölum fyrirtækja.')
    return parser.parse_args()


def lesa_skra(file_path):
    """
    Lesa inntaksskrá og skila lista af línum
    :param file_path: (str) Slóð að skrá
    :return:          (list) Listi af línum
    """

    with open(file_path, 'r') as file:
        return file.readlines()


def prenta_nidurstodur(kennitolur):
    """
    Prentar út niðurstöður í console
    :param kennitolur: (list) Listi af kennitölum
    :return:           None
    """

    if kennitolur:
        print("Fundnar kennitölur:")
        for kt in kennitolur:
            print(kt)
    else:
        print("Engar kennitölur fundust.")


def finna_kennitolur(text, leit_af_einstaklingum, leit_af_fyrirtaekjum):
    """
    Leita að kennitölum í texta með reglulegum segðum
    :param text:                    (list) Listi af línum
    :param leit_af_einstaklingum:   (bool) Leita að kennitölum einstaklinga
    :param leit_af_fyrirtaekjum:    (bool) Leita að kennitölum fyrirtækja
    :return:                        (list) Listi af kennitölum
    """

    kennitolur = []

    if leit_af_einstaklingum:
        # Regluleg segð fyrir kennitölur einstaklinga
        raise NotImplementedError("Fall sem leitar að kt einstaklinga hefur enn ekki verið útfært.")

    if leit_af_fyrirtaekjum:
        # Regluleg segð fyrir kennitölur fyrirtækja
        raise NotImplementedError("Fall sem leitar að kt fyrirtækja hefur enn ekki verið útfært.")

    return kennitolur


def main():
    """
    Keyrslufall sem les inn skrá, leitar að kennitölum og prentar niðurstöður.
    :return: None
    """

    args = parse_arguments()

    # Athuga hvort valkostir séu valdir; ef ekkert er valið, hætta og sýna villu
    if not args.einstaklingar and not args.fyrirtaeki:
        print("Þú verður að velja annað hvort --einstaklingar eða --fyrirtaeki eða bæði.")
        return

    text = lesa_skra(args.file)
    kennitolur = finna_kennitolur(text, args.einstaklingar, args.fyrirtaeki)

    prenta_nidurstodur(kennitolur)


if __name__ == "__main__":
    main()



# *Spurning 2: Leita af netfangi*

Reglulega segðin:
```regex
r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,3}(?:\.[a-zA-Z]{2,})?$'
```

Þessi reglulega segð leitar af leyfilegu netfangi:
```regex
^ 
```
Byrjun á streng.


```regex
[a-zA-Z0-9_.+-]+ 
```

Passar notendanafnið (bókstafir, tölustafir og sérstafir eins og punktur, undirstika o.s.frv.).
```regex
@ 
```
Táknar að það sé „at“ merki.

```regex
[a-zA-Z0-9-]+
```
Passar  lén (bókstafir og tölustafir, með bandstrik mögulegt).```

```regex
\. 
```
Táknar punkt á undan lénaviðbót.


```regex
[a-zA-Z]{2,3}
```
Passar á tveggja eða þriggja stafa lénaviðbót (t.d. .com, .is).
```
(?:\.[a-zA-Z]{2,})?
```
Valfrjáls lengri viðbót fyrir lén (t.d. .co.uk).
```regex
$ 
```
lok strengs.


Mögulega þarf að nota þennan kóða til að keyra file fyrir Spurningu 2
```regex
python3 sp2.py --file data/email.txt
```
# KÓÐI FYRIR SPURNINGU 2:

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


def finna_netfong(text): #Hér á ég að breyta einhverju.
    """
    Leita að netföngum í texta
    r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,3}(?:\.[a-zA-Z]{2,})?$'
    :param text: (list) Listi af línum
    :return:     (list) Listi af netföngum
    """

    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,3}(?:\.[a-zA-Z]{2,})?$' 
    # útilokar ólögleg netföng

    Cp = re.compile(pattern)
    matches_list = []

    for line in text:
        matches = Cp.finditer(line)
        #print(matches)
    
        for match in matches:
                matches_list.append(f"Match: {match.group(0)} @ {match.start()}: {match.end()}") #@
    return matches_list
    
    #raise NotImplementedError("Regluleg segð til að finna netföng hefur ekki verið útfærð.")
    


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



# *Spurning 3: Endurraða skrá*
sp3.py er python skjal fyrir dæmi 3. Keyra skrá með:

Þá býr hann til skjal í data möppunni þar sem búið er að endur raða. skipunin tekur inn skránna nafn_heimilisfang_simanumer.csv og skilar skránni heimilisfang_simanumer_nafn.tsv (í data möppu).

Við notum requests til að sækja HTML-skjalið af tímataka.net og reglulega segð til að greina gögnin. Lausnin greinir sjálfkrafa hvort keppnin sé einstaklingskeppni, liðakeppni eða hraðaniðurstöður og sækir viðeigandi gögn. Niðurstöðurnar eru svo vistaðar í CSV-skrá með pandas fyrir frekari greiningu. Auk þess er möguleiki á að vista HTML-skjalið til að skoða það betur. Lausnin tryggir að gögnin séu unnin rétt óháð keppnisformi.

Reglulega segðin: 
```regex
r"^(\w+(?:\s+\w+)?)\s+(\w+),\s*(.*?),\s*(\d{3}.*?),\s(.*?)$"
```
**Útskýring**
```regex
^:
```
Táknar byrjun línunnar. 
```regex
(\w+(?:\s+\w+)?)
```
\w+: Passar einn eða fleiri bókstafi, tölustafi eða undirstrik.
(?:\s+\w+)?: Valfrjáls hópur sem passar á bil (\s+) og annað orð (\w+). Þetta gerir það mögulegt að fyrsta hluti geti verið eitt orð eða tvö orð. Þetta er fyrsta fang (capture group).
```regex
\s+(\w+)
```
\s+: Passar eitt eða fleiri bil.
(\w+): Passar eitt orð og fangar það. Þetta er annað fang.
```regex
,\s*(.*?)
```
,: Passar kommumark.
\s*: Passar engin eða fleiri bil.
(.*?): Passar hvaða texta sem er þar til næsta kommumark og fangar það. Þetta er þriðja fang.
```regex
,\s*(\d{3}.*?)
```
,: Passar kommumark.
\s*: Passar engin eða fleiri bil.
(\d{3}.*?): Passar þrjár tölur og eftirfylgjandi texta og fangar það. Þetta er fjórða fang.

```regex
,\s(.*?)$
```
,: Passar kommumark.
\s: Passar eitt bil.
(.*?): Passar hvaða texta sem er þar til endir línunnar og fangar það. Þetta er síðasta fang.
$: Táknar endir línunnar.



# KÓÐI FYRIR SPURNINGU 3:
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
    """"
    Endurröðun lína úr CSV formi í TSV form með notkun reglulegra segða.
    :param linur: (list) Listi af línum úr CSV skránni
    :return:      (list) Listi af endurröðuðum línum
    """
    
    nyjar_linur = []
    # Regluleg segð til að finna nafn, heimilisfang, póstnúmer og símanúmer
    segd = r"^(\w+(?:\s+\w+)?)\s+(\w+),\s*(.*?),\s*(\d{3}.*?),\s(.*?)$"

    for lina in linur:
        ny_lina = re.sub(segd, r"\3\t\4\t\5\t\2, \1", lina.strip())
        nyjar_linur.append(ny_lina)
    
    return nyjar_linur


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



# *Spurning 4: Gagnaúrvinnsla af tímataka.net*

Notum:

python3 sp4.py --url "https://timataka.net/snaefellsjokulshlaupid2014/urslit/?race=1&cat=overall" --output data/hlaup.csv --debug

Til að keyra. Getur valið vefslóð af timataka.net

Getum notað

https://timataka.net/hyrox-06-2024/urslit/?race=1&cat=m&age_from=10&age_to=99&division=Kk%20pro

https://timataka.net/jokulsarhlaup2024/urslit/?race=2&cat=m

https://www.timataka.net/snaefellsjokulshlaupid2014/urslit/?race=1&cat=m&age=0039

Regluleg segð fyrir URL ^https://(www.)?timataka.net/[\w\d-]+/urslit/?race=\d+(&cat=\w+)(&age=\d+)?(&age_from=\d+&age_to=\d+)?(&division=\w+%20\w+)?$

Aðeins flóknara fyrir hitt.

Tekur inn vefslóð og skilar .csv skrá í hlaup.csv. Einnig er hægt að sjá hlaup.html sem er unnið úr.

# KÓÐI FYRIR SPURNINGU 4:


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

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Tókst ekki að sækja gögn af {url}")
        return None


def detect_format(html):
    if re.search(r'\bTeam\b', html, re.IGNORECASE):
        return 'team'
    elif re.search(r'\bPace\b', html, re.IGNORECASE):
        return 'pace'
    elif re.search(r'\bBehind\b', html, re.IGNORECASE):
        return 'individual'
    else:
        return 'unknown'


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

def skrifa_nidurstodur(data, output_file):
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
