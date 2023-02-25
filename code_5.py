import pandas as pd
us_chronic_disease_file = './US_chronic_diseases.csv'
df = pd.read_csv(us_chronic_disease_file, low_memory=False)
#Use LocationAbbr to filter by state code

def get_melanoma_mortality_information_by_state(state_code):
    #Question = "Column Melanoma, mortality"
    #DataValueAlt
    pass # Remove this line and code your function

def get_asthma_mortality_information_by_state(state_Code):
    #Question = "Asthma mortality rate"
    #DataValueAlt
    pass # Remove this line and code your function

def get_chronic_liver_mortality_by_state(state_code):
    #Question = "Chronic liver disease mortality"
    #DataValueType = "Crude Rate"
    #DataValueAlt
    pass # Remove this line and code your function

def get_missing_values_count_by_state(state_code):
    #DataValueAlt
    #isnull().sum() functions to count all null values
    pass # Remove this line and code your function

if __name__ == "__main__":
    pass # Remove this line and code your user interface