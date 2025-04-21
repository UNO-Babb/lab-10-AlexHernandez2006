#MapPlot.py
#Name: Alex Hernandez Lopez
#Date: 04/20/25
#Assignment: Lab 10

import video_games
import matplotlib.pyplot as plt
import pandas
video_game = video_games.get_video_game()

scores = []
years = []
for game in video_game:
    score = game["Metrics"]["Review Score"]
    year = game["Release"]["Year"]
    scores.append(score)
    years.append(year)

df = pandas.DataFrame({"Year": years, "Review Score": scores})
print(df)

df.plot(kind = 'scatter', x = 'Year', y = 'Review Score')
plt.savefig('output')

"""The graph tells us the score a game was given during the year that is was released.
    It makes that clear by plotting the scores along the y-axis and the release years on the x-axis."""