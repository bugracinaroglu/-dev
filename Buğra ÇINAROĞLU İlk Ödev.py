class is_firmus:
    def __init__(self, first_b, second_b):
        self.first=first_b
        self.second=second_b
    
    def find_upper(self):
        if (self.first[1]+self.first[3])/2 > (self.second[1]+self.second[3])/2:
            return self.first
        else:
            return self.second
    def find_lower(self):
        if self.find_upper()==self.first:
            return self.second
        else:
            return self.first
    def condition_1(self):
        if self.find_lower()[1]==0 or self.find_lower()[3]==0:
            return True
        else:
            return False
    def condition_2(self):
        self.area()
        if self.upy_lower==self.lowy_upper:
            return True
        else:
            return False

    def condition_3(self):
        self.cm=(self.find_upper()[0]+self.find_upper()[2])/2
        if self.find_lower()[0]<self.find_lower()[2]:
            if self.cm>=self.find_lower()[0] and self.find_lower()[2]>=self.cm:
                return True
            else:
                return False
        else:
            if self.cm>=self.find_lower()[2] and self.find_lower()[0]>=self.cm:
                return True
            else:
                return False
    
    def area(self):
        if self.find_lower()[0]>self.find_lower()[2]:
            self.rightx_lower=self.find_lower()[0]
            self.leftx_lower=self.find_lower()[2]
        else:
            self.rightx_lower=self.find_lower()[2]
            self.leftx_lower=self.find_lower()[0] 
        
        if self.find_upper()[0]>self.find_upper()[2]:
            self.rightx_upper=self.find_upper()[0]
            self.leftx_upper=self.find_upper()[2]
        else:
            self.rightx_upper=self.find_upper()[2]
            self.leftx_upper=self.find_upper()[0] 
        
        if self.find_lower()[1]>self.find_lower()[3]:
            self.upy_lower=self.find_lower()[1]
            self.lowy_lower=self.find_lower()[3]
        else:
            self.upy_lower=self.find_lower()[3]
            self.lowy_lower=self.find_lower()[1] 
        
        if self.find_upper()[1]>self.find_upper()[3]:
            self.upy_upper=self.find_upper()[1]
            self.lowy_upper=self.find_upper()[3]
        else:
            self.upy_upper=self.find_upper()[3]
            self.lowy_upper=self.find_upper()[1] 

        self.area_lower=abs((self.rightx_lower-self.leftx_lower)*(self.upy_lower-self.lowy_lower))
        self.area_upper=abs((self.rightx_upper-self.leftx_upper)*(self.upy_upper-self.lowy_upper))
        self.total=self.area_lower+self.area_upper
        
        self.dis_x=min(self.rightx_upper,self.rightx_lower)-max(self.leftx_lower,self.leftx_upper)
        self.dis_y=min(self.upy_upper,self.upy_lower)-max(self.lowy_lower,self.lowy_upper)
        if self.dis_x < 0 or self.dis_y < 0:
            self.overlap = 0
        else:
            self.overlap = self.dis_x * self.dis_y
        
        self.total_area=self.total - self.overlap
        return self.total_area

    def result(self):
        if self.condition_1()==True and self.condition_2()==True and self.condition_3()==True:
            return ["FIRMUS", self.area()]
        elif self.condition_1()==True and self.condition_2()==True and self.condition_3()==False:
            self.area()
            if self.cm <  self.leftx_lower:
                self.x1=self.rightx_upper
                self.x2=2*self.leftx_lower-self.leftx_upper
            else:
                self.x2=self.leftx_upper
                self.x1=2*self.rightx_lower-self.rightx_upper
            return ["ADDENDUM", [self.x1,self.lowy_upper,self.x2,self.upy_upper]]
        else:
            return ["DAMNARE", float(self.area())]

print(is_firmus([-0.5,10,-6,13],[-7,0,3,10]).result())
print(is_firmus([0.5,19,9.5,9],[3.8,9,5.5,0]).result())
print(is_firmus([-8,11,2,5],[1,0,-2,5]).result())  
print(is_firmus([-7,5,7,10],[9.5,12.6,-1,10]).result())
print(is_firmus([-3,7,5,15],[-7,0,7,5]).result())
print(is_firmus([6,4,3.9,-1],[0.5,14.2,9.5,4]).result())
print(is_firmus([0,0,2.4,5.2],[-8.7,10,0,0]).result()) 
print(is_firmus([0,10,-8.7,0],[-4,9,-1,14]).result())