## Segðir Útskýringar

### *Kennitala einstaklinga*

Segðin sem segir til um reglur kennitalna einstaklinga: 

**\b[0-3]\d(0\d|1[0-2])\d{2}-[2-9]\d{2}[8,9,0]\b**

1. \b byrjar segðina. 
2. [0-3] þýðir að fyrsta talan í kennitölunni er tala á bilinu 0 upp í 3
3. \d þýðir að næsta tala (önnur tala í kennitölu) má vera hvaða tala sem er á bilinu 0 upp í 9
4. (0\d|1[0-2]) segir til um þriðju og fjórðu tölu í kennitölu. Segði segir að ef þriðja talan er 0 þá getur fjórða talan verið hvaða tala sem er á bilinu 0 upp í 9. Ef þriðja talan er 1 þá getur fjórða talan aðeins verið á bilinu 0 upp í 2 svo mánuður verði löglegur. 
5. \d{2} segir svo að næstu tvær tölur geti verið hvaða tölur sem er á bilinu 0 og upp í 9
6. $-$ segir að næst kemur strik, strik á eftir fyrstu 6 tölustöfum. 
7. [2-9] segir til um að sjöundi tölustafur er á bilinu 2 og upp í 9 (Þar sem tölustafir 7 og 8 eru alltaf >20).
8. \d{2} segir svo að tölustafir 8 og 9 megi vera hvaða tölustafir sem er.
9. [8,9,0] þýðir að seinasti tölustafurinn er alltaf 8 9 eða 0
10. \b endar segðina. 

### *Kennitala fyrirtækja*

Segðin sem segir til um reglur kennitalna fyrirtækja: 

**\b[4-9]\d{5}-\d{4}\b**

1. \b byrjar segðina.
2. Þýðir að fyrst talan þarf að vera á bilinu 4 og upp í 9.
3. Næstu 5 tölur eru á bilinu 0 og upp í 9
4. $-$ þýðir að næst kemur lína. Á eftir fyrstu 6 tölustöfum. 
5. \d{4}næstu fjórar tölur eru á bilinu 0 og upp í 9. 
6. \b endar svo segðina.