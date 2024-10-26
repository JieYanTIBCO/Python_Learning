import random


def monty_hall_simulation(trials):
    switch_wins = 0
    stay_wins = 0

    for i in range(trials):
        # Randomly place the car behind one of the three doors
        car_position = random.randint(0, 2)

        # Player makes an initial choice randomly
        player_choice = random.randint(0, 2)

        # Host reveals a door that doesn't have the car and wasn't chosen by the player
        possible_reveal = [door for door in range(
            3) if door != car_position and door != player_choice]
        host_reveal = random.choice(possible_reveal)
        print(f"=================this is test{i+1}==============")
        print(f"Car Position is: {car_position}")
        print(f"Player Choice is: {player_choice}")
        print(f"possible_reveal is: {possible_reveal}")
        print(f"host_reveal is: {host_reveal}")


# Run the simulation for 10 trials
monty_hall_simulation(10)
