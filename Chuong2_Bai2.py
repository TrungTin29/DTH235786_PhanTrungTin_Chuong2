#tinh gio phut giay

t=int(input("Nhap vao so giay bat ki: "))
hour = (t/3600)%24
minute=(t%3600)/60
second=(t%3600)%60

print(hour,":",minute,":",second)