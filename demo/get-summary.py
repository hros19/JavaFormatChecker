import xml.etree.ElementTree as ET
import sys
from collections import defaultdict

def parse_checkstyle_results(input_file):
    tree = ET.parse(input_file)
    root = tree.getroot()
    
    error_counts = defaultdict(int)
    for error in root.findall('.//error'):
        error_type = error.get('source')
        error_counts[error_type] += 1
    
    return error_counts

def write_summary(error_counts, output_file):
    with open(output_file, 'w') as f:
        f.write("Resumen de errores y warnings de Checkstyle:\n\n")
        for error_type, count in error_counts.items():
            f.write(f"{error_type}: {count}\n")
        f.write(f"\nTotal de tipos de errores/warnings distintos: {len(error_counts)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script.py <archivo_entrada.xml> <archivo_salida.txt>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    error_counts = parse_checkstyle_results(input_file)
    write_summary(error_counts, output_file)

    print(f"Resumen generado en {output_file}")