import logging
import os
import re
import sys
import traceback
import urllib.request


class OpenMovie:

    # constructor:
    def __init__(self, title=None, posterURL=None):
        self.title = title
        self.posterURL = posterURL
        self.posterFileName = None
        path = "Posters"

        try:
            os.mkdir(path)
            logging.info(" Successfully created the directory %s " % path)
        except OSError:
            if os.path.isdir(path) is True:
                logging.warning(" the directory %s already exists" % path)
            else:
                print(" Creation of the directory %s failed" % path)
                logging.error(" Creation of the directory %s failed" % path)

    def getPoster(self):
        # log the event of calling getPoster() method
        logging.info(" getPoster() method is called")
        logging.info(" Poster's name: %s" % self.title)
        logging.info(" Poster's URL %s" % self.posterURL)

        # substitute every symbol and spaces in title with underline
        re.sub(r"[^a-zA-Z0-9]", "_", self.title)  # is it self.title = re.sub or just call re.sub?
        self.posterFileName = "Posters/%s" % self.title
        # use urlretrieve to download the file from posterURL, store it in posterFileName, return True
        try:
            urllib.request.urlretrieve(self.posterURL, self.posterFileName)
            return True
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stdout)
            # print("*** tb_lineno:", exc_traceback.tb_lineno)
            logging.error("*** tb_lineno:", exc_traceback.tb_lineno)
            return False

