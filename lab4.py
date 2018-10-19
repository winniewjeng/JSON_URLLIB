# I don't know why if I simply write "import OpenMovie" my program won't import it...
from OpenMovie import *
import configparser, json, logging, sys

if __name__ == "__main__":

    try:
        config = configparser.RawConfigParser()
        # read in the "movie.cfg" file
        config.read("movies.cfg")
    except:
        print("Config fail")
        logging.error("Config fail")
        sys.exit()

    # if the configuration has a section named ”LOGGING”,
    # read the LOG_FILE field of it and store the name in log_file_name
    # else set log file name to ”default.log”
    if config.has_section('LOGGING'):
        log_file_name = config.get('LOGGING', 'log_file')

    else:
        log_file_name = "default.log"

    # create a logging basiConfig
    logging.basicConfig(filename=log_file_name, level=logging.DEBUG,
                        format='%(asctime)s,%(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    # create a logging instance using log_file_name
    logging.info(" %s opens. Program starts." % log_file_name)

    # read the ”movies.json” file and load its data
    try:
        contents = open('movies.json', 'r')
    except:
        print("Failed to open JSON file")
        logging.error("Failed to open JSON file")
        sys.exit()

    # get a dictionary from the ”movie posters” field of the json data named data
    data = json.load(contents)

    # test code to print out the data dictionary of json objects
    # print(data['movie_posters'])
    # for i in data['movie_posters']:
    #     print(i, data['movie_posters'][i])

    # for each item in this dictionary,
    # a. create an instance of OpenMovie using the key for the title and the value for the posterURL
    # b. call the getPoster method of this instance of OpenMovie
    # c. delete this instance of OpenMovie
    for i in data['movie_posters']:
        # instance = OpenMovie.OpenMovie.__init__(i, data['movie_posters'][i])
        instance = OpenMovie(i, data['movie_posters'][i])
        instance.getPoster()
        del instance

    contents.close()