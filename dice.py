import random

total_score = 0
rolls = 0
while True:
    roll_sum = 0
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    roll_sum = dice_1 + dice_2
    if rolls < 3:
        if roll_sum == 7:
            print(f"Roll sum: {roll_sum}")
            total_score = total_score + 70
            print(f"Total: {total_score}")
            rolls = rolls + 1
            print(f"Rolls: {rolls}")
        else:
            print(f"Roll sum: {roll_sum}")
            total_score = total_score + roll_sum
            print(f"Total: {total_score}")
            rolls = rolls + 1
            print(f"Rolls: {rolls}")
    else:
        if not roll_sum == 7 and not (dice_1 == dice_2):
            print(f"Roll sum: {roll_sum}")
            total_score = total_score + roll_sum
            print(f"Total: {total_score}")
            rolls = rolls + 1
            print(f"Rolls: {rolls}")
        elif dice_1 == dice_2:
            print(f"You rolled doubles!")
            print(f"Roll sum: {roll_sum}")
            total_score = total_score * 2
            print(f"Total: {total_score}")
            rolls = rolls + 1
            print(f"Rolls: {rolls}")
        else:
            print(f"Roll sum: {roll_sum}")
            print("You rolled a 7!")
            print(f"Final Total: {total_score}")
            break