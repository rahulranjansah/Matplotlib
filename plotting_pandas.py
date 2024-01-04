from collections import Counter
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

data = pd.read_csv("data.csv")
ids = data["Responder_id"]
lang_responses = data["LanguagesWorkedWith"]

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(";"))

languages = []
popularity = []

for item in language_counter.most_common(20):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)
plt.xlabel("Number of users")
plt.ylabel("Languages")

plt.tight_layout()

plt.show()


