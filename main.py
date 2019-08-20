'''
Objetivs:
Take two folders, and check the content of each one.
In the files of each folder, check file size and created date.
If the name, file size and created date is the same. delete one of the files.
'''


import easygui as eg
import os, stat
from datetime import datetime

class Folder():

    def __init__(self, folder):
        self.folder = folder
        self.files_info = {}

    def folder_path(self):
        '''
        Get the folder path variable
        :return: the folder path
        '''
        return self.folder

    def get_all_files(self):
        '''
        It will get the name of all files in the folder path.
        :return: A list with all the names inside the folder.
        '''

        return os.listdir(self.folder)

    def get_files_information(self):
        '''
        Get the size and the created date of the file, and it will save it on a dictionary.
        :return: files_info is updated
        '''
        files = self.get_all_files()
        for file in files:
            if os.path.isdir(self.folder + "\\" + file):
                pass
            else:
                file_size = os.path.getsize(self.folder + "\\\\" + file)

                temp_timestamp = os.path.getctime(self.folder + "\\\\" + file)
                file_datecreated = datetime.fromtimestamp(temp_timestamp).strftime('%Y-%m-%d %H:%M:%S')

                extension_type = os.path.splitext(self.folder + "\\\\" + file)[1]


                #print(f'Name: "{file}"    Size:{file_size} bits    Date Created: {file_datecreated}   Extension: {extension_type}')
                self.files_info[file] = [extension_type, file_size, file_datecreated, self.folder + "\\\\" + file]


def remove_file(file_path):
    '''

    :param file_path:
    :return:
    '''
    os.chmod(file_path, stat.S_IWRITE)

    os.remove(file_path)



if __name__ == '__main__':
    # Create two instances of the Folder (to have the two folder)
    first_folder = Folder((eg.diropenbox(title="Choose the first folder you want to see the files.")).replace("\\", "\\\\"))
    second_folder = Folder((eg.diropenbox(title="Choose the second folder you want to see the files.")).replace("\\", "\\\\"))

    # Get files and files information of the folder
    first_folder.get_all_files()
    first_folder.get_files_information()

    # Get files and files information of the folder
    second_folder.get_all_files()
    second_folder.get_files_information()

    #print("Primeira pasta: " +  str(first_folder.files_info.keys()))



    for file_firstfolder in first_folder.files_info.keys():
        for file_secondfolder in second_folder.files_info.keys():
            if file_firstfolder == file_secondfolder:
                print(f'The file "{file_firstfolder}" is the same the both folders.')

                if len(first_folder.files_info.keys()) > len(second_folder.files_info.keys()):
                    remove_file(second_folder.files_info[file_secondfolder][3])

                else:
                    os.remove(first_folder.files_info[file_firstfolder][3])
                    remove_file(first_folder.files_info[file_firstfolder][3])

            else: pass


    print("Done!")

