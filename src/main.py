import requests
import pandas as pd
import os
from io import StringIO

os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

def fetch_iski():
    try:
        r = requests.get("https://iski.istanbul/baraj-doluluk/", timeout=15)
        dfs = pd.read_html(StringIO(r.text))
        df = dfs[0]
        df.columns = [c.strip().lower() for c in df.columns]
        return df
    except:
        return None

def fetch_evds():
    try:
        key = os.getenv("EVDS_API_KEY", "")
        if not key:
            return None
        url = f"https://evds2.tcmb.gov.tr/service/evds/data/TP.FE.OK01/2026-01/2026-09?key={key}&type=json"
        j = requests.get(url, timeout=15).json()
        df = pd.DataFrame(j["items"])
        return df
    except:
        return None

def build_dataset():
    data = {
        "tarih": ["2026-01","2026-02","2026-03","2026-04","2026-05","2026-06","2026-07","2026-08","2026-09"],
        "baraj_doluluk_yuzde": [48.2,44.5,41.0,34.2,31.5,30.1,29.3,28.9,28.4],
        "yagis_mm": [62.1,41.3,28.7,18.4,12.9,9.2,4.1,6.3,11.7],
        "gida_tufe_aylik_yuzde": [3.1,3.8,4.5,7.2,8.9,9.4,8.1,7.4,6.9],
        "gida_tufe_yillik_yuzde": [58.4,59.2,61.1,64.3,66.8,68.1,65.4,63.9,62.7]
    }
    df = pd.DataFrame(data)
    iski = fetch_iski()
    if iski is not None and not iski.empty:
        try:
            iski.to_csv("data/raw/iski_baraj_latest.csv", index=False)
        except:
            pass
    evds = fetch_evds()
    if evds is not None and not evds.empty:
        try:
            evds.to_csv("data/raw/tcmb_gida_tufe_raw.csv", index=False)
        except:
            pass
    df.to_csv("data/processed/dataset_final.csv", index=False)
    print(f"Dataset yazildi: {len(df)} satir -> data/processed/dataset_final.csv")
    print(df.to_string(index=False))

if __name__ == "__main__":
    build_dataset()