import Pokemon
Pokemon.Craw_pokemon_data("http://bulbapedia.bulbagarden.net/wiki/Ivysaur_(Pok%C3%A9mon)")

print("-----------------------------")
Pokemon.Craw_pokemon_data("http://bulbapedia.bulbagarden.net/wiki/Butterfree_(Pok%C3%A9mon)")

# Em thử tự động lấy link từ bảng Generation I nhưng link nó toàn kiểu
# "/wiki/Bulbasaur_(Pok%C3%A9mon)" mà không có phần trước thì làm kiểu gì hả anh?
# Với cả em dùng khi cop link vào luôn phải thêm dấu " ở đầu cuối, nếu em thêm " vào def thì nó tự hiểu là kí hiệu string ý ạ...
