from __future__ import print_function
from builtins import str
from builtins import input
from builtins import object
import configparser
import argparse
import glob
from sys import exit
from subprocess import call


class wwt_Uploader(object):
    def __init__(self):
        print('\n{:^80}'.format("###########################################"))
        print('\n{:^80}'.format("Author : Xonshiz"))
        print('\n{:^80}'.format("###########################################\n"))
        self.main()

    def version(self):
        print("2017.01.12")

    def main(self):

        parser = argparse.ArgumentParser(
            description='WWT Uploader can upload all your torrents to WWT via API. You can automate this script easily.')
        parser.add_argument('--version', action='store_true', help='Shows current version and exits.')
        parser.add_argument('--id', action='store_true', help='Lists the categories and their IDs.')
        parser.add_argument('--setup', action='store_true', help='Starts a setup for making an INI file.')

        args = parser.parse_args()

        if args.version:
            self.version()
            exit()
        if args.id:
            self.idList()
            exit()

        if args.setup:
            config = configparser.ConfigParser()
            config['MainSettings'] = {}

            hKey = str(input("Enter your API Key : ")).strip()

            config['MainSettings']['hKey'] = '%s' % hKey

            try:
                with open("Description.txt", "r") as desc:
                    description = desc.read()
            except:
                exit(
                    "Unable to find 'Description.txt' file. If it's not there, please make it and paste your desired description in it.")

            category = str(eval(input("Enter the torrent Category (run with --id to see id list) : "))).strip()

            config['MainSettings']['description'] = '%s' % description

            config['MainSettings']['category'] = '%s' % category

            with open('Settings.ini', 'w') as configfile:
                config.write(configfile)

            print("There should be a Settings.ini file in the folder now. Please don't delete it.")
            exit()

        config = configparser.ConfigParser(allow_no_value=True)
        config.read('Settings.ini')
        hKey = config.get('MainSettings', 'hkey')
        description = config.get('MainSettings', 'description')
        category_id = config.get('MainSettings', 'category')
        self.mainUploader(api_key=hKey, description=description, category=category_id)

    def mainUploader(self, api_key, description, category):

        for filename in glob.glob('*.torrent'):
            torrentName = str(filename).replace(".torrent", "")
            uploadCommand = 'curl -i -X POST -H "X-Authorization: %s" -H "Content-Type: multipart/form-data" -F "torrent_file=@%s" -F "name=%s" -F "category_id=%s" -F "description=%s" https://worldwidetorrents.eu/api/account/upload/' % (
                api_key, filename, torrentName, category, description)
            # print(uploadCommand)
            call(uploadCommand)
            print("\n############\n")

    def idList(self):
        idList = {'81': 'Anime', '1': 'Movies-->3D Movies', '2': 'Movies-->Music Videos', '3': 'Movies-->Dubbed Movies',
                  '4': 'Movies-->Handheld', '5': 'TV-->DVD', '6': 'TV-->Divx/Xvid', '7': 'TV-->SVCD/VCD',
                  '9': 'Documentaries-->All', '10': 'Games-->Windows', '12': 'Games-->Xbox ONE', '13': 'Games-->Xbox',
                  '14': 'Games-->Xbox360', '15': 'Games-->PS1', '16': 'Games-->PS2', '17': 'Games-->Wii',
                  '18': 'Apps-->Windows', '19': 'Apps-->Mac', '20': 'Apps-->Linux', '21': 'Apps-->Unix',
                  '22': 'Music-->MP3', '23': 'Music-->AAC', '24': 'Music-->Lossless', '25': 'Music-->Transcode',
                  '26': 'Music-->Soundtrack', '27': 'Music-->Radio Shows', '28': 'Anime-->Movie',
                  '33': 'Other-->Pictures', '34': 'Other-->Sound Clips', '35': 'Other-->Covers',
                  '36': 'Books-->E-Books', '37': 'Other-->Wallpapers/Screensavers', '38': 'Other-->Fonts',
                  '39': 'Other-->Unsorted', '40': 'Other-->Tutorials', '41': 'TV-->HD', '42': 'Movies-->Movie clips',
                  '43': 'Games-->PSP', '44': 'Games-->PS3', '45': 'Games-->PS4', '46': 'Games-->NDS',
                  '48': 'Games-->Handheld', '59': 'Unity Asset-->All', '50': 'Books-->Comics', '51': 'Books-->Manga',
                  '52': 'Books-->Magazines', '53': 'Books-->Textbooks', '54': 'Books-->Fiction',
                  '55': 'Books-->Non-fiction', '56': 'Books-->Audio books', '57': 'Books-->Academic',
                  '58': 'Games-->Android', '60': 'Books-->Poetry', '62': 'Books-->Newspapers', '65': 'XXX-->Video',
                  '66': 'XXX-->HD Video', '75': 'XXX-->Books', '71': 'XXX-->Pictures', '72': 'XXX-->Magazines',
                  '73': 'XXX-->UltraHD', '76': 'XXX-->Hentai', '77': 'XXX-->XXX Games', '78': 'XXX-->Other XXX',
                  '79': 'Other-->Subtitles', '80': 'Anime-->Anime Music Video', '81': 'Anime-->English-translated',
                  '82': 'Anime-->Other Anime', '83': 'Apps-->iOS', '84': 'Apps-->Android', '85': 'Apps-->Handheld',
                  '86': 'Apps-->Other Applications', '87': 'Books-->Programming', '88': 'Books-->Medical',
                  '89': 'Books-->Cooking', '90': 'Books-->Sport', '91': 'Books-->Other Books', '92': 'Games-->Mac',
                  '93': 'Games-->Linux', '94': 'Games-->Cheats', '95': 'Games-->Other Games', '96': 'Movies-->iPad',
                  '97': 'Movies-->Highres Movies', '98': 'Movies-->UltraHD', '99': 'Movies-->Bollywood',
                  '100': 'Movies-->Concerts', '101': 'Movies-->Asian', '102': 'Movies-->Animation',
                  '103': 'Movies-->Documentary', '104': 'Movies-->Academic Movies', '105': 'Movies-->Sport',
                  '106': 'Movies-->Trailer', '107': 'Movies-->Other Movies', '108': 'Music-->Karaoke',
                  '109': 'Music-->Classic', '110': 'Music-->Other Music', '111': 'Movies-->DVD, DVDRip, PDVD',
                  '112': 'Movies-->Web rip, x264, x265', '113': 'TV/HD-->Sports', '114': 'Movies-->Action',
                  '115': 'Movies-->Drama', '116': 'Movies-->Western', '117': 'Movies-->Family',
                  '118': 'TV-->SD x264 x265', '119': 'Movies-->Animated Short', '120': 'Movies-->TS/Cam Rip',
                  '121': 'Movies-->Horror', '122': 'Movies-->Comedy', '123': 'Movies-->Sci-Fi',
                  '124': 'Movies-->Biography', '125': 'Movies-->Mystery/Thriller', '126': 'Movies-->War',
                  '127': 'Games-->Table Top', '128': 'Movies-->Dual Audio', '129': 'Movies-->Adventure',
                  '130': 'Movies-->DVD Screener', '132': 'Comics-->Nem43 Comics', }
        for x in list(idList.keys()):
            print('{:^80}'.format("%s ==> %s") % (x, idList[x]))
