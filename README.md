# UST-python-assessment 

This project consists of several Python programs, each implementing a specific functionality. The goal of the project is to demonstrate modular code, parallel processing, and unit testing. The following instructions guide you through setting up, running, and testing the code.

## Table of Contents
1. [Requirements](#requirements)
2. [Running programs](#running-programs)
3. [Running Unit Tests](#running-unit-tests)
4. [Project Structure](#project-structure)


---
## Requirements
- python>=3.9 version 

## Running programs 
- Run the Main Program: This will execute all three programs in parallel using multi-threading..

`bash`
python -m bin.main

## Running Unit Tests
- Each function in the code has associated unit tests, located in the tests/ folder.

- To run all unit tests:

`bash`
python -m tests.unit_test


## Project Structure

```plaintext
UST-python-assessment/
├── bin
|     |__ main.py                        # Main entry point to call all functions  
|                      
├── input_data/                          # Input data folder for all programs
│   ├── circular_queue_input.txt         # Input for Program 2 (Circular Queue)
│   ├── password_validator_input.txt     # Input for Program 3 (Password Validator)
│   └── word_frequency_input.txt         # Input for Program 1 (Word Frequency Counter)
├── src/                                 # Source code folder for all programs
│   ├── circular_queue.py                # Code for Program 2 (Circular Queue)
│   ├── password_validator.py            # Code for Program 3 (Password Validator)
│   └── word_frequency.py                # Code for Program 1 (Word Frequency Counter)
├── tests/                               # Folder for unit tests
│   |__ unit_test.py                     # Unit tests for all programs
│     
|__ README.md                            # Instructions on how to use the code                            

---



