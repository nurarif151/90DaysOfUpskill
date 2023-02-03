# database untuk menyimpan data

data = []

def creat_data(name, age):
    data.append({
        "name" : name,
        "age" : age
    })

    print("Data berhasil ditambahkan")

def read_data():
    if data:
        for i, d in enumerate(data):
            print(f"Data ke-{i}:", d)
    else:
        print("Data tidak ada")

def update_data(index, name, age):
    try:
        data[index].update({
            "name" : name,
            "age" : age
        })
        print("data berhasil di update")
    except IndexError:
        print("Maaf data pada index yang anda masukkan tidak ada")

def delete_data(index):
    try:
        date.pop(index)
        print("data berhasil dihapus")
    except IndexError:
        print("Index data tidak ditemukan")

def main():
    while True:
        print("\n-----Program CRUD Data-----")
        print("1. Tambah Data")
        print("2. Update Data")
        print("3. Tampilkan Data")
        print("4. Delete Data")
        print("5. Keluar")

        pilihan = int(input("pilij menu 1 - 5 yang anda perlukan : "))

        if pilihan == 1:
            name = input("Masukkan nama : ")
            age = int(input("Masukkan umur : "))
            creat_data(name, age)
        elif pilihan == 3:
            read_data()
        elif pilihan == 2:
            index = int(input("Masukkan index data : "))
            name = input("Masukkan nama : ")
            age = int(input("Masukkan usia : "))
            update_data(index, name, age)
        elif pilihan == 4:
            index = int(input("Masukkan index data : "))
            delete_data(index)
        elif pilihan == 5:
            break
        else:
            print("Menu yang anda masukkan tidak ditemukan")
if __name__ == "__main__":
    main()
