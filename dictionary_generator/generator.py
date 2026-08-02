from .mutations import generate_mutations


def create_dictionary():

    print("=" * 40)
    print("Dictionary Generator")
    print("=" * 40)

    name = input("Name : ").strip()
    dob = input("DOB (DDMMYYYY) : ").strip()

    words = set()

    words.update(generate_mutations(name))

    if dob:

        words.add(dob)

        words.add(name + dob)

        words.add(name + dob[-4:])

        words.add(name.capitalize() + dob[-4:])

    with open("output/wordlist.txt", "w") as file:

        for password in sorted(words):
            file.write(password + "\n")

    print("\nWordlist generated successfully.")
    print("Saved as output/wordlist.txt")