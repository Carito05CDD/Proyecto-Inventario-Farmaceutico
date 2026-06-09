import pandas as pd
import sqlite3

archivo_csv = "global_test_set.csv"
base_datos = "farmacia.db"
tabla = "ventas_farmaceuticas"

df = pd.read_csv(archivo_csv, sep=";")
df["addeddate"] = pd.to_datetime(df["addeddate"])

conexion = sqlite3.connect(base_datos)

df.to_sql(tabla, conexion, if_exists="replace", index=False)

consulta = """
SELECT name, SUM(Sales_Sheet) AS total_ventas
FROM ventas_farmaceuticas
GROUP BY name
ORDER BY total_ventas DESC
LIMIT 10;
"""

resultado = pd.read_sql_query(consulta, conexion)

print("Base de datos creada correctamente.")
print("Tabla creada:", tabla)
print("Registros cargados:", len(df))
print("\nTop 10 productos por volumen de ventas:")
print(resultado)

conexion.close()
