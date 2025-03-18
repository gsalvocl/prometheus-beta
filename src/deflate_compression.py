import zlib

def deflate_compress(data):
    """
    Compress data using the Deflate compression algorithm.

    Args:
        data (bytes or str): The input data to compress. 
                              If str, it will be encoded to bytes.

    Returns:
        bytes: Compressed data using Deflate algorithm.

    Raises:
        TypeError: If input is not bytes or str.
        ValueError: If input is empty.
    """
    # Validate input
    if data is None:
        raise ValueError("Input data cannot be None")
    
    # Convert str to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate input type
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Check for empty input
    if len(data) == 0:
        raise ValueError("Input data cannot be empty")
    
    # Compress using zlib's Deflate implementation
    try:
        compressed_data = zlib.compress(data)
        return compressed_data
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")

def deflate_decompress(compressed_data):
    """
    Decompress data that was compressed using the Deflate algorithm.

    Args:
        compressed_data (bytes): The compressed data to decompress.

    Returns:
        bytes: Decompressed data.

    Raises:
        TypeError: If input is not bytes.
        ValueError: If input is empty.
        RuntimeError: If decompression fails.
    """
    # Validate input
    if compressed_data is None:
        raise ValueError("Compressed data cannot be None")
    
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Compressed data must be bytes")
    
    # Check for empty input
    if len(compressed_data) == 0:
        raise ValueError("Compressed data cannot be empty")
    
    # Decompress using zlib's Deflate implementation
    try:
        decompressed_data = zlib.decompress(compressed_data)
        return decompressed_data
    except Exception as e:
        raise RuntimeError(f"Decompression failed: {str(e)}")