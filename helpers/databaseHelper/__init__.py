import pandas as pd
 
class DatabaseHelper:
    
    def extractColumnsForTranslation(self, path, surveySheetName,
                                     responseSheetName,
                                     surveyColumnsLocation="A",
                                    responseColumnsLocation=12):
        
        rawItalianColumns = pd.read_excel(path, usecols=surveyColumnsLocation,
                                          engine="openpyxl", sheet_name=surveySheetName)
        responseColumns = pd.read_excel(path, skiprows=responseColumnsLocation, nrows=1, 
                                        engine="openpyxl", sheet_name=responseSheetName)
        if 'Unnamed: 0' in responseColumns.columns:
            responseColumns.drop("Unnamed: 0", axis = 1, inplace=True)
            
        responseColumns = responseColumns.columns.to_list()
        responseColumns = [responseColumns[x].replace(",", ".",) for x in range(len(responseColumns))]

        responseColumnsValues = []

        for i in range(len(rawItalianColumns)):
            try:
                if any(responseColumns[x] in rawItalianColumns.iloc[i, 0] for x
                       in range(len(responseColumns))):
                    responseColumnsValues.append(rawItalianColumns.iloc[i, 0])
            except TypeError:
                pass
        
        return responseColumnsValues
        
        