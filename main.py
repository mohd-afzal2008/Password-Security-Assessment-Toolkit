from dictionary_generator.generator import create_dictionary
from password_strength.analyzer import analyze_password
from hash_demo.hash_generator import generate_hashes
from hash_demo.hash_identifier import identify_hash
from bruteforce_demo.simulator import brute_force_simulation
from reports.report_generator import generate_report


def menu():

    while True:

        print("\n")
        print("=" * 50)
        print("Password Security Assessment Toolkit")
        print("=" * 50)

        print("1. Dictionary Generator")
        print("2. Password Strength Analyzer")
        print("3. Hash Generator")
        print("4. Hash Identifier")
        print("5. Brute-force Simulator")
        print("6. Generate Report")
        print("7. Exit")

        choice = input("\nSelect : ")

        if choice == "1":
            create_dictionary()

        elif choice == "2":

            analyze_password()

        elif choice == "3":

            generate_hashes()


        elif choice == "4":

            identify_hash()

        elif choice == "5":

            brute_force_simulation()


        elif choice == "6":

            generate_report()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Module coming soon...")


if __name__ == "__main__":
    menu()
