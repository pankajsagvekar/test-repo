import pandas as pd

def process_data(data_frame):
    # Filter the data first while the 'age' column still exists
    filtered_data = data_frame[data_frame['age'] > 30].copy()
    # Drop the 'age' column after filtering is complete
    processed_data = filtered_data.drop(columns=['age'])
    return processed_data

data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, 32, 28, 45],
        'city': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)

try:
    processed_df = process_data(df.copy())
    print(processed_df)
except Exception as e:
    print(f"An error occurred: {e}")