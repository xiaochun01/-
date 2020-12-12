from nb_log import LogManager


logger = LogManager('lla').get_logger_and_add_handlers(is_add_stream_handler=True,log_filename='log.log')

logger.info('蓝色')