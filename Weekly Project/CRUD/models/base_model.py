class BaseModel:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def create(self):
        # kode untuk menambahkan data ke database
        pass

    def read(self, id=None):
        # kode untuk mengambil data dari database
        pass

    def update(self, id, name):
        # kode untuk mengupdate data di database
        pass

    def delete(self, id):
        # kode untuk menghapus data dari database
        pass
