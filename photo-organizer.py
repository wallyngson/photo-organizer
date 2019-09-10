import os
import shutil
from PIL import Image
from datetime import datetime

# Photo Organized
# Develope with Python 3.6

class PhotoOrganizer :
    extensions = ['JPEG', 'jpeg', 'JPG', 'jpg', 'PNG', 'png']
    
    # captura o nome da pasta...
    def name_folder(self, file) :
        date = self.photo_shooting_date(file)
        return date.strftime('%Y') + '/' + date.strftime('%Y-%m-%d')
    
    # capta as datas e as horas das imagens para poder organizar por pastas...
    def photo_shooting_date(self, file) :
        photo = Image.open(file)
        info = photo._getexif()

        if 36867 in info:
            # 36867 código onde aparece onde a foto foi tirada...
            date = info[36867]
            date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
    
        else: 
            date = datetime.fromtimestamp(os.path.getmtime(file))

        return date

    # função para mover as fotos para as pastas...
    def move_photo(self, file) :
        new_folder = self.name_folder(file)
    
        # se a pasta ainda não existe com o nome...
        # criando pasta...
        if not os.path.exists(new_folder) :
            os.makedirs(new_folder)
    
        # mover o aquivo para a nova pasta...
        shutil.move(file, new_folder + '/' + file)

    def organize(self) :
        photo = [
            filename for filename in os.listdir('.') if any(filename.endswith(ext) for ext in self.extensions)
        ]

        for filename in photo :
            self.move_photo(filename)

PO = PhotoOrganizer()
PO.organize()
    