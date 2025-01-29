print("SuperMan e Flash encontram o portal:\n")

confirm = False
while(confirm == False):
    escolha = input("Escolha um caminho:\nRápido: Chegam rápido, mas enfrentam danos mágicos.\nSeguro: Chegam ao castelo, mas perdem tempo.\n(escolha 1 para o caminho rapido e 2 para o caminho seguro:) ")
    
    if(escolha == "1"):
        print("\nEles lavaram danos magicos mas, chegaram no castelo e entraram em labirinto de espelhos.")
        
        while(confirm == False):
            espelho = input("Existe 3 espelhos escolha 1(digite um numero de 1 a 3) ")
            
            if (espelho == "1"):
                print("\nArmadilha!!! SuperMan e Flash voltaram para o inicio do labirinto")
                
            elif (espelho == "2"):
                print("SuperMan e Flash acharam o feiticiro.")
                lutar = input("Quem irá lutar, SuperMan ou Flash (digite 1 para SuperMan ou 2 para flash)")
                
                if(lutar == "1"):
                    print("Superman resiste e vence, YOU WIN !!!")
                    exit()
                elif(lutar == "2"):
                    print("Flash desvia e derrota o Feiceiro, YOU WIN !!!")
                    exit()
                    
            elif (espelho == "3"):
                print("Encontram o Feiceiro, mas ele ataca, eles levaram muito dano e perderam. \nYOU LOSER!!!")
            
                exit()
            
            else:
                print("DIGITE UM NUMERO DE 1 a 3:")
            
    elif(escolha == "2"):
        print("\nChegam ao castelo, mas perdem tempo.")
        
        while(confirm == False):
            espelho = input("Existe 3 espelhos escolha 1(digite um numero de 1 a 3) ")
            
            if (espelho == "1"):
                print("\nArmadilha!!! SuperMan e Flash voltaram para o inicio do labirinto\nEles perderam muito tempo e perderam.\nYOU LUSER!!!")
                exit()
                
            elif (espelho == "2"):
                print("SuperMan e Flash acharam o feiticiro.")
                lutar = input("Quem irá lutar, SuperMan ou Flash (digite 1 para SuperMan ou 2 para flash)")
                
                if(lutar == "1"):
                    print("Superman resiste e vence, YOU WIN !!!")
                    exit()
                elif(lutar == "2"):
                    print("Flash desvia e derrota o Feiceiro, YOU WIN !!!")
                    exit()
                    
            elif (espelho == "3"):
                print("Encontram o Feiceiro, mas ele ataca, o feiticeiro é quase derrotado mas foge.")
            
            else:
                print("\nDIGITE UM NUMERO DE 1 a 3:\n")
    else:
        print("\nDIGITE UM 1 OU 2:\n")

        
