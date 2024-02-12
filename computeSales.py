"""
This script computes the total cost of sales from a sales record file,
using prices specified in a product list file. It outputs the result to
both the console and a file named SalesResults.txt, including the execution time.
"""

import argparse
import json
import time


def load_json_file(filename):
    """Load JSON data from a file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    except PermissionError:
        print(f"Error: No permission to read the file {filename}.")
    except json.JSONDecodeError:
        print(f"Error: File {filename} contains invalid JSON.")
    except Exception as exception:
        raise exception
    return None


def compute_total_sales(product_list, sales_records):
    """Compute the total cost of all sales."""
    total_cost = 0
    price_lookup = {item['title']: item['price'] for item in product_list}
    for sale in sales_records:
        product_name = sale['Product']
        quantity = sale['Quantity']
        if product_name in price_lookup:
            total_cost += price_lookup[product_name] * quantity
        else:
            print(f"Warning: Product {product_name} not found in product list.")
    return total_cost


def write_results_to_file(filename, total_cost, elapsed_time):
    """Write the results to a file."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"Total Sales Cost: ${total_cost:.2f}\n")
        file.write(f"Time Elapsed: {elapsed_time:.2f} seconds\n")


def main(args_):
    """Run the script with provided arguments."""
    start_time = time.time()

    product_list = load_json_file(args_.product_list)
    sales_records = load_json_file(args_.sales_record)

    if product_list is None or sales_records is None:
        return

    total_cost = compute_total_sales(product_list, sales_records)

    elapsed_time = time.time() - start_time

    print(f"Total Sales Cost: ${total_cost:.2f}")
    print(f"Time Elapsed: {elapsed_time:.2f} seconds")

    write_results_to_file("SalesResults.txt", total_cost, elapsed_time)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Compute the total sales from sales records using a product list.'
    )
    parser.add_argument(
        'product_list', help='Filename of the product list JSON file'
    )
    parser.add_argument(
        'sales_record', help='Filename of the sales record JSON file'
    )
    args = parser.parse_args()

    main(args)
