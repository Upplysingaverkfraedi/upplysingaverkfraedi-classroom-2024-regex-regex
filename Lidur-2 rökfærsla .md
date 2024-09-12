2. Leit að netfangi 
Hér útfærðum við eina reglulega segð sem leitar eftir löglegum netföngum. 
Reglulega segðin er eftirfarandi: 
email_regex = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,5}\.[a-zA-Z]{2,3}$|^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,5}$)'

Hér er svo niðurbrot á því hvað er að gerast í reglulegu segðinni: 

“^”:Stendur fyrir upphaf strengs, segðin byrjar að leita frá byrjun strengsins.  

“[a-zA-Z0-9_.+-]+”: Er leyfilegir stafir í netfanginu fyrir framan @. Þar mega vera litlir og stórir stafir frá a-z, undirstrik, punktur, plús og bandstrik. Plúsinn í lokin segir að það þarf amk. að vera eitt tákn en þau mega vera fleiri. 

“@”:  Táknar @ sem er nauðsynlegt fyrir netföng. 

[a-zA-Z0-9-]+: Er leyfilegir stafir í netfanginu eftir @. Þar mega vera litlir og stórir stafir  frá a-z, tölustafir og bandstrik. Plúsinn í lokin segir að það þarf amk. að vera eitt tákn en þau mega vera fleiri.

\.: Punktur er nauðsynlegur til að aðskilja aðal lénið frá top-level domain. 

[a-zA-Z]{2,5}: Þetta er fyrir top level domain, það leyfir bókstafi og þarf að vera 2-5 að lengd. 

\.[a-zA-Z]{2,3}: Þetta er til þess að það sé hægt að hafa undir lén sem er 2-3 stafir. 

$: Táknar enda strengsins, segðin leitar að löglegu netfangi og engir aukastafir eru leyfðir á eftir því. 

| : Þetta er or/eða aðgerð. Þannig annað hvort þarf fyrri partur segðarinnar að passa eða seinni hlutinn. 

^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,5}$: Þetta er síðan seinni parturinn. Sem er eins og fyrri parturinn nema hér eru engin undir lén. En fyrriparturinn var nauðsynlegur fyrir undir lén. Því með því að hafa báðar aðgerðirnar inni fáum við öll netföng sem eru lögleg sem hafa bæði undir lén og þau netföng sem hafa eingöngu top-level lén.

