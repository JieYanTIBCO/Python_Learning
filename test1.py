import cudf
import numpy as np

# Generate a large dataset
n_rows = 10_000_000  # 10 million rows
data = {
    'category': np.random.choice(['A', 'B', 'C', 'D'], size=n_rows),
    'value': np.random.rand(n_rows)
}

# Create a cuDF DataFrame
gdf = cudf.DataFrame(data)

# Perform a grouped aggregation
result = gdf.groupby('category').agg({'value': ['mean', 'sum', 'count']})

# Display the result
print(result)