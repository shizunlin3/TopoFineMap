from pathlib import Path
import json, sys, pandas as pd
ROOT=Path(__file__).resolve().parents[2]
df=pd.read_csv(ROOT/"data/source_tables/Supplementary_Table_S6A_canonical_28_primary.tsv",sep="\t")
tn=json.loads((ROOT/"data/source_tables/TNFAIP3_canonical_summary.json").read_text())
errors=[]
if len(df)!=28: errors.append(f"rows={len(df)}")
if df.locus.nunique()!=18: errors.append(f"loci={df.locus.nunique()}")
if int(((df.pip_corrected-df.pip_baseline).abs()<=0.005+1e-12).sum())!=27: errors.append("corrected gate")
if int((df.fold_uncorrected>1).sum())!=28: errors.append("expansion gate")
if abs(df.fold_uncorrected.median()-36.316)>0.001: errors.append("median fold")
if abs(df.fold_uncorrected.min()-4.678)>0.001: errors.append("min fold")
if abs(df.fold_uncorrected.max()-437.902)>0.001: errors.append("max fold")
mst=df[df.locus=="mst1_3p21"].iloc[0]
if (mst.pip_baseline,mst.pip_uncorrected,mst.pip_corrected)!=(0.1915,0.006,0.1755): errors.append("MST1")
atg=df[df.locus=="atg16l1"].iloc[0]
if (atg.pip_baseline,atg.pip_uncorrected,atg.pip_corrected)!=(0.002,0.207,0.002): errors.append("ATG16L1")
if tn["repaired_pruned_graph_edges"]!=69629: errors.append("TNFAIP3 edges")
traj=(tn["rs6927172"]["baseline"],tn["rs6927172"]["uncorrected_alpha_0.1"],tn["rs6927172"]["degree_corrected_alpha_0.1"])
if traj!=(0.0295,1.0,0.023): errors.append("TNFAIP3 trajectory")
print("=== TopoFineMap public release validation ===")
if errors:
    print("STATUS = FAIL"); [print("ERROR:",e) for e in errors]; sys.exit(1)
print("STATUS = PASS")
print("28-row canonical hold-out: PASS")
print("27/28 corrected focal PIPs within 0.005: PASS")
print("28/28 uncorrected model-size expansions: PASS")
print("TNFAIP3 repaired-lineage summary: PASS")
