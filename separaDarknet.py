import os
import json

# Função para converter anotações COCO para formato YOLO
def coco_to_yolo(coco_annotation, img_width, img_height):
    x, y, w, h = coco_annotation['bbox']
    # Normalizar coordenadas
    x_center = (x + w / 2) / img_width
    y_center = (y + h / 2) / img_height
    w = w / img_width
    h = h / img_height
    
    # Retornar no formato YOLO (class_id, x_center, y_center, width, height)
    return f"{coco_annotation['category_id']} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}"

# Caminho base do diretório
base_dir = r'D:\Laboratorio\Machine_gun'

# Percorrer todas as pastas e arquivos no diretório
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".json"):
            json_path = os.path.join(root, file)
            
            # Abrir e ler o arquivo JSON
            with open(json_path, 'r') as f:
                data = json.load(f)
            
            # Assumindo que as informações de largura e altura da imagem estão em 'images'
            images_info = {img['id']: (img['width'], img['height'], img['file_name']) for img in data['images']}
            
            # Processar as anotações
            for annotation in data['annotations']:
                img_id = annotation['image_id']
                width, height, img_name = images_info[img_id]
                
                # Converter a anotação para o formato YOLO
                yolo_annotation = coco_to_yolo(annotation, width, height)
                
                # Nome da pasta (exemplo PAH1_C1_P1_V1_HB_3)
                folder_name = os.path.basename(root)
                
                # Gerar o nome do arquivo no formato desejado
                output_txt_name = f"{folder_name}_frame_{img_id:04d}.txt"
                output_txt_path = os.path.join(root, output_txt_name)
                
                # Escrever a anotação no arquivo
                with open(output_txt_path, 'a') as out_f:
                    out_f.write(yolo_annotation + "\n")

print("Conversão concluída!")
