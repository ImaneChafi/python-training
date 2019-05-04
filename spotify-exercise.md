# Spotify exercise (Draft)

Download a dataset of Spotify's [Top Tracks of 2018](https://www.kaggle.com/nadintamer/top-spotify-tracks-of-2018/). The dataset is a CSV ('comma-separated values') file.

### Part 1
Write a program to parse the dataset and compute the average song tempo.

Hint: use the [csv](https://docs.python.org/3/library/csv.html) module.

### Part 2
Adjust your program so that it computes the average song tempo grouped by the songs' `valence`. The output should be something like:

```
For songs with 0.0 <= valence < 0.1, average tempo is 70 BPM.
For songs with 0.1 <= valence < 0.2, average tempo is 80 BPM.
For songs with 0.2 <= valence < 0.3, average tempo is 60 BPM.
...
For songs with 0.9 <= valence <= 1.0, average tempo is 80 BPM.
```

### Part 3
For each song, download related artist information using the MusicBrainz API.
Show the average tempo by artist country.