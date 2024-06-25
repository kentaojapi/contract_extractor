import pytest

from contract_extractor.add_document import PDFLoader


class TestPDFLOader:
    @pytest.mark.parametrize(
        "input_text, expected_output",
        [
            ("Hello World", "HelloWorld"),
            ("Hello\nWorld", "HelloWorld"),
            ("Hello\u3000World", "HelloWorld"),
            ("Hello\u2003World", "HelloWorld"),
            ("Hello World\n\u3000\u2003", "HelloWorld"),
            ("   ", ""),
            ("Hello", "Hello"),
            ("", ""),
        ],
    )
    def test_clean_text(self, input_text: str, expected_output: str) -> None:
        assert PDFLoader._clean_text(input_text) == expected_output
