# load data from sample_data directory 
import os
import csv 
import json 
# locate data of CSV type 

ashu_data = "/content/sample_data/hotel_hospitality_data.csv"
ashu_clean_data = []
# opening file and check data 
with open(ashu_data,'r',encoding='utf-8-sig') as f1:
  ashu_csv_reader = csv.reader(f1)
  for i in ashu_csv_reader:
    for j in i: 
      try:
        # replace brackets , double quotes , 
        replace_data1 = j.replace('["','').replace('"]','').replace('\"','"')
        # load each object data in json context  
        replace_data1_json = json.loads(replace_data1)
        # append data in a list for futher saving 
        ashu_clean_data.append(replace_data1_json)
      except json.JSONDecodeError as e: 
        print("some error found")

# lets printing clean data
print(ashu_clean_data[0])

# save this data for reuse 
ashu_data_jsonl = "/content/sample_data/ashu_hotel_hospitality_data.jsonl"
# using file handling 
with open(ashu_data_jsonl,'w',encoding='utf-8') as f2:
  for items in ashu_clean_data:
    f2.write(json.dumps(items) + '\n')
      

# printing data for validataion purpose
with open(ashu_data_jsonl,'r',encoding='utf-8') as f3:
  ashu_datasets = [ json.loads(i) for i in f3]

# total length 
print("length of data dataset is ",len(ashu_datasets))
print("first example ")
for ashud in ashu_datasets[0]['messages']:
  print(ashud)
