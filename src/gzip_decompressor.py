import gzip
import os

def decompress_gzip_file(input_path, output_path=None):
    """
    Decompress a gzip file to a specified output path.

    Args:
        input_path (str): Path to the input gzip file.
        output_path (str, optional): Path to save the decompressed file. 
                                     If not provided, uses input path without .gz extension.

    Returns:
        str: Path to the decompressed file.

    Raises:
        FileNotFoundError: If the input file does not exist.
        PermissionError: If there are permission issues reading/writing files.
        ValueError: If input file is not a gzip file.
    """
    # Validate input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    # Validate input file is a gzip file
    if not input_path.endswith('.gz'):
        raise ValueError(f"Input file must have .gz extension: {input_path}")

    # Determine output path if not provided
    if output_path is None:
        output_path = input_path.rstrip('.gz')

    try:
        # Open and read the gzip file
        with gzip.open(input_path, 'rb') as f_in:
            # Write the decompressed content to output file
            with open(output_path, 'wb') as f_out:
                f_out.write(f_in.read())

        return output_path

    except PermissionError:
        raise PermissionError(f"Permission denied when accessing files: {input_path} or {output_path}")
    except gzip.BadGzipFile:
        raise ValueError(f"Invalid gzip file: {input_path}")