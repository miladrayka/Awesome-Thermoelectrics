"""Plot histogram of publication years."""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import re

with open("README.md", "r", encoding="utf-8") as file:
    markdown_content = file.read()

extracted_years = [int(match) for match in re.findall(r'\|\s*(20\d{2})', markdown_content)]
data = np.array(extracted_years)

years, counts = np.unique(data, return_counts=True)

sns.set_theme(style="white", context="talk")  
plt.rcParams["font.family"] = "sans-serif"

fig, ax = plt.subplots(figsize=(10, 6))

sns.histplot(
    data,
    discrete=True,
    color="#2b5c8f",  
    alpha=0.85,  
    edgecolor="white",  
    linewidth=1.5,
)

sns.despine()

plt.xlabel("Year", fontsize=14, fontweight="bold", labelpad=13, color="#333333")
plt.ylabel("Count", fontsize=14, fontweight="bold", labelpad=13, color="#333333")
plt.xticks(years, color="#555555")  
plt.yticks(color="#555555")

plt.title(
    "Annual Growth Trends",
    fontsize=20,
    fontweight="bold",
    pad=20,
    loc="left",
    color="#1a1a1a",
)

plt.tight_layout()
plt.savefig("histogram.png", dpi=300, bbox_inches="tight")