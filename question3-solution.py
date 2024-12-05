# Name: Ogundana joseph moyinoluwa
# Matric-No: RUN/IFT/22/13194

import matplotlib.pyplot as p

with_music = [304, 257, 174, 214, 69, 317, 387, 47, 157, 0, 332, 308, 317, 286, 236, 299, 206, 278, 188, 43, 0, 0, 0, 0, 0]
without_music = [292, 270, 47, 288, 324, 292, 364, 316, 287, 75, 282, 149, 274, 319, 213, 3, 324, 2, 128, 219, 94, 164, 0, 0, 0]

# Dot Plot: With Music
p.figure(figsize=(8, 5))
p.scatter(range(len(with_music)), with_music, color='blue', label='With Music')
p.title("Dot Plot: With Music")
p.xlabel("Plant Index")
p.ylabel("Growth (mm)")
p.legend()
p.show()

# Dot Plot: Without Music
p.figure(figsize=(8, 5))
p.scatter(range(len(without_music)), without_music, color='green', label='Without Music')
p.title("Dot Plot: Without Music")
p.xlabel("Plant Index")
p.ylabel("Growth (mm)")
p.legend()
p.show()

# Histogram: With Music
p.figure(figsize=(8, 5))
p.hist(with_music, bins=10, color='blue', alpha=0.7, label='With Music')
p.title("Histogram: With Music")
p.xlabel("Growth (mm)")
p.ylabel("Frequency")
p.legend()
p.show()

# Histogram: Without Music
p.figure(figsize=(8, 5))
p.hist(without_music, bins=10, color='green', alpha=0.7, label='Without Music')
p.title("Histogram: Without Music")
p.xlabel("Growth (mm)")
p.ylabel("Frequency")
p.legend()
p.show()
