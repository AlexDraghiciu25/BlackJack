import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play_or_no = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

end_game = 0    #Not finished yet
if play_or_no == "n":
    end_game = 1    #Finished game

while end_game == 0:
    print(art.logo)
    total_player = 0    #The value of the player sum of cards
    total_computer = 0  #The value of the computer sum of cards

    player_cards = []
    computer_cards = []
    if total_player == 0:
        # First 2 cards for player
        random_var = random.randint(0, 12)
        player_cards.append(cards[random_var])
        total_player += cards[random_var]

        random_var = random.randint(0, 12)
        player_cards.append(cards[random_var])
        total_player += cards[random_var]

        while total_player > 21 and 11 in player_cards:
            poz = player_cards.index(11)
            player_cards[poz] = 1
            total_player -= 10

        # First card for computer
        random_var = random.randint(0, 12)
        computer_cards.append(cards[random_var])
        total_computer += cards[random_var]

        print(f"    Your cards: {player_cards}, current score: {total_player}")
        print(f"    Computer's first card: {computer_cards[0]}")

    lose = 0    #Still playable

    another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    while another_card == "y" and lose == 0:
        random_var = random.randint(0, 12)
        player_cards.append(cards[random_var])
        total_player += cards[random_var]

        while total_player > 21 and 11 in player_cards:
            poz = player_cards.index(11)
            player_cards[poz] = 1
            total_player -= 10

        if total_player <= 21:
            print(f"    Your cards: {player_cards}, current score: {total_player}")
            print(f"    Computer's first card: {computer_cards[0]}")
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        else:
            print(f"    Your final hand: {player_cards}, final score: {total_player}")
            print(f"    Computer's final hand: {computer_cards}, final score: {total_computer}")
            print("You went over. You lose! :((((((")
            lose = 1    #We lost the game

    if lose == 0:
        while total_computer < 17:
            random_var = random.randint(0, 12)
            computer_cards.append(cards[random_var])
            total_computer += cards[random_var]

            while total_computer > 21 and 11 in computer_cards:
                poz = computer_cards.index(11)
                computer_cards[poz] = 1
                total_computer -= 10

        print(f"    Your final hand: {player_cards}, final score: {total_player}")
        print(f"    Computer's final hand: {computer_cards}, final score: {total_computer}")

        if total_computer > 21:
            print("Opponent went over. You win! :)")
        elif total_player > total_computer:
            print("You win! 🎉")
        elif total_player < total_computer:
            print("You lose! :(")
        else:
            print("It's a draw!")

    play_or_no = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    end_game = 0  # Not finished yet
    if play_or_no == "n":
        end_game = 1  # Finished game