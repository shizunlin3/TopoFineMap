from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]

def test_s6a_contract():
    df=pd.read_csv(ROOT/"data/source_tables/Supplementary_Table_S6A_canonical_28_primary.tsv",sep="\t")
    assert len(df)==28
    assert df.locus.nunique()==18
    assert ((df.pip_corrected-df.pip_baseline).abs()<=0.005+1e-12).sum()==27
    assert (df.fold_uncorrected>1).sum()==28
    assert abs(df.fold_uncorrected.median()-36.316)<0.001

def test_exemplars():
    df=pd.read_csv(ROOT/"data/source_tables/Supplementary_Table_S6A_canonical_28_primary.tsv",sep="\t")
    mst=df[df.locus=="mst1_3p21"].iloc[0]
    assert (mst.pip_baseline,mst.pip_uncorrected,mst.pip_corrected)==(0.1915,0.006,0.1755)
    atg=df[df.locus=="atg16l1"].iloc[0]
    assert (atg.pip_baseline,atg.pip_uncorrected,atg.pip_corrected)==(0.002,0.207,0.002)
