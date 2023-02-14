from models.base_model import BaseModel

class Product(BaseModel):
    def __init__(self, id, name, price):
        super().__init__(id, name)
        self.price = price

    def create(self):
        # kode untuk menambahkan data produk ke database
        pass

    def read(self, id=None):
        # kode untuk mengambil data produk dari database
        pass

    def update(self, id, name, price):
        # kode untuk mengupdate data produk di database
        pass

    def delete(self, id):
        # kode untuk menghapus data produk dari database
        pass
