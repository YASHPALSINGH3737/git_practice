#list of destinations that we’re going to be using

destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]

#Our test traveler

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

#print(get_destination_index("Hyderabad, India"))

def get_traveler_location(traveler):
  traveler_destination = test_traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)

#print(test_destination_index)

#Visiting Interesting Places

attractions = [[], [], [], [], []]

#print(attractions)

def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
  except:
    return
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)
  return attractions_for_destination
#print(attractions)
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])

add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
#print(attractions)
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

#print(attractions)

#Finding the Best Places to Go

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  #loop over attractions list in one destination
  for place in attractions_in_city:
    possible_attraction = place
    attraction_tags = possible_attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])

  return attractions_with_interest

#la_arts = find_attractions('Paris, France', ['monument'])

#print(la_arts)

#See The Parts of a City You want to See

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  #print(traveler_interests)
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  print(traveler_attractions)
  interests_string = "Hi "+traveler[0]+", we think you'll like these places around "+traveler[1]+":"
  for interest in traveler_attractions:
    interests_string = interests_string +" "+interest
    #print(interest_string)
  return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', "Paris, France", ["art"]])

print(smills_france)
