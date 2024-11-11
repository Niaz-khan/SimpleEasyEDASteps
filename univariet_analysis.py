from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# ABS strategy
class UnivarietAnlysisStrategy(ABC):
    @abstractmethod
    def analyze(self, df: pd.DataFrame, feature: str):
        """
        Perform univariet analysis on specific column of Data Frame.

        Parameter:
        df (pd.DataFrame): A data frame from which we analyze the column.
        feature (str): A feature which has to analyze.

        Return:
        None: It visualize the feature info.
        """
        pass


# concreat class class for NUMERICAL feature
class NumericalFeatureAnalysisStrategy(UnivarietAnlysisStrategy):
    def analyze(self, df, feature):
        """
        Perform univariet analysis on Numerical feature of Data Frame.

        Parameter:
        df (pd.DataFrame): A data frame from which we analyze the column.
        feature (str): A feature which has to analyze.

        Return:
        None: It visualize the feature info.
        """
        plt.figure(figsize=(10, 8))
        sns.histplot(df[feature], kde=True, bins=30)
        plt.title(f'Distribution of {feature}')
        plt.xlabel(feature)
        plt.ylabel("Frequency")
        plt.show()


class CategoricalFeatureAnalysisStrategy(UnivarietAnlysisStrategy):
    def analyze(self, df, feature):
        """
        Perform univariet analysis on Categorical feature of Data Frame.

        Parameter:
        df (pd.DataFrame): A data frame from which we analyze the column.
        feature (str): A feature which has to analyze.

        Return:
        None: It visualize the feature info.
        """
        plt.figure(figsize=(10, 8))
        sns.countplot(x=feature, data=df, palette="viridis")
        plt.title(f'Distribution of {feature}')
        plt.xlabel(feature)
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.show()



# Strategy Selector
class UnivarietStrategyAnalyzer:
    def __init__(self, strategy: UnivarietAnlysisStrategy):
        """
        Inializes the StrategyAnalyzer  with a specific analyze strategy.
        
        Parameters:
        strategy (DataInspectionStrategy) the strategy to be used for the feature analysis.
        
        Retruns:
        None
        """
        self._strategy = strategy

    def set_strategy(self, strategy: UnivarietAnlysisStrategy):
        """
        Set a new strategy for feature analysis.
        
        Parameters:
        strategy (DataInspectionStrategy) the strategy to be used for the feature analysis.
        
        Retruns:
        None
        """
        self._strategy = strategy

    def execute_analysis(self, df: pd.DataFrame, feature: str):
        """
        Excute the analyze using the current Srartegy.

        Parameters:
        strategy (DataInspectionStrategy) the strategy to be used for the feature analysis.
        
        Retruns:
        None
        """ 
        self._strategy.analyze(df, feature) 



if __name__ == "__main__":

    # df = pd.read_csv(r"D:\data_sets\fusers.csv")
    # print(df)
    # analyzer = UnivarietStrategyAnalyzer(CategoricalFeatureAnalysisStrategy())
    # analyzer.execute_analysis(df, "name")
    pass