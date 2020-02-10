# MovingwallsTest
Just a testing and a practice to hone my django and python skills

# Chapter 1 - Feb 4 2020 20:00 - 23:00
Was planning on adding APIs for the Hotel, Airplane and City Taxi.
Would base on the rate of everything base on real time prices and mock computation from respective APIs,
but didnt find any free API so will make manual records via DB for the sake of test.

# Chapter 2 - Feb 5 2020 21:00 - 23:00
Due to the complication of what I've thought of using for the computation of the distance between locations
I changed the structure of the database and tested geopy to compute the distance between cities.
It works like a charm but there is no routing of streets and traffic.
So I'm going to base the computation based on the this computation

BASE FARE * DISTANCE IN KPH + ( (BASE FARE * DISTANCE IN KPH) * (DISTANCE IN KPH / 20 KPH)

Due to the place being far the taxi will need additional for their gas and whatnot(Just an additional). 

# Chapter 3 - Feb 9 2020 20:00 - 23:00
Changes had to occur to make everything as simple as possible and model dependent.
Had to change the formula based on the input in the model to be used in the views.
Change location to a coordinate basis, this is not accurate due to the distance is not measured by street km.
Was unable to use APIs due to don't want to hook my credit card to any services that I might tend to forget.
Models are final for now as long as there are no changes in the future while building the views.

# Chapter 4 - Feb 10 2020 21:00 - 00:00
Trying as much as possible to limit the process to the generics of the django, to utilize the 
requirements and to practice myself on the other parts of django that I haven't explored yet.
so far there is the half of the create view for the travel form being created. but will still amend that due
to the conditioning per fields that is needed to make the validations as complete as possible.

## Limitations
Due to my limited time to work with the project due to being a on-call personnel.
Here are the limitations of the app:
  -- The looks are bare minimun - not really my strong suit - though I can design websites I need
     more time compared to web designers.
  -- Coordinate level location is good for planes but not cars, since was unable to secure an API 
     with road origin and destination measurements with and traffic, the computation base formula
     will be based on the intercity travel of cars.
  -- Manual mapping of location tier list to check if the cities are available via taxi travel.
  -- 

#Requirements
--EMPTY FOR NOW TILL THE PROGRAM IS FINISH
#END Requirements

##TODO: 
## Will Add '--' to finished to do for tracking purposes

#Sub and own requirements
Extend city to user account and add other City if city designation of employee is not supported by system.
Add Airport and airline partnership prices.
Create a custom migration data for sample.

#Main Requirements Examination
Creating the employee booking form.
Create the manager booking form.
Create the manager approval form.
Create the finance manager approval form.

##END TODO
