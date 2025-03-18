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
        # Look for the best match
        best_length = 0
        best_offset = 0
        
        # Search back up to 65535 bytes (max window size)
        for j in range(max(0, i - 65535), i):
            # Find longest matching sequence
            match_length = 0
            while (i + match_length < len(data) and 
                   j + match_length < i and 
                   data[j + match_length] == data[i + match_length] and 
                   match_length < 255 + 15):  # Adjust max match length
                match_length += 1
            
            # Update best match if found
            if match_length > best_length:
                best_length = match_length
                best_offset = i - j
        
        # Encode based on the match
        if best_length >= 4:
            # Encode a match
            # First byte encodes match length and initial literal
            if best_length > 15:
                # Handle long match lengths
                compressed.append(15 + (best_length - 15))
            else:
                compressed.append(best_length)
            
            # Next two bytes encode offset
            compressed.append(best_offset & 0xFF)  # Low byte
            compressed.append((best_offset >> 8) & 0xFF)  # High byte
            
            i += best_length
        else:
            # Encode literal byte
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
        # Current processing byte
        current_byte = compressed_data[i]
        
        # Check if it's a literal or a match
        if current_byte < 15:
            # Literal byte or short match
            length = current_byte
            
            # Process literal bytes
            for j in range(length):
                if i + 1 + j >= len(compressed_data):
                    raise ValueError("Incomplete compressed data")
                decompressed.append(compressed_data[i + 1 + j])
            
            # If this was a match
            if length == 15 and i + 1 < len(compressed_data):
                # Add extra length bytes for matches > 15
                while compressed_data[i + 1] == 255:
                    length += 255
                    i += 1
                    if i + 1 >= len(compressed_data):
                        break
                
                # Add final extra length byte
                if i + 1 < len(compressed_data):
                    length += compressed_data[i + 1]
            
            # Advance index
            i += length + 1
        else:
            # It's a match sequence
            # Ensure we have enough bytes to process the match
            if i + 2 >= len(compressed_data):
                raise ValueError("Invalid compressed data")
            
            # Match length is in the high 4 bits
            match_length = current_byte - 15
            
            # Offset is in the next two bytes (little-endian)
            offset = (compressed_data[i+2] << 8) | compressed_data[i+1]
            
            # Validate offset
            if offset == 0:
                raise ValueError("Invalid offset in compressed data")
            
            # Compute copy starting location
            start = len(decompressed) - offset
            
            # Safely copy matched sequence
            for _ in range(match_length):
                if start < 0:
                    raise ValueError("Invalid match sequence")
                decompressed.append(decompressed[start])
                start += 1
            
            # Move index past the match encoding
            i += 3
    
    return bytes(decompressed)