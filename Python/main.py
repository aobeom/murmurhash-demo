import mmh3
import binascii


# Return 32 bit unsigned int (2911983372)
def calc32(key):
    h32 = mmh3.hash(key, signed=False)
    return h32


# Return 128 bit hex (09c01ad2296d65bdb32ceb54cdb5b54a)
def calc128(key):
    # 1. unsigned int to bytes
    # h128 = mmh3.hash128(key)
    # h128_int_len = h128.bit_length()
    # h128_byte_len, rem = divmod(h128_int_len, 8)
    # if rem:
    #     h128_byte_len += 1
    # h128_bytes = h128.to_bytes(h128_byte_len, 'little')

    # 2. get bytes
    h128_bytes = mmh3.hash_bytes(key)

    h128_hex = binascii.b2a_hex(h128_bytes).decode("utf-8")
    return h128_hex


def main():
    key = "Hello world"
    c32 = calc32(key)
    print(f"Python 32 Bit: {c32}")

    c128 = calc128(key)
    print(f"Python x64 128 Bit: {c128}")


if __name__ == "__main__":
    main()
