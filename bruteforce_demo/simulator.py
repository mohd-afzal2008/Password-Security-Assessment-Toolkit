import time
import itertools
import string


def brute_force_simulation():

    print("=" * 40)
    print("Brute-force Simulation Demo")
    print("=" * 40)

    target = input("Enter demo password (use small password): ")

    characters = string.ascii_lowercase + string.digits


    print("\nStarting simulation...")
    print("Character set:")
    print("a-z + 0-9")


    attempts = 0
    start_time = time.time()

    found = False


    # Maximum length for safe demo
    for length in range(1, 6):

        for combination in itertools.product(characters, repeat=length):

            attempts += 1

            guess = "".join(combination)


            if guess == target:

                found = True
                end_time = time.time()

                break


        if found:
            break



    total_time = round(
        end_time - start_time,
        4
    ) if found else 0



    print("\n========== RESULT ==========")


    if found:

        print("Password Found:", target)

        print("Attempts:", attempts)

        print("Time Taken:", total_time, "seconds")


    else:

        print("Password not found")

        print("Try a smaller demo password")
