# IMPORT MODULES
import csv
import pandas as pd

# READ THE CSV
rows = []

with open("stars.csv",'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

headers = rows[0]
star_data = rows[1:]
#print(headers)
#print(star_data)

df = pd.read_csv("stars.csv")
solar_mass_list = df["solar_mass"].tolist()
solar_radius_list = df["solar_radius"].tolist()

solar_mass_list.pop(0)
solar_radius_list.pop(0)

# CONVERT STAR SOLAR MASS INTO SI UNIT OR KILOGRAM
star_solar_mass_si_unit = []

for data in solar_mass_list:

    si_unit = float(data)*1.989e+30
    star_solar_mass_si_unit.append(si_unit)

print(star_solar_mass_si_unit)

# CONVERT STAR SOLAR RADIUS INTO SI UNIT OR METERS
star_solar_radius_si_unit = []

for data in solar_radius_list:
    si_unit = float(data)* 6.957e+8
    star_solar_radius_si_unit.append(si_unit)

print(star_solar_radius_si_unit)

# CALCULATE THE GRAVITY OF EACH PLANET

star_masses = star_solar_mass_si_unit
star_radiuses = star_solar_radius_si_unit
star_names = df["star_names"].tolist()
star_names.pop(0)

star_gravities = []

for index,data in enumerate(star_names):
    
    
    a = float(star_masses[index])*5.972e+24
    b = float(star_radiuses[index])*float(star_radiuses[index])*6371000*6371000*6.674e-11    
    print("a ", a)
    print("b ", int(b))
    gravity =  0 
    if int(b):
        gravity =  a/b 
    
    star_gravities.append(gravity)

print(star_gravities)

# CREATE A NEW CSV WITH GRAVITY DATA
j = "extra"
star_gravities.append(j)
df["star_gravity"] = star_gravities
df.to_csv("upgrade.csv")