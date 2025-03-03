import hashlib
import os

linux_folders = {
    "1": ["Scrivania", "Desktop"],
    "2": ["Scaricati", "Downloads"],
    "3": ["Documenti", "Documents"],
    "4": ["Immagini", "Pictures"]
}

windows_folders = {
    "1": "Desktop",
    "2": "Downloads",
    "3": "Documents",
    "4": "Pictures"
}

protected_paths = [
    "C:\\Windows", "C:\\Program Files", "C:\\Program Files (x86)", "C:\\ProgramData",
    "/bin", "/boot", "/dev", "/etc", "/lib", "/lib64", "/opt", "/proc", "/root", "/sbin", "/sys", "/usr", "/var"
]


def get_valid_linux_path(choice):
    """ Return the correct path of the selected folder on Linux, handling languages """
    home = os.path.expanduser("~")

    if choice in linux_folders:
        for folder in linux_folders[choice]:
            path = os.path.join(home, folder)
            if os.path.exists(path):
                return path
    return None


def get_valid_windows_path(choice):
    """ Return the correct path of the selected folder on Windows """
    home = os.path.expanduser("~")

    if choice in windows_folders:
        path = os.path.join(home, windows_folders[choice])
        if os.path.exists(path):
            return path

    return None


def sanitize_filepath(filepath: str) -> str | None:
    """ Remove any double quotes present in the path """

    # Check if the path is enclosed in double quotes
    path = filepath.strip().strip('"').strip("\n")

    # Check if the path is not a directory
    if os.path.isdir(path):
        print("    [!] ERROR: Cannot compute the hash of a directory!\n")
        return None

    # Check if the path refers to protected paths (system directories)
    for protected_path in protected_paths:
        if path.startswith(protected_path):
            print("    [!] ERROR: Protected directories cannot be used!")
            return None

    # Check if the path refers to a valid file
    if not os.path.isfile(path):
        print("    [!] ERROR: The path inserted does not refer to a valid file!")
        return None

    return path


def sanitize_hash(_hash: str) -> str | None:
    """ Remove any spaces or double quotes present in the hash """
    _hash = _hash.strip().strip('"').strip("\n").replace(" ", "")

    # Check if the hash is valid
    if len(_hash) == 0:
        print("[!] ERROR: The hash provided is empty!\n")
        return None

    return _hash


def calculate_file_hash(filepath: str, hash_function: str) -> str | None:
    """ Compute the hash of the file using the provided algorithm """
    hash_func = getattr(hashlib, hash_function)
    hasher = hash_func()

    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        print(f"[!] ERROR: {e}")
        return None


def get_hash_algorithms():
    """ Print the available hash functions """
    algorithms = list(hashlib.algorithms_available)
    print("[*] Available hash functions:")
    for i in range(0, len(algorithms), 5):
        print("       " + " | ".join(algorithms[i:i + 5]))

    return algorithms


def select_filepath():
    """ Select the root folder or manually insert the path """

    if os.name == "posix":  # Linux/macOS
        for key, names in linux_folders.items():
            print(f"   {key}) ~/{names[0]}")

        while True:
            choice = input("\n[+] Select a root folder or enter a complete path: ").strip()

            if choice.isdigit():
                if choice in linux_folders:
                    root_path = get_valid_linux_path(choice)
                    if root_path:
                        filename = input(f"\n[+] Enter the file name (or its relative path): {root_path}/").strip()
                        filepath = os.path.join(root_path, filename)
                        break
                elif choice == "0":
                    print("[!] Exiting... Bye Bye!")
                    exit()
                else:
                    print("[!] ERROR: Invalid choice!")
            else:
                # Get the full path
                filepath = sanitize_filepath(choice)
                if filepath is not None:
                    break

    else:  # Windows
        for key, name in windows_folders.items():
            print(f"   {key}) ~\\{name}")

        while True:
            choice = input("\n[+] Select a root folder or enter the complete path ([0] to exit): ").strip()

            # Check if choice is an integer
            if choice.isdigit():
                if choice in windows_folders:
                    root_path = get_valid_windows_path(choice)
                    if root_path:
                        filename = input(f"    Enter the file name (or its relative path): {root_path}\\").strip()
                        filepath = os.path.join(root_path, filename)

                        filepath = sanitize_filepath(filepath)
                        if filepath is not None:
                            break
                elif choice == "0":
                    print("[!] Exiting... Bye Bye!")
                    exit()
                else:
                    print("[!] ERROR: Invalid choice!")
            else:
                # Get the full path
                filepath = sanitize_filepath(choice)
                if filepath is not None:
                    break

    if filepath is not None:
        print(f"    Path sanitized: {filepath}")

    return filepath
