# XML to Excel Processing

This Python code converts XML files into an Excel spreadsheet. It utilizes the `xml.etree.ElementTree`, `pandas`, and `tqdm` libraries. The code is designed to process XML files in batches, creating DataFrames and consolidating them into a single Excel sheet.

## Usage

1. Make sure you have the following libraries installed:

```cmd
pip install xml.etree.ElementTree
pip install pandas
pip install tqdm

```

3. Place your XML files in the "xml2" folder.

4. Run the Python script.

The code will process XML files in the "xml2" folder, generate individual DataFrames for each file, and merge them into a single DataFrame. This resulting DataFrame will be saved as an Excel file named "output.xlsx."

## Key Functions

### `simplify_tag(tag)`

This function simplifies an XML tag by removing namespaces and special characters, making it suitable as a column name.

### `process_element(element, parent_path, data, current_tags)`

This recursive function processes an XML element, extracts its content, and builds a data dictionary used to create a DataFrame.

### `adjust_decimal_values(value)`

This function checks if a value is a string containing a decimal number and, if so, converts it to a float. This ensures proper handling of decimal numbers.

### Screen Clearing

The code includes functions `limpar_tela_windows()` and `limpar_tela_linux()` to clear the command prompt screen on Windows and Linux, respectively. The `limpar_tela()` function determines the operating system and calls the appropriate function to clear the screen before displaying the progress bar.

### Batch Processing

The code processes XML files in batches of 100 for efficient handling of large datasets.

## Output

The final result is an Excel file named "output.xlsx," containing consolidated data from the processed XML files.

**Note**: Customize batch settings (`batch_size`) and the XML file directory (`xml_folder`) as needed.


<details>
  <summary> Tradução PT-BR </summary>

# Processamento de XML para Excel

Este código Python converte arquivos XML em uma planilha Excel. Ele utiliza as bibliotecas `xml.etree.ElementTree`, `pandas` e `tqdm`. O código foi desenvolvido para processar arquivos XML em lotes, criar DataFrames e consolidá-los em uma única planilha do Excel.

## Uso

1. Certifique-se de ter as seguintes bibliotecas instaladas:

```cmd
pip install xml.etree.ElementTree
pip install pandas
pip install tqdm

```

2. Coloque seus arquivos XML na pasta "xml2".

3. Execute o script Python.

O código irá processar os arquivos XML na pasta "xml2", gerar DataFrames individuais para cada arquivo e mesclá-los em um único DataFrame. Este DataFrame final será salvo como um arquivo Excel chamado "output.xlsx".

## Funções Principais

### `simplify_tag(tag)`

Esta função simplifica uma etiqueta XML removendo namespaces e caracteres especiais, tornando-a adequada como nome de coluna.

### `process_element(element, parent_path, data, current_tags)`

Esta função recursiva processa um elemento XML, extrai seu conteúdo e cria um dicionário de dados usado para criar um DataFrame.

### `adjust_decimal_values(value)`

Esta função verifica se um valor é uma string contendo um número decimal e, se for, converte-o em um número de ponto flutuante. Isso garante o tratamento adequado de números decimais.

### Limpeza de Tela

O código inclui as funções `limpar_tela_windows()` e `limpar_tela_linux()` para limpar a tela do prompt de comando no Windows e no Linux, respectivamente. A função `limpar_tela()` determina o sistema operacional e chama a função apropriada para limpar a tela antes de exibir a barra de progresso.

### Processamento em Lotes

O código processa arquivos XML em lotes de 100 para lidar eficientemente com conjuntos de dados grandes.

## Saída

O resultado final é um arquivo Excel chamado "output.xlsx" que contém dados consolidados dos arquivos XML processados.

**Observação**: Personalize as configurações de lote (`batch_size`) e o diretório de arquivos XML (`xml_folder`) conforme necessário.

</details>
