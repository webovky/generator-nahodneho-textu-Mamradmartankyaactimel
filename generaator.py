from random import randint,choice

samohlasky= "aeiou"
souhlasky= "qwrtzpsdfghjklxcvbnm"
pismenaa= "qwertzuiopasdfghjklyxcvbnm"

while True :
    try:
        pslov = int(input("počet slov : "))
        filename = input("jméno souboru : ")
        with open(filename, 'w') as z:
            pocet = 1
            slovo = ""
            delkaradku = 0

            while pocet <= pslov:
                delkaslova = randint(1,7)
                slovo =""
                for x in range(delkaslova):
                    if x == 0:
                        slovo = slovo + choice(pismenaa)
                    else:
                        if slovo[x - 1] in samohlasky:
                            slovo = slovo + choice(souhlasky)
                        else:
                            slovo = slovo + choice(samohlasky)
                slovo = slovo + " "
                z.write(slovo)

                delkaradku = delkaradku + len(slovo)
                if 70 <= delkaradku <=80:
                    z.write("\n")
                    delkaradku=0

                pocet = pocet + 1
        break
    except:
        print("chybička se vloudila")

