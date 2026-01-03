import random


def simulate_round(rng=None, verbose=True):
    """Simulate a single round of the 'bank' dice game.

    Args:
        rng: object with `randint(a, b)` method. If None, uses the standard
             `random` module.
        verbose: when True, print the same messages the original script did.

    Returns:
        (final_total, history) where history is a list of per-roll dicts:
            {"dice_1": int, "dice_2": int, "sum": int, "total": int, "rolls_after": int}
    """
    if rng is None:
        rng = random1

    total_score = 0
    rolls = 0
    history = []

    while True:
        dice_1 = rng.randint(1, 6)
        dice_2 = rng.randint(1, 6)
        roll_sum = dice_1 + dice_2

        if rolls < 3:
            if roll_sum == 7:
                if verbose:
                    print(f"Roll sum: {roll_sum}")
                total_score += 70
            else:
                if verbose:
                    print(f"Roll sum: {roll_sum}")
                total_score += roll_sum

            rolls += 1
            if verbose:
                print(f"Total: {total_score}")
                print(f"Rolls: {rolls}")

        else:
            # After the first three rolls
            if dice_1 == dice_2:
                if verbose:
                    print(f"You rolled doubles!")
                    print(f"Roll sum: {roll_sum}")
                total_score *= 2
                rolls += 1
                if verbose:
                    print(f"Total: {total_score}")
                    print(f"Rolls: {rolls}")
            elif roll_sum == 7:
                if verbose:
                    print(f"Roll sum: {roll_sum}")
                    print("You rolled a 7!")
                    print(f"Final Total: {total_score}")
                break
            else:
                if verbose:
                    print(f"Roll sum: {roll_sum}")
                total_score += roll_sum
                rolls += 1
                if verbose:
                    print(f"Total: {total_score}")
                    print(f"Rolls: {rolls}")

        history.append({
            "dice_1": dice_1,
            "dice_2": dice_2,
            "sum": roll_sum,
            "total": total_score,
            "rolls_after": rolls,
        })

    return total_score, history


if __name__ == "__main__":
    simulate_round()