# database untuk menyimpan data
data = []


def create_data(name, age):
    data.append({"name": name, "age": age})
    print("Data berhasil ditambahkan")


def read_data():
    if data:
        for i, d in enumerate(data):
            print(f"Data ke-{i}:", d)
    else:
        print("Tidak ada data")


def update_data(index, name, age):
    try:
        data[index].update({"name": name, "age": age})
        print("Data berhasil diperbaharui")
    except IndexError:
        print("Index data tidak ditemukan")


def delete_data(index):
    try:
        data.pop(index)
        print("Data berhasil dihapus")
    except IndexError:
        print("Index data tidak ditemukan")


def main():
    while True:
        print("\n--- CRUD Data ---")
        print("1. Tambah data")
        print("2. Tampilkan data")
        print("3. Perbaharui data")
        print("4. Hapus data")
        print("5. Keluar")

        choice = int(input("Pilih menu (1-5): "))

        if choice == 1:
            name = input("Masukkan nama: ")
            age = int(input("Masukkan usia: "))
            create_data(name, age)
        elif choice == 2:
            read_data()
        elif choice == 3:
            index = int(input("Masukkan index data: "))
            name = input("Masukkan nama: ")
            age = int(input("Masukkan usia: "))
            update_data(index, name, age)
        elif choice == 4:
            index = int(input("Masukkan index data: "))
            delete_data(index)
        elif choice == 5:
            break
        else:
            print("Menu tidak ditemukan")


if __name__ == "__main__":
    main()
