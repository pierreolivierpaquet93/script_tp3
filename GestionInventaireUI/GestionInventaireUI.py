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
		self.FrameLayout()
		self.mainloop()

	# ----------------------------------------------------------------------
	def FrameLayout( self ):
		top_height = 60
		mid_height = 300
		self._left_top_frame = tkinter.Frame( self, bg="#FF0000" )
		self._left_top_frame.place(x=0,y=0,height=top_height,relwidth=0.50)
		self._left_mid_frame = tkinter.Frame( self, bg="#FF9900" )
		self._left_mid_frame.place( x=0, y=0+top_height,height=mid_height,relwidth=0.50 )
		self._left_bot_frame = tkinter.Frame( self, bg="#D9FF00" )
		self._left_bot_frame.place( x=0, y=0+top_height+mid_height,height=int(APP_WINDOW_HEIGHT)-top_height-mid_height,relwidth=0.50   )
		self._right_frame = tkinter.Frame( self, bg="#00FFD5" )
		self._right_frame.place( relx=0.5, y=0, heigh=APP_WINDOW_HEIGHT, relwidth=0.5 )

	# ----------------------------------------------------------------------
	

# ----------------------------------------------------------------------[ MAIN ]
def main():
	my_app = MyInventoryApp()

if __name__ == "__main__":
	main()
