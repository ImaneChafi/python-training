# MusicBrainz exercise

Use the [MusicBrainz Search API](https://musicbrainz.org/doc/Development/XML_Web_Service/Version_2/Search) to display information about artists.

### Part 1
Write a program to display the number of male, female and other artists. Only count artists who are a 'person' (rather than a 'group').

Hint: use the [`artist` API](https://musicbrainz.org/doc/Development/XML_Web_Service/Version_2/Search#Artist). Use [urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) to access the API. 

### Part 2
Make an interactive command line program that allows the user to search for artists.

Example:
```
> python artist_search.py
Hey there! Use this program to search for artists.
Type Ctrl+C at any time to quit.

Type an artist's name:
    > Queen
    There are 369 artists with 'Queen' in their name.

Type another artist's name:
    > asfhhklasjhf
    No artists with this name.

Type another artist's name:
    > <Ctrl+C>

Goodbye :)
```

### Part 3
Add some useful information about the artist and their tags. Exclude tags with a score of zero or below.

Example usage:
```
Type an artist's name:
    > Queen
    There are 369 artists with 'Queen' in their name.
    The first one is Queen (UK rock group).
    Queen has 9 tags. The first 5 are:
        rock, british, hard rock, glam rock, art rock
```