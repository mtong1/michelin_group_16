import pandas as pd

def extract_csv_context(file):
    # Load the CSV file
    df = pd.read_csv(file)
    
    # Extract general information
    context = {
        'file_name': file,
        'shape': df.shape,
        'num_rows': df.shape[0],
        'num_columns': df.shape[1],
        'sample_data': df.head()
    }

    # Column information and data types
    context['column_details'] = {}
    for column in df.columns:
        column_info = {}
        column_info['data_type'] = df[column].dtype
        column_info['num_unique_values'] = df[column].nunique()
        column_info['num_missing_values'] = df[column].isnull().sum()
        
        # Basic statistics for numeric columns
        if pd.api.types.is_numeric_dtype(df[column]):
            column_info['mean'] = df[column].mean()
            column_info['min'] = df[column].min()
            column_info['max'] = df[column].max()
            column_info['std_dev'] = df[column].std()
        

        context['column_details'][column] = column_info
    
    return context

context = extract_csv_context('data/Crash data_LA_county.csv')
print(context)