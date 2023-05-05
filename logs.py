import logging

class Logger():

    # loginimo sukurimas

    def logger_creation(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter=logging.Formatter('%(asctime)s, %(name)s, %(levelname)s, %(message)s')
        file_handler = logging.FileHandler('istorija.log')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter('%(asctime)s, %(name)s, %(levelname)s, %(message)s'))
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        self.logger.info('prisijungimas')

    def gamescore(self, game_score):
        self.logger.info(f"Gamescore: {game_score}")