"""
Knowledge Service Module
Provides functions to build a knowledge graph from a dataset and retrieve relevant chunks based on a query.
"""

from lib.commons.MathUtils import MathUtils as MathUtils
from lib.core.providers.LLMProviderFactory import LLMProviderFactory

current_provider = LLMProviderFactory.get_instance()

class KnowledgeService(object):

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(KnowledgeService, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def build_knowledge(dataset):
        """Builds a knowledge graph from a dataset.
        Args: dataset (list): A list of lines.
        """
        knowledge = []
        for i, chunk in enumerate(dataset):
            embedding = current_provider.embed(text=chunk)
            knowledge.append((chunk, embedding))
        return knowledge

    @staticmethod
    def get_most_relevant_chunks(query, knowledge, top_n=3):
            """Finds the most relevant chunks from a knowledge base based on a query.

            Args:
                query (str): The input query string to find relevant chunks for.
                knowledge (list): A list of tuples where each tuple contains a chunk (str)
                    and its corresponding embedding (list or array).
                top_n (int, optional): The number of most relevant chunks to return. Defaults to 3.

            Returns:
                list: A list of the top N most relevant chunks, each represented as a tuple
                    containing the chunk (str) and its similarity score (float).
            """
            query_embedding = current_provider.embed(text=query)
            # Temporary list to store (chunk, similarity) pairs
            similarities = []
            for chunk, embedding in knowledge:
                similarity = MathUtils.cosine_similarity(query_embedding, embedding)
                similarities.append((chunk, similarity))

            # Sort by similarity in descending order, because higher similarity means more relevant chunks
            similarities.sort(key=lambda x: x[1], reverse=True)

            # Finally, return the top N most relevant chunks
            return similarities[:top_n]

    @staticmethod
    def get_best_matching_chunk(query, chunks):
        """Finds the best matching chunk from a list of chunks based on a query.

        Args:
            query (str): The input query string to find the best matching chunk for.
            chunks (list): A list of chunk strings.
        Returns:
            dict: A dictionary containing the best matching chunk and its similarity score.
        """
        query_embedding = current_provider.embed(text=query)
        best_match = None
        highest_similarity = -1  # Initialize with a very low value

        for chunk in chunks:
            chunk_embedding = current_provider.embed(text=chunk)
            similarity = MathUtils.cosine_similarity(query_embedding, chunk_embedding)

            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match = chunk

        if best_match is not None:
            return {"match": best_match, "similarity": highest_similarity}
        else:
            return None