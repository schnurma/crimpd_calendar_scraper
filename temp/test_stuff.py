import getpass
import logging

# Global Constants for Libraries:
# Set Value to True to show debugging messages
DEBUG_MODE = True

def set_up_logging() -> None:
    """ Function for setting up the logging """
    # https://docs.python.org/3/library/logging.html
    # set up logging: set level to DEBUG to see all messages
    # set up logging: set level to WARNING to only see warnings and errors
    if DEBUG_MODE:
        logging.basicConfig(level=logging.DEBUG)
        logging.debug("Logging is set to DEBUG")
    logging.basicConfig(level=logging.WARNING)


def get_credentials() -> str:
    """ Function for getting the credentials """
    # Get the credentials from the user
    # https://martinheinz.dev/blog/59
    try:
        #username = getpass.getpass(prompt="Enter your username: ")
        username = input("Enter your username or email: ")
    except Exception as err:
        logging.debug("Error: %s" ,err)
    try :
        password = getpass.getpass(prompt="Enter your password: ")
    except Exception as err:
        logging.debug("Error: %s" ,err)
    
    #print(username, password)
    return username, password
        
def main() -> None:
    set_up_logging()
    logging.warning("Starting Initial Setup...")
    logging.debug("Locale is set to:")
    
    #print(get_credentials())
    
if __name__ == "__main__":
    main()
