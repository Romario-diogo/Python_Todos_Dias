vendas = [
    {"data": "2025-01-01", "produto": "Arroz 5kg", "quantidade": 3, "preco_unit": 28.90},
    {"data": "2025-01-01", "produto": "Feijão 1kg", "quantidade": 5, "preco_unit": 8.90},
    {"data": "2025-01-01", "produto": "Café 500g", "quantidade": 2, "preco_unit": 16.90},

    {"data": "2025-01-02", "produto": "Detergente 500ml", "quantidade": 6, "preco_unit": 3.99},
    {"data": "2025-01-02", "produto": "Papel higiênico 12un", "quantidade": 2, "preco_unit": 19.90},
    {"data": "2025-01-02", "produto": "Leite UHT 1L", "quantidade": 12, "preco_unit": 5.49},

    {"data": "2025-01-03", "produto": "Camiseta básica", "quantidade": 4, "preco_unit": 49.90},
    {"data": "2025-01-03", "produto": "Calça jeans", "quantidade": 2, "preco_unit": 129.90},

    {"data": "2025-01-04", "produto": "Tênis casual", "quantidade": 1, "preco_unit": 199.90},
    {"data": "2025-01-04", "produto": "Meias esportivas", "quantidade": 5, "preco_unit": 12.90},

    {"data": "2025-01-05", "produto": "Smartphone Android 128GB", "quantidade": 1, "preco_unit": 1699.90},
    {"data": "2025-01-05", "produto": "Fone Bluetooth", "quantidade": 2, "preco_unit": 149.90},

    {"data": "2025-01-06", "produto": "Notebook i5", "quantidade": 1, "preco_unit": 3899.00},
    {"data": "2025-01-06", "produto": "Mouse sem fio", "quantidade": 3, "preco_unit": 79.90},

    {"data": "2025-01-07", "produto": "Panela antiaderente", "quantidade": 2, "preco_unit": 99.90},
    {"data": "2025-01-07", "produto": "Air Fryer 4L", "quantidade": 1, "preco_unit": 399.90},

    {"data": "2025-01-08", "produto": "Shampoo 400ml", "quantidade": 6, "preco_unit": 24.90},
    {"data": "2025-01-08", "produto": "Creme hidratante", "quantidade": 4, "preco_unit": 34.90},

    {"data": "2025-01-09", "produto": "Perfume 100ml", "quantidade": 2, "preco_unit": 129.90},
    {"data": "2025-01-09", "produto": "Escova secadora", "quantidade": 1, "preco_unit": 219.90},

    {"data": "2025-01-10", "produto": "Ração cão 10kg", "quantidade": 2, "preco_unit": 149.90},
    {"data": "2025-01-10", "produto": "Brinquedo pet", "quantidade": 3, "preco_unit": 19.90},

    {"data": "2025-01-11", "produto": "Bola de futebol", "quantidade": 2, "preco_unit": 89.90},
    {"data": "2025-01-11", "produto": "Corda de pular", "quantidade": 4, "preco_unit": 29.90},

    {"data": "2025-01-12", "produto": "Caderno universitário", "quantidade": 6, "preco_unit": 29.90},
    {"data": "2025-01-12", "produto": "Caneta kit 10", "quantidade": 5, "preco_unit": 14.90},

    {"data": "2025-01-13", "produto": "Óleo 5W30", "quantidade": 3, "preco_unit": 39.90},
    {"data": "2025-01-13", "produto": "Palheta limpador", "quantidade": 2, "preco_unit": 59.90},

    {"data": "2025-01-14", "produto": "Carregador veicular", "quantidade": 4, "preco_unit": 29.90},
    {"data": "2025-01-14", "produto": "Smart TV 50\"", "quantidade": 1, "preco_unit": 2499.00},

    {"data": "2025-01-15", "produto": "Caixa de som portátil", "quantidade": 2, "preco_unit": 199.90},
    {"data": "2025-01-15", "produto": "Smartwatch", "quantidade": 2, "preco_unit": 299.90},
]

dia_anterio = "0"

for d in vendas:
    if dia_anterio == "0":
        dia_anterio = d["data"][-2:]

    if dia_anterio == d["data"][-2:]:
        print(dia_anterio)
        
    if dia_anterio != d["data"][-2:]:
        break        

