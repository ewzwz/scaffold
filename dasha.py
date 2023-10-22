guess=('sobaka')
leng=len(guess)
slovo=("_ "*leng)
print (slovo)
slovo = list(slovo)
while leng>0:
    lett=str(input("Введите букву: "))
    if lett in guess:
        leng-=guess.count(lett)
        print("Такая буква есть в слове!")
        for i in range (len(guess)):
            if guess[i]==lett:
                slovo[i*2]=lett
                print ("".join(slovo))
    else:
        print ("Masha")
print ("Вы выйграли!!!)))))")
