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
            elif item == "tests":
                os.makedirs(path, exist_ok=True)  # Create 'tests' directory
                # Create a sample test file in 'tests'
                with open(os.path.join(path, "test_sample.py"), "w") as f:
                    f.write(
                        "import unittest\n\n"
                        "class TestSample(unittest.TestCase):\n"
                        "    def test_example(self):\n"
                        "        self.assertEqual(1 + 1, 2)\n\n"
                        "if __name__ == '__main__':\n"
                        "    unittest.main()"
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
