#!/usr/bin/env python3

from utils import select_filepath, sanitize_hash, calculate_file_hash, get_hash_algorithms


def main():
    print("\n<- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ->")

    print(r"""
                         _   _           _          ____                     _ 
                        | | | | __ _ ___| |__      / ___|_   _  __ _ _ __ __| |
                        | |_| |/ _` / __| '_ \    | |  _| | | |/ _` | '__/ _` |
                        |  _  | (_| \__ \ | | |   | |_| | |_| | (_| | | | (_| |
                        |_| |_|\__,_|___/_| |_|    \____|\__,_|\__,_|_|  \__,_| 
        """)

    print("\n<- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ->\n")

    print("What would you like me to do?\n" +
          "   1) Verify file integrity\n" + "   2) Calculate file hash")

    while True:
        mode = input("\n[+] Select an option ([0] to exit): ").strip()
        if mode in ["1", "2"]:
            break
        elif mode == "0":
            print("[!] Exiting... Bye Bye!")
            exit(0)
        print("[!] ERROR: Invalid selection. Try again.")

    print("\n<- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ->\n")

    print("Select the file from:")
    filepath = select_filepath()

    print("\n<- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ->\n")

    algorithms = get_hash_algorithms()

    while True:
        hash_function = input("\n[+] Enter the hash algorithm to use (exact name): ").strip().lower().replace("\n", "")

        if hash_function not in algorithms:
            print("    [!] ERROR: The selected function is not valid (or not supported).")
        else:
            print(f"    Hash function selected: {hash_function}")
            break

    if mode == "1":
        while True:
            provided_hash = input("\n[+] Enter the provided digest: ")
            provided_hash = sanitize_hash(provided_hash)

            if provided_hash is not None:
                break

            print("    [!] ERROR: The hash provided is not valid.")

    print("\n<- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ->\n")

    file_hash = calculate_file_hash(filepath, hash_function)
    if file_hash is None:
        return

    if mode == "1":
        print(f"[*] PROVIDED HASH: {provided_hash}")

    print(f"[*] COMPUTED HASH: {file_hash}")

    if mode == "1":
        if file_hash == provided_hash:
            print("\n[!] DIGESTS ARE EQUAL. Integrity verified.")
        else:
            print("\n[!] DIGESTS ARE DIFFERENT! Integrity compromised.")

    print("\n<- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ->")


if __name__ == "__main__":
    main()
