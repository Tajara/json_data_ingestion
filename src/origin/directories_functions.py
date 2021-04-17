import os,json
import zipfile

class DirectoriesFunctions():
    path = "D:\Projetos\json_data_ingestion\input_data\_tmp"

    def create_tmp_dir():
        # FUNCTION RESPONSIBLE FOR CREATE A TEMPORARY PATH TO EXTRACT THE .ZIP FILE

        # path creation
        path = "D:\Projetos\json_data_ingestion\input_data\_tmp"

        # define the access rights
        access_rights = 0o755

        # Remove directory

        try:
            os.mkdir(path, access_rights)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s" % path)
        pass

    def unzip():
        # FUNCTION RESPONSIBLE TO UNZIP THE FILE WITH THE JSON FILES
        path = "D:\Projetos\json_data_ingestion\input_data\_tmp"

        with zipfile.ZipFile('D:\Projetos\json_data_ingestion\input_data\Payload.zip', 'r') as zip_ref:
            zip_ref.extractall(path)
        pass

pass