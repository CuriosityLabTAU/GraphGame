#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging


class GLogger ():
    logger = None
    log_output_type = ""
    log_level = logging.INFO
    #log levels chart
    # 0 = ERROR
    # 1 = WARNING
    # 2 = INFO
    # 3 = DEBUG

    def __init__(self,output_type, writing_location,level="INFO", *args):
        GLogger.log_level =logging.getLevelName(level)
        self.set_logger(output_type,writing_location,*args)


    def set_logger(self, output_type, writing_location,*args):
        if output_type == "file" :
            GLogger.logger = file_logger(writing_location)

        elif output_type== "server":
             GLogger.logger = server_logger (writing_location, *args)

        # elif output_type == "console":
        #     self.logger =

        else:
            raise ValueError ("invalid output type")
    @staticmethod
    def format_log_msg(msg, **kwargs):
        new_message = msg
        for key, value in kwargs.iteritems():
            new_message = "{0}, {1}={2}".format(new_message, key, value)
        return new_message

    @staticmethod
    def log(log_level, msg , **kwargs):
        try:
            if log_level < log_level:
                return
            elif isinstance(GLogger.logger, server_logger):
                if not kwargs:
                    GLogger.logger.log_write(action=LogAction.none, obj='', comment=msg)
                else:
                    GLogger.logger.log_write(**kwargs)
            else:
                msg = GLogger.format_log_msg(msg, **kwargs)
                GLogger.logger.log_write(msg)
        except:
            pass #print('Error in GLogger.log!!!')


# Enum: LogAction: non, press, play, stop, move, down, up, text, spinner, data
class LogAction:
    none = 'none'
    press = 'press'
    move = 'move'
    down = 'down'
    up = 'up'
    text = 'text'
    data = 'data'

    def __init__(self):
        pass

class server_logger ():
    ip = ""

    def __init__(self, writing_location, user_data_dir):
        self.ip = writing_location
        self.init_communication(self.ip,user_data_dir)

    def log_write (self,**kwargs):
        from KivyCommunication import *
        KL.log.insert(**kwargs)


    def init_communication(self, server_ip, user_data_dir):
        from KivyCommunication import *
        """
        Initiolize the communication protocol to the server.
        """
        KC.start(the_ip=server_ip, the_parents=[self])
        KL.start(mode=[DataMode.file], pathname=user_data_dir)
        KL.restart()

    #
    # @staticmethod
    # def on_connection():
    #     pass



class file_logger ():
    path = ""

    def __init__(self, writing_location):
        self.path = writing_location
        open(self.path, 'w').close()

    def log_write (self,msg):
        log_file = open(self.path, 'a')
        log_file.write("{}\n".format(msg))
        log_file.close()