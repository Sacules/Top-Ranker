# Top Ranker

A simple, basic Python script that reads text files that contain ranked lists of movies, videogames, albums, etc. Top Ranker gathers those, give them a score based on position, and ranks them - top 10, top 50, etc. Useful for gathering info about a community's tastes on the mentioned items.

At this very stage, it can only read local files, and it's terminal-based. The resulting top is saved into a text file.

Output example of top 10 albums from 6 lists:
```
N°   Album                                                                                           Score
----------------------------------------------------------------------------------------------------------
1.   Burial - Untrue                                                                                 12
2.   Peste Noire - L'Ordure à rétal Pur                                                              10
3.   Porcupine Tree - In Absentia                                                                    10
4.   Porcupine Tree - Fear of a Blank Planet                                                         10
5.   The Mars Volta - Frances the Mute                                                               10
6.   Steve Reich - Phases                                                                            10
7.   Dream Theater - Octavarium                                                                      10
8.   Opeth - Ghost Reveries                                                                          9
9.   Nine Inch Nails - The Downward Spiral                                                           9
10.  Godspeed You! Black Emperor - F# A# Infinity                                                    9

```
As you can see, with only 6 lists and 10 albums, there isn't really much coincidence. Note that, if you choose to make a top 10 for example, the script will only load the first 10 items of your lists. I recommend taking big lists and choosing, at least, a top 50 or top 100 for better results.
