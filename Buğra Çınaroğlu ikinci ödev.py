import random 
class adventure_game:
    def __init__(self=0, treasure=0,monster=0,sword=0,potion=0,venom=0,score=0) -> None:
        self.treasure=treasure
        self.monster=monster
        self.sword=sword
        self.potion=potion
        self.venom=venom
        self.score=score
        self.life=True
        self.map_making_position()

    def map_making_position(self):
        maporigin=[[" ", " ", " ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " ", " ", " "]]
        maping=[[" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "]]
        self.mapnew=maping
        self.map=maporigin
        T,M,S,P,V=0,0,0,0,0
        while T<5:
            y,x=random.randint(0,5),random.randint(0,6)
            if self.map[y][x]==" ":
                self.map[y][x]="T"
                T +=1
            else:
                continue
        while M<5:
            y,x=random.randint(0,5),random.randint(0,6)
            if self.map[y][x]==" ":
                self.map[y][x]="M"
                M +=1
            else:
                continue
        while S<2:
            y,x=random.randint(0,5),random.randint(0,6)
            if self.map[y][x]==" ":
                self.map[y][x]="S"
                S +=1
            else:
                continue
        while P<3:
            y,x=random.randint(0,5),random.randint(0,6)
            if self.map[y][x]==" ":
                self.map[y][x]="P"
                P +=1
            else:
                continue
        while V<3:
            y,x=random.randint(0,5),random.randint(0,6)
            if self.map[y][x]==" ":
                self.map[y][x]="V"
                V +=1
            else:
                continue 
        bool=True
        while bool==True:
            y,x=random.randint(0,5),random.randint(0,6)
            if self.map[y][x]==" ":
                self.map[y][x]="E"
                self.mapnew[y][x]="E"
                self.position=[x,y]
                bool=False
            else:
                 continue
   
    def konumlar(self,a,b):
        self.score +=1
        if self.map[b][a]=="T":
            self.score +=1
            self.mapnew[b][a]="T"
            print("+TREASURE")
        elif self.map[b][a]=="M":
            self.mapnew[b][a]="M"
            print("Oh NO! MONSTER!!!")
            if self.sword>0:
                self.sword -=1
                print("Sword is used!")
            else:
                self.score -=1
                self.life=False
                print("YOU ARE DEAD!!!")
        elif self.map[b][a]=="S":
            self.sword +=1
            self.mapnew[b][a]="S"
            print("+SWORD")
        elif self.map[b][a]=="P":
            self.potion +=1
            self.mapnew[b][a]="P"
            print("+POTİON")
        elif self.map[b][a]=="V":
            self.mapnew[b][a]="V"
            print("Oh NO! VENOM!!!")
            if self.potion>0:
                self.potion -=1
                print("Potion is used!")
            else:
                self.score -=1
                self.life=False
                print("YOU ARE DEAD!!!")
        elif self.map[b][a]==" ":
                    self.mapnew[b][a]="E"

    def hareket(self):#hareket edince skor artır
        print("-"*50)
        a=input("Press L,U,R,D to move:")
        a=a.upper().strip()
        if a =="R":# sağa
            if self.position[0]+1<7:
                if self.mapnew[self.position[1]][self.position[0]+1]==" ":
                    self.position[0] +=1
                    self.konumlar(self.position[0],self.position[1])
                else:
                    print("\n","Gidemezsin","\n")
            else:
                print("\n","Gidemezsin","\n")

        elif a=="L":# sola
            if self.position[0]-1>-1:
                if self.mapnew[self.position[1]][self.position[0]-1]==" ":
                    self.position[0] -=1
                    self.konumlar(self.position[0],self.position[1])
                else:
                    print("\n","Gidemezsin","\n")
            else:
                print("\n","Gidemezsin","\n")
        elif a=="U":# yukarı
            if self.position[1]-1>-1:
                if self.mapnew[self.position[1]-1][self.position[0]]==" ":
                    self.position[1] -=1
                    self.konumlar(self.position[0],self.position[1])
                else:
                    print("\n","Gidemezsin","\n")
            else:
                print("\n","Gidemezsin","\n")
        elif a=="D":# aşağı
            if self.position[1]+1<6:
                if self.mapnew[self.position[1]+1][self.position[0]]==" ":
                    self.position[1] +=1
                    self.konumlar(self.position[0],self.position[1])
                else:
                    print("\n","Gidemezsin","\n")
            else:
                print("\n","Gidemezsin","\n")
        else:#hatalı yada aynı yer vs.
            print("\n","Yanlış karakter","\n")
        
    def runner(self):
        while self.life:    
            print("-"*50)
            for i in self.mapnew:
                print(i)
            self.hareket()
            print("-"*50)
            print("Score:",self.score, "Sword:", self.sword, "Potion:", self.potion)
        else: print("The game ends.")


deneme=adventure_game()
deneme.runner()