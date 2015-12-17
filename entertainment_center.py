import media
import fresh_tomatoes



the_jerk= media.Movie(
'The Jerk',
"""An idiotic man struggles to make it through life on his own in St. Louis.""",
'Comedy',
'94',
'Steve Martin, Bernadette Peters, Catlin Adams',
'https://upload.wikimedia.org/wikipedia/en/3/3e/The_Jerk.jpg',
'https://www.youtube.com/watch?v=2Qut3v1KlSs',
'1979',
'R',
'4.0')

stripes=media.Movie(
'Stripes',
'Two friends who are dissatisfied with their jobs decide to join the army for a bit of fun.',
'Comedy',
'106',
'Bill Murray, John Candy, Harold Ramis',
'https://upload.wikimedia.org/wikipedia/en/3/3e/Stripesposter.jpg',
'https://www.youtube.com/watch?v=Yajlukh8sic',
'1981',
'R',
'3.5')

fury=media.Movie(
'Fury',
"""Army sergeant named Wardaddy commands a Sherman tank and his five-man
crew on a deadly mission behind enemy lines.""",
'Drama, Historical Fiction',
'134',
'Brad Pitt, Shia LaBeouf, Logan Lerman',
'https://upload.wikimedia.org/wikipedia/en/1/17/Fury_2014_poster.jpg',
'https://www.youtube.com/watch?v=DNHuK1rteF4',
'2014',
'R',
'4.0')

gran_torino=media.Movie(
'Gran Torino',
"""Disgruntled Korean War veteran Walt Kowalski sets out to reform his neighbor,
a Hmong teenager who tried to steal Kowalski\'s prized possession: a 1972 Gran Torino.""",
'Drama',
'116',
'Clint Eastwood, Bee Vang, Christopher Carley',
'https://upload.wikimedia.org/wikipedia/en/c/c6/Gran_Torino_poster.jpg',
'https://www.youtube.com/watch?v=3WkGaPMInMc',
'2008',
'R',
'4.5'
)

star_wars=media.Movie(
'Star Wars',
"""A boys joins forces with a Jedi Knight, a cocky pilot, a wookiee, and two
 droids to save the universe from the Empire\'s world destroying battle-station""",
'Sci-Fi, Action, Adventure, Fantasy',
'120',
'Mark Hammil, Harrison Ford, Carrie Fisher',
'https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg',
'https://www.youtube.com/watch?v=vZ734NWnAHA',
'1977',
'PG',
'4.5' )

inside_out=media.Movie(
'Inside Out',
"""After Riley is uprooted from her Midwest life and moved to San Francisco,
her emotions - Joy, Fear, Anger, Disgust, and Sadness - conflict on how best
to navigate a new city, house, and school""",
'Animation, Adventure, Comedy, Family',
'120',
'Amy Poehler, Bill Hader, Lewis Black',
'https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg',
'https://www.youtube.com/watch?v=7ZLOYXKmIkw',
'2015',
'G',
'5' )



movies=[gran_torino,stripes, fury, the_jerk, star_wars, inside_out]

fresh_tomatoes.open_movies_page(movies)
