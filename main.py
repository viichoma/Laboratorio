import os
import shutil

# Caminho para o diretório principal
main_dir = r'D:\Laboratorio\Machine_gun'  # Ajuste para o seu diretório
dest_dir = os.path.join(main_dir, 'imagens_sem_txt')  # Diretório de destino

# Cria o diretório de destino, se não existir
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# Extensões de arquivos de imagem (pode ajustar conforme necessário)
image_extensions = ['.jpg', '.jpeg', '.png']

# Percorre cada pasta dentro do diretório principal
for root, dirs, files in os.walk(main_dir):
    for file in files:
        # Verifica se é um arquivo de imagem
        if any(file.lower().endswith(ext) for ext in image_extensions):
            # Nome do arquivo sem a extensão
            file_name = os.path.splitext(file)[0]
            
            # Verifica se existe um arquivo .txt com o mesmo nome
            txt_file = file_name + '.txt'
            if txt_file not in files:
                # Cria a mesma estrutura de diretórios dentro do destino
                relative_path = os.path.relpath(root, main_dir)
                dest_sub_dir = os.path.join(dest_dir, relative_path)
                if not os.path.exists(dest_sub_dir):
                    os.makedirs(dest_sub_dir)
                
                # Move a imagem para o novo diretório
                source_file = os.path.join(root, file)
                dest_file = os.path.join(dest_sub_dir, file)
                shutil.move(source_file, dest_file)
                print(f'Movido: {source_file} -> {dest_file}')
