"""Script using converter class to execute the file convertions."""

from data_converter import DataConverter
from functions_helper import check_quit, get_valid_filename

if __name__ == "__main__":
    """Script execution to convert file"""
    
    print("===================================================================")
    print("========================= FILE CONVERTER ==========================")
    print("===================================================================")
    print("\nEnter 'q' at anytime to quit.\n")



    while True:
        # Ask to the user the source informations about the file to convert
        source_filename = get_valid_filename(
                "What file do you want to convert (ex: test.json)? "
                )
        source_path = input(
            "What's the path of your file to convert (ex: home/user/...)? "
        )
        check_quit(source_path)

        # Ask to the user the new informations wished for your new convert file
        new_filename = get_valid_filename(
            "\nEnter the filename with the extension for your convert file: "
        )
        new_path = input(
            "Enter the path for your convert file: "
        )
        check_quit(new_path)

        # Split the extension, filename + extension
        source_filename = source_filename.rsplit(sep='.')
        new_filename = new_filename.rsplit(sep='.')

        # Creat an instance of DataConverter
        convert = DataConverter(source_filename[0], source_path)

        # Get the extensions
        ext_sources = source_filename[-1].lower().strip()
        ext_new = new_filename[-1].lower().strip()

        # Convert CSV to JSON
        if  ext_sources == 'csv' and ext_new == 'json':
            message, file = convert.csv_to_json(new_filename[0], new_path)
            print(f"\n{message}")
        
        # Convert JSON to CSV
        elif ext_sources == 'json' and ext_new == 'csv':
            message, file = convert.json_to_csv(new_filename[0], new_path)
            print(f"\n{message}")

        # Input not valid or extension not supported
        else:
            print("\nSorry, conversion not supported.")
            print("Supported: CSV → JSON or JSON → CSV")

        
        more_convert = input("\nDo you want convert another file?(y/n) ")
        check_quit(more_convert)

        if more_convert.lower().strip() in ['n', 'no']:
            exit()



    


    
    

    

