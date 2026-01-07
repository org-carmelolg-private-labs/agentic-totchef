"""
Module providing mathematical utility functions.
"""
def cosine_similarity(a, b):
        """
        Compute the cosine similarity between two vectors.

        Cosine similarity measures the cosine of the angle between two non-zero vectors
        in an inner product space. It is a commonly used measure to determine how
        similar two vectors are in terms of direction, ignoring their magnitude.

        Args:
            a (list[float]): The first vector, represented as a list of numbers.
            b (list[float]): The second vector, represented as a list of numbers.
                Both vectors should be the same length. If the vectors differ in
                length, the function will compare elements up to the length of the
                shorter one (behaviour inherited from zip).

        Returns:
            float: The cosine similarity between vectors `a` and `b`. The value is
                   in the range [-1.0, 1.0], where:
                     - 1.0 indicates the vectors are identical in direction,
                     - 0.0 indicates orthogonality (no directional similarity),
                     - -1.0 indicates opposite directions.

        Raises:
            ZeroDivisionError: If either vector has zero magnitude (norm 0), the
                               function will attempt to divide by zero and raise
                               a ZeroDivisionError. Callers may want to guard
                               against zero vectors before calling this function.

        Notes:
            - This implementation computes the dot product and L2 norms directly.
            - For large vectors or many repeated similarity computations, consider
              using optimized numerical libraries such as NumPy for performance
              and numerical stability.

        Example:
            >>> a = [1.0, 2.0, 3.0]
            >>> b = [4.0, 5.0, 6.0]
            >>> cosine_similarity(a, b)
            0.9746318461970762
        """
        dot_product = sum([x * y for x, y in zip(a, b)])  # Compute the dot product of the two vectors
        norm_a = sum([x ** 2 for x in a]) ** 0.5          # Compute the L2 norm of the first vector
        norm_b = sum([x ** 2 for x in b]) ** 0.5          # Compute the L2 norm of the second vector
        return dot_product / (norm_a * norm_b)            # Return the cosine similarity

