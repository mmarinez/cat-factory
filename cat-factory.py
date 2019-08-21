import os


def main():
    print_header()
    folder = get_or_create_output_folder()

    print('Found or created folder: ' + folder)

def print_header():
    print('----------------------')
    print('      Cat Factory')
    print('----------------------')


def get_or_create_output_folder():
    folder_name = 'cat_pictures'

    folder_dir = os.path.abspath(os.path.join('.', folder_name))
    print(folder_dir)

    if not os.path.exists(folder_dir) or not os.path.isdir(folder_dir):
        print('Creating new directory at {}'.format(folder_dir))
        os.mkdir(folder_dir)

    return folder_dir

if __name__ == "__main__":
    main()
