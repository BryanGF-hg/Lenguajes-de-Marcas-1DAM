import pandas as pd

diccionario = [{'ID': 1, 'Nombre': 'Ana', 'Apellidos': 'López García', 'Email': 'ana.lopez@example.com', 'Teléfono': 600123123, 'Dirección': 'Calle Mayor 12', 'Ciudad': 'Valencia', 'País': 'España'}, {'ID': 2, 'Nombre': 'Carlos', 'Apellidos': 'Pérez Ruiz', 'Email': 'carlos.perez@example.com', 'Teléfono': 611222333, 'Dirección': 'Av. Libertad 45', 'Ciudad': 'Madrid', 'País': 'España'}, {'ID': 3, 'Nombre': 'María', 'Apellidos': 'Santos Díaz', 'Email': 'maria.santos@example.com', 'Teléfono': 644555777, 'Dirección': 'C/ Río Turia 8', 'Ciudad': 'Sevilla', 'País': 'España'}, {'ID': 4, 'Nombre': 'Javier', 'Apellidos': 'Molina Torres', 'Email': 'javier.molina@example.com', 'Teléfono': 699888777, 'Dirección': 'Plaza Central 3', 'Ciudad': 'Barcelona', 'País': 'España'}]


# Convertir a DataFrame
df = pd.DataFrame(diccionario)

# Exportar a Excel
df.to_excel("noticias.xlsx", index=False)

print("Archivo creado: noticias.xlsx")
