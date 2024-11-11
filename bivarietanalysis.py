from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# ABS strategy
class BivarietAnlysis(ABC):
    @abstractmethod
    def analyze(self, df: pd.DataFrame, feature_1: str, feature_2: str):
        """
        Perform bivariet analysis on columns of Data Frame.

        Parameter:
        df (pd.DataFrame): A data frame from which we analyze the columns.
        feature_1 (str): Feature 1 which has to analyze.
        feature_2 (str): Feature 2 which has to analyze.

        Return:
        None: It visualize the feature info.
        """
        pass


# concreat class class for NUMERICAL feature
class NumericalVsNumerical(BivarietAnlysis):
    def analyze(self, df, feature_1, feature_2):
        """
        Perform Bivariet analysis on Numerical features of Data Frame.

        Parameter:
        df (pd.DataFrame): A data frame from which we analyze the columns.
        feature_1 (str): Feature 1 which has to analyze.
        feature_2 (str): Feature 2 which has to analyze.

        Return:
        None: It visualize the feature info.
        """
        plt.figure(figsize=(10, 8))
        sns.scatterplot(x=feature_1, y=feature_2, data=df)
        plt.title(f'{feature_1} VS {feature_2}')
        plt.xlabel(feature_1)
        plt.ylabel(feature_2)
        plt.show()


class CategoricalVsNumerical(BivarietAnlysis):
    def analyze(self, df, feature_1, feature_2):
        """
        Perform Bivariet analysis on Numerical features of Data Frame.

        Parameter:
        df (pd.DataFrame): A data frame from which we analyze the columns.
        feature_1 (str): Feature 1 which has to analyze.
        feature_2 (str): Feature 2 which has to analyze.

        Return:
        None: It visualize the feature info.
        """
        plt.figure(figsize=(6, 4))
        sns.boxplot(x=feature_1, y=feature_2, data=df)
        plt.title(f'{feature_1} VS {feature_2}')
        plt.xlabel(feature_1)
        plt.ylabel(feature_2)
        plt.xticks(rotation=45)
        plt.show()



# Strategy Selector
class BivarietAnalyzer:
    def __init__(self, strategy: BivarietAnlysis):
        """
        Inializes the StrategyAnalyzer  with a specific analyze strategy.
        
        Parameters:
        strategy (BivarietAnlysisStrategy) the strategy to be used for the feature analysis.
        
        Retruns:
        None
        """
        self._strategy = strategy

    def set_strategy(self, strategy: BivarietAnlysis):
        """
        Set a new strategy for feature analysis.
        
        Parameters:
        strategy (BivarietAnlysisStrategy) the strategy to be used for the feature analysis.
        
        Retruns:
        None
        """
        self._strategy = strategy

    def execute_analysis(self, df: pd.DataFrame, feature_1: str, feature_2: str):
        """
        Excute the analyze using the current Srartegy.

        Parameters:
        strategy (BivarietAnlysisStrategy) the strategy to be used for the feature analysis.
        
        Retruns:
        None
        """ 
        self._strategy.analyze(df, feature_1, feature_2) 



if __name__ == "__main__":

    # df = pd.read_csv(r"D:\data_sets\fusers.csv")
    # print(df)
    # analyzer = UnivarietStrategyAnalyzer(CategoricalFeatureAnalysisStrategy())
    # analyzer.execute_analysis(df, "name", "name2")
    pass