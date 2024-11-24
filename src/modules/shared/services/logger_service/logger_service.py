import logging
import colorlog

class LoggerService:
    FLASK_ID = "werkzeug"
    ROOT_ID = "root"
    GLOBAL_ID = "GLOBAL"

    @staticmethod
    def setup():
        handler = logging.StreamHandler()
        handler.setFormatter(colorlog.ColoredFormatter(
            '%(log_color)s[%(asctime)s]: %(reset)s%(message)s',
            datefmt=None,
            reset=True,
            log_colors={
                'DEBUG':    'cyan',
                'INFO':     'green',
                'WARNING':  'yellow',
                'ERROR':    'red',
                'CRITICAL': 'red,bg_white',
            },
            secondary_log_colors={},
            style='%'
        ))
        logging.getLogger(LoggerService.FLASK_ID).setLevel(logging.CRITICAL)
        logging.getLogger(LoggerService.ROOT_ID).setLevel(logging.FATAL)
        log = logging.getLogger(LoggerService.GLOBAL_ID)
        log.setLevel(logging.INFO)
        log.addHandler(handler)

    @staticmethod
    def info(msg: str):
        log = logging.getLogger(LoggerService.GLOBAL_ID)
        log.info(msg=msg)
        
    @staticmethod
    def warn(msg: str):
        log = logging.getLogger(LoggerService.GLOBAL_ID)
        log.warn(msg=msg)
    
    @staticmethod
    def error(msg: str):
        log = logging.getLogger(LoggerService.GLOBAL_ID)
        log.error(msg=msg)
    
    @staticmethod
    def title(msg: str):
        title = "=" * 12 + f" {msg} " + "=" * 12
        logging.getLogger(LoggerService.GLOBAL_ID).info(msg=f"\n\n{title}")