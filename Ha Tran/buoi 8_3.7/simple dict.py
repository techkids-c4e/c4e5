##simple_dict={
##    'name':'Khanh',
##    'age':18
##    }
##print(simple_dict['name'])
movie1 = {
"original_name": "The hunger's game",
"name": "Đấu trường sinh tử",
"year": 2016}
movie2={
"original_name": "Point Break",
"name": "ranh giới chết",
"year": 2016}

movies=[movie1,movie2]
#Adding     
o,n,y=input('New movie information: ').split(',')
x={"original_name":str(o),
   "name":str(n),
   "year":int(y)
   }

movies.append(x)
print(movies)
#edit movie

while True:
    n=input('Which movie do you want to edit?')
    original,name,year=input('New information').split(',')
    y={"original_name":original,
       "name":str(name),
       "year":int(year)
       }
    for movie in movies:
        for key,value in movie.items():
            if value==n:
                for key in movie:
                    movie[key]=y[key]

    print(movies)
                
        
#remove movie
n=input('Which movie do you want to remove?')
for movie in movies:
    if movie["original_name"]==n:
        movies.pop(movies.index(movie))


        
print(movies)
    
        
