import logging
import functools
import inspect

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
            # Ensure logging is configured
            logging.basicConfig(
                level=logging.DEBUG, 
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            
            # Create a logger for this function
            logger = logging.getLogger(func.__name__)
            logger.setLevel(log_level)
            
            # Validate arguments
            try:
                # Log input arguments
                log_message = f"Input arguments: args={args}, kwargs={kwargs}"
                if log_level == logging.WARNING:
                    logger.warning(log_message)
                elif log_level <= logging.INFO:
                    logger.info(log_message)
                
                # Validate number of arguments
                if not args and not kwargs:
                    logger.warning("No arguments provided")
                
                # Validate argument types
                signature = inspect.signature(func)
                bound_arguments = signature.bind(*args, **kwargs)
                bound_arguments.apply_defaults()
                
                for param_name, param_value in bound_arguments.arguments.items():
                    param = signature.parameters[param_name]
                    if param.annotation != inspect.Parameter.empty:
                        # Check type annotation
                        if not isinstance(param_value, param.annotation):
                            raise TypeError(f"Argument {param_name} must be of type {param.annotation.__name__}")
                
                # Perform function call
                result = func(*args, **kwargs)
                
                # Log successful validation
                success_message = "Input validation successful"
                if log_level <= logging.INFO:
                    logger.info(success_message)
                
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