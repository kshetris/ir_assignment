import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils.wordprocess import WordProcess

from models.models import Paper

class Search():
    
    def __init__(self, query):
        self.query = query

    @classmethod
    def union(cls, lists):
        union = list(set.union(*map(set, lists)))
        union.sort()
        return union

    @classmethod
    def intersection(cls, lists):
        intersect = list(set.intersection(*map(set, lists)))
        intersect.sort()
        return intersect

    def search_using_cosinesimilarity(self):
        wp = WordProcess()
        vectorizer = TfidfVectorizer()
        df = wp.preprocess_df()
        tfidf_matrix = vectorizer.fit_transform(df['title'].to_numpy())
        preprocessed_query = wp.preprocess_text(self.query)
        query_tfidf = vectorizer.transform([preprocessed_query])
        similarities = cosine_similarity(query_tfidf, tfidf_matrix, dense_output=True).flatten()
        indices = similarities.argsort()[::-1]
        results = df.loc[indices]
        data_list = []
        for idx, (_, row) in enumerate(results.iterrows()):
            if(similarities[indices[idx]] > 0):
                paper = Paper.query.filter(Paper.id == row['id']).first()
                data_dict = {
                    'id': row['id'], 
                    'title': paper.title, 
                    'link':paper.link, 
                    'published_date':paper.published_date, 
                    'score': similarities[indices[idx]],
                    'authors': paper.authors
                }
                data_list.append(data_dict)
        return data_list

    def search_using_and(self):
        retrieved = list()
        data_list = []
        with open('indexes.json', 'r') as index_file:
            data = json.load(index_file)
            wp = WordProcess()
            preprocessed_query = wp.preprocess_text(self.query)
            words_in_query = preprocessed_query.split()
            for word in words_in_query:
                if word in data.keys():
                    retrieved.append(data[word])

        print(retrieved)
        if len(retrieved) != len(words_in_query):
            return data_list
        
        if len(retrieved) > 0:
            matched = Search.intersection(retrieved)
            for id in matched:
                paper = Paper.query.filter(Paper.id == id).first()
                if paper is not None:
                    data_dict = {
                        'id': paper.id, 
                        'title': paper.title, 
                        'link':paper.link, 
                        'published_date':paper.published_date, 
                        'authors': paper.authors
                    }
                data_list.append(data_dict)
        return data_list
            
    def search_using_or(self):
        retrieved = list()
        with open('indexes.json', 'r') as index_file:
            data = json.load(index_file)
            wp = WordProcess()
            preprocessed_query = wp.preprocess_text(self.query)
            words_in_query = preprocessed_query.split()
            for word in words_in_query:
                if word in data.keys():
                    retrieved.append(data[word])
        data_list = []
        if len(retrieved) > 0:
            matched = Search.union(retrieved)
            for id in matched:
                paper = Paper.query.filter(Paper.id == id).first()
                if paper is not None:
                    data_dict = {
                        'id': paper.id, 
                        'title': paper.title, 
                        'link':paper.link, 
                        'published_date':paper.published_date, 
                        'authors': paper.authors
                    }
                data_list.append(data_dict)
        return data_list



