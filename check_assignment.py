import os
import sys
import importlib
import pytest
import re
import requests
from sphinx.cmd.build import build_main

def check_calculator_implementation():
    try:
        from src.calculator import Calculator
        calc = Calculator()
        assert hasattr(calc, 'multiply'), "multiply method is not implemented"
        assert hasattr(calc, 'divide'), "divide method is not implemented"
        assert calc.multiply(2, 3) == 6, "multiply method is not working correctly"
        assert calc.divide(6, 2) == 3, "divide method is not working correctly"
        print("Calculator implementation: PASS")
        return True
    except Exception as e:
        print(f"Calculator implementation: FAIL - {str(e)}")
        return False

def check_tests():
    exit_code = pytest.main(["-v", "tests/test_calculator.py"])
    if exit_code == 0:
        print("Tests: PASS")
        return True
    else:
        print("Tests: FAIL")
        return False

def check_docstrings():
    try:
        from src.calculator import Calculator
        assert Calculator.multiply.__doc__, "multiply method is missing a docstring"
        assert Calculator.divide.__doc__, "divide method is missing a docstring"
        print("Docstrings: PASS")
        return True
    except Exception as e:
        print(f"Docstrings: FAIL - {str(e)}")
        return False

def check_usage_doc():
    with open('docs/usage.md', 'r') as f:
        content = f.read()
    if 'multiply' in content and 'divide' in content:
        print("Usage documentation: PASS")
        return True
    else:
        print("Usage documentation: FAIL - missing examples for multiply and divide")
        return False

def check_sphinx_config():
    if os.path.exists('docs/conf.py'):
        print("Sphinx configuration: PASS")
        return True
    else:
        print("Sphinx configuration: FAIL - conf.py is missing")
        return False

def build_docs():
    result = build_main(['-b', 'html', 'docs', 'docs/_build'])
    if result == 0:
        print("Documentation build: PASS")
        return True
    else:
        print("Documentation build: FAIL")
        return False

def check_readthedocs_link():
    with open('README.md', 'r') as f:
        content = f.read()
    
    match = re.search(r'\[Read the Docs\]\((https?://.*\.readthedocs\.io/.*)\)', content)
    
    if not match:
        print("Read the Docs link: FAIL - Link not found in README.md")
        return False
    
    link = match.group(1)
    
    try:
        response = requests.get(link)
        if response.status_code == 200:
            print(f"Read the Docs link: PASS - {link}")
            return True
        else:
            print(f"Read the Docs link: FAIL - Link returned status code {response.status_code}")
            return False
    except requests.RequestException:
        print(f"Read the Docs link: FAIL - Unable to access {link}")
        return False

def main():
    checks = [
        check_calculator_implementation,
        check_tests,
        check_docstrings,
        check_usage_doc,
        check_sphinx_config,
        build_docs
        check_readthedocs_link
    ]
    
    results = [check() for check in checks]
    
    if all(results):
        print("\nAll checks passed successfully!")
        sys.exit(0)
    else:
        print("\nSome checks failed. Please review the output above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
