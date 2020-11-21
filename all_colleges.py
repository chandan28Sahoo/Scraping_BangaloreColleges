import json,string,csv
with open("colleges.json","r",encoding="utf-8") as file:
    data=json.load(file)

try:
    with open("clg.csv","w+") as wr:
        w=csv.writer(wr)
        w.writerow(['link','college name','Estd','Rating','Review','facilities','image','Address','contact_no','website'])
        for d in data["result"]:
            w.writerow([d['link'],d['college name'],d['Estd'],d['Rating'],d['Review'],d['facilities'],d['image'],d['Address'],d['contact_no'],d['website']])
except UnicodeEncodeError:
    pass