# NumPy Analyzer

## Project Overview

NumPy Analyzer is a beginner-friendly Python project designed to demonstrate practical use of the **NumPy library** for creating, manipulating, analyzing, and performing mathematical and statistical operations on multidimensional arrays.

The project provides an interactive menu-driven interface that allows users to work with **1D, 2D, and 3D NumPy arrays**.

---

# Objectives

The project aims to help learners understand:

- NumPy arrays
- 1D, 2D, and 3D arrays
- Array dimensions and shapes
- Array indexing
- Array slicing
- Element-wise mathematical operations
- Array concatenation
- Array splitting
- Searching array values
- Sorting arrays
- Filtering arrays
- Boolean masks
- Statistical calculations
- Percentiles
- Correlation
- Python classes and objects
- Class variables
- Getters and setters
- Input validation
- Menu-driven programming

---

# Features

## 1. Create a NumPy Array

The program allows users to create:

- 1D arrays
- 2D arrays
- 3D arrays

Users enter the required dimensions and numeric elements. The program validates the number of elements before creating the array.

The program also displays:

- Number of dimensions
- Array shape
- Total number of elements
- Current active array

---

## 2. Indexing and Slicing

For 2D and 3D arrays, users can perform:

### Indexing

Retrieve a single value using its position.

### Slicing

Extract a selected portion of an array using:

- Row slicing
- Column slicing
- Depth slicing for 3D arrays

---

## 3. Mathematical Operations

The program supports element-wise operations between two arrays of the same shape:

- Addition
- Subtraction
- Multiplication
- Division

The program also checks for division by zero.

---

## 4. Combine or Split Arrays

Users can perform:

### Concatenation

Combine two arrays along a selected axis.

### Splitting

Split an array into multiple equal parts along a selected axis.

---

## 5. Search, Sort, and Filter

The program provides several array analysis operations.

### Search

Search for a target value and display its coordinates.

### Sort

Sort array values in:

- Ascending order
- Descending order

### Filter

Filter array values using comparison operators:

- `>`
- `<`
- `>=`
- `<=`
- `==`

The program displays both the Boolean mask and filtered values.

---

## 6. Statistical Dashboard

The statistical dashboard calculates:

- Sum
- Mean
- Median
- Standard Deviation
- Variance
- Minimum
- Maximum
- Percentile
- Correlation Matrix

The user can also enter a secondary dataset to calculate correlation with the active array.

---

# Technologies Used

- Python
- NumPy

---

# Python Concepts Used

This project demonstrates:

- Variables
- Functions
- Classes
- Objects
- Class variables
- Instance variables
- Encapsulation
- Getters and setters
- Conditional statements
- Loops
- Exception handling
- User input
- Input validation
- List comprehension
- NumPy arrays
- Array reshaping
- Array indexing
- Array slicing
- Array operations
- Statistical functions

---
# Main Menu

After running the program, the following options are available:

- 1. Create a NumPy Array
- 2. Perform Mathematical Operations
- 3. Combine or Split Arrays
- 4. Search, Sort, or Filter Arrays
- 5. Compute Aggregates and Statistics
- 6. Exit

The user can select an option by entering the corresponding number.

---
# Example Workflow
1. Create a NumPy Array
        ↓
2. Enter Array Dimensions
        ↓
3. Enter Array Elements
        ↓
4. View Array Information
        ↓
5. Perform Indexing or Slicing
        ↓
6. Perform Mathematical Operations
        ↓
7. Search, Sort, or Filter
        ↓
8. View Statistical Results
        ↓
9. Exit

---
# Class Used
## DataAnalytics

The DataAnalytics class manages the current NumPy array.

### Main Attributes
- _current_array – Stores the currently active NumPy array.
- total_sessions – Class variable that counts the number of created DataAnalytics objects.
### Main Methods
- get_array() – Returns the current active array.
- set_array() – Sets a new NumPy array after validating its type.
- print_array_info() – Displays information about the current array.
---
# Functions

The project contains separate functions for different operations:

- parse_floats() – Converts user input into floating-point values.
- get_shape_from_user() – Gets array dimensions from the user.
- parse_slice() – Processes slicing input.
- create_array_menu() – Creates arrays and handles indexing and slicing.
- math_operations_menu() – Performs mathematical operations.
- combine_split_menu() – Handles concatenation and splitting.
- search_sort_filter_menu() – Performs searching, sorting, and filtering.
- stats_menu() – Calculates statistical values.
- main() – Controls the main program and menu system.
---
# Error Handling

The program includes validation for:

- Invalid numeric input
- Invalid array dimensions
- Incorrect number of elements
- Invalid array axes
- Index out of bounds
- Invalid slicing format
- Division by zero
- Invalid menu choices
- Missing active array
- Learning Outcomes
---
### After completing this project, learners can understand how NumPy can be used to:

- Create multidimensional arrays
- Access individual elements
- Extract array sections
- Perform fast mathematical operations
- Combine and split arrays
- Search and filter data
- Sort numerical data
- Calculate statistical measurements
- Work with correlation
- Build interactive data analysis applications
- Future Improvements
----
## The project can be extended with:

- Saving arrays to files
- Loading arrays from files
- CSV file support
-Pandas integration
- Data visualization using Matplotlib
- More advanced statistical analysis
- Matrix multiplication
- Broadcasting operations
- Interactive GUI
- Streamlit web interface
- Data import and export functionality
---
# Conclusion

- NumPy Analyzer is a practical project for learning how to use Python and NumPy for numerical computing and basic data analysis. It combines NumPy array operations with Python programming concepts such as classes, functions, input validation, and menu-driven application design.
