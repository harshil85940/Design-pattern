class Window:
   __language = ""
   __purpose = ""

   def __init__(self, language, purpose):
      self.__language = language
      self.__purpose = purpose
   
   def getlanguage(self):
      return self.__language
   
   def getType(self):
      return self.__purpose

class GtkHindi(Window):
   def __init__(self):
      Window.__init__(self, "Gtk", "Hindi")

class GtkMarathi(Window):
   def __init__(self):
      Window.__init__(self, "Gtk", "Marathi")

class GtkGujrati(Window):
   def __init__(self):
      Window.__init__(self, "Gtk", "Gujrati")

class QtSpanish(Window):
   def __init__(self):
      Window.__init__(self, "Qt", "Spanish")

class QtChinese(Window):
   def __init__(self):
      Window.__init__(self, "Qt", "Chinese")

class QtNepali(Window):
   def __init__(self):
      Window.__init__(self, "Qt", "Nepali")

# Abstract factory class
class UIFactory:
   def getHindi(self): pass
   def getMarathi(self): pass
   def getGujrati(self): pass

class GtkUIFactory(UIFactory):
   def getHindi(self):
      return GtkHindi()
   def getMarathi(self):
      return GtkMarathi()
   def getGujrati(self):
      return GtkGujrati()

class QtUIFactory(UIFactory):
   def getToolboxWindow(self):
      return QtToolboxWindow()
   def getLayersWindow(self):
      return QtLayersWindow()
   def getMainWindow(self):
      return QtMainWindow()

if __name__ == "__main__":
   gnome = True
   kde = not gnome
   
   if gnome:
      ui = GtkUIFactory()
   elif kde:
      ui = QtUIFactory()
   
   toolbox = ui.getHindi()
   layers = ui.getMarathi()
   main = ui.getGujrati()
   
   print(toolbox.getlanguage(), toolbox.getType())
   print(layers.getlanguage(), layers.getType())
   print(main.getlanguage(), main.getType())
