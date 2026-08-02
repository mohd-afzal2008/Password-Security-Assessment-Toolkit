def identify_hash():

    print("=" * 40)
    print("Hash Identifier")
    print("=" * 40)


    hash_value = input("Enter hash: ")


    length = len(hash_value)


    if length == 32:

        result = "MD5"


    elif length == 64:

        result = "SHA-256"


    elif length == 128:

        result = "SHA-512"


    else:

        result = "Unknown hash type"


    print("\nPossible Hash Type:")
    print(result)