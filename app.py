from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class childApp(GridLayout):
    def __init__(self,**kwargs):
        
        
        super(childApp,self).__init__()
        self.cols=2
        self.add_widget(Label(text="Enter Name 1"))
        self.name1=TextInput()
        self.add_widget(self.name1)

        self.add_widget(Label(text="Enter Name 2"))
        self.name2=TextInput()
        self.add_widget(self.name2) 

        self.press=Button(text="Find out") 
        self.press.bind(on_press=self.find_out)
        self.add_widget(self.press)  

        self.solution=TextInput(readonly=True)
        self.solution.text=''
        self.add_widget(self.solution)



    def find_out(self,instance):
        B=self.name1.text
        G=self.name2.text
        if(B=="" or G==""):
            self.solution.text="Please enter both names"
            return
        elif(B==G):
            self.solution.text="Both are same names"
            return
        BB=list(B)
        GG=list(G)
        c=0
        for i in range(len(BB)):
            for j in range(len(GG)):
                if(BB[i]==GG[j]):
                    BB[i]=GG[j]=0
                    c+=2
                    break
        c=len(B)+len(G)-c
        Flames=['F','L','A','M','E','S']
        i=0
        p=0
        x=0
        mainp=0
        while(True):
            if(Flames[i]!=0):
                p+=1
                if(p==c):
                    mainp=Flames[i]
                    Flames[i]=0
                    p=0
                    x+=1
                    if(x==6):               
                        break        
            if(i==len(Flames)-1):
                i=0
            else:
                i+=1

        if(mainp=="F"):
            mainp="Friendship"
        elif(mainp=="L"):
            mainp="Loyal"
        elif(mainp=="A"):
            mainp="Affection"
        elif(mainp=="M"):
            mainp="Merry"
        elif(mainp=="E"):
            mainp="Enemy"
        elif(mainp=="S"):
            mainp="Sibling like"
            
        self.solution.text=mainp

        
class parentApp(App):
    def build(self):
        return childApp()

if __name__=="__main__":
    parentApp().run()