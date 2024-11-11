import os
import zipfile
from abc import ABC, abstractmethod

import pandas as pd

# Defining an abstract class of Data Ingester
class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, file_path: str)-> pd.DataFrame:
        """Abstract method to ingest data from a given file."""
        pass


# implementing a concreate class for ZIP ingestion
class ZipDataIngestor(DataIngestor):
    def ingest(self, file_path: str)-> pd.DataFrame:
        """Extract .zip file and returns the content as pandas Dataframe."""
        
        # ensuring the file is .zip
        if not file_path.endswith(".zip"):
            raise ValueError("File is not a zip file.")
        
        # extrating the zip
        with zipfile.ZipFile(file_path, 'r') as file_ref:
            file_ref.extractall("Extracted_Data")

        # find the extracted CSV file
        extracted_files = os.listdir("Extracted_Data")
        csv_files = [f for f in extracted_files if f.endswith('.csv')]

        if len(csv_files) == 0:
            raise FileNotFoundError("There is no csv files.")
        if len(csv_files) > 1:
            raise ValueError("There are multiple csv files.")
        
        # read the csv into the data frame
        csv_file_path = os.path.join("Extracted_Data", csv_files[0])
        df = pd.read_csv(csv_file_path)
        
        # returning the DataFrame
        return df
    

# creating the factory class to create DataIngesters
class DataIngesterFactory:
    @staticmethod
    def get_data_ingester(file_extension: str)-> DataIngestor:
        """simply retruns the apropriet data ingester based on extension."""

        if file_extension == '.zip':
            return ZipDataIngestor()
        else:
            raise ValueError("There is no appropriet ingestor.")



if __name__ == "__main__":
    
    # # specify the file path
    # file_path = "D:\data_sets\Iris.zip"

    # # determine the file extension
    # file_ext = os.path.splitext(file_path)[1]
    # # print(file_ext) => ('D:\\data_sets\\BANANA', '.zip')

    # # get the appropriate Dataingestor
    # ingestor = DataIngesterFactory.get_data_ingester(file_ext)
    # # print(ingestor) => <__main__.ZipDataIngestor object at 0x000002936E753EC0>

    # # ingest the data & load into the data frame
    # df = ingestor.ingest(file_path)

    # print(df.head())
    pass
