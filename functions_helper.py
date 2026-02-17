def check_quit(user_input: str):
    """Check if the user want to quit the script"""
    if user_input.lower().strip() in ['q', 'quit']:
        exit()

def get_valid_filename(prompt: str) -> str:
    """Check if the filename give by the user is valid"""
    while True:
            filename = input(prompt)
            check_quit(filename)
            if ' ' in filename or filename.count('.') != 1:
                print("Filename not valid.")
            else:
                break
    return filename