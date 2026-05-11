names = ["An","Bình","Chi","Đạt","Quỳnh"]

name_lengths={n: len(n) for n in names if len(n)<=3}
print("Tên các bạn có độ dài nhỏ hơn 4 là: ",name_lengths)
#Kết quả: {'An': 2, 'Chi': 3, 'Đạt': 3}


