
def helpMessage():
    help = '''
\033[1;32mA simple utillity for uploading files 
\033[0;49mUsage: fhost [OPTION]... [FILE/FOLDER]...

Options:
    --help, -h 
            returns this help message
    -y
            runs command non interactively
    --links -l
            generates a links file to upload
    '''
    print(help)
