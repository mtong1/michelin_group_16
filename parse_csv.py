# parse_csv.py
# making a very basic instantiation to test out querry_llama

import pandas as pd

def extract_csv_context(file_path):
    #Gathering key information about the DataFrame instance
    # such as its structure and content.
    df = pd.read_csv(file_path)
    
    context = {
        "file_name": file_path,
        "shape": df.shape,
        "columns": list(df.columns),
        "data_types": df.dtypes.apply(str).to_dict(),
        "sample_data": df.head().to_dict(orient="records"),
    }
    return context

def extract_csv_metadata(df):
    #metadata= data desribing other data, in this case the dataframe instance
    if df.empty:
        return {"message": "The DataFrame is empty."}
    
    metadata = {
        "columns": list(df.columns),
        "data_types": df.dtypes.apply(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "unique_values": {col: df[col].nunique() for col in df.columns if df[col].dtype != 'object'},
        "sample_data": df.head().to_dict(orient="records")
    }
    return metadata

