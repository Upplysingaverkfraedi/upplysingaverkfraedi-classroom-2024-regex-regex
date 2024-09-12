**TBL: Reglulegar segðir**

**Spurning 3: Endurraða skrá**
Notið reglulega segð til að endurraða línum úr CSV-skrá með nafni, heimilisfangi og símanúmeri.
Umbreytið gögnunum í sniði: heimilisfang, símanúmer og nafn. Skiptið , út fyrir \t nema á eftir kenninafni.
Vistaðu úttakið í TSV-skrá með Python kóða.

**Reglulega segðin**
([^,]+)\s([^,]+),\s([^,]+),\s([^,]+),\s(.+)

**Reglulega segðin ([^,]+)**
Þessi segð kemur fram fjórum sinnum til þess að skipta línunni upp í fjóra parta. 
Passar við einn staf sem er ekki til í listanum hér að neðan [^,].
Plús "+" Passar við fyrri táknið á milli eins og ótakmarkaðs tíma, eins oft og mögulegt er, gefur til baka eftir þörfum.

**Meta escape**
\s passar við hvaða hvíta staf "whitespace character" sem er (jafngildir [\r\n\t\f\v ])

**Reglulega segðin (.+), aftasti hópurinn**
Þetta er segðin sem kemur fyrir aftast í stóru reglulegu segðinni. 
Punktur "." passar við hvaða staf sem er (nema fyrir línulok). 
Plús "+" passar við fyrri táknið á milli eins og ótakmarkaðs tíma, eins oft og mögulegt er og gefur til baka eftir þörfum. 