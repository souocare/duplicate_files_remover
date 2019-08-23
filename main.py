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

                temp_timestamp = os.path.getmtime(self.folder + "\\\\" + file)
                file_datecreated = datetime.fromtimestamp(temp_timestamp).strftime('%Y-%m-%d %H:%M:%S')

                extension_type = os.path.splitext(self.folder + "\\\\" + file)[1]


                #print(f'Name: "{file}"    Size:{file_size} bits    Date Created: {file_datecreated}   Extension: {extension_type}')
                self.files_info[file] = [extension_type, file_size, file_datecreated, self.folder + "\\\\" + file]


def remove_file(file_path):
    '''
    Disable "Read-Only" from the given file and delete it.
    :param file_path: File path to the file to remove
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
            # Now, it will be checked if the files informations (name, size, and date) are the same
            if file_firstfolder == file_secondfolder and \
                    first_folder.files_info[file_firstfolder][1] == second_folder.files_info[file_secondfolder][1] and \
                    first_folder.files_info[file_firstfolder][2] == second_folder.files_info[file_secondfolder][2]:

                folder_to_delete = eg.buttonbox(msg="The file '{}' is the same the both folders. "
                                                "The first folder as {} files and the second folder as {} "
                                                "files.".format(file_firstfolder, len(first_folder.files_info.keys()),
                                                                len(second_folder.files_info.keys())),
                             choices=["Delete file from first folder", "Delete file form second folder"],
                             title="Delete file")

                if folder_to_delete == "Delete file from first folder":
                    remove_file(first_folder.files_info[file_firstfolder][3])
                elif folder_to_delete == "Delete file form second folder":
                    remove_file(second_folder.files_info[file_secondfolder][3])
                else:
                    print("No file was deleted.")
                    pass

            else: pass


    print("Done!")
