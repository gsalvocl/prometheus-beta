import functools
import time
import logging

def log_execution_time(logger=None):
    """
    A decorator to log the execution time of a function.
    
    Args:
        logger (logging.Logger, optional): Logger to use for recording execution time. 
                                           If None, uses basic print logging.
    
    Returns:
        callable: Decorated function that logs its execution time
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Start timing
            start_time = time.time()
            
            # Execute the function
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                # Log any exceptions that occur
                if logger:
                    logger.error(f"Error in {func.__name__}: {str(e)}")
                else:
                    print(f"Error in {func.__name__}: {str(e)}")
                raise
            
            # Calculate execution time
            end_time = time.time()
            execution_time = end_time - start_time
            
            # Log the execution time
            log_message = f"Function '{func.__name__}' executed in {execution_time:.4f} seconds"
            if logger:
                logger.info(log_message)
            else:
                print(log_message)
            
            return result
        return wrapper
    return decorator