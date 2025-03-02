# HashGuard
HashGuard is a Python script designed to either verify the integrity of a file or simply compute its hash. The
script provides a command-line interface to guide the user through the process.

The project uses the `hashlib` library in Python. Hence, the available hash algorithms are the ones supported by
`hashlib` (depending on the system), such as:

{ `sha224`, `sha256`, `md5`, `sha512`, `sm3`, `sha1`, `sha384`, `md5-sha1`, `shake_256`, `sha512_224`,
`sha3_224`, `sha3_384`, `blake2b`, `shake_128`, `ripemd160`, `sha3_512`, `sha512_256`, `sha3_256`, `blake2s` }


## How it works
Upon execution, the script prompts the user to select one of the following operations:

1) **Verify a file's integrity:**
   The user provides the path to the file to be verified and the hash to compare with. Once the hash algorithm is
   selected, the script computes the hash itself and compares it with the given one.
   If the hashes match, the file's integrity is confirmed.

2) **Compute the hash of a file:**
   The user provides the path to the file and selects the hash algorithm to use. The script computes and displays the
   file's hash without performing any verification.

The script does not allow selecting files from **protected directories** (e.g., `C:\Windows`, `C:\Program Files`, `/etc`, `/bin`, etc.).


## Usage
To use this script, clone (or download) the repository, and run the script:

```bash
git clone https://github.com/Mahnz/hash_guard.git
cd hash_guard

./hash_guard.py
```

The script will guide you through the selected process, whether verifying a file or calculating its hash.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.