(define (problem hiking1)
(:domain travel)
(:objects
 Romania Italy Spain France Germany - country
 plane1 plane2 plane3 car1 car2 car3 car4 bus1 bus2 bus3 - transport
 backpack0 - backpack
 person1 person2 person3 - person
 group0 - group
 restaurant1 restaurant2 restaurant3 fastfood1 fastfood2 fastfood3 - place-to-eat
 euro - money
 colosseum prado - sight
)
(:init
    (home group0 Romania)
    (visited_country Romania)
    (partners group0 person1 person2 person3)
    (have_water person3 backpack0)
    (have_money euro group0)
    (on_wishlist Spain group0)
    (on_wishlist Italy group0)
    (here group0 Romania)
    (exist_transport plane1 Romania Spain)
    (exist_transport plane2 Spain Italy)
    (sight_here prado Spain)
    (sight_here colosseum Italy)
    (have_camera group0 backpack0)
    (thirsty person3)
    (exist_place_to_eat fastfood1 Spain)
    (exist_place_to_eat fastfood2 Spain)
    (exist_place_to_eat fastfood3 Spain)
    (hungry group0 Spain)
    (exist_place_to_eat restaurant1 Italy)
    (exist_place_to_eat restaurant2 Italy)
    (exist_place_to_eat restaurant3 Italy)
    (exist_transport bus1 Spain France)
    (exist_transport bus2 France Germany)
    (exist_transport bus3 Germany Italy)
    (hungry group0 Italy)

    (exist_transport car1 Romania Spain)
    (exist_transport car2 Romania Spain)
    (exist_transport car3 Spain Italy)
    (exist_transport car4 Spain Italy)

    (= (cost_transport plane1) 17)
    (= (cost_transport plane2) 14)
    (= (cost_transport car1) 11)
    (= (cost_transport car2) 10)
    (= (cost_transport car3) 9)
    (= (cost_transport car4) 11)
    (= (cost_transport bus1) 3)
    (= (cost_transport bus2) 2)
    (= (cost_transport bus3) 2)

    (= (cost_mancare restaurant1) 3)
    (= (cost_mancare restaurant2) 3)
    (= (cost_mancare restaurant3) 2)
    (= (cost_mancare fastfood1) 3)
    (= (cost_mancare fastfood2) 4)
    (= (cost_mancare fastfood3) 3)


)
(:goal
   (and
    (visited_country group0 Italy)
    (visited_country group0 Spain)
    (not (hungry group0 Spain))
    (not (hungry group0 Italy))
   )
)
    (:metric minimize (total-cost))
)