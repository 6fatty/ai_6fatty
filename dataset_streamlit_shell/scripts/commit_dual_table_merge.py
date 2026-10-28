import pandas as pd
from pathlib import Path

base = Path("dataset_streamlit_shell/workspace")
pax = pd.read_csv(base / "integration/passengers.csv")
voy = pd.read_csv(base / "integration/voyage.csv")

print("passengers:", pax.shape, "voyage:", voy.shape)
print("voyage key unique:", voy["PassengerId"].is_unique)
print("overlap:", len(set(pax["PassengerId"]) & set(voy["PassengerId"])))

merged = pax.merge(voy, on="PassengerId", how="left")
print("merged:", merged.shape)
print("null Fare:", merged["Fare"].isna().sum())

merged.to_csv(base / "original.csv", index=False)
merged.to_csv(base / "working.csv", index=False)
print("cols:", list(merged.columns))
