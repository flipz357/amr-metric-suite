import logging


def get_logger(i):
    ch = logging.StreamHandler()
    logger = logging.getLogger("app")
    if i == 1:
        logger.setLevel(logging.DEBUG)
        ch.setLevel(logging.DEBUG)
    if i == 2:
        logger.setLevel(logging.INFO)
        ch.setLevel(logging.INFO)
    if i == 3:
        logger.setLevel(logging.WARNING)
        ch.setLevel(logging.WARNING)
    if i == 4:
        logger.setLevel(logging.ERROR)
        ch.setLevel(logging.ERROR)
    if i == 5:
        logger.setLevel(logging.CRITICAL)
        ch.setLevel(logging.CRITICAL)
    logger.addHandler(ch)
    return logger

class LogHelper:

    def __init__(self, loglevel=5):
        self.logger = get_logger(loglevel)
        self.ll = loglevel
        return None

    def debug(self,*args):
        if self.ll != 1:
            return None
        #first is the msg second are potentially non-string args
        msg = str(args[0])
        print(args,",")
        if len(args) == 1:
            self.logger.debug(msg)
        else:
            string = ""
            for arg in args[1:]:
                string+=str(arg)+" "
            string=string.strip()
            self.logger.debug(msg+": {}".format(string))
        return None
    
    def info(self,*args):
        if self.ll != 2:
            return None
        #first is the msg second are potentially non-string args
        msg = str(args[0])
        if len(args) == 1:
            self.logger.info(msg)
        else:
            string = ""
            for arg in args[1:]:
                string+=str(arg)+" "
            string=string.strip()
            self.logger.info(msg+": {}".format(string))
        return None
    
    def warning(self,*args):
        if self.ll != 3:
            return None
        #first is the msg second are potentially non-string args
        msg = str(args[0])
        if len(args) == 1:
            self.logger.warning(msg)
        else:
            string = ""
            for arg in args[1:]:
                string+=str(arg)+" "
            string=string.strip()
            self.logger.warning(msg+": {}".format(string))
        return None
    
    def error(self,*args):
        #first is the msg second are potentially non-string args
        if self.ll != 4:
            return None
        msg = str(args[0])
        if len(args) == 1:
            self.logger.error(msg)
        else:
            string = ""
            for arg in args[1:]:
                string+=str(arg)+" "
            string=string.strip()
            self.logger.error(msg+": {}".format(string))
        return None
    
    def critical(self,*args):
        if self.ll !=5:
            return None
        #first is the msg second are potentially non-string args
        msg = str(args[0])
        if len(args) == 1:
            self.logger.critical(msg)
        else:
            string = ""
            for arg in args[1:]:
                string+=str(arg)+" "
            string=string.strip()
            self.logger.critical(msg+": {}".format(string))
        return None
