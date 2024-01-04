from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

# slices = [60,40, 30, 20] # should not add up to 100, it will figure out proportions
# labels = ["Sixty", "Forty", "Thirty", "Twenty"]
# colors = ["#008fd5", "#fc4fc0", "#ffff0e", "blue"]


# Language Popularity
# slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
# labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.3, 0]

plt.title("My Pie-Chart")

plt.pie(slices, labels = labels, explode = explode, wedgeprops = {"edgecolor": "black"}, 
        shadow = True, startangle = 90, autopct = "%2.1f%%")
plt.tight_layout()
plt.show()

