"""
Unit tests for lib.core.service.KnowledgeService.
"""

from unittest.mock import patch, MagicMock
import lib.core.service.KnowledgeService as ks


class TestKnowledgeService:
    def _mock_embed(self, vectors):
        """Helper: returns a side_effect function that returns vectors in order."""
        iterator = iter(vectors)

        def embed_fn(text):
            return next(iterator)

        return embed_fn

    def test_build_knowledge(self):
        vectors = [[1.0, 0.0], [0.0, 1.0]]
        dataset = ["chunk1", "chunk2"]
        with patch.object(ks, "current_provider") as mock_provider:
            mock_provider.embed.side_effect = vectors
            result = ks.build_knowledge(dataset)
        assert len(result) == 2
        assert result[0] == ("chunk1", [1.0, 0.0])
        assert result[1] == ("chunk2", [0.0, 1.0])

    def test_get_most_relevant_chunks(self):
        # knowledge: (chunk, embedding)
        knowledge = [
            ("about cats", [1.0, 0.0]),
            ("about dogs", [0.0, 1.0]),
            ("about fish", [0.5, 0.5]),
        ]
        query_embedding = [1.0, 0.0]  # most similar to cats
        with patch.object(ks, "current_provider") as mock_provider:
            mock_provider.embed.return_value = query_embedding
            result = ks.get_most_relevant_chunks("cats", knowledge, top_n=2)
        assert len(result) == 2
        # first result should have highest similarity
        assert result[0][0] == "about cats"

    def test_get_best_matching_chunk_returns_match(self):
        chunks = ["apple", "banana", "cherry"]
        query_vec = [1.0, 0.0, 0.0]
        # embeddings: apple is most similar to query
        embeddings = {
            "apple": [1.0, 0.0, 0.0],
            "banana": [0.0, 1.0, 0.0],
            "cherry": [0.0, 0.0, 1.0],
        }
        with patch.object(ks, "current_provider") as mock_provider:
            def embed_fn(text):
                return embeddings.get(text, query_vec)
            mock_provider.embed.side_effect = embed_fn
            # first call is for query
            result = ks.get_best_matching_chunk("apple", chunks)
        assert result is not None
        assert result["match"] == "apple"
        assert result["similarity"] == 1.0

    def test_get_best_matching_chunk_returns_none_when_empty(self):
        with patch.object(ks, "current_provider") as mock_provider:
            mock_provider.embed.return_value = [1.0, 0.0]
            result = ks.get_best_matching_chunk("query", [])
        assert result is None
