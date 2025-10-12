import tkinter

# ----------------------------------------------------------------[ CONSTANT.S ]

MY_INVENTORY_TITLE = "Enonce 04 - Pierre Olivier Paquet"
MY_INVENTORY_HEADING = "Gestion de l'inventaire"
HEADING_FONT = "Arial"

APP_WINDOW_WIDTH = "750"
APP_WINDOW_HEIGHT = "500"
APP_WINDOW_RES = f"{APP_WINDOW_WIDTH}x{APP_WINDOW_HEIGHT}"

# ------------------------------------------------------------------[ CLASSE.S ]

# MyInventoryApp inherits from Tk
# so it becomes a Window
class MyInventoryApp( tkinter.Tk ):
	def __init__( self ):
		super().__init__()
		self.geometry( APP_WINDOW_RES )
		self.title( MY_INVENTORY_TITLE )
		self.FrameLayout()
		self.Heading(MY_INVENTORY_HEADING)
		self.ListBox()
		self.InsertList() #TO delete -> Used for scrollbar tests
		self.Buttons()

	# ----------------------------------------------------------------------
	def FrameLayout( self ):
		top_height = 60
		mid_height = 300
		self._left_top_frame = tkinter.Frame( self, bg="#FF0000" )
		self._left_top_frame.place(x=0,y=0,height=top_height,relwidth=0.45)
		self._left_mid_frame = tkinter.Frame( self, bg="#FF9900" )
		self._left_mid_frame.place( x=0, y=0+top_height,height=mid_height,relwidth=0.45 )
		self._left_bot_frame = tkinter.Frame( self, bg="#D9FF00" )
		self._left_bot_frame.place( x=0, y=0+top_height+mid_height,height=int(APP_WINDOW_HEIGHT)-top_height-mid_height,relwidth=0.45   )
		self._right_frame = tkinter.Frame( self, bg="#00FFD5" )
		self._right_frame.place( relx=0.45, y=0, heigh=APP_WINDOW_HEIGHT, relwidth=0.55 )
		self._right_top_info_frame = tkinter.Frame( self._right_frame, bg="#5900FF")
		self._right_top_info_frame.place( relx=0.10, y=top_height+25,relwidth=0.8, height=30 )
		self._right_mid_info_frame = tkinter.Frame( self._right_frame, bg="#5900FF")
		self._right_mid_info_frame.place( relx=0.10, y=top_height+100,relwidth=0.8, height=30 )
		self._right_bot_info_frame = tkinter.Frame( self._right_frame, bg="#5900FF")
		self._right_bot_info_frame.place( relx=0.10, y=top_height+175,relwidth=0.8, height=30 )

	# ----------------------------------------------------------------------
	def Heading( self, heading: str):
		self._label_heading = tkinter.Label( self._left_top_frame, text=heading, font=(HEADING_FONT, 20), bg="#FF0000" )
		self._label_heading.pack(side=tkinter.LEFT, padx=10 )

	# ----------------------------------------------------------------------
	def ListBox( self ):
		self._listbox = tkinter.Listbox(self._left_mid_frame, selectmode=tkinter.SINGLE, width=40)
		self._listbox.pack(side=tkinter.LEFT, padx=10, fill=tkinter.Y)
		self._listbox_scrollbar = tkinter.Scrollbar( self._left_mid_frame, orient=tkinter.VERTICAL )
		self._listbox_scrollbar.pack( side=tkinter.LEFT, fill=tkinter.Y )
		self._listbox.config(yscrollcommand=self._listbox_scrollbar.set)
		self._listbox_scrollbar.config(command=self._listbox.yview)

	# ----------------------------------------------------------------------
	def InsertList( self ):
		for i in range(50):
			self._listbox.insert( tkinter.END, f"Element_{i}" )

	# ----------------------------------------------------------------------
	def Buttons( self ):
		self._button_add_product = tkinter.Button(self._left_bot_frame, text="Ajouter Produit" )
		self._button_add_product.pack(side=tkinter.LEFT, anchor=tkinter.N, padx=10, pady=10)
		self._button_del_product = tkinter.Button( self._left_bot_frame, text="Retirer Produit" )
		self._button_del_product.pack( side=tkinter.LEFT, anchor = tkinter.NW, pady=10 )

# ----------------------------------------------------------------------[ MAIN ]
def main():

	my_app = MyInventoryApp()
	my_app.mainloop()

if __name__ == "__main__":
	main()
