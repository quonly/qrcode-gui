from barcode.codex import Code128
from barcode.writer import SVGWriter
import csv
import os

BARCODE_SCALE = 3

if not os.path.exists('gen_svg'):
    os.makedirs('gen_svg')


def generate_barcode_svg(code):
    barcode_svg = Code128(code, writer=SVGWriter())
    return barcode_svg.render()


with open('products.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        svg_name = row['code']
        product_string = row['code'] + ' : ' + row['name']
        barcode_svg = generate_barcode_svg(product_string)
        with open(f'gen_svg/{svg_name}.svg', 'w') as f:
            f.write(barcode_svg.decode('utf-8'))