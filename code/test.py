import re

text = "Ég á 3 epli, 5 perur, og 10 appelsínur."

# Finna allar tölur í textanum
tölur = re.findall(r'\d+', text)
print(tölur)  # Úttak: ['3', '5', '10']
