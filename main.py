import time

class ByteConverter:
    def __init__(self) -> None:
        self._input_filename = None
        self._output_filename = None
        self._array_name = None

    def _get_input(self, prompt: str) -> str:
        return input(prompt).strip()

    def get_data(self):
        if self._input_filename is None:
            self._input_filename = self._get_input("Enter input filename: ")
        if self._output_filename is None:
            self._output_filename = self._get_input("Enter output filename: ")
        if self._array_name is None:
            self._array_name = self._get_input("Enter array name: ")

    def file_to_header(self):
        self.get_data()
        start_time = time.time()
        print(f"Converting {self._input_filename} to {self._output_filename} with array name {self._array_name}")

        try:
            with open(self._input_filename, "rb") as image_file:
                image_data = image_file.read()

            header_content = [f"unsigned char {self._array_name}[] = {{\n"]
            header_content.extend([f"0x{byte:02x}, " for byte in image_data])
            header_content.append("\n};\n")
            header_content.append(f"unsigned int {self._array_name}_size = sizeof({self._array_name});\n")

            with open(self._output_filename, "w") as header_file:
                header_file.write(''.join(header_content))

            end_time = time.time()
            print(f"Converted {self._input_filename} to {self._output_filename} in {end_time - start_time:.2f} seconds")

        except IOError as e:
            print(f"File operation failed: {e}")

if __name__ == "__main__":
    tool = ByteConverter()
    tool.file_to_header()