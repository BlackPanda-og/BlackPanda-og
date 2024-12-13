import pandas as pd
import numpy as np
import mysql.connector as c
from sklearn.neighbors import NearestNeighbors

# Database connection
myconn = c.connect(host="localhost", user="root", password="1234", database="Prod_Reccomend_Sys")
mycur = myconn.cursor()

# Fetch data from the Content_Store and User_Login tables
mycur.execute("SELECT * FROM Content_Store")
content_data = mycur.fetchall()
mycur.execute("SELECT * FROM User_Login")
user_data = mycur.fetchall()

# Convert to DataFrame
content_df = pd.DataFrame(content_data, columns=['ContentID', 'Type', 'Title', 'Genre', 'Description', 'WebRatings'])
user_df = pd.DataFrame(user_data, columns=['uID', 'Name', 'Password', 'Email_ID', 'Contact_No'])

# Simulate user ratings (1-5 scale)
num_users = user_df.shape[0]
num_content = content_df.shape[0]

# Create a random ratings matrix
np.random.seed(42)  # For reproducibility
ratings_matrix = np.random.randint(1, 6, size=(num_users, num_content))  # Random ratings between 1 and 5

# Create a user-item matrix DataFrame
user_item_matrix = pd.DataFrame(ratings_matrix, index=user_df['uID'], columns=content_df['ContentID'])

# Prepare data for KNN
X = user_item_matrix.values

# Create and train the KNN model
knn_model = NearestNeighbors(n_neighbors=5, algorithm='brute', metric='cosine')
knn_model.fit(X)

# Function to recommend content for a user
def recommend_content(user_id):
    if user_id not in user_item_matrix.index:
        return "User  ID not found."
    
    user_index = user_item_matrix.index.get_loc(user_id)
    distances, indices = knn_model.kneighbors(X[user_index].reshape(1, -1), n_neighbors=6)  # 6 to include the user themselves
    recommended_indices = indices.flatten()[1:]  # Exclude the first index (the user themselves)
    recommended_content_ids = user_item_matrix.columns[recommended_indices]
    return content_df[content_df['ContentID'].isin(recommended_content_ids)]

# Example usage
user_id = 1  # Replace with the desired user ID
recommendations = recommend_content(user_id)
print("Recommended Content:")
print(recommendations[['Title', 'Genre', 'WebRatings']])
