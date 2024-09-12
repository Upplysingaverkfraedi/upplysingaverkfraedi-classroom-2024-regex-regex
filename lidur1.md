# *Spurning 1: Leita af kennitölu:*

    I. Skrifið tvær reglulegar segðir til að finna kennitölur einstaklinga og   fyrirtækja í texta.

    II. Skrifið Python kóða sem leitar að kennitölum samkvæmt reglulegu segðunum og prentar niðurstöðurnar.
    
    III. Keyrið kóðann með valmöguleikum til að leita annað hvort af einstaklinga, fyrirtækja eða báðum í einu.

## *LAUSN:*
Byrjum á að svara fyrstu spurningunni þar sem við eigum að skrifa tvær reglulegar segðir til að finna kennitölur einstaklinga og á hinn bóginn kennitölur fyrirtækja í texta:

**Forsendur: Samkvæmt Þjóðskrá Íslands** 
Form einstaklings kennitalna á Íslandi er alltaf það sama þ.e. Kennitalann er í heildina 10 tölustafir þar sem fyrstu 6 eru myndaðir af fæðingardagsetningu einstaklingsins.  
Næstu tveir tölustafir hafa í raun enga merkingu og er þeim alla jafna úthlutað í röð frá og með 20, t.d. 120160-33.   
Því næst er svokölluð öryggistalan reiknuð út en hún má vera á bilinu 0 til 9. Aftasti stafur í kennitölu er 8, 9 eða 0 og merkir hann öldina sem viðkomandi er fæddur á.

Form fyrirtækis kennitalna á Íslandi er þó aðeins frábrugðið. Kennitalan er í heild sinni 6 stafir myndaðir af stofnunardagsetningu fyrirtækisins en fyrsta talan er hækkuð um 4. Sem dæmi segjum að fyrirtæki sé stofnað 05.11.2005 þá yrði kennitalan án upphækkunarinnar 051105 en á réttu formi yrði fyrsta talan hækkuð um 4 og því yrði lokaútgáfan kt. 451105. Því getur fyrsta talann einungis verið 4, 5, 6 eða 7. Vegna 0+4, 1+4, 2+4, 3+4. Enginn mánuður hefur 40 daga.

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

560787: Fæðingardagsetning (16. Júlí 1987). Búið að uppfæra fyrsta staf um +4
Sjáum að tölurnar tvær í miðjunni geta ekki verið 00 eða 13,14,15... o.s.frv og fyrsta talan getur einungis verið 4,5,6 eða 7.
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
