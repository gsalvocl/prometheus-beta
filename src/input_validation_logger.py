import logging
import functools
import inspect

class InputValidationLogger:
    """
    A utility class for logging input validation messages.
    """
    
    @classmethod
    def validate_input(cls, log_level=logging.WARNING):
        """
        A decorator for logging input validation messages.
        
        Args:
            log_level (int, optional): Logging level to use. Defaults to logging.WARNING.
        
        Returns:
            callable: Decorated function that logs input validation messages.
        
        Example:
            @InputValidationLogger.validate_input()
            def process_data(data):
                if not isinstance(data, str):
                    raise ValueError("Data must be a string")
                return data.upper()
        """
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # Create a logger for this function
                logger = logging.getLogger(func.__name__)
                logger.setLevel(log_level)
                
                # Validate arguments
                try:
                    # Log input arguments
                    log_message = f"Input arguments: args={args}, kwargs={kwargs}"
                    logger.log(log_level, log_message)
                    
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
                    logger.log(logging.INFO, success_message)
                    
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
    
    @staticmethod
    def get_log_messages(logger_name):
        """
        Retrieve log messages for a specific logger.
        
        Args:
            logger_name (str): Name of the logger.
        
        Returns:
            list: List of log records for the given logger.
        """
        # Configure logging to capture log records
        logger = logging.getLogger(logger_name)
        
        # Create a memory handler to capture log records
        log_records = []
        handler = logging.handlers.MemoryHandler(capacity=1000, flushLevel=logging.DEBUG)
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        
        # Temporarily attach the handler
        logger.addHandler(handler)
        
        # Return the captured log records
        return log_records

validate_input = InputValidationLogger.validate_input