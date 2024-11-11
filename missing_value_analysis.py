import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
import seaborn as sns

# Abstract class for Missing Values
# ---------------------------------
# template for missing value analysis

class MissingValueAnalysisTemp(ABC):
    def analyze(self, df: pd.DataFrame):
        """
        Perform complete missing value anlysis by identifying and visualizing.

        Parameter:
        df (pd.DataFrame) a data frame to be analyze.

        Return:
        None: it just visualyze and identify the missing values.
        """
        self.identify_missing_values(df)
        self.visualize_missing_values(df)
    
    @abstractmethod
    def identify_missing_values(self, df: pd.DataFrame):
        """
        Identify the missing values

        Parameter:
        df (pd.DataFrame) a data frame to be analyze.

        Return:
        None: This method should print the missing values.
        """
        pass

    @abstractmethod
    def visualize_missing_values(self, df: pd.DataFrame):
        """
        Visualize the missing values

        Parameter:
        df (pd.DataFrame) a data frame to be analyze.

        Return:
        None: This method should print the missing values.
        """
        pass


# concreate class
class SimpleMissingValueAnalysis(MissingValueAnalysisTemp):
    def identify_missing_values(self, df):
        """
        Prints the count of missing values for each column.

        Parameter:
        df (pd.DataFrame) a data frame to be analyze.

        Return:
        None: Prints the missing values to the console.
        """
        print("Missing Value Columns.")
        miss_value = df.isnull().sum()
        print(miss_value[miss_value > 0])

    def visualize_missing_values(self, df):
        """
        Visualize the count of missing values.

        Parameter:
        df (pd.DataFrame) a data frame to be analyze.

        Return:
        None: Visualize the missing values.
        """
        print("\nVisualizing the missing values...")
        plt.figure(figsize=(10, 6))
        sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
        plt.title("visualizing the missing values".upper())
        plt.show()
        


# example
if __name__ == "__main__":
    
    # df = pd.read_csv(r"D:\data_sets\fusers.csv")
    # # 
    # simp = SimpleMissingValueAnalysis()
    # simp.identify_missing_values(df)
    # simp.visualize_missing_values(df)
    pass