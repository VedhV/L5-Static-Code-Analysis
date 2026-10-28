# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis?

Static code analysis examines source code without executing it. It helps identify potential bugs, security vulnerabilities, and style violations before the software is deployed.

## 2. What did Pylint, Bandit, and Flake8 identify?

Pylint identified code-quality issues such as missing docstrings, inconsistent naming, broad exception handling, and unused or poorly structured code. Bandit identified security risks involving XML-RPC and unsafe HTML rendering. Flake8 identified formatting issues such as missing blank lines and lines that exceeded the permitted length.

## 3. How did fixing the issues improve the program?

The changes improved input handling, auction validation, HTML safety, readability, and maintainability. The program now rejects seller self-bids and bids below the reserve price, enforces the minimum increment, and escapes untrusted text before rendering HTML.

## 4. What did I learn from this lab?

I learned that different static-analysis tools identify different categories of problems. Pylint focuses on code quality, Bandit focuses on security, and Flake8 focuses on style. Running these tools again after making changes helps verify that the reported issues have been addressed. Static analysis should be combined with running and testing the program because not every logical bug is automatically detected by a tool.
