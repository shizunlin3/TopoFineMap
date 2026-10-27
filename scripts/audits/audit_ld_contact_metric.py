from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[2]
df=pd.read_csv(ROOT/"data/source_tables/Supplementary_Table_S8_LD_contact_overlap.tsv",sep="\t")
assert (df.median_sd_ratio_tied_distant<1).all()
assert abs(df.median_sd_ratio_tied_distant.min()-0.3671)<1e-12
assert abs(df.median_sd_ratio_tied_distant.max()-0.8798)<1e-12
print("PASS")
