# Automated Documentation Assignment

## Introduction

This assignment is designed to teach you how to create and maintain automated documentation for a Python project. You will learn to write documentation in Markdown, create docstrings, use Sphinx to generate documentation, and publish it using Read the Docs.

## Objectives

By the end of this assignment, you should be able to:

1. Write documentation in Markdown
2. Understand and explain the concept of "documentation as code"
3. Write proper docstrings for Python functions
4. Set up Sphinx to generate documentation
5. Create a Read the Docs account and publish a documentation page

## Setup

This project is configured to work with GitHub Codespaces, providing you with a pre-configured development environment. Here's how to get started:

1. Open the project in GitHub Codespaces:
   - Go to the GitHub repository page
   - Click on the "Code" button
   - Select the "Codespaces" tab
   - Click on "Create codespace on main"

2. Once the Codespace is ready, you'll have a fully configured Visual Studio Code environment in your browser.

3. The required packages should already be installed in the Codespace. To verify, open a new terminal in VS Code and run:
   ```
   pip list
   ```
   You should see packages like `pytest`, `sphinx`, and `myst-parser` in the list.

4. If any required packages are missing, you can install them using:
   ```
   pip install -r requirements.txt
   ```

5. You're now ready to start working on the assignment!

Note: If you prefer to work locally instead of using Codespaces, you can clone the repository to your local machine and follow the standard setup process (creating a virtual environment and installing dependencies).

## Tasks

### 1. Implement Calculator Class Methods

1. Open `src/calculator.py`
2. Implement the `multiply` and `divide` methods, including appropriate docstrings
3. Ensure the `divide` method handles division by zero

### 2. Write Unit Tests

1. Open `tests/test_calculator.py`
2. Implement test cases for the `multiply` and `divide` methods
3. Ensure tests cover both normal cases and edge cases (like division by zero)

### 3. Update Usage Documentation

1. Open `docs/usage.md`
2. Add usage examples for the `multiply` and `divide` methods

### 4. Configure Sphinx

1. Check the `docs/conf.py` file to ensure it's configured correctly
2. If you need to use Markdown files, make sure the `myst_parser` extension is added to the `extensions` list

### 5. Generate Documentation

1. Run the following command in the project root directory:
   ```
   sphinx-build -b html docs docs/_build/html
   ```
2. Check the generated HTML files to ensure the documentation is correct

### 6. Set Up Read the Docs

1. Create an account on [Read the Docs](https://readthedocs.org/)
2. Import your GitHub repository to Read the Docs
3. Trigger a documentation build
4. Check the generated documentation page to ensure everything is in order

### 7. Final Check

1. Run the automated check script:
   ```
   python check_assignment.py
   ```
2. Ensure all checks pass
3. If you encounter any issues, fix them based on the error messages

## Submission

After completing all tasks:

1. Commit all changes to GitHub:
   ```
   git add .
   git commit -m "Complete automated documentation assignment"
   git push origin main
   ```
2. Add your Read the Docs documentation link at the bottom of this README file in the specified format.
3. Run the final check:
   ```
   python check_assignment.py
   ```
4. Ensure all checks pass, including the Read the Docs link check.
5. Submit your GitHub repository link to your instructor.

Note: The automated check will verify your Read the Docs link, so make sure it's correctly added to the README and the documentation is successfully published before submitting.

## Grading Criteria

Your assignment will be evaluated based on the following criteria:

1. Correct implementation of the Calculator class (20%)
2. Completeness of unit tests (20%)
3. Quality and completeness of documentation (20%)
4. Correct Sphinx configuration (20%)
5. Successful publication of Read the Docs page (20%)

## Getting Help

If you encounter any issues while completing the assignment:

1. Carefully read the error messages
2. Consult the official documentation of the relevant tools (Python, Sphinx, Read the Docs)
3. If you still can't resolve the issue, contact your instructor or teaching assistant

Good luck with your assignment!

---

## My Read the Docs Documentation Link

[Read the Docs](https://your-project-name.readthedocs.io/)
