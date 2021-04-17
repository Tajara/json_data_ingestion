from src.origin.load_files import LoadFilesModule
from src.origin.directories_functions import DirectoriesFunctions


def load_files():
    """Process to load .json files from directory to dataframe"""
    json_files = LoadFilesModule.read_json()
    df = LoadFilesModule.dict_to_df(json_files)
    df.show()


def extract_files():
    """Process to extract files from .zip and move them"""
    DirectoriesFunctions.create_tmp_dir()
    DirectoriesFunctions.unzip()
    pass


if __name__ == '__main__':
    extract_files()  # Function responsible to Extract archives from a .zip file
    files = load_files()  # Function responsible to Load the .json files into a dataframe
