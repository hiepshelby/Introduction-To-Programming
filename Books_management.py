class Book:
    def __init__(self,name,type,author):
        self.name = name
        self.type = type
        self.author = author

    def all_books(self):
        self.all_books = str(i+1) + ". " + self.name + ": " + self.type + " - " + self.author
        return self.all_books

    def books_read(self):
        self.books_read = str(i+1) + ". " + self.name + ": " + self.type + " - " + self.author
        return self.books_read

    def books_unread(self):
        self.books_unread = str(i+1) + ". " + self.name + ": " + self.type + " - " + self.author
        return self.books_unread

    def print_all_books(self):
        print(self.all_books())

    def print_books_read(self):
        print(self.books_read())

    def print_books_unread(self):
        print(self.books_unread())

b1 = Book("Pháo Đài Số","Tiểu thuyết","Dan Brown")
b2 = Book("Hai Số Phận","Tiểu thuyết","Jeffrey Archer")
b3 = Book("Tôi Tài Giỏi Bạn Cũng Thế","Phương pháp học tập","Adam Khoo")
b4 = Book("Đắc Nhân Tâm","Giao tiếp","Dale Carnegie")
b5 = Book("Không Gia Đình","Tiểu thuyết","Hector Malot")
b6 = Book("Nhà Lãnh Đạo Không Chức Danh","Phát triển bản thân","Robin Sharma")
b7 = Book("Phi Lý Trí","Tư duy","Dan Ariely")
b8 = Book("Đánh Thức Con Người Phi Thường Trong Bạn","Phát triển bản thân","Tony Robbins")
b9 = Book("Đắc Nhân Tâm Kiểu Nhật","Giao tiếp","Mizushima Hiroko")
b10 = Book("Khéo Ăn Khéo Nói Sẽ Có Được Thiên Hạ","Giao tiếp","Trác Nhã")
b11 = Book("Học Đâu Nhớ Đó","Phương pháp học tập","Peter Brown")
b12 = Book("Trên Đường Băng","Phát triển bản thân","Tony Buổi Sáng")
b13 = Book("Đời Ngắn Đừng Ngủ Dài","Phát triển bản thân","Robin Sharma")
b14 = Book("Nghệ Thuật Đầu Tư Dhandho","Đầu tư","Monish Pabrai")
b15 = Book("Bí mật của Phan Thiên Ân","Phát triển bản thân","Tiến sĩ Alan Phan")

all_books = []
all_books.append(b1)
all_books.append(b2)
all_books.append(b3)
all_books.append(b4)
all_books.append(b5)
all_books.append(b6)
all_books.append(b7)
all_books.append(b8)
all_books.append(b9)
all_books.append(b10)
all_books.append(b11)
all_books.append(b12)
all_books.append(b13)
all_books.append(b14)
all_books.append(b15)

books_read = []
books_read.append(b1)
books_read.append(b15)

books_unread = []
books_unread.append(b2)
books_unread.append(b3)
books_unread.append(b4)
books_unread.append(b5)
books_unread.append(b6)
books_unread.append(b7)
books_unread.append(b8)
books_unread.append(b9)
books_unread.append(b10)
books_unread.append(b11)
books_unread.append(b12)
books_unread.append(b13)
books_unread.append(b14)

if len(all_books) < 2:
    print("You are currently having: " + str(len(all_books)) + " book")
    print("-----------")
else:
    print("You are currently having: " + str(len(all_books)) + " books")
    print("-----------")

for i in range(len(all_books)):
    all_books[i].print_all_books()

print("\nBooks read: " + str(len(books_read)) + "/" + str(len(all_books)))
print("-----------")
for i in range(len(books_read)):
    books_read[i].print_books_read()

print("\nBooks unread: " + str(len(books_unread)) + "/" + str(len(all_books)))
print("-----------")
for i in range(len(books_unread)):
    books_unread[i].print_books_unread()