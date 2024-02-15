# Document Clustering System

## Overview
- This project implements a document clustering system using KMeans clustering. The system collects a number of documents from different categories (e.g., Sport, Tech, Business), clusters them using KMeans, and allows users to input new documents to assign them to existing clusters. I have used the News_category data from Kaggle. <https://www.kaggle.com/datasets/rmisra/news-category-dataset>

## Requirements
- Python 3.x
- Libraries:
- pandas
- scikit-learn
- matplotlib
- seaborn
- nltk
- tkinterDocument Clustering System

## Usage
- Collecting Documents: Before running the code, collect a sufficient number of documents from different categories (e.g., Sport, Health, Business). Store the documents in a CSV file with columns for category and text body.

## Running the Code:
1. Make sure all required libraries are installed.
2. Run the script document_clustering.py.
3. Follow the instructions to input new documents and assign them to existing clusters.

## Files
- document_clustering.py: Main Python script implementing the document clustering system.
- News.csv: Sample CSV file containing collected documents.

## Explanation
- The code reads the documents from the CSV file, preprocesses them (removing stopwords and punctuation), and converts them into numerical vectors using TF-IDF vectorization.
- It determines the optimal number of clusters using the elbow method and performs KMeans clustering.
- Clustering performance metrics such as silhouette score and Davies–Bouldin index are computed to evaluate the quality of clustering.
- The clusters and centroids are visualized using PCA for dimensionality reduction.
- Users can input new documents, which are preprocessed and assigned to existing clusters using the trained KMeans model.

## Contributors
Ghanshyam Kshetri

## License
This project is licensed under the MIT License.
