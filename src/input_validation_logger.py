import logging
import functools

def validate_input(log_level=logging.WARNING):
    """
    A decorator for logging input validation messages.
    
    Args:
        log_level (int, optional): Logging level to use. Defaults to logging.WARNING.
    
    Returns:
        callable: Decorated function that logs input validation messages.
    
    Example:
        @validate_input()
        def process_data(data):
            if not isinstance(data, str):
                raise ValueError("Data must be a string")
            return data.upper()
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Configure logging if not already configured
            logging.basicConfig(
                level=logging.DEBUG, 
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            logger = logging.getLogger(func.__name__)
            
            # Validate arguments
            try:
                # Log input arguments
                logger.log(log_level, f"Input arguments: args={args}, kwargs={kwargs}")
                
                # Validate number of arguments
                if not args and not kwargs:
                    logger.warning("No arguments provided")
                
                # Perform function call
                result = func(*args, **kwargs)
                
                # Log successful validation
                logger.info("Input validation successful")
                
                return result
            
            except TypeError as e:
                logger.error(f"Type error in input validation: {e}")
                raise
            except ValueError as e:
                logger.error(f"Value error in input validation: {e}")
                raise
            except Exception as e:
                logger.critical(f"Unexpected error during input validation: {e}")
                raise
        
        return wrapper
    
    return decorator