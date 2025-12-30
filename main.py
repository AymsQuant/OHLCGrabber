import requests, csv, time, math
from datetime import datetime

pair = input("Pair (e.g., BTCUSDT): ").strip().upper()
interval = input("Interval (1m, 5m, 1h, 1d...): ").strip()
start = int(datetime.strptime(input("Start (YYYY-MM-DD): "), "%Y-%m-%d").timestamp()*1000)
end = int(datetime.strptime(input("End (YYYY-MM-DD): "), "%Y-%m-%d").timestamp()*1000)
file = f"{pair}_{interval}_{datetime.utcfromtimestamp(start/1000).strftime('%Y%m%d')}_{datetime.utcfromtimestamp(end/1000).strftime('%Y%m%d')}.csv"

ms = {"1m":60000,"3m":180000,"5m":300000,"15m":900000,"30m":1800000,"45m":2700000,
      "1h":3600000,"2h":7200000,"4h":14400000,"6h":21600000,"8h":28800000,"12h":43200000,
      "1d":86400000,"3d":259200000,"1w":604800000,"1M":2592000000}[interval]

batch = 1000*ms
est = math.ceil((end-start)/ms)

def fetch(s,e): return requests.get("https://api.binance.com/api/v3/klines", params={"symbol":pair,"interval":interval,"startTime":s,"endTime":e,"limit":1000}).json()

with open(file,"w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["time","open","high","low","close","volume"])
    t=0
    c=start
    while c<end:
        d = fetch(c,min(c+batch,end))
        if not d: break
        for o in d:
            ts=o[0]
            if ts>=end: break
            w.writerow([datetime.utcfromtimestamp(ts/1000).strftime('%Y-%m-%d %H:%M:%S')]+list(map(float,o[1:6])))
            t+=1
        c=d[-1][0]+ms
        p=int(t/est*30)
        print(f"\r[{('█'*p)+('-'*(30-p))}] {t}/{est} candles",end="")
        time.sleep(0.3)

print(f"\nDone! Saved to {file}")
