import numpy as np


class DataAnalytics:
    total_sessions = 0

    def __init__(self):
        self.__current_array = None
        DataAnalytics.increment_sessions()

    @classmethod
    def increment_sessions(cls):
        cls.total_sessions += 1

    @classmethod
    def get_total_sessions(cls):
        return cls.total_sessions


    def get_array(self):
        return self.__current_array

    def set_array(self, new_array):
        if isinstance(new_array, np.ndarray):
            self.__current_array = new_array
            return True
        return False

    
    def __compute_array_meta(self):
        if self.__current_array is None:
            return {"ndim": 0, "shape": (), "size": 0, "dtype": None}
        return {
            "ndim": self.__current_array.ndim,
            "shape": self.__current_array.shape,
            "size": self.__current_array.size,
            "dtype": self.__current_array.dtype
        }

    
    @staticmethod
    def parse_float_input(raw_input):
        cleaned = raw_input.strip()
        if len(cleaned) == 0:
            return []
            
        parts = cleaned.split()
        parsed_numbers = []
        
        for part in parts:
            is_valid_number = True
            dot_count = 0
            
            for idx, char in enumerate(part):
                if char == '-':
                    if idx != 0 or len(part) == 1:
                        is_valid_number = False
                        break
                elif char == '.':
                    dot_count += 1
                    if dot_count > 1:
                        is_valid_number = False
                        break
                elif not char.isdigit():
                    is_valid_number = False
                    break
            
            if is_valid_number and len(part) > 0:
                parsed_numbers.append(float(part))
            else:
                return []  
                
        return parsed_numbers

    def print_array_status(self):
        """Helper to print current array status along with private internal metadata."""
        if self.__current_array is None:
            print("\n[Current State]: No array loaded.")
        else:
            meta = self.__compute_array_meta()
            print("\n--- Current Active Array ---")
            print(f"Dimensions: {meta['ndim']}D | Shape: {meta['shape']} | Total Elements: {meta['size']}")
            print(self.__current_array)
            print("----------------------------")



def display_main_menu():
    print("\nWelcome to the NumPy Analyzer!")
    print("===================================")
    print("Choose an option:")
    print("1. Create a NumPy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort, or Filter Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Exit")


def input_dimensions():
    print("\nSelect Array Dimension:")
    print("1. 1D Array")
    print("2. 2D Array")
    print("3. 3D Array")
    dim_choice = input("Enter choice (1-3): ").strip()

    if dim_choice == '1':
        len_str = input("Enter length of array: ").strip()
        if len_str.isdigit() and int(len_str) > 0:
            return (int(len_str),)
    elif dim_choice == '2':
        r_str = input("Enter number of rows: ").strip()
        c_str = input("Enter number of columns: ").strip()
        if r_str.isdigit() and c_str.isdigit() and int(r_str) > 0 and int(c_str) > 0:
            return (int(r_str), int(c_str))
    elif dim_choice == '3':
        d_str = input("Enter depth: ").strip()
        r_str = input("Enter number of rows: ").strip()
        c_str = input("Enter number of columns: ").strip()
        if d_str.isdigit() and r_str.isdigit() and c_str.isdigit() and int(d_str) > 0 and int(r_str) > 0 and int(c_str) > 0:
            return (int(d_str), int(r_str), int(c_str))
            
    print("[-] Invalid dimensions specified.")
    return None


def create_array_workflow(analytics):
    shape = input_dimensions()
    if shape is None:
        return

    expected_size = 1
    for dim in shape:
        expected_size *= dim

    print(f"\nEnter exact {expected_size} numeric elements separated by spaces.")
    raw_val = input("Elements: ")
    elements = DataAnalytics.parse_float_input(raw_val)

    if len(elements) != expected_size:
        print(f"[-] Error: Received {len(elements)} items, but expected exactly {expected_size} items.")
        return

    arr = np.array(elements).reshape(shape)
    analytics.set_array(arr)
    print("\n[+] Array successfully created!")
    analytics.print_array_status()


    if arr.ndim >= 2:
        while True:
            print("\n--- Indexing & Slicing Sub-Menu ---")
            print("1. Indexing (Retrieve single value)")
            print("2. Slicing (Extract range)")
            print("3. Go Back")
            sub_choice = input("Enter choice (1-3): ").strip()

            if sub_choice == '1':
                if arr.ndim == 2:
                    r_str = input(f"Enter Row index (0 to {arr.shape[0]-1}): ").strip()
                    c_str = input(f"Enter Column index (0 to {arr.shape[1]-1}): ").strip()
                    if r_str.isdigit() and c_str.isdigit():
                        r, c = int(r_str), int(c_str)
                        if 0 <= r < arr.shape[0] and 0 <= c < arr.shape[1]:
                            print(f"\n[Result] Value at coordinate ({r}, {c}): {arr[r, c]}")
                        else:
                            print("[-] Out of bounds coordinate indices!")
                    else:
                        print("[-] Index values must be non-negative integers.")

                elif arr.ndim == 3:
                    d_str = input(f"Enter Depth index (0 to {arr.shape[0]-1}): ").strip()
                    r_str = input(f"Enter Row index (0 to {arr.shape[1]-1}): ").strip()
                    c_str = input(f"Enter Column index (0 to {arr.shape[2]-1}): ").strip()
                    if d_str.isdigit() and r_str.isdigit() and c_str.isdigit():
                        d, r, c = int(d_str), int(r_str), int(c_str)
                        if 0 <= d < arr.shape[0] and 0 <= r < arr.shape[1] and 0 <= c < arr.shape[2]:
                            print(f"\n[Result] Value at coordinate ({d}, {r}, {c}): {arr[d, r, c]}")
                        else:
                            print("[-] Out of bounds coordinate indices!")
                    else:
                        print("[-] Index values must be non-negative integers.")

            elif sub_choice == '2':
                if arr.ndim == 2:
                    print("Enter slice range for Rows (Format 'start:end' or leave blank for all):")
                    r_slice = input("Row slice: ").strip()
                    print("Enter slice range for Columns (Format 'start:end' or leave blank for all):")
                    c_slice = input("Column slice: ").strip()

                    r_start, r_end = 0, arr.shape[0]
                    c_start, c_end = 0, arr.shape[1]
                    valid_inputs = True

                    if ":" in r_slice:
                        parts = r_slice.split(":")
                        if parts[0].isdigit(): r_start = int(parts[0])
                        if parts[1].isdigit(): r_end = int(parts[1])
                    elif len(r_slice) > 0:
                        valid_inputs = False

                    if ":" in c_slice:
                        parts = c_slice.split(":")
                        if parts[0].isdigit(): c_start = int(parts[0])
                        if parts[1].isdigit(): c_end = int(parts[1])
                    elif len(c_slice) > 0:
                        valid_inputs = False

                    if valid_inputs:
                        sliced = arr[r_start:r_end, c_start:c_end]
                        print("\n[Result] Extracted Sub-Array Slice:")
                        print(sliced)
                    else:
                        print("[-] Invalid slice notation format.")

                elif arr.ndim == 3:
                    d_start, d_end = 0, arr.shape[0]
                    r_start, r_end = 0, arr.shape[1]
                    c_start, c_end = 0, arr.shape[2]
                    
                    d_slice = input("Depth slice (start:end): ").strip()
                    r_slice = input("Row slice (start:end): ").strip()
                    c_slice = input("Column slice (start:end): ").strip()

                    if ":" in d_slice:
                        parts = d_slice.split(":")
                        if parts[0].isdigit(): d_start = int(parts[0])
                        if parts[1].isdigit(): d_end = int(parts[1])
                    if ":" in r_slice:
                        parts = r_slice.split(":")
                        if parts[0].isdigit(): r_start = int(parts[0])
                        if parts[1].isdigit(): r_end = int(parts[1])
                    if ":" in c_slice:
                        parts = c_slice.split(":")
                        if parts[0].isdigit(): c_start = int(parts[0])
                        if parts[1].isdigit(): c_end = int(parts[1])

                    sliced = arr[d_start:d_end, r_start:r_end, c_start:c_end]
                    print("\n[Result] Extracted 3D Slice:")
                    print(sliced)

            elif sub_choice == '3':
                break
            else:
                print("[-] Invalid choice. Return to indexing sub-menu.")


def math_operations_workflow(analytics):
    arr = analytics.get_array()

    print("\n--- Advanced Mathematical Operations ---")
    print("1. Element-wise Addition")
    print("2. Element-wise Subtraction")
    print("3. Element-wise Multiplication")
    print("4. Element-wise Division")
    choice = input("Select Operation (1-4): ").strip()

    if choice not in ['1', '2', '3', '4']:
        print("[-] Invalid math operation selected.")
        return

    if choice in ['1', '2', '3', '4']:
        print(f"\nEnter a secondary matching array of shape {arr.shape}:")
        raw_input = input("Elements: ")
        sec_elements = DataAnalytics.parse_float_input(raw_input)

        if len(sec_elements) != arr.size:
            print(f"[-] Shape mismatch! Require exactly {arr.size} elements.")
            return

        second_arr = np.array(sec_elements).reshape(arr.shape)
        print("\nOriginal Array:")
        print(arr)
        print("Second Array:")
        print(second_arr)

        if choice == '1':
            res = arr + second_arr
            print("\n[Result] Element-wise Addition:")
        elif choice == '2':
            res = arr - second_arr
            print("\n[Result] Element-wise Subtraction:")
        elif choice == '3':
            res = arr * second_arr
            print("\n[Result] Element-wise Multiplication:")
        elif choice == '4':
            # Check for zero-division structural risks
            if 0.0 in second_arr:
                print("[-] Division by zero encountered in secondary array!")
                return
            res = arr / second_arr
            print("\n[Result] Element-wise Division:")
        print(res)


def combine_split_workflow(analytics):
    arr = analytics.get_array()

    print("\n--- Combine or Split Sub-Menu ---")
    print("1. Combine Arrays (Concatenate)")
    print("2. Split Array")
    choice = input("Select choice (1-2): ").strip()

    if choice == '1':
        print(f"\nEnter an identical secondary array matching total elements ({arr.size}):")
        raw_input = input("Elements: ")
        sec_elements = DataAnalytics.parse_float_input(raw_input)

        if len(sec_elements) != arr.size:
            print(f"[-] Dimension Error: Received {len(sec_elements)} elements, expected {arr.size}.")
            return

        second_arr = np.array(sec_elements).reshape(arr.shape)

        axis_input = input(f"Enter Axis along which to concatenate (0 to {arr.ndim-1}): ").strip()
        if axis_input.isdigit():
            axis = int(axis_input)
            if 0 <= axis < arr.ndim:
                res = np.concatenate((arr, second_arr), axis=axis)
                print("\nOriginal Array:")
                print(arr)
                print("Second Array:")
                print(second_arr)
                print(f"\n[Result] Combined Array along Axis {axis}:")
                print(res)
            else:
                print("[-] Invalid concatenation axis provided.")
        else:
            print("[-] Axis must be an integer.")

    elif choice == '2':
        axis_input = input(f"Enter Axis to split along (0 to {arr.ndim-1}): ").strip()
        if not axis_input.isdigit():
            print("[-] Axis must be an integer.")
            return

        axis = int(axis_input)
        if axis < 0 or axis >= arr.ndim:
            print("[-] Specified axis out of matrix range bounds.")
            return

        axis_dim_size = arr.shape[axis]
        print(f"Dimension length along Axis {axis} is {axis_dim_size}.")
        parts_str = input("Enter number of equal sub-arrays to split into: ").strip()

        if parts_str.isdigit() and int(parts_str) > 0:
            num_parts = int(parts_str)

            if axis_dim_size % num_parts == 0:
                splits = np.split(arr, num_parts, axis=axis)
                print("\nOriginal Array:")
                print(arr)
                print(f"\n[Result] Split Array into {num_parts} sub-arrays:")
                for idx, sub_arr in enumerate(splits):
                    print(f"-- Part {idx+1} --")
                    print(sub_arr)
            else:
                print(f"[-] Invalid split! Length {axis_dim_size} is not divisible into {num_parts} equal parts.")
        else:
            print("[-] Sub-array part count must be a positive integer.")


def search_sort_filter_workflow(analytics):
    arr = analytics.get_array()

    print("\n--- Search, Sort, or Filter ---")
    print("1. Search Target Value")
    print("2. Sort Array")
    print("3. Filter Array with Boolean Mask")
    choice = input("Select option (1-3): ").strip()

    if choice == '1':
        target_str = input("Enter target numeric value to find: ").strip()
        parsed_target = DataAnalytics.parse_float_input(target_str)

        if len(parsed_target) == 1:
            target = parsed_target[0]
            indices = np.argwhere(arr == target)

            print("\nOriginal Array:")
            print(arr)
            if indices.size > 0:
                print(f"\n[Result] Found value {target} at matching coordinate index matrix:")
                print(indices)
            else:
                print(f"\n[Result] Value {target} was NOT found in active matrix.")
        else:
            print("[-] Please provide a valid single numeric target.")

    elif choice == '2':
        print("\nSelect Sort Strategy:")
        print("1. Ascending")
        print("2. Descending")
        sort_dir = input("Choice (1-2): ").strip()

        if sort_dir in ['1', '2']:
            is_descending = (sort_dir == '2')
            
            print("\nOriginal Array:")
            print(arr)
            
            if arr.ndim == 1:
                sorted_arr = np.sort(arr)
                if is_descending:
                    sorted_arr = sorted_arr[::-1]
            else:
                # Row-wise matrix sorting
                sorted_arr = np.sort(arr, axis=-1)
                if is_descending:
                    sorted_arr = np.flip(sorted_arr, axis=-1)

            order_lbl = "Descending" if is_descending else "Ascending"
            print(f"\n[Result] Sorted Array ({order_lbl}):")
            print(sorted_arr)
        else:
            print("[-] Invalid sort direction option.")

    elif choice == '3':
        print("\nSupported Operators: >, <, >=, <=, ==")
        op = input("Enter relational operator: ").strip()
        val_str = input("Enter numeric threshold value: ").strip()
        parsed_val = DataAnalytics.parse_float_input(val_str)

        if len(parsed_val) == 1 and op in ['>', '<', '>=', '<=', '==']:
            thresh = parsed_val[0]

            if op == '>':
                mask = arr > thresh
            elif op == '<':
                mask = arr < thresh
            elif op == '>=':
                mask = arr >= thresh
            elif op == '<=':
                mask = arr <= thresh
            elif op == '==':
                mask = arr == thresh

            filtered_elements = arr[mask]

            print("\nOriginal Array:")
            print(arr)
            print("\n[Result] Generated Boolean Mask:")
            print(mask)
            print(f"\n[Result] Filtered Elements satisfying (x {op} {thresh}):")
            print(filtered_elements)
        else:
            print("[-] Invalid operator or numeric threshold value provided.")


def stats_aggregating_workflow(analytics):
    arr = analytics.get_array()

    print("\n=============================================")
    print("      STATISTICAL & AGGREGATE DASHBOARD      ")
    print("=============================================")
    print("Original Active Array:")
    print(arr)
    print("---------------------------------------------")

    # Aggregate Metrics
    total_sum = np.sum(arr)
    arithmetic_mean = np.mean(arr)
    median_val = np.median(arr)
    std_dev = np.std(arr)
    variance_val = np.var(arr)
    min_val = np.min(arr)
    max_val = np.max(arr)

    print(f"Total Sum           : {total_sum}")
    print(f"Arithmetic Mean     : {arithmetic_mean:.4f}")
    print(f"Median              : {median_val:.4f}")
    print(f"Standard Deviation  : {std_dev:.4f}")
    print(f"Variance            : {variance_val:.4f}")
    print(f"Absolute Minimum    : {min_val}")
    print(f"Absolute Maximum    : {max_val}")
    print("---------------------------------------------")

    # Percentile Calculation
    p_str = input("\nEnter Percentile rank to compute (0 - 100): ").strip()
    p_parsed = DataAnalytics.parse_float_input(p_str)
    if len(p_parsed) == 1 and 0.0 <= p_parsed[0] <= 100.0:
        p_val = p_parsed[0]
        perc_res = np.percentile(arr, p_val)
        print(f"[Result] {p_val}th Percentile: {perc_res:.4f}")
    else:
        print("[-] Invalid percentile value! Skipping percentile computation.")

    # Correlation Matrix
    print(f"\nTo compute Correlation Matrix, enter a secondary dataset of matching size ({arr.size}):")
    corr_input = input("Secondary Dataset Elements: ").strip()
    corr_elements = DataAnalytics.parse_float_input(corr_input)

    if len(corr_elements) == arr.size:
        sec_flat = np.array(corr_elements)
        primary_flat = arr.flatten()
        corr_matrix = np.corrcoef(primary_flat, sec_flat)

        print("\n[Result] Canonical Correlation Matrix:")
        print(corr_matrix)
    else:
        print(f"[-] Secondary dataset length ({len(corr_elements)}) does not match primary array size ({arr.size}). Skipping correlation.")


def main():
    analytics = DataAnalytics()

    while True:
        display_main_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            create_array_workflow(analytics)

        elif choice in ['2', '3', '4', '5']:
            # Predictive validation enforcing array initialization before module execution
            if analytics.get_array() is None:
                print("\n[!] Warning: No array created yet! Please choose Option 1 to create an active NumPy array first.")
            else:
                if choice == '2':
                    math_operations_workflow(analytics)
                elif choice == '3':
                    combine_split_workflow(analytics)
                elif choice == '4':
                    search_sort_filter_workflow(analytics)
                elif choice == '5':
                    stats_aggregating_workflow(analytics)

        elif choice == '6':
            print(f"\nThank you for using NumPy Analyzer! Total active sessions logged: {DataAnalytics.get_total_sessions()}")
            print("Exiting application...")
            break

        else:
            print("[-] Invalid main menu choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
