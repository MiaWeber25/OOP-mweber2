"""
Module to test the Cups code (main code)
"""
import unittest
from hypothesis import given, strategies as st
from unittest.mock import patch
from typing import List, Tuple
import io
from cups import main


class TestMain(unittest.TestCase):
    @given(
        input_data=st.lists(
            st.one_of(
                st.tuples(
                    st.integers(
                        min_value=1, max_value=50).map(
                            lambda x: str(x * 2)),
                    st.text(
                        min_size=1, max_size=10, alphabet=st.characters(
                            min_codepoint=97, max_codepoint=122))
                ),
                st.tuples(
                    st.text(min_size=1, max_size=10, alphabet=st.characters(
                        min_codepoint=97, max_codepoint=122)),
                    st.integers(min_value=1, max_value=100)
                )
            ),
            unique_by=lambda x: x[1], min_size=1, max_size=20
        )
    )  # this was a nightmare -> causing problems!
    def test_main(self, input_data: List[Tuple[str, str]]) -> None:
        """ Test the main functionality - calls appropriate functions. """
        formatted = f"{len(input_data)}\n"
        formatted += "\n".join(
            f"{item[0]} {item[1]}" if item[0].isdigit() else
            f"{int(item[1]) * 2} {item[0]}" for item in input_data
        ) + '\n'

        with patch('sys.stdin', new=io.StringIO(formatted)), \
             patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            main()

        processed = [
            (int(num) // 2 if num.isdigit() else int(
                color), color if num.isdigit() else num)
            for num, color in input_data
        ]
        processed.sort(key=lambda x: x[0])

        expected = "\n".join(color for _, color in processed) + '\n'
        actual = mock_stdout.getvalue()

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
