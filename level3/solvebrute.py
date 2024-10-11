import hashlib
import binascii


def sha256_hash_bytearray(input_bytearray):
    input_bytearray = bytearray(input_bytearray)
    # Create a new SHA-256 hash object
    sha256 = hashlib.sha256()
    # Update the hash object with the bytearray
    sha256.update(input_bytearray)
    # Return the hexadecimal representation of the hash
    return sha256.hexdigest()


def compute_md5_hash(byte_array):
    # Convert byte array to bytes
    byte_data = bytes(byte_array)
    # Calculate the MD5 hash
    return hashlib.md5(byte_data).hexdigest()


# Function to compute CRC32 from a bytearray
def crc32_hash_bytearray(input_bytearray):
    # Compute the CRC32 checksum
    input_bytearray = bytearray(input_bytearray)
    checksum = binascii.crc32(input_bytearray) & 0xFFFFFFFF  # Ensure it's unsigned
    return checksum


def solvemd5(equal):
    for x in range(256):
        for y in range(256):
            if compute_md5_hash([x, y]) == equal:
                print([x, y])


def solvesha(equal):
    for x in range(256):
        for y in range(256):
            if sha256_hash_bytearray([x, y]) == equal:
                print([x, y])


def solvesha(equal):
    for x in range(256):
        for y in range(256):
            if sha256_hash_bytearray([x, y]) == equal:
                print([x, y])


def solvecrc(equal):
    for x in range(256):
        for y in range(256):
            if crc32_hash_bytearray([x, y]) == equal:
                print([x, y])


# solvecrc(8, 2) == 0x61089C5C
# solvecrc(34, 2) == 0x5888FC1B
# solvecrc(63, 2) == 0x66715919
# solvecrc(78, 2) == 0x7CAB8D64

solvecrc(0x61089C5C)
solvecrc(0x5888FC1B)
solvecrc(0x66715919)
solvecrc(0x7CAB8D64)

# hash.sha256(14, 2) == "403d5f23d149670348b147a15eeb7010914701a7e99aad2e43f90cfa0325c76f"
# hash.sha256(56, 2) == "593f2d04aab251f60c9e4b8bbc1e05a34e920980ec08351a18459b2bc7dbf2f6"

solvesha("403d5f23d149670348b147a15eeb7010914701a7e99aad2e43f90cfa0325c76f")
solvesha("593f2d04aab251f60c9e4b8bbc1e05a34e920980ec08351a18459b2bc7dbf2f6")

# hash.md5(0, 2) == "89484b14b36a8d5329426a3d944d2983"
# hash.md5(76, 2) == "f98ed07a4d5f50f7de1410d905f1477f"
# hash.md5(50, 2) == "657dae0913ee12be6fb2a6f687aae1c7"
# hash.md5(32, 2) == "738a656e8e8ec272ca17cd51e12f558b"

solvemd5("89484b14b36a8d5329426a3d944d2983")
solvemd5("f98ed07a4d5f50f7de1410d905f1477f")
solvemd5("657dae0913ee12be6fb2a6f687aae1c7")
solvemd5("738a656e8e8ec272ca17cd51e12f558b")

# [114, 101]
# [101, 65]
# [110, 46]
# [110, 58]
# [32, 115]
# [102, 108]
# [114, 117]
# [105, 111]
# [51, 65]
# [117, 108]

uint8_8 == 114 
uint8_9 == 101
uint8_34 == 101 
uint8_35 == 65
uint8_63 == 110 
uint8_64 == 46
uint8_78 == 110 
uint8_79 == 58
uint8_14 == 32 
uint8_15 == 115
uint8_56 == 102 
uint8_57 == 108
uint8_0 == 114 
uint8_1 == 117
uint8_76 == 105 
uint8_77 == 111
uint8_50 == 51 
uint8_51 == 65
uint8_32 == 117 
uint8_33 == 108
