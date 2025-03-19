def find_palindrome_pair_indices(words):
    """
    Find pairs of indices where the corresponding words are palindromes when reversed.
    
    Args:
        words (list): A list of words to check for palindrome pairs.
    
    Returns:
        list: A list of tuples containing indices of palindrome pairs.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If list contains non-string elements.
    """
    # Input validation
    if not isinstance(words, list):
        raise TypeError("Input must be a list of words")
    
    if any(not isinstance(word, str) for word in words):
        raise ValueError("All elements must be strings")
    
    # Store palindrome pair indices
    palindrome_pairs = []
    
    # Check all pairs of indices
    for i in range(len(words)):
        for j in range(len(words)):
            # Skip comparing a word with itself
            if i == j:
                continue
            
            # Reverse the current word
            reversed_word = words[j][::-1]
            
            # Check if the reversed word matches the original
            if words[i] == reversed_word:
                palindrome_pairs.append((i, j))
    
    return palindrome_pairs