import csv

animals = {}

total_animals = 0

most_animal_count = 0
most_animal_name = ""

with open("zoo.csv", 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    # Loop through the data
    for row in csvreader:

      animal_type = row[0]

      total_animals = total_animals + 1

      if animal_type in animals:
        animals[animal_type] = animals[animal_type] + 1
      else:
        animals[animal_type] = 1

for key, value in animals.items():

  if value > most_animal_count:
    most_animal_name = key
    most_animal_count = value

  print(key + ":" + str(value))

print('\nMost Animal:')

print(most_animal_name + ": " + str(most_animal_count))


