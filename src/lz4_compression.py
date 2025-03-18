"""
LZ4 Compression Algorithm Implementation

This module provides a basic implementation of the LZ4 compression algorithm.
LZ4 is a fast lossless compression algorithm that provides a good balance 
between compression speed and compression ratio.

Note: This is a simplified implementation and may not be fully compliant 
with the official LZ4 specification.
"""

def lz4_compress(data):
    """
    Compress input data using a simplified LZ4 compression algorithm.
    
    Args:
        data (bytes or str): The input data to compress
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes or str
        ValueError: If input is empty
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Convert to bytes if input is a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Ensure input is bytes
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Compression implementation
    compressed = bytearray()
    i = 0
    while i < len(data):
        # Look for repeated sequences
        match_found = False
        
        # Check back up to 65535 bytes (maximum offset)
        for j in range(max(0, i - 65535), i):
            # Find longest matching sequence
            match_length = 0
            while (i + match_length < len(data) and 
                   data[j + match_length] == data[i + match_length] and 
                   match_length < 255):
                match_length += 1
            
            # If match is long enough (4 or more bytes)
            if match_length >= 4:
                # Encode match
                compressed.append(match_length)
                offset = i - j
                compressed.append(offset & 0xFF)  # Low byte
                compressed.append((offset >> 8) & 0xFF)  # High byte
                i += match_length
                match_found = True
                break
        
        # If no match found, encode literal byte
        if not match_found:
            compressed.append(data[i])
            i += 1
    
    return bytes(compressed)

def lz4_decompress(compressed_data):
    """
    Decompress data compressed with the LZ4 compression algorithm.
    
    Args:
        compressed_data (bytes): The compressed input data
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty or compressed data is invalid
    """
    # Validate input
    if not compressed_data:
        raise ValueError("Input compressed data cannot be empty")
    
    if not isinstance(compressed_data, bytes):
        raise TypeError("Compressed data must be bytes")
    
    # Decompression implementation
    decompressed = bytearray()
    i = 0
    
    while i < len(compressed_data):
        # Check current byte
        current_byte = compressed_data[i]
        
        # If less than 15, it's a literal byte
        if current_byte < 15:
            decompressed.append(current_byte)
            i += 1
        else:
            # It's a match sequence
            # First byte indicates length
            length = current_byte
            
            # Next two bytes indicate offset
            if i + 2 >= len(compressed_data):
                raise ValueError("Invalid compressed data")
            
            offset = (compressed_data[i+2] << 8) | compressed_data[i+1]
            
            # Validate offset
            if offset == 0:
                raise ValueError("Invalid offset in compressed data")
            
            # Copy matched sequence
            start = len(decompressed) - offset
            for _ in range(length):
                # Safely copy bytes from previous part of decompressed data
                if start < 0:
                    raise ValueError("Invalid match sequence")
                decompressed.append(decompressed[start])
                start += 1
            
            # Move index past the match encoding
            i += 3
    
    return bytes(decompressed)