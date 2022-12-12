import logging

class LogGen:
    @staticmethod
    def loggen():
        #logPath=r'C:\Users\Tanmay.Gupta\PycharmProjects\nopcommerce\Logs'
        logging.basicConfig(filename="C:\\Users\\Tanmay.Gupta\\PycharmProjects\\nopcommerce\\Logs\\automation.log",
                        format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', force=True)
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger