# Kitap sınıfı (Book class)
class Book:
    def __init__(self, title, author, genre, stock):
        self.title = title  # Kitap adı
        self.author = author  # Kitap yazarı
        self.genre = genre  # Kitap türü (Roman, Dergi vs.)
        self.stock = stock  # Kitap stok durumu (kaç adet var)

    def borrow_book(self):
        if self.stock > 0:  # Eğer stokta varsa
            self.stock -= 1  # Stok bir azaltılır
            print(f'Kitap ödünç alındı: {self.title}')
        else:
            print(f'{self.title} kitabı stokta yok!')

    def return_book(self):
        self.stock += 1  # Kitap geri verildiğinde stok artırılır
        print(f'Kitap geri getirildi: {self.title}')

    def __str__(self):
        return f'Kitap: {self.title}, Yazar: {self.author}, Tür: {self.genre}, Stok: {self.stock}'


# Kütüphane sınıfı (Library class)
class Library:
    def __init__(self):
        self.books_by_genre = {}  # Kitapları türlerine göre saklayacağız

    def add_book(self, book):
        if book.genre not in self.books_by_genre:
            self.books_by_genre[book.genre] = []  # Eğer o türde kitap yoksa yeni liste oluştur
        self.books_by_genre[book.genre].append(book)
        print(f'Yeni kitap eklendi: {book.title}')

    def borrow_book(self, title):
        for genre, books in self.books_by_genre.items():
            for book in books:
                if book.title == title:
                    book.borrow_book()
                    return
        print(f'{title} adlı kitap bulunamadı!')

    def return_book(self, title):
        for genre, books in self.books_by_genre.items():
            for book in books:
                if book.title == title:
                    book.return_book()
                    return
        print(f'{title} adlı kitap bulunamadı!')

    def list_books(self):
        if not self.books_by_genre:
            print('Kütüphanede kitap yok.')
        else:
            print('Kütüphanedeki Kitaplar:')
            for genre, books in self.books_by_genre.items():
                print(f'\nTür: {genre}')
                for book in books:
                    print(book)


# Ana program (Main function)
def main():
    library = Library()  # Kütüphane nesnesi oluşturuluyor

    while True:
        print("\n1. Kitap Ekle")
        print("2. Kitap Ödünç Al")
        print("3. Kitap Geri Ver")
        print("4. Tüm Kitapları Listele")
        print("5. Çıkış")

        choice = input("Seçim yapın: ")

        if choice == "1":
            title = input("Kitap Adı: ")
            author = input("Yazar: ")
            genre = input("Tür: ")
            stock = int(input("Stok Miktarı: "))
            new_book = Book(title, author, genre, stock)
            library.add_book(new_book)  # Kitap ekleniyor

        elif choice == "2":
            title = input("Ödünç alınacak kitap adı: ")
            library.borrow_book(title)  # Kitap ödünç alınıyor

        elif choice == "3":
            title = input("Geri verilecek kitap adı: ")
            library.return_book(title)  # Kitap geri veriliyor

        elif choice == "4":
            library.list_books()  # Kitaplar listeleniyor

        elif choice == "5":
            print("Çıkış yapılıyor.")
            break  # Döngüden çıkılır

        else:
            print("Geçersiz seçim, tekrar deneyin.")


if __name__ == "__main__":
    main()
