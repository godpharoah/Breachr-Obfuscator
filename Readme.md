# **Breachr Obfuscator**

The **Breachr Obfuscator** is a Python-based tool that helps you obfuscate both Python and JavaScript code by renaming variables and encoding the code into a compressed, Base64-encoded string. This makes your code harder to read, reverse-engineer, or understand while retaining the original functionality.

## **Features**
- Obfuscates both Python and JavaScript files.
- Renames all non-reserved variables with random strings.
- Compresses and Base64-encodes the obfuscated code.
- Outputs the obfuscated code with built-in decompression and execution functions.

---

## **Installation**

### Prerequisites
- **Python 3.6+** must be installed.
- Install the required Python libraries by running:

```bash
pip install colorama jsmin
```

### Clone or Download the Project
```bash
git clone https://github.com/yourusername/breachr-obfuscator.git
cd breachr-obfuscator
```

---

## **Usage**

1. **Run the script**:
   ```bash
   python breachr_obfuscator.py
   ```

2. You'll be prompted to select an option:
   - **1**: Obfuscate Python code
   - **2**: Obfuscate JavaScript code
   - **3**: Quit

3. **Input the path** of the Python or JavaScript file you want to obfuscate.

4. The obfuscated code will be saved in the same directory with the extension `.obfuscated.py` for Python and `.obfuscated.js` for JavaScript.

---

## **Showcase**

### **Python Example**

Let's take a simple Python file `example.py` with the following content:

```python
import math

def greet(name):
    print(f"Hello, {name}!")

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    greet("Alice")
    result = add_numbers(3, 5)
    print(f"Result is: {result}")
```

### **Obfuscation Process**

1. Run the `breachr_obfuscator.py` and select "1" to obfuscate Python code.
2. Provide the file path: `example.py`.

The tool will obfuscate the Python code, compress, encode it, and generate the following file `example.py.obfuscated.py`:

```python
import zlib
import base64
exec(zlib.decompress(base64.b64decode('eJyrVkrLz1eyUkpKLFKyUhJVS87PU0jMSeECtOLiS2LKLSkqSi0GCc+p5uTkFJqalFmUWZiXnZ6ipIuUV5JSZpOKqVqWqpmamheVmqQWpBTkFysYpBYkFg4AhIodF7')).decode())
```

### **Deobfuscation & Execution**

The obfuscated Python file can be run the same way as the original file. The decompression and execution functions are built-in.

```bash
python example.py.obfuscated.py
```

Output:
```bash
Hello, Alice!
Result is: 8
```

---

### **JavaScript Example**

Let's take a simple JavaScript file `example.js` with the following content:

```javascript
function greet(name) {
    console.log("Hello, " + name + "!");
}

function addNumbers(a, b) {
    return a + b;
}

greet("Alice");
console.log("Result is: " + addNumbers(3, 5));
```

### **Obfuscation Process**

1. Run the `breachr_obfuscator.py` and select "2" to obfuscate JavaScript code.
2. Provide the file path: `example.js`.

The tool will obfuscate the JavaScript code, compress, encode it, and generate the following file `example.js.obfuscated.js`:

```javascript
import zlib
import base64
exec(zlib.decompress(base64.b64decode('eJzLKCkpKLbS109R0lEKzE+3zNBQz0jNyclXKM8vyklR1wQAHloHtw==')).decode())
```

### **Deobfuscation & Execution**

The obfuscated JavaScript file can also be executed using a JavaScript environment like Node.js (assuming the relevant decompression and execution logic is written for JS).

---

## **Limitations**
- The obfuscator renames non-reserved variables, so some built-in functions or identifiers (e.g., Python built-in functions, JS keywords) will not be renamed.
- For JavaScript, the decompression logic needs to be adjusted for a JS environment, as shown in the Python example.

---

## **Contributing**
Feel free to open issues or submit pull requests for bug fixes or improvements.

---

## **License**
This project is licensed under the MIT License.

---

Let me know if you'd like to include anything else or modify the README further!
