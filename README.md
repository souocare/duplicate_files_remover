# duplicate_files_remover

## Description
This will remove duplicate files from two different folders. It will check for name of the file, the date created, and the size. If they are the same, it will ask if they want to delete the file.
**Be careful using because it will delete permanently the file**

## Dependencies
* [Easygui](http://easygui.sourceforge.net/index.html)
* Os
* Stat
* datetime

## Versions
### 0.1
#### Changes
* Added start file to GitHub [here](https://github.com/souocare/duplicate_files_remover)
* **Note:** it only checks for the same name at the moment.
* **Note 2:** It delets the file in the folder that contains less files.

#### Issues and future plans
* Like the note says, it only checks the name file to compare to see if the files are the name. Probably next version, the program will check for everything
* Ask the folder the person want to delete the duplicate file, and ask if they really want to delete the file. 
* No excpetions errors handeling. Will be added in one of the next versions
* Add more ways to check if files are the same 
* Better GUI and Progress Bar
