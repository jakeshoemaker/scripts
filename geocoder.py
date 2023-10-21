# this file will convert a csv of zips & turn it to lat/lng coords


import csv
import pgeocode

nomi = pgeocode.Nominatim('us')

read_file = 'harborcap.csv'
write_file = 'lat_lng.csv'

headers = ["lat", "lng"]
rows = []
with open(read_file, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        if row:
            data = nomi.query_postal_code(row[0])
            rows.append({ "lat": data["latitude"], "lng": data["longitude"]})
    print(rows)

with open(write_file, 'w') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(rows)
