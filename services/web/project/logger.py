import os
import functools
import logging
from pathlib import Path

def log_function_call(logger):
    """
    A decorator that wraps the passed in function and logs 
    exceptions should one occur
    
    @param logger: The logging object
    """
    
    def decorator(func):
    
        def wrapper(*args, **kwargs):
            try:
                func_ret = func(*args, **kwargs)
                logging.info(f'Function "{func.__name__}" called successfully ' \
                             f'with compound {args[0]}\n')
                return func_ret
            except:
                err = "There was an exception in  "
                err += func.__name__
                logger.exception(err)

                # Raise the error to stop the programm, else it'll continue
                raise
            
        return wrapper
    return decorator

def create_logger():

    # Creating pyforge-proj/services/web/logs directory
    logs_dir_path = Path(__file__).parent / "../logs/"
    if not os.path.exists(logs_dir_path):
        os.mkdir(logs_dir_path)

    # Setting up the logger configurations
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter=logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", '%m-%d-%Y %H:%M:%S')

    # Creating a file handler, so that INFO level messages
    # only get to the log.txt
    file_handler = logging.FileHandler(logs_dir_path / "log.txt")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
