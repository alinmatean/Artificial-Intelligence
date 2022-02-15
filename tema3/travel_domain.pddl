(define (domain travel)
(:requirements :strips :equality :typing :action-costs)  
(:types country transport backpack person group place-to-eat money sight)
  (:predicates 
             (hungry ?g - group ?c - country)
             (on_wishlist ?c - country ?g - group)
             (visited_sight ?g - group ?s - sight ?c - country)
             (visited_country ?g - group ?c - country)
             (exist_transport ?t - transport ?c1 - country ?c2 - country)
             (exist_place_to_eat ?p - place-to-eat ?c - country)
             (have_money ?m - money ?p - group)
             (have_camera ?p - group ?b - backpack)
             (have_water ?p - person ?b - backpack)
             (sight_on_camera ?s - sight ?c - country)
             (thirsty ?p1 - person)
             (partners ?group - group ?p1 - person ?p2 - person ?p3 - person)
             (here ?g - group ?c - country)
             (start ?g - group)
             (sight_here ?s - sight ?c - country)
             (home ?g - group ?c - country)
    )
    
    
    (:functions
        (cost_transport ?transport) - number
        (cost_mancare ?place-to-eat) - number 
        (total-cost) - number)

    (:action start_trip
        :parameters (?group ?p1 ?p2 ?p3 ?country)
        :precondition (and (not (start ?group))
                    (partners ?group ?p1 ?p2 ?p3)
                    (home ?group ?country)
        )
        :effect (and (not (home ?group ?country)) 
                    (start ?group)
                (increase (total-cost) 1)
                )
    )

    (:action enter_country    
     :parameters (?group ?transport ?country1 ?country2) 
     :precondition (and (start ?group)
                    (not (here ?group ?country2))
                    (here ?group ?country1)
                    (not (visited_country ?group ?country2))
                    (exist_transport ?transport ?country1 ?country2)
                    (not (= ?country1 ?country2))
                 )
     :effect (and (here ?group ?country2)
                (not (here ?group ?country1)) 
                (increase (total-cost) (cost_transport ?transport) ))
        )

    (:action take_photo
     :parameters (?group ?backpack ?sight ?country)
     :precondition (and (here ?group ?country)
                   (on_wishlist ?country ?group)
                   (have_camera ?group ?backpack)
                   (not (sight_on_camera ?sight ?country))
                   (sight_here ?sight ?country) )
     :effect (and (sight_on_camera ?sight ?country)
            (increase (total-cost) 1))
           )
    
    (:action visit_sight
     :parameters (?group ?sight ?country ?money)
     :precondition (and (have_money ?money ?group)
                   (here ?group ?country) 
                   (sight_on_camera ?sight ?country)
                   (not (visited_sight ?group ?sight ?country)))
     :effect (and (visited_sight ?group ?sight ?country)
                (increase (total-cost) 1))
            )

    (:action visit_country
     :parameters (?group ?sight ?country)
     :precondition (and (not (visited_country ?group ?country))
                   (visited_sight ?group ?sight ?country)
                   (here ?group ?country) )
     :effect (and (visited_country ?group ?country)
            (increase (total-cost) 1))
           )
    (:action drink_water
     :parameters (?person ?backpack)
     :precondition (and (thirsty ?person) 
                   (have_water ?person ?backpack)
                   )
     :effect (and (not (thirsty ?person))
             (not (have_water ?person ?backpack))
             (increase (total-cost) 1))
             
                )

    (:action eat
        :parameters (?group ?country ?place_to_eat ?money)
        :precondition (and (hungry ?group ?country)
                       (have_money ?money ?group)
                       (exist_place_to_eat ?place_to_eat ?country)
                       (here ?group ?country) )
        :effect (and (not (hungry ?group ?country))
        (increase (total-cost) (cost_mancare ?place_to_eat)))
    )

    ; (:action go_home    
    ;      :parameters (?home ?group)
    ;      :precondition (and
    ;         (not (stop_trip ?group ?home))
    ;           (forall (?i_country - country)
    ;               (visited_country ?group ?i_country)
    ;           ) 
    ;          )
    ;      :effect (and (stop_trip ?group ?home) )
    ;             )
    
)