from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import mutagen.id3
from mutagen.id3 import ID3, TIT2, TIT3, TALB, TPE1, TRCK, TYER
import os
import sys
import glob
import numpy as np
import re
import logging
from utils import setup_logger
import eyed3

# https://methodmatters.github.io/editing-id3-tags-mp3-meta-data-in-python/

def get_mp3_tag_data(path):
    try:
        trackInfo = eyed3.load(path)
        artist, title, album = trackInfo.tag.artist, trackInfo.tag.title, trackInfo.tag.album,
    except:
        logging.exception('error reading eyed3 {path)')
    return (artist, title, album)
    # set the album name
    #mp3_metadata['album'] = ['Punk-O-Rama Vol. 1 (1994)']
    # set the albumartist name
    #mp3_metadata['albumartist'] = ['Punk-O-Rama Vol. 1']
    # set the track number with the proper format
    #mp3_metadata['tracknumber'] = str(tracknum) + '/' + str(len(filez))

def read_tags(dir_path, file_extention):
    # extract the file names (with file paths)
    file_path_dict = {}
    for dirname, subdirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            absolute_filename = os.path.join(dirname, filename)

            match = re.search(file_extention, absolute_filename)
            if match:
                # we make the call to get the file name -> MP3 tags
                file_path_dict[absolute_filename] = get_mp3_tag_data(absolute_filename)
            else:
                logging.debug(f"ignore {absolute_filename}...")
    return(file_path_dict)

    # filez = glob.glob("{dir_name}/{file_extention}")
    # # loop through the mp3 files, extracting the track number,
    # # then setting the album, albumartist and track number
    # # to the appropriate values
    # for i in np.arange(0, len(filez)):
    #     # extract the length of the directory
    #     length_directory = len(filez[i].split("/"))
    #     # extract the track number from the last element of the file path
    #     tracknum = filez[i].split("/")[length_directory - 1][0:2]
    #     # mp3 name (with directory) from filez
    #     song = filez[i]
    #     # turn it into an mp3 object using the mutagen library
    #     mp3file = MP3(song, ID3=EasyID3)
    #     # set the album name
    #     mp3file['album'] = ['Punk-O-Rama Vol. 1 (1994)']
    #     # set the albumartist name
    #     mp3file['albumartist'] = ['Punk-O-Rama Vol. 1']
    #     # set the track number with the proper format
    #     mp3file['tracknumber'] = str(tracknum) + '/' + str(len(filez))
    #     # save the changes that we've made
    #     mp3file.save()

def get_mp3_metadata(metadata):
    Artist = metadata['artist'][0]
    Album = metadata['album'][0]
    Title = metadata['title'][0]
    s = 'foo bar' # f“Artist: {Artist}, Album: {Album} Title: {Title}")
    return(s)


if __name__ == '__main__':
    exe_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
    setup_logger(exe_name, '/tmp', logging.INFO)
    logging.debug("starting %s", exe_name)
    dir_name = '/Volumes/music/'
    file_extention_re = ".mp3$"    # have to use RE to identify file extention
    fn_dict = read_tags(dir_name, file_extention_re)

    for path_name, metadata in fn_dict.items():
        print (key, metadata)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
