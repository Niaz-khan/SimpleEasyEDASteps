import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
import seaborn as sns

# Abstract class for Multivariete analysis
# ---------------------------------
# template for Multivariete analysis

class MultivarietAnalysisTemplate(ABC):
    def analyze(self, df: pd.DataFrame):
        """
        Perform complete multivariet anlysis visualization.

        Parameter:
        df (pd.DataFrame) a data frame to be analyze.

        Return:
        None: it just visualyze.
        """
        self.generate_corelation_heatmap(df)
        self.generate_pairplot(df)
    
    @abstractmethod
    def generate_corelation_heatmap(self, df: pd.DataFrame):
        """
        Perform complete multivariet anlysis  with heatmap visualization.

        Parameter:
        df (pd.DataFrame) a data frame to be analyze.

        Return:
        None: it just visualyze.
        """
        pass

    @abstractmethod
    def generate_pairplot(self, df: pd.DataFrame):
        """
        Perform complete multivariet anlysis  with pairplot visualization.

        Parameter:
        df (pd.DataFrame) a data frame to be analyze.

        Return:
        None: it just visualyze.
        """
        pass


# concreate class
class SimpleMultivarietAnalysis(MultivarietAnalysisTemplate):
    def generate_corelation_heatmap(self, df):
        """
        Perform complete multivariet anlysis  with heatmap visualization.

        Parameter:
        df (pd.DataFrame) a data frame to be analyze.

        Return:
        None: it just visualyze.
        """
        
        plt.figure(figsize=(12, 8))
        sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
        plt.title("Correlation Heatmap".upper())
        plt.show()
        

    def generate_pairplot(self, df: pd.DataFrame):
        """
        Perform complete multivariet anlysis  with pairplot visualization.

        Parameter:
        df (pd.DataFrame) a data frame to be analyze.

        Return:
        None: it just visualyze.
        """
        sns.pairplot(df)
        plt.suptitle("pairplot of features".upper(), y=1.2)
        plt.show()
        


# example
if __name__ == "__main__":
    
    # df = pd.read_csv(r"D:\data_sets\fusers.csv")
    # # 
    # simp = SimpleMissingValueAnalysis()
    # simp.identify_missing_values(df)
    # simp.visualize_missing_values(df)
    pass