import pandas as pd
from pathlib import Path

INPUT = Path("/home/romain/Programmation/DjangoMlops/ml/data/raw/eCO2mix_RTE_En-cours-TR.xls")
OUTPUT = Path("/home/romain/Programmation/DjangoMlops/ml/data/raw/eCO2mix_RTE_En-cours-TR.csv")

df = pd.read_csv(INPUT, sep=';', encoding='latin1')
df.to_csv(OUTPUT, index=False)

print("Conversion complete:", OUTPUT)
