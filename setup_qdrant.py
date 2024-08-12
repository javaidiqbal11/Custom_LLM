from qdrant_client import QdrantClient
from qdrant_client.http import models as rest

# Connect to Qdrant instance
client = QdrantClient("http://localhost:6333")

# Define the vector configuration
vectors_config = rest.VectorParams(
    size=128,  # Define the dimension of your vectors
    distance="Cosine"  # Choose the distance metric: "Cosine", "Euclidean", or "Dot"
)

# Create or recreate the collection with the vectors configuration
client.recreate_collection(
    collection_name="my_collection",
    vectors_config=vectors_config
)

# Insert example data into the collection
points = [
    {
        "id": 1,
        "vector": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0] * 12,  # Example vector data (128 dimensions)
        "payload": {"tag": "example1"}
    },
    {
        "id": 2,
        "vector": [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1] * 12,
        "payload": {"tag": "example2"}
    }
    # Add more data points as needed
]

# Upsert (Insert or update) the data points into the collection
client.upsert(
    collection_name="my_collection",
    points=points
)
