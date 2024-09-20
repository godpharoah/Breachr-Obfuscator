import ast
import jsmin
import random
import string
import base64
import zlib
from colorama import Fore, init
import keyword

init(autoreset=True)

class BreachrObfuscator:
    def __init__(self):
        self.breachr_replacements = {}
        self.python_keywords = set(keyword.kwlist)  # Python reserved keywords
        self.js_keywords = set(['function', 'return', 'var', 'let', 'const'])  # JS reserved keywords

    def obfuscate_python(self, breachr_code):
        breachr_tree = ast.parse(breachr_code)
        self.rename_breachr_variables(breachr_tree)
        breachr_obfuscated_code = ast.unparse(breachr_tree)
        return self.compress_and_encode(breachr_obfuscated_code)

    def rename_breachr_variables(self, breachr_node):
        for breachr_child in ast.iter_child_nodes(breachr_node):
            if isinstance(breachr_child, ast.Name):
                if breachr_child.id not in self.python_keywords and breachr_child.id not in dir(__builtins__):
                    breachr_new_name = self.random_breachr_string()
                    self.breachr_replacements[breachr_child.id] = breachr_new_name
                    breachr_child.id = breachr_new_name
            self.rename_breachr_variables(breachr_child)

    def obfuscate_javascript(self, breachr_code):
        breachr_minified_code = jsmin.jsmin(breachr_code)
        breachr_obfuscated_code = self.rename_breachr_js_variables(breachr_minified_code)
        return self.compress_and_encode(breachr_obfuscated_code)

    def rename_breachr_js_variables(self, breachr_code):
        breachr_lines = breachr_code.splitlines()
        breachr_obfuscated_lines = []
        for breachr_line in breachr_lines:
            breachr_obfuscated_line = self.obfuscate_breachr_js_line(breachr_line)
            breachr_obfuscated_lines.append(breachr_obfuscated_line)
        return "\n".join(breachr_obfuscated_lines)

    def obfuscate_breachr_js_line(self, breachr_line):
        breachr_words = breachr_line.split()
        breachr_obfuscated_line = []
        for breachr_word in breachr_words:
            if breachr_word.isidentifier() and breachr_word not in self.js_keywords:
                breachr_obfuscated_line.append(self.random_breachr_string())
            else:
                breachr_obfuscated_line.append(breachr_word)
        return ' '.join(breachr_obfuscated_line)

    def random_breachr_string(self, breachr_length=8):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=breachr_length))

    def compress_and_encode(self, breachr_code):
        breachr_compressed_code = zlib.compress(breachr_code.encode())
        breachr_encoded_code = base64.b64encode(breachr_compressed_code).decode()
        # Add the necessary imports to the obfuscated code
        return (
            "import zlib\n"
            "import base64\n"
            f"exec(zlib.decompress(base64.b64decode('{breachr_encoded_code}')).decode())"
        )

    def save_obfuscated_code(self, breachr_obfuscated_code, breachr_file_path):
        with open(breachr_file_path, 'w') as breachr_file:
            breachr_file.write(breachr_obfuscated_code)

if __name__ == "__main__":
    breachr_obfuscator = BreachrObfuscator()
    
    while True:
        print(Fore.CYAN + "1. Obfuscate Python code")
        print(Fore.GREEN + "2. Obfuscate JavaScript code")
        print(Fore.YELLOW + "3. Quit")
        breachr_choice = input(Fore.MAGENTA + "Enter your choice: ")

        if breachr_choice == "1":
            breachr_file_path = input(Fore.BLUE + "Enter the Python file path: ")
            with open(breachr_file_path, 'r') as breachr_file:
                breachr_code = breachr_file.read()
            breachr_obfuscated_code = breachr_obfuscator.obfuscate_python(breachr_code)
            breachr_obfuscator.save_obfuscated_code(breachr_obfuscated_code, breachr_file_path + '.obfuscated.py')
            print(Fore.GREEN + "Python code obfuscated successfully!")
        elif breachr_choice == "2":
            breachr_file_path = input(Fore.BLUE + "Enter the JavaScript file path: ")
            with open(breachr_file_path, 'r') as breachr_file:
                breachr_code = breachr_file.read()
            breachr_obfuscated_code = breachr_obfuscator.obfuscate_javascript(breachr_code)
            breachr_obfuscator.save_obfuscated_code(breachr_obfuscated_code, breachr_file_path + '.obfuscated.js')
            print(Fore.GREEN + "JavaScript code obfuscated successfully!")
        elif breachr_choice == "3":
            print(Fore.RED + "Exiting the obfuscator. Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")
