import sys
import csv

if len(sys.argv) != 2:
    print("Please provide ONE and only ONE dataset")
    exit(1)

to_pop = []
data = []
with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    featured = False
    for row in csv_reader:
        if line_count == 0:
            features = row
            line_count += 1
        else:
            # Check numerical column
            if featured == False:
                for i in range(len(row)):
                    try:
                        float(row[i])
                    except:
                        to_pop.insert(0, i)
                featured = True
            else:
                data.append(row)
                line_count += 1

# Pop non numerical features
for i in to_pop:
    features.pop(i)

print("         ", end='')

for feat in features:
    print(f'{feat}      ', end='')
        
print("\nCount    ", end='')
for rows in features:
    print('{:.6f}'.format(line_count-1)+'  ', end='')
print("\nMean    ")
print("Std    ")
print("Min    ")
print("25%    ")
print("50%    ")
print("75%    ")
print("Max    ")

