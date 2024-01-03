import logging

# Configure the logging system
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Example usage of logging
def divide(a, b):
    try:
        result = a / b
        logging.debug(f"Division result: {result}")
    except ZeroDivisionError:
        logging.error("Attempted to divide by zero.")
    except Exception as e:
        logging.exception(f"An error occurred: {e}")

# Call the function with some values
divide(10, 2)
divide(5, 0)
