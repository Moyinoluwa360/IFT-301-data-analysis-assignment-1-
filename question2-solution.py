# Name: Ogundana Joseph Moyinoluwa
# Matric: RUN/IFT/22/13194

import matplotlib.pyplot as plot
import pandas as pd

data = {
    "Height_Female": [175, 158, 166, 175, 160, 165, 166, 170, 170, 172],
    "Breath_Held_Female": [22.22, 30.57, 17.47, 22.39, 26.90, 36.85, 27.33, 29.55, 13.87, 34.66],
    "Height_Male": [184, 182, 180, 191, 189, 181, 180, 170, 176, 185],
    "Breath_Held_Male": [60.75, 67.41, 42.19, 59.74, 52.64, 43.37, 73.27, 59.09, 51.15, 58.32]
}

female_times = data["Breath_Held_Female"]
male_times = data["Breath_Held_Male"]
all_times = female_times + male_times

plot.figure(figsize=(10, 5))
plot.hist(all_times, bins=8, color='skyblue', edgecolor='black')
plot.xlabel('Breath Held Time (s)')
plot.ylabel('Frequency')
plot.title('Histogram of Breath Holding Times')
plot.show()

plot.figure(figsize=(10, 5))
plot.scatter([1]*len(female_times), female_times, color='red', label='Female')
plot.scatter([2]*len(male_times), male_times, color='blue', label='Male')
plot.xticks([1, 2], ['Female', 'Male'])
plot.ylabel('Breath Held Time (s)')
plot.title('Side-by-Side Dot Plot of Breath Holding Times')
plot.legend()
plot.show()
