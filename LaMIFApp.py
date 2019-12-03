import os, requests
import random as rd
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen,ScreenManager
from threading import Thread
from GeneExo_MIFA import *
# Nécessite Internet




def dossier():
    os.chdir("Google Drive//Python//La Mif App (Activite Mentale)")


def formula_as_file( formula, file, negate=False ):
    tfile = file
    if negate:
        tfile = 'tmp.png'
    r = requests.get( 'http://latex.codecogs.com/png.latex?\dpi{300} \huge %s' % formula )
    f = open( tfile, 'wb' )
    f.write( r.content )
    f.close()
    if negate:
        os.system( 'convert tmp.png -channel RGB -negate -colorspace rgb %s' %file )



sm = ScreenManager()

class ScreenAcceuil(Screen):
    def build(self):
        Layout = BoxLayout(orientation = "vertical")
        Picture = Image(source = "/Image/Acceuil.jpeg")


        self.add_widget(Layout)

class ScreenLatex(Screen):
    def build(self,StrImage,StrTexte,name):
        self.StrImage = StrImage
        self.StrTexte = StrTexte
        self.name = name
        Layout = LayoutLatex()
        Layout.build(self.StrImage,self.StrTexte,self.name)
        self.add_widget(Layout)
        sm.add_widget(self)


class LayoutLatex(BoxLayout):
    def build(self,StrImage,StrTexte,name):
        self.StrImage = StrImage
        self.StrTexte = StrTexte
        self.LatexImage = Image(source=self.StrImage, pos_hint={'center_x': 0.5, 'center_y': .6})
        self.name = name
        self.orientation = "vertical"
        Consigne = Label(text=self.StrTexte, color=[200,200,120,120])
        Consigne.size_hint_y = 0.1
        Consigne.font_size = 50
        self.add_widget(Consigne)
        self.add_widget(self.LatexImage)
        enter = Button(text='Suivant', size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5, 'center_y': .1})
        enter.bind(on_press = self.Suivant)
        self.add_widget(enter)
    def Suivant(self,instance):
        if self.name != "Enoncé4":
            dest = self.name[:-1]
            i = int(self.name[len(self.name)-1])
            dest = dest + str(i+1)
            sm.current = dest






class MyApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        ScreenEnonce = []
        for i in range(5):
            Screen = ScreenLatex()
            nomScreen = "Enoncé" + str(i)
            Screen.build(ListeNomFigureQuestion[i] + ".png",ListeConsigne[i],nomScreen)
            ScreenEnonce.append(Screen)
        sm.current = ScreenEnonce[0].name
        return sm

ListeNomFigureReponse = ["R1","R2","R3","R4","R5"]
ListeNomFigureQuestion = ["Q1","Q2","Q3","Q4","Q5"]
ListeExo = []
ListeConsigne = []
ListeConsigneCorrection = []
Type = ["D\\'eveloppement","In\\'equation","Equation","Fraction","Tableaux de Variation"]


for i in range(5):
    Exo = Exercice()
    u = rd.randint(0,4)
    Exo.type = Type[u]
    Exo.classe = "Terminale"
    Exo.FaireEnonce()
    Exo.FaireCorrection()
    Exo.EcrireExo()
    Exo.EcrireCorrection()
    ListeConsigne.append(Exo.consigne)
    ListeConsigneCorrection.append(Exo.consignecorrection)
    Exo.VersLatex()
    FormulaEnonce = Exo.enonce
    FormulaCorrection = Exo.correction
    formula_as_file(FormulaEnonce,ListeNomFigureQuestion[i] + ".png")
    formula_as_file(FormulaCorrection,ListeNomFigureReponse[i]+ ".png")


print(ListeConsigne)
print(ListeConsigneCorrection)
root = MyApp()
root.run()