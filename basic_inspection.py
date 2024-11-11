from abc import ABC, abstractmethod
import pandas as pd

# using strategy Design pattern

class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, df: pd.DataFrame):
        """
        Perform a specific type of data inspection
        
        Parameters:
        df (pd.DataFrame): The data frame on which inspection has to perform.
        
        Returns:
        None: it returns nothing just print the info.
        """
        pass


class DataTypesStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """
        Inspect and prints the data types & nun-null counts.

        Parameters:
        df (pd.DataFrame): The data frame on which inspection has to perform.
        
        Returns:
        None: it returns nothing just prints the info.
        """
        print('\nData Types & Nun-null counts')
        print(df.info())
        

class DataSummaryStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """
        Inspect and prints statistical summary.

        Parameters:
        df (pd.DataFrame): The data frame on which inspection has to perform.
        
        Returns:
        None: it returns the summary of df.
        """
        print("========================================\nStatistical Summary (Numerical features)\n========================================")
        print(df.describe())
        print("\n")
        print("==========================================\nStatistical Summary (Categorical features)\n==========================================")
        print(df.describe(include=['object']))
        print("\n")
        obj_features = df.columns[df.dtypes == 'object']
        # print(obj_features)
        # print(obj_features[0])
        for feature in obj_features:
            print(df[feature].value_counts())
            print("\n\n")
        # print(df.select_dtypes(include=['object']).value_counts())



class DataInspector:
    def __init__(self, strategy: DataInspectionStrategy):
        """
        Inializes the DataInspector with a specific inspection strategy.
        
        Parameters:
        strategy (DataInspectionStrategy) the strategy to be used for the data inspection.
        
        Retruns:
        None
        """
        self._strategy = strategy

    def set_strategy(self, strategy: DataInspectionStrategy):
        """
        Set a new strategy for inspection.
        
        Parameters:
        strategy (DataInspectionStrategy) the strategy to be used for the data inspection.
        
        Retruns:
        None
        """
        self._strategy = strategy

    def execute_inspection(self, df: pd.DataFrame):
        """
        Excute the inspection using the current Srartegy.

        Parameters:
        strategy (DataInspectionStrategy) the strategy to be used for the data inspection.
        
        Retruns:
        None
        """ 
        self._strategy.inspect(df) 


if __name__ == "__main__":
    # # Example of usage

    # # load the data
    # df = pd.read_csv(r"D:\test_data.csv")

    # # initialize the inspector
    # inspector = DataInspector(DataTypesStrategy()) 
    # inspector.execute_inspection(df)

    # # for summary
    # inspector.set_strategy(DataSummaryStrategy())
    # inspector.execute_inspection(df)
    pass