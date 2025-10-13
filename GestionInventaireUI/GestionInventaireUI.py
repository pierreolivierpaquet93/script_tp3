import tkinter
from tkinter import ttk

# ----------------------------------------------------------------[ CONSTANT.S ]

MY_INVENTORY_TITLE = "Enonce 04 - Pierre Olivier Paquet"
MY_INVENTORY_HEADING = "Gestion de l'inventaire"
HEADING_FONT = "Arial"

APP_WINDOW_WIDTH = "750"
APP_WINDOW_HEIGHT = "500"
APP_WINDOW_RES = f"{APP_WINDOW_WIDTH}x{APP_WINDOW_HEIGHT}"

PRODUCT_TYPES = [
	"Ordinateur",
	"Écran",
	"Clavier",
	"Souris"
]
NEW_PRODUCT_NAME = "NEW"
NEW_PRODUCT_TYPE = ""

ESC = "\033["
BLU = f"{ESC}1;34m"
RST = f"{ESC}0m"

# ------------------------------------------------------------------[ CLASSE.S ]

# --------------------[ Product ]

class Product():
	def __init__(
		self,
		name: str = NEW_PRODUCT_NAME,
		type: str = NEW_PRODUCT_TYPE
	):
		self._name = name
		self._type = type
	
	def GetName( self ):
		return self._name

	def SetName( self, new_name: str = "" ):
		self._name = new_name

	def GetType( self ):
		return self._type
	
	def SetType( self, new_type: str = "" ):
		self._type = new_type
 
# --------------------[ Inventory ]

class Inventory():
	def __init__( self ):
		self.__products: list[Product] = []

	def AddProduct( self, item: Product = None ):
		if item:
			self.__products.append( item )
		else:
			new_product = Product()
			self.__products.append( new_product )

# --------------------[ MyInventoryApp ]

# MyInventoryApp inherits from Tk
# so it becomes a Window
class MyInventoryApp( tkinter.Tk ):
	def __init__( self ):
		super().__init__()
		self._n_event = 0
		self.inventory = Inventory()
		self.geometry( APP_WINDOW_RES )
		self.title( MY_INVENTORY_TITLE )
		self.FrameLayout()
		self.Heading(MY_INVENTORY_HEADING)
		self.ListBox()
		self.Buttons()
		self.Labels()
		self.Entry()
		self.ComboBox()

	# ----------------------------------------------------------------------

	def __log( self, msg: str ):
		self._n_event += 1
		print( f"\t{BLU}{self._n_event} :: {msg}{RST}" )

	# ----------------------------------------------------------------------
	def FrameLayout( self ):
		top_height = 60
		mid_height = 300

	# Left hand side of the inventory UI.
		self._left_top_frame = tkinter.Frame( self )
		self._left_top_frame.place(
			x=0,
			y=0,
			height=top_height,
			relwidth=0.45
		)
		self._left_mid_frame = tkinter.Frame( self )
		self._left_mid_frame.place(
			x=0,
			y=top_height,
			height=mid_height,
			relwidth=0.45
		)
		self._left_bot_frame = tkinter.Frame( self )
		self._left_bot_frame.place(
			x=0,
			y=top_height+mid_height,
			height=int(APP_WINDOW_HEIGHT)-top_height-mid_height,
			relwidth=0.45
		)

	# Right hand side of the Inventory UI.
		self._right_frame = tkinter.Frame( self )
		self._right_frame.place(
			relx=0.45,
			y=0,
			heigh=APP_WINDOW_HEIGHT,
			relwidth=0.55
		)
		self._right_top_info_frame = tkinter.Frame( self._right_frame )
		self._right_top_info_frame.place(
			relx=0.10,
			y=top_height+25,
			relwidth=0.8,
			height=30
		)
		self._right_mid_info_frame = tkinter.Frame( self._right_frame )
		self._right_mid_info_frame.place(
			relx=0.10,
			y=top_height+100,
			relwidth=0.8,
			height=30
		)
		self._right_bot_info_frame = tkinter.Frame( self._right_frame )
		self._right_bot_info_frame.place(
			relx=0.10,
			y=top_height+175,
			relwidth=0.8,
			height=30
		)

	# ----------------------------------------------------------------------
	def Heading( self, heading: str):
		self._label_heading = tkinter.Label(
			self._left_top_frame,
			text=heading,
			font=(HEADING_FONT, 20)
		)
		self._label_heading.pack( side=tkinter.LEFT, padx=10 )

	# ----------------------------------------------------------------------
	def ListBox( self ):
		self._listbox = tkinter.Listbox(
			self._left_mid_frame,
			selectmode=tkinter.SINGLE,
			width=40
		)
		self._listbox.pack(
			side=tkinter.LEFT,
			padx=10,
			fill=tkinter.Y
		)
		self._listbox_scrollbar = tkinter.Scrollbar(
			self._left_mid_frame,
			orient=tkinter.VERTICAL
		)
		self._listbox_scrollbar.pack( side=tkinter.LEFT, fill=tkinter.Y )
		self._listbox.config( yscrollcommand=self._listbox_scrollbar.set )
		self._listbox_scrollbar.config( command=self._listbox.yview )

	# ----------------------------------------------------------------------
	def Buttons( self ):
		self._button_add_product = tkinter.Button(
			self._left_bot_frame,
			text="Ajouter Produit",
			command=self.AddProduct
		)
		self._button_add_product.pack(
			side=tkinter.LEFT,
			anchor=tkinter.N,
			padx=10,
			pady=10
		)
		self._button_del_product = tkinter.Button(
			self._left_bot_frame,
			text="Retirer Produit"
		)
		self._button_del_product.pack(
			side=tkinter.LEFT,
			anchor = tkinter.NW,
			pady=10
		)
		self._button_update = tkinter.Button(
			self._right_frame,
			text="Update Content"
		)
		self._button_update.place( relx=0.3, rely=0.74 )

	# ----------------------------------------------------------------------
	def Labels( self ):
		self._label_name = tkinter.Label(
			self._right_top_info_frame,
			text="Nom du produit:"
		)
		self._label_name.place( x=0, y=0 )
		self._label_type = tkinter.Label(
			self._right_mid_info_frame,
			text="Type de produit:"
		)
		self._label_type.place( x=0, y=0 )
		self._label_quantity = tkinter.Label(
			self._right_bot_info_frame,
			text="Quantité:"
		)
		self._label_quantity.place( x=0, y=0 )

	def Entry( self ):
		self._entry_name = tkinter.Entry( self._right_top_info_frame )
		self._entry_name.place( rely=0.05, relx=0.3, relwidth=0.70 )
		self._entry_quantity = tkinter.Entry( self._right_bot_info_frame )
		self._entry_quantity.place( rely=0.05, relx=0.3, relwidth=0.70 )

	# ----------------------------------------------------------------------
	def ComboBox( self ):
		self._combobox = ttk.Combobox(
			self._right_mid_info_frame,
			values=PRODUCT_TYPES,
			state="readonly"
		)
		self._combobox.current(0)
		self._combobox.place( rely=0.05, relx=0.3, relwidth=0.40 )

	def AddProduct( self ):
		self.inventory.AddProduct( Product() )
		self.__log( "New Product has been added to the inventory." )
		self._listbox.insert( tkinter.END, NEW_PRODUCT_NAME )
		self.__log( "'NEW' product has been added to the listbox." )


# ----------------------------------------------------------------------[ MAIN ]
def main():

	my_app = MyInventoryApp()
	my_app.mainloop()

if __name__ == "__main__":
	main()
