#!/usr/bin/python3
"""
Main file for testing
"""
def validUTF8(data):
    # Helper function to count the number of leading 1's in a byte
    def count_leading_ones(byte):
        count = 0
        for i in range(7, -1, -1):
            if byte & (1 << i):
                count += 1
            else:
                break
        return count

    # Number of bytes left to check for the current character
    bytes_to_process = 0

    for byte in data:
        # Mask to only get the 8 least significant bits of the byte
        byte = byte & 0xFF

        if bytes_to_process == 0:
            # Count leading ones to determine the byte length of the character
            leading_ones = count_leading_ones(byte)

            if leading_ones == 0:
                # Single byte character (ASCII)
                continue
            elif 2 <= leading_ones <= 4:
                # Multi-byte character
                bytes_to_process = leading_ones - 1
            else:
                # Invalid UTF-8 leading byte
                return False
        else:
            # Check if the current byte is a continuation byte (starts with 10)
            if byte >> 6 != 0b10:
                return False
            bytes_to_process -= 1

    # Ensure all bytes for the last character were processed
    return bytes_to_process == 0
