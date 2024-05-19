#!/usr/bin/python3
"""UTF-8 validation module."""


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints.
    """
    def is_valid_byte(byte):
        """Checks if the given byte is a valid continuation byte (10xxxxxx)."""
        return (byte & 0b11000000) == 0b10000000

    i = 0
    n = len(data)

    while i < n:
        byte = data[i]
        if byte < 0 or byte > 0x10FFFF:
            return False

        if (byte & 0b10000000) == 0:
            # 1-byte character (0xxxxxxx)
            i += 1
        elif (byte & 0b11100000) == 0b11000000:
            # 2-byte character (110xxxxx 10xxxxxx)
            if i + 1 >= n or not is_valid_byte(data[i + 1]):
                return False
            i += 2
        elif (byte & 0b11110000) == 0b11100000:
            # 3-byte character (1110xxxx 10xxxxxx 10xxxxxx)
            if (i + 2 >= n or
                    not is_valid_byte(data[i + 1]) or
                    not is_valid_byte(data[i + 2])):
                return False
            i += 3
        elif (byte & 0b11111000) == 0b11110000:
            # 4-byte character (11110xxx 10xxxxxx 10xxxxxx 10xxxxxx)
            if (i + 3 >= n or
                    not is_valid_byte(data[i + 1]) or
                    not is_valid_byte(data[i + 2]) or
                    not is_valid_byte(data[i + 3])):
                return False
            i += 4
        else:
            return False

    return True
