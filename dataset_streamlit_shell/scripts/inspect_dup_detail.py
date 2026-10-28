import pandas as pd
df = pd.read_csv("dataset_streamlit_shell/workspace/working.csv")
for name in ["Braund, Mr. Owen Harris", "Hays, Mrs. Charles Melville (Clara Jennings Gregg)"]:
    sub = df[df["Name"] == name]
    print("===", name)
    print(sub.T.to_string())
    print()
