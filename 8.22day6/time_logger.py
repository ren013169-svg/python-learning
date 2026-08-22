import datetime
now=datetime.datetime.now()
with open("runlog.txt","a",encoding="utf-8") as f:
    f.write(f"{now}\n")