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
        best_length = 0
        best_offset = 0
        
        # Search back for the longest matching sequence
        for j in range(max(0, i - 65535), i):
            match_length = 0
            while (i + match_length < len(data) and 
                   data[j + match_length] == data[i + match_length] and 
                   match_length < 255):
                match_length += 1
            
            # Update best match if found
            if match_length > best_length:
                best_length = match_length
                best_offset = i - j
        
        # Encode the compressed data
        if best_length >= 4:
            # Encode a match
            compressed.append(best_length)
            compressed.append(best_offset & 0xFF)
            compressed.append((best_offset >> 8) & 0xFF)
            i += best_length
        else:
            # Encode a literal byte
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
        # Check if it's a literal or a match
        if compressed_data[i] < 15:
            # Literal byte
            decompressed.append(compressed_data[i])
            i += 1
        else:
            # Match sequence
            length = compressed_data[i]
            offset = (compressed_data[i+2] << 8) | compressed_data[i+1]
            
            # Validate offset and length
            if offset == 0 or length == 0:
                raise ValueError("Invalid compressed data")
            
            # Copy matched sequence
            start = len(decompressed) - offset
            for _ in range(length):
                decompressed.append(decompressed[start])
                start += 1
            
            i += 3
    
    return bytes(decompressed)