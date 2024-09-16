Spurning 3
sp3.py er python skjal fyrir dæmi 3.
Keyra skrá með:

python3 code/regex_reorder.py --infile data/nafn_heimilisfang_simanumer.csv --outfile data/heimilisfang_simanumer_nafn.tsv

tekur inn t.d.

Jón Jónsson, Litla-Saurbæ, 816 Ölfusi, 555-1234
Guðrún Helgadóttir, Fiskislóð 15, 101 Reykjavík, 510-7000
Jón Oddur Guðmundsson, Úthlíð 6, 450 Patreksfirði, 897-1234

og breytir í

Litla-Saurbæ 816 Ölfusi 555-1234 Jónsson, Jón
Fiskislóð 15 101 Reykjavík 510-7000 Helgadóttir, Guðrún
Úthlíð 6 450 Patreksfirði 897-1234 Guðmundsson, Jón Oddur

Þá býr hann til skjal í data möppunni þar sem búið er að endur raða. skipunin tekur inn skránna nafn_heimilisfang_simanumer.csv og skilar skránni heimilisfang_simanumer_nafn.tsv (í data möppu).

Spurning 4
Í skjali sp4.py
Við notum requests til að sækja HTML-skjalið af tímataka.net og reglulega segð til að greina gögnin. Lausnin greinir sjálfkrafa hvort keppnin sé einstaklingskeppni, liðakeppni eða hraðaniðurstöður og sækir viðeigandi gögn. Niðurstöðurnar eru svo vistaðar í CSV-skrá með pandas fyrir frekari greiningu. Auk þess er möguleiki á að vista HTML-skjalið til að skoða það betur. Lausnin tryggir að gögnin séu unnin rétt óháð keppnisformi.

Notum:

python3 code/timataka.py --url "https://timataka.net/snaefellsjokulshlaupid2014/urslit/?race=1&cat=overall" --output data/hlaup.csv --debug

Til að keyra. Getur valið vefslóð af timataka.net

Getum notað

https://timataka.net/hyrox-06-2024/urslit/?race=1&cat=m&age_from=10&age_to=99&division=Kk%20pro

https://timataka.net/jokulsarhlaup2024/urslit/?race=2&cat=m

https://www.timataka.net/snaefellsjokulshlaupid2014/urslit/?race=1&cat=m&age=0039

Regluleg segð fyrir URL
^https://(www.)?timataka.net/[\w\d-]+/urslit/?race=\d+(&cat=\w+)(&age=\d+)?(&age_from=\d+&age_to=\d+)?(&division=\w+%20\w+)?$

Tekur inn vefslóð og skilar .csv skrá í hlaup.csv. Einnig er hægt að sjá hlaup.html sem er unnið úr.
