import csv
from pathlib import Path

p = Path("dataset_streamlit_shell/workspace/integration/voyage.csv")
raw = p.read_text(encoding="utf-8-sig")
lines = raw.splitlines()
header = lines[0].split(",")
assert header[0] == "passenger_id", header
header[0] = "PassengerId"
lines[0] = ",".join(header)
p.write_text("\n".join(lines) + "\n", encoding="utf-8")

print("new header:", lines[0])
print("rows:", len(lines) - 1)
