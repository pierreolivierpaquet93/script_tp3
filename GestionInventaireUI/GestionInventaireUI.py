import tkinter

# ----------------------------------------------------------------[ CONSTANT.S ]

MY_INVENTORY_TITLE = "Enonce 04 - Pierre Olivier Paquet"
MY_INVENTORY_HEADING = "Gestion de l'inventaire"
HEADING_FONT = "Arial"

APP_WINDOW_WIDTH = "800"
APP_WINDOW_HEIGHT = "600"
APP_WINDOW_RES = f"{APP_WINDOW_WIDTH}x{APP_WINDOW_HEIGHT}"

# ------------------------------------------------------------------[ CLASSE.S ]

# MyInventoryApp inherits from Tk
# so it becomes a Window
class MyInventoryApp( tkinter.Tk ):
	def __init__( self ):
		super().__init__()
		self.geometry( APP_WINDOW_RES )
		self.FrameLayout()
		self.mainloop()

	# ----------------------------------------------------------------------
	def FrameLayout( self ):
		self._left_frame = tkinter.Frame( self, bg="#FF0000" )
		self._left_frame.place(relx=0,rely=0,height=30,relwidth=0.50)
		self._test_frame = tkinter.Frame( self, bg="#FFD900" )
		self._test_frame.pack()
		self.test_label = tkinter.Label(self._left_frame , text=MY_INVENTORY_HEADING )
		self.test_label.pack(side="left")

	# ----------------------------------------------------------------------
	

# ----------------------------------------------------------------------[ MAIN ]
def main():
	my_app = MyInventoryApp()

if __name__ == "__main__":
	main()
