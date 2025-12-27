import pandas as pd
import openpyxl
import os


class ExcelService:

    def read_excel(self, file_path: str) -> pd.DataFrame:
        return pd.read_excel(file_path)

    def add_record(self, file_path: str, record: dict, sheet_name: str = "Sheet1"):
        """
        Agrega un registro (fila) a un archivo Excel validando columnas.
        - Si el archivo no existe, lo crea con las columnas del registro.
        - Si existe, valida que las columnas del registro existan en el Excel.
        """

        # --- Caso 1: el archivo NO existe ---
        if not os.path.exists(file_path):
            df = pd.DataFrame([record])
            df.to_excel(file_path, index=False, sheet_name=sheet_name)
            return

        # --- Caso 2: el archivo existe ---
        df = pd.read_excel(file_path, sheet_name=sheet_name)

        columnas_excel = set(df.columns)
        columnas_registro = set(record.keys())

        columnas_invalidas = columnas_registro - columnas_excel
        if columnas_invalidas:
            raise ValueError(
                f"Columnas no existentes en el Excel: {columnas_invalidas}"
            )

        # Agregar el registro
        new_row = pd.DataFrame([record])
        df = pd.concat([df, new_row], ignore_index=True)

        # Guardar cambios
        df.to_excel(file_path, index=False, sheet_name=sheet_name)
