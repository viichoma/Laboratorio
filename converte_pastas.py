import os

def rename_files_to_folder_name(directory_path):
    # Lista todas as pastas no diretório
    folders = [f for f in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, f))]
    
    for folder in folders:
        folder_path = os.path.join(directory_path, folder)
        
        # Lista todos os arquivos na pasta
        files = os.listdir(folder_path)
        
        for file in files:
            file_path = os.path.join(folder_path, file)
            file_extension = os.path.splitext(file)[1]  # Obtém a extensão do arquivo
            
            # Define o novo nome usando o nome da pasta
            new_file_name = f"{folder}{file_extension}"
            new_file_path = os.path.join(folder_path, new_file_name)
            
            # Renomeia o arquivo
            os.rename(file_path, new_file_path)
            
            print(f"Renomeado: {file_path} para {new_file_path}")

# Exemplo de uso
directory = "D:\\ArquivosYOLOv10\\Dataset\\No_Gun"  # Substitua pelo caminho do seu diretório
rename_files_to_folder_name(directory)
