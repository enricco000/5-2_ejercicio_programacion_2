"""
This script computes the total cost of sales from a sales record file, using prices specified in a price catalogue file.
It outputs the result to both the console and a file named SalesResults.txt, including the execution time.
"""

import argparse
import json
import time

def load_json_file(filename):
    """Load JSON data from a file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading file {filename}: {e}")
        return None

def compute_total_sales(price_catalogue, sales_record):
    """Compute the total cost of all sales."""
    total_cost = 0
    for sale in sales_record:
        item_id = sale['item_id']
        quantity = sale['quantity']
        if item_id in price_catalogue:
            total_cost += price_catalogue[item_id] * quantity
        else:
            print(f"Warning: Item ID {item_id} not found in price catalogue.")
    return total_cost

def write_results_to_file(filename, total_cost, elapsed_time):
    """Write the results to a file."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"Total Sales Cost: ${total_cost:.2f}\n")
        file.write(f"Time Elapsed: {elapsed_time:.2f} seconds\n")

def main(args):
    start_time = time.time()

    price_catalogue = load_json_file(args.price_catalogue)
    sales_record = load_json_file(args.sales_record)

    if price_catalogue is None or sales_record is None:
        return

    total_cost = compute_total_sales(price_catalogue, sales_record)

    elapsed_time = time.time() - start_time

    print(f"Total Sales Cost: ${total_cost:.2f}")
    print(f"Time Elapsed: {elapsed_time:.2f} seconds")

    write_results_to_file("SalesResults.txt", total_cost, elapsed_time)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compute the total sales cost from sales records using a price catalogue.')
    parser.add_argument('price_catalogue', help='Filename of the price catalogue JSON file')
    parser.add_argument('sales_record', help='Filename of the sales record JSON file')
    args = parser.parse_args()

    main(args)
