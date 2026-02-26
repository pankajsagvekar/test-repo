import pandas as pd

def process_data(data_frame):
    # Perform filtering based on 'age' before dropping the column
    filtered_data = data_frame[data_frame['age'] > 30].copy()
    # Drop 'age' column after filtering is complete
    return filtered_data.drop(columns=['age'])

data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, 32, 28, 45],
        'city': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)

try:
    processed_df = process_data(df.copy())
    print(processed_df)
except Exception as e:
    print(f"An error occurred: {e}")