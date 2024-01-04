# standard library 
from collections import Counter
import csv
import numpy as np
from matplotlib import pyplot as plt

# styling of the plot takes care of color, linewidth, linestyle, etc
plt.style.use("ggplot")

with open("data.csv") as csvfile:
    reader = csv.DictReader(csvfile)

    language_counter = Counter()
    for row in reader:
        language_counter.update(row["LanguagesWorkedWith"].split(";")) # dictreader gives the value and split stores it in list which is read by counter to update dictonary count
# passes an iterable in this case list and return values in dict-pairs
        
languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

# want to show the data using reverse order
languages.reverse()
popularity.reverse()


plt.barh(languages, popularity) # many data? use barh method
plt.ylabel("Most popular coding lang")
plt.xlabel("Number of users")

plt.title("Languages by stackoverflow community 2019")

plt.tight_layout()

plt.show()

    