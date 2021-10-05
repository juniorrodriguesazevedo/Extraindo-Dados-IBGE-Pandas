import pandas as pd
from generate_csv import GenerateCSV

csv = GenerateCSV()

def main():
    uf = input('Digite o UF do estado: ').upper().strip()
    data = csv.get_state(uf)
    csv.export_csv(data, uf)

if __name__ == '__main__':
    main()