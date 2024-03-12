import pandas as pd
import numpy as np

# Useful classes
class Data_cleaning():
    """
    A class for data cleaning operations on a DataFrame.
    """
    def __init__(self, df) -> None:
        """
        Constructor method to initialize the DataCleaning object.

        Parameters:
        df (DataFrame): The DataFrame to be cleaned.
        """
        self.df = df
    
    def converting_data_types(self, columns):
        """
        Method to convert data types of specified columns in the DataFrame.

        Parameters:
        columns (dict): A dictionary specifying the columns and their corresponding data types.

        Returns:
        DataFrame: The cleaned DataFrame with converted data types.
        """
        
        print("\n --- converting_data_types method executed --- \n")
        self.df.replace('\\N', np.nan, inplace=True)

        # Switch based on data type
        def switch(case):
            if case == 'int_cols':
                print('converting int_cols')
                self.df[columns['int_cols']] = self.df[columns['int_cols']].astype('Int32', errors='ignore')
                #self.df['difficulty_feedback'] = self.df['difficulty_feedback'].astype('Int32')
            elif case == 'float_cols':
                print('converting float_cols')
                self.df[columns['float_cols']] = self.df[columns['float_cols']].apply(pd.to_numeric, errors='ignore')
            elif case == 'datetime':
                print('converting datetime')
                self.df[columns['datetime']] = self.df[columns['datetime']].apply(pd.to_datetime, errors='coerce')
            elif case == 'boolean':
                print('converting boolean')
                self.df[columns['boolean']] = self.df[columns['boolean']].replace({'t': True, 'f': False}) # string case
                self.df[columns['boolean']] = self.df[columns['boolean']].replace({'1': True, '0': False}) # string case
                self.df[columns['boolean']] = self.df[columns['boolean']].replace({1: True, 0: False}) # int case
            else:
                print('Anything converted')
        
        if columns:
            for data_type in columns:
                switch(data_type)            
            
            self.df.replace({pd.NA: np.nan}, inplace=True)
            return self.df
        else:
            pass
    
    def check_data_type(self):
        """
        Method to check the data types of columns in the DataFrame.
        """
        print("\n --- check_data_type method executed --- \n")
        print(self.df.dtypes)
    
    def check_duplicated(self):
        """
        Method to check for duplicate rows in the DataFrame.
        """
        print("\n --- check_duplicate method executed --- \n")
        print(self.df.duplicated(keep='last'))

    def check_unit_columns(self, columns):
        """
        Method to check the unique values of specified columns in the DataFrame.

        Parameters:
        columns (list): A list of column names to check.
        """
        print("\n --- check_unit_columns method executed --- \n")
        if columns:
            for column in columns:
                print(self.df[column].value_counts())
        else: 
            pass
