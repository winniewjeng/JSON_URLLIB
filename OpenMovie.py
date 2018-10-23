import json, logging, os, re, sys, traceback, urllib.request


class OpenMovie:

    # constructor:
    def __init__(self, title=None, posterURL=None):
        # instance variables - accessed by self.element
        self.title = title
        self.posterURL = posterURL

        # define the name of the directory to be created
        path = "Posters"

        # safely create the poster directory using os.mkdir()
        try:
            os.mkdir(path)
            print(" Successfully created the directory %s " % path)
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
        self.title = re.sub(r"[^a-zA-Z0-9]", "_", self.title)  # is it self.title = re.sub or just call re.sub?
        self.title = "Posters/%s" % self.title
        # use urlretrieve to download the file from posterURL, store it in posterFileName, return True
        try:
            self.posterFileName = urllib.request.urlretrieve(self.posterURL, self.title)
            return True
        # not sure if my traceback and error handling / logging is done correctly
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stdout)
            print("*** tb_lineno:", exc_traceback.tb_lineno)
            logging.error("*** tb_lineno:", exc_traceback.tb_lineno)
            return False


title = None
posterURL = None
posterFileName = None
