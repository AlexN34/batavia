from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class AsciiTests(TranspileTestCase):
    def test_ascii(self):
        self.assertCodeExecution("""
            print(ascii("aaa"))
            print(ascii("übermöhren"))
            print(ascii("バタビア"))
            print(ascii("a𓈈"))
            """)


class BuiltinAsciiFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["ascii"]

    not_implemented = [
        'test_class',
        'test_NotImplemented',
    ]
