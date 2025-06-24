s = input("縦長: H \n横長: V\nを入力してください: ")
if s == "h" or s == "H":
    a = input("縦長の形式に対応したやつやります。\nファイル名はどこから？IMGの後の数字を入力 :")
    b = input("何個？ :")
    for i in range(int(a), int(a) + int(b)):
        print('<img src="images/horizontal/h' + str(i) + '.JPG" alt="横長'+str(i)+'" class="w-full h-[40vh] object-cover rounded-lg shadow" />')
elif s == "V" or s == "v":
    a = input("横長の形式に対応したやつやります。\nファイル名はどこから？IMGのの数字を入力 :")
    b = input("何個？ :")
    for i in range(int(a), int(a) + int(b)):
         print('<img src="images/vertical/v'+str(i)+'.JPG" alt="縦長'+str(i)+'" class="w-full object-cover rounded-lg shadow" />')