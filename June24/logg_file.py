import logging

def logg():
    logging.basicConfig(filename="log_.txt",
                        filemode='a',
                        format='%asctime)s - %(message)s',
                        level=logging.INFO)
    return logging