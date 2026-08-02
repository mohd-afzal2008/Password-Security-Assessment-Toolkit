import hashlib


def generate_hashes():

    print("=" * 40)
    print("Hash Generator")
    print("=" * 40)

    password = input("Enter text to hash: ")


    md5_hash = hashlib.md5(
        password.encode()
    ).hexdigest()


    sha256_hash = hashlib.sha256(
        password.encode()
    ).hexdigest()


    sha512_hash = hashlib.sha512(
        password.encode()
    ).hexdigest()


    print("\n========== HASH RESULTS ==========")

    print("\nMD5:")
    print(md5_hash)


    print("\nSHA-256:")
    print(sha256_hash)


    print("\nSHA-512:")
    print(sha512_hash)