"""
Module providing mathematical utility functions.
"""

class MathUtils(object):
    """
    Singleton class for mathematical utility functions.

    This class provides static methods for common mathematical operations, such as vector similarity measures.
    It follows the singleton pattern to ensure only one instance exists, though the methods are static and
    can be called without instantiation.

    Attributes:
        __instance: The singleton instance of the class.
    """

    __instance = None

    @staticmethod
    def get_instance():
        """
        Get the singleton instance of MathUtils.

        Returns:
            MathUtils: The singleton instance of the MathUtils class.
        """
        if MathUtils.__instance is None:
            MathUtils()
        return MathUtils.__instance

    def __init__(self):
        """
        Initialize the singleton instance of MathUtils.

        Raises:
            Exception: If an instance of MathUtils already exists (singleton violation).
        """
        if MathUtils.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            MathUtils.__instance = self

    @staticmethod
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
            >>> MathUtils.cosine_similarity(a, b)
            0.9746318461970762
        """
        dot_product = sum([x * y for x, y in zip(a, b)])  # Compute the dot product of the two vectors
        norm_a = sum([x ** 2 for x in a]) ** 0.5          # Compute the L2 norm of the first vector
        norm_b = sum([x ** 2 for x in b]) ** 0.5          # Compute the L2 norm of the second vector
        return dot_product / (norm_a * norm_b)            # Return the cosine similarity

