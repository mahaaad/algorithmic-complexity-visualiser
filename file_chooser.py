from menu import *
from files_and_directories import *
import os

def get_file_path_and_name(prompt='Choose a file by number:',
                           dir='.',
                           pattern='*',
                           allow_cd=False):
    while True:
        filenames = get_filenames(dir, pattern)
        if allow_cd:
            print('Current directory is\n' + os.getcwd())
            print()
        print('Showing ' + str(len(filenames)) +\
              ' files matching pattern "' + pattern +'".')
        menu_choices = filenames
        if allow_cd: # change directory allowed?
            menu_choices += ['<<Change directory>>'] # Yes, add this choice.
        menu_choice = do_menu(prompt,menu_choices)
        print()
        if allow_cd and (menu_choice == len(filenames)):
            dir_names = get_subdirectories(dir)
            print('Current directory is\n' + os.getcwd())
            dir_menu_choice = do_menu('Choose a directory by number:',\
                                      dir_names + ['^^Go up a directory^^'])
            print()
            if dir_menu_choice == len(dir_names) + 1:
                os.chdir('..')
            elif dir_menu_choice != None:
                os.chdir(dir_names[dir_menu_choice - 1])
        elif menu_choice == None:
            return None
        else:
            return os.getcwd(), filenames[menu_choice - 1] # (path, filename)

def main():
    """Test function for file_chooser module."""
    file_path = get_file_path_and_name(pattern='*.py')
    if file_path != None:
        print('Path:',file_path[0])
        print('File:',file_path[1])
        print('Both:',os.path.join(file_path[0],file_path[1]))
    print()
    #Repeat, allowing change of directory
    file_path = get_file_path_and_name(pattern='*.py',allow_cd=True)
    if file_path != None:
        print('Path:',file_path[0])
        print('File:',file_path[1])
        print('Both:',os.path.join(file_path[0],file_path[1]))
    print('Done test.')

if __name__ == '__main__':
    main()
