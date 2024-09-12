Þessi reglulega segð **r'<tr.*?>.*?<td.*?>(\d+)</td>.*?<td.*?>(\d+)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(\d{2}:\d{2}:\d{2})</td>'** er notuð til að draga út ákveðin gögn úr HTML töflum þar sem upplýsingar um keppendur eru geymdar í `<tr>` (röðum) og `<td>` (dálkum). Regluleg segð notuð hér er samansett til að ná í fjóra mikilvæga reiti fyrir hvern keppanda: staðsetningu, BIB-númer, nafn og tíma.

### Skref fyrir skref útskýring á reglulegri segð í lið 4:

1. **`<tr.*?>`**:
   - Þetta þýðir að við erum að leita að byrjun á töfluröð (`<tr>`).
   - `.*?` innan `<tr>` leyfir hvaða HTML eiginleika sem er á milli merkjanna (eins og `class` eða `id`), en það er gert eins stutt og mögulegt er með `?` (non-greedy matching).

2. **`.*?<td.*?>(\d+)</td>`** (Fyrsta td):
   - `.*?<td.*?>` byrjar á fyrsta dálkinum (`<td>`) í röðinni.
   - `(\d+)`: Þetta er það sem reglulega segðin sækir – það passar við **eina eða fleiri tölustafi** (þ.e. keppnisstöðu keppandans, t.d. 1, 2, 3). Tölustafurinn er settur í hliðarsviga `()` til að grípa þetta gildi sem hluta af niðurstöðunni.
   - `</td>` lokar dálknum.

3. **`.*?<td.*?>(\d+)</td>`** (Annað td):
   - Þetta er svipað og fyrri `<td>`, nema að hér erum við að grípa **BIB-númer keppandans** (t.d. 1234). Það passar einnig við einn eða fleiri tölustafi.

4. **`.*?<td.*?>(.*?)</td>`** (Þriðja td):
   - Þetta þýðir að hér sækjum við **nafn keppandans**.
   - `.*?` er non-greedy samhæfing sem passar við hvaða texta sem er inni í dálknum, þar til við hittum á `</td>`. 
   - Hliðarsvigarnir `()` safna þessu gildi (nafnið) til notkunar seinna.

5. **`.*?<td.*?>(\d{2}:\d{2}:\d{2})</td>`** (Fjórða td):
   - Þetta sækir **tímann** á formi **HH:MM:SS**.
   - `\d{2}` leitar að nákvæmlega tveimur tölustöfum (klukkustundir, mínútur og sekúndur).
   - `:` er notað til að passa við tvípunktana á milli tölustafanna.
   - Hliðarsvigar `()` safna öllum þessum hluta saman (tíminn) sem eitt gildi.

### Notkun á **re.S**:

- **`re.S`** er viðbótarmöguleiki sem stendur fyrir "DOTALL" ham. Þetta breytir hegðun **`.`** táknsins í reglulegri segð þannig að það passar við **öll tákn**, þar á meðal nýlínur (newline characters). Þetta er mikilvægt ef HTML-strúktúrinn er dreifður á mörgum línum, þannig að regluleg segð getur samt sem áður passað við gögnin rétt.

### Í samhengi við kóðann:

Þessi reglulega segð er notuð til að vinna úr hverri röð í HTML töflunni og grípa fjögur mismunandi gildi:
1. **Staða keppanda** (fyrsta `<td>`).
2. **BIB-númer** (annað `<td>`).
3. **Nafn keppanda** (þriðja `<td>`).
4. **Keppnistími** (fjórða `<td>`).

Eftir að við vinnum úr öllum röðum í töflunni, er hver keppandi geymdur sem lista af gögnum (`[place, bib, name, time]`), og niðurstöðurnar eru vistaðar í CSV-skrá.

### Dæmi:

Ef HTML-gögn líta svona út:

```html
<tr>
    <td>1</td>
    <td>1234</td>
    <td>John Doe</td>
    <td>01:23:45</td>
</tr>
```

Þá mun reglulega segðin grípa:
- Staða: `1`
- BIB-númer: `1234`
- Nafn: `John Doe`
- Tími: `01:23:45`

Þessi gögn verða síðan sett í CSV-skrá með þessum dálkum: **Place**, **BIB**, **Name**, **Time**.