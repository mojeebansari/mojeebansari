movie={
      'tytle': 'tale of the tales',
      'year':  1977,
      'cast':  ['mojeeb','zameer','zabi','fazil']
      
}



print(movie)
print('title=',movie['tytle'])
print('action start=',movie['cast'])
print('production year=',movie['year'])
print(movie.get('budget'))

movie['budget']=25000
print(movie['budget'])

movie.update({'tytle':'story of me and you','year':1990,'cast': ['mojeeb','zameer','zabi','fazil'],'budget':1900})
del movie['cast']
year=movie.pop('year')
print ( year)

print(movie.keys())
print (movie.items())
print(movie.values())

print(movie)


for key, value in movie.items():
    print(key,':',value)


mojeeb=input('please enter the name of the movie')
if mojeeb=='tytle':
    print(movie['tytle'])
    
    
    