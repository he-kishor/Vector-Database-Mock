import numpy as np
import array_data

class Vector_Db_Mock:
    def __init__(self,query):
        embeddings=array_data.embeddings
        self.product_name=array_data.products
        # query embedding
        query_embedding = np.random.rand(5)
        #call function for cosine similarity, which caluculate value between angle cos=0 is 1, cos=90 is 0 and cos=180=-1
        similarities=self.calculate_cosine_similarity(query_embedding,embeddings)
        results = list(zip(self.product_name, similarities))
        sorted_results = sorted(results, key=lambda x: x[1], reverse=True)
        top_3 = sorted_results[:3]

        #***************print_result**************************************
        print("Top Matches:")
        for idx, (product, similarity) in enumerate(top_3, start=1):
            print(f"{idx}. Product: \"{product}\" | Similarity: {similarity:.3f}")
                
        
        

    def calculate_cosine_similarity(self,query, embeddings):
        similarities = []
        #cosine similarity (A.B/||A||||B||)
        for embedding in embeddings:
            #I prefer to instead skitlearn cosine to cosine hardocode logic
            
            # sum the all vector product 
            dot_product = sum(q * e for q, e in zip(query, embedding))
            
            query_magnitude = np.sqrt(sum(q**2 for q in query))
            embedding_magnitude = np.sqrt(sum(e**2 for e in embedding))
            
            if query_magnitude == 0 or embedding_magnitude == 0:
                similarity = 0  
            else:
                similarity = dot_product / (query_magnitude * embedding_magnitude)
            
            # Append similarity to the list
            similarities.append(similarity)
        
        return similarities
    
    
t1=Vector_Db_Mock

query=input('Enter the product Description: ')
t1(query)
