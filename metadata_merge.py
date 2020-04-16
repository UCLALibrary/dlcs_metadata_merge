import csv

#merges two dictionaries together
def Merge(dict1, dict2): 
    res = {**dict1, **dict2} 
    return res 

#function to get all headers in DLCS export csv and then add three from eureka csv
def get_headers(file_name):
    with open(file_name, 'r', newline='') as f:
        r = csv.reader(f, delimiter=',')
        headers = next(r)
        headers.extend(['Bucketeer State','IIIF Access URL', 'IIIF Manifest URL'])
        return headers

#inputs from terminal for eureka csv and dlcs export csv
eureka = str(input('Eureka CSV:')).strip(' ')
dlcs_export = str(input('DLCS Export CSV:')).strip(' ')


cursor = csv.DictReader(open(eureka),
    delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

#dictionary for iiif metadata from eureka csv
iiif_dict = {}

#adds iiif metadata to iiif_dict
for row in cursor:
    item_ark = row['Item ARK']
    bucketeer = row['Bucketeer State']
    iiif_access = row['IIIF Access URL']
    iiif_manifest = row['IIIF Manifest URL']
    iiif_dict[item_ark] = {
        'Bucketeer State': bucketeer,
        'IIIF Access URL': iiif_access,
        'IIIF Manifest URL': iiif_manifest
        }

cursor_dlcs = csv.DictReader(open(dlcs_export),
    delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

#overwrtie eureka file with new, merged dictionary metadata
#will only write rows for metadata in eureka csv
with open(eureka, 'w') as out:
    writer = csv.DictWriter(out, fieldnames=get_headers(dlcs_export))
    writer.writeheader()
    for row in cursor_dlcs:
        for item_ark in iiif_dict.keys():
            if row['Item ARK'] == item_ark:
                new_row = Merge(row, iiif_dict[item_ark])
                writer.writerow(new_row)
            else:
                pass




