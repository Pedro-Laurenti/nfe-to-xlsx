import xml.etree.ElementTree as ET
import pandas as pd
import os
from tqdm import tqdm

def simplify_tag(tag):
    parts = tag.split("}")[-1]
    return parts

def process_element(element, parent_path, data, current_tags):
    tag = element.tag
    content = element.text.strip() if element.text else ''
    path = f"{parent_path}/{tag}"

    simplified_tag = simplify_tag(tag)
    parent_name = parent_path.split("/")[-1].replace("}", "_").replace("{", "_").replace(":", "_")
    current_tags.append(simplified_tag)
    
    if parent_name:
        simplified_tag = f"{parent_name}_{simplified_tag}"

    data[simplified_tag] = content

    for child in element:
        process_element(child, path, data, current_tags)
    
    current_tags.pop()
    
# Pasta que contém os arquivos XML
xml_folder = "xml2"

# Lista para armazenar os DataFrames de cada arquivo
dfs = []

# Função para ajustar valores decimais na DataFrame
def adjust_decimal_values(value):
    if isinstance(value, str) and "." in value:
        try:
            return float(value)
        except ValueError:
            return value
    return value

# Processar em lotes de 100 arquivos
batch_size = 100
xml_files = [os.path.join(xml_folder, filename) for filename in os.listdir(xml_folder) if filename.endswith(".xml")]

# Função para limpar a tela do prompt no Windows
def limpar_tela_windows():
    os.system('@echo off')  # Desativa a exibição dos comandos
    os.system('cls')  # Limpa a tela

# Função para limpar a tela do prompt no Linux
def limpar_tela_linux():
    os.system('clear')

# Determinar o sistema operacional e chamar a função apropriada
def limpar_tela():
    if os.name == 'nt':  # Verificar se é Windows
        limpar_tela_windows()
    else:
        limpar_tela_linux()

# Limpar a tela antes de exibir a barra de progresso
limpar_tela()

# Inicializar a barra de progresso
print()  # Esta linha imprime uma linha em branco
with tqdm(total=len(xml_files), desc="XML / XLSX") as pbar:
    for i in range(0, len(xml_files), batch_size):
        batch_files = xml_files[i:i+batch_size]
        batch_dfs = []

        for xml_file in batch_files:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            
            data = {}  # Dicionário para armazenar os dados
            current_tags = []
            
            process_element(root, "", data, current_tags)
            
            # Criar o DataFrame a partir dos dados
            df = pd.DataFrame([data])
            
            # Ajustar valores decimais na DataFrame
            for column in df.columns:
                df[column] = df[column].apply(adjust_decimal_values)
            
            batch_dfs.append(df)
        
        # Concatenar DataFrames do lote atual
        batch_df = pd.concat(batch_dfs, ignore_index=True)
        dfs.append(batch_df)
        
        # Atualizar a barra de progresso
        pbar.update(len(batch_files))

# Concatenar todos os DataFrames em um único DataFrame final
final_df = pd.concat(dfs, ignore_index=True)

# Salvar o DataFrame final como um arquivo Excel
output_file = "output.xlsx"
final_df.to_excel(output_file, index=False)
print()
print("Planilha gerada com sucesso!")
print()
