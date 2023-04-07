import re
import csv
from collections import defaultdict

def read_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def sum_amounts(content):
    gesamtbetrag_pattern = r"(?:Gesamtbetrag|Total amount) (?:CHF|EUR) (\d+)(?:\.\d+)?(?:.–)?"
    amounts = re.findall(gesamtbetrag_pattern, content)
    total = sum(float(amount) for amount in amounts if float(amount) != 0)
    return total

def list_products(content):
    order_pattern = r"(Bestellung(?:.|\n)+?)(?:(?=Bestellung)|$)"
    orders = re.findall(order_pattern, content)
    product_pattern = r"(\d+)×\n(.+)"
    product_dict = defaultdict(lambda: {'quantity': 0, 'total_price': 0.0, 'dates': []})
    product_id = 0

    for order in orders:
        amount = re.search(r"(?:Gesamtbetrag|Total amount) (?:CHF|EUR) (\d+)(?:\.\d+)?(?:.–)?", order)
        date = re.search(r"Bestellung \d+ vom ([\d.]+)", order)
        if amount and date:
            total_price = float(amount.group(1))
            order_date = date.group(1)
            products = re.findall(product_pattern, order)
            num_products = sum(int(product[0]) for product in products)
            if num_products > 0 and total_price != 0:
                price_per_product = total_price / num_products
                for product in products:
                    quantity, name = product
                    unique_name = f"{name.strip()}_{product_id}"
                    product_dict[unique_name]['quantity'] += int(quantity)
                    product_dict[unique_name]['total_price'] += int(quantity) * price_per_product
                    product_dict[unique_name]['dates'].append(order_date)
                    product_id += 1

    return product_dict

def export_to_csv(products, file_path):
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Kategorie', 'Name', 'Menge', 'Gesamtpreis', 'Datum'])
        for unique_name, product_info in products:
            name = unique_name.rsplit('_', 1)[0]
            category, *rest_name = name.split(' ', 1)
            rest_name = ' '.join(rest_name)
            quantity = product_info['quantity']
            total_price = product_info['total_price']
            dates = ', '.join(product_info['dates'])
            csv_writer.writerow([category, rest_name, quantity, f"CHF {total_price:.2f}", dates])

def main():
    file_path = "beträge.txt" # Ändern Sie den Dateipfad entsprechend
    content = read_txt_file(file_path)

    total_amount = sum_amounts(content)
    print(f"Die Gesamtsumme beträgt: CHF {total_amount:.2f}\n")

    print("Produkte, Mengen, Gesamtpreise und Datum:")
    products = list_products(content)
    sorted_products = sorted(products.items(), key=lambda x: (-x[1]['quantity'], x[0]))
    for unique_name, product_info in sorted_products:
        name = unique_name.rsplit('_', 1)[0]
        quantity = product_info['quantity']
        total_price = product_info['total_price']
        dates = ', '.join(product_info['dates'])
        print(f"{quantity}× {name} (Gesamtpreis: CHF {total_price:.2f}, Datum: {dates})")

    csv_file_path = "export.csv" # Ändern Sie den Dateipfad entsprechend
    export_to_csv(sorted_products, csv_file_path)
    print(f"\nDaten wurden in die CSV-Datei {csv_file_path} exportiert.")

if __name__ == "__main__":
    main()