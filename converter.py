import unittest
import os
from .converter import ByteConverter

class TestByteConverter(unittest.TestCase):

    def setUp(self):
        # Setup a test environment
        self.test_input_file = 'test_input.bin'
        self.test_output_file = 'test_output.h'
        self.test_array_name = 'testArray'
        # Create a small test file
        with open(self.test_input_file, 'wb') as f:
            f.write(b'\x00\x01\x02\x03')

    def tearDown(self):
        # Clean up the test environment
        os.remove(self.test_input_file)
        if os.path.exists(self.test_output_file):
            os.remove(self.test_output_file)

    def test_file_to_header(self):
        # Test the file_to_header function
        converter = ByteConverter()  # Adjusted reference to the class
        converter._input_filename = self.test_input_file
        converter._output_filename = self.test_output_file
        converter._array_name = self.test_array_name
        converter.file_to_header()

        self.assertTrue(os.path.exists(self.test_output_file))
        with open(self.test_output_file, 'r') as f:
            content = f.read()
        expected_content = (
            f"unsigned char {self.test_array_name}[] = {{\n"
            "0x00, 0x01, 0x02, 0x03, \n"
            "};\n"
            f"unsigned int {self.test_array_name}_size = sizeof({self.test_array_name});\n"
        )
        self.assertEqual(content, expected_content)

if __name__ == '__main__':
    unittest.main()