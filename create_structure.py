import os

def create_project_structure(project_name):
    # Define the basic structure of the project
    structure = {
        project_name: [
            "src",
            "tests",
            "docs",
            "venv",            # Virtual environment folder (optional, usually created manually)
            ".gitignore",
            "README.md",
            "requirements.txt",
        ]
    }

    # Create the directories and files
    for folder, subfolders in structure.items():
        os.makedirs(folder, exist_ok=True)  # Create the main project directory
        for item in subfolders:
            path = os.path.join(folder, item)
            if item == "src":
                os.makedirs(path, exist_ok=True)  # Create 'src' directory
                # Create a sample Python file in 'src'
                with open(os.path.join(path, "__init__.py"), "w") as f:
                    f.write("# This is the init file for the package.\n")
                # Create a generic processor class file
                with open(os.path.join(path, "generic_processor.py"), "w") as f:
                    f.write(
                        "class GenericProcessor:\n"
                        "    def __init__(self):\n"
                        "        pass\n\n"
                        "    def process(self, items, operation):\n"
                        "        \"\"\"\n"
                        "        Process a list of items based on the specified operation.\n"
                        "        :param items: A list of items to process.\n"
                        "        :param operation: A callable that defines the processing operation.\n"
                        "        :return: A list of processed items.\n"
                        "        \"\"\"\n"
                        "        return [operation(item) for item in items]\n"
                    )
                # Create a main file in 'src'
                with open(os.path.join(path, "main.py"), "w") as f:
                    f.write(
                        "from generic_processor import GenericProcessor\n\n"
                        "def main():\n"
                        "    processor = GenericProcessor()\n"
                        "    data = [1, 2, 3, 4, 5]\n"
                        "    # Example operation: doubling the values\n"
                        "    doubled = processor.process(data, lambda x: x * 2)\n"
                        "    print(\"Doubled values:\", doubled)  # Should print [2, 4, 6, 8, 10]\n\n"
                        "if __name__ == \"__main__\":\n"
                        "    main()\n"
                    )
            elif item == "tests":
                os.makedirs(path, exist_ok=True)  # Create 'tests' directory
                # Create a sample test file in 'tests'
                with open(os.path.join(path, "test_generic_processor.py"), "w") as f:
                    f.write(
                        "import unittest\n"
                        "from src.generic_processor import GenericProcessor\n\n"
                        "class TestGenericProcessor(unittest.TestCase):\n"
                        "    def setUp(self):\n"
                        "        self.processor = GenericProcessor()\n\n"
                        "    def test_process(self):\n"
                        "        data = [1, 2, 3]\n"
                        "        result = self.processor.process(data, lambda x: x * 2)\n"
                        "        self.assertEqual(result, [2, 4, 6])\n\n"
                        "if __name__ == '__main__':\n"
                        "    unittest.main()\n"
                    )
            elif item == "docs":
                os.makedirs(path, exist_ok=True)  # Create 'docs' directory
            elif item == ".gitignore":
                with open(path, "w") as f:
                    f.write(
                        "__pycache__/\n"
                        "venv/\n"
                        "*.pyc\n"
                        "*.pyo\n"
                        "*.pyd\n"
                        "*.egg-info/\n"
                    )
            elif item == "README.md":
                with open(path, "w") as f:
                    f.write("# " + project_name + "\n\n" "## Description\n\n")
            elif item == "requirements.txt":
                with open(path, "w") as f:
                    f.write("# List your project dependencies here\n")

    print(f"Project structure for '{project_name}' created successfully.")

if __name__ == "__main__":
    project_name = input("Enter the project name: ")
    create_project_structure(project_name)
