# Sports Betting Toolkit - Tkinter GUI for odds conversion
# author: Evan Harrell
# created: 2025-04-07
# purpose: Simple GUI for converting sports betting odds
# CODING ASSISTANCE was used and is annotated

# psudo code
# Create a window with title label
# Add input for odds and drop down for format
# Check if input valid, show result
# Show help window with instructions

# import easyframe and set up GUI structure, Import odds conversion funtion
from breezypythongui import EasyFrame
from calculators import convert_odds
import tkinter.messagebox
import tkinter
import os

class OddsCalculators(EasyFrame):
    """Displays GUI converting sports betting odds."""

    def __init__(self):
        """Sets up windows and widgets."""
       # Initialicze easyframe, add widgets
        EasyFrame.__init__(self, title="Quick Access Odds Calculators")

        # Add title label
        self.addLabel(text="Quick Access Odds Calculators",row=0, column=0, columnspan=2)


        # add calculator picture
        self.addLabel(text= "Calculator Icon", row=1, column=0)
        self.image = self.addLabel(text="", row=1, column=1)
        self.image["image"] = self.loadImage("calculator.png")


        # add sports logo picture
        self.addLabel(text= "Sports Icon", row=1, column=0)
        self.image1 = self.addLabel(text="", row=4, column=1)
        self.image1["image"] = self.loadImage("sports.png")                



        # Add label and input field and dropdown for odds        
        # # AI ASSISTANCE: used CHat GPT to help me with dropdown box
        self.addLabel(text="Enter odds (example, +200):", row=2, column=0)
        self.oddsField = self.addTextField(text="", row=2,column=1)
        self.formatChoice = self.addComboBox (row=3, column=0, columnspan=2,
                                             values=["American", "Decimal"],
                                             default="American")



        # add result label
        self.resultLabel = self.addLabel(text= "Results Here", row=5, column=0, columnspan=2)

        # add the buttons
        self.addButton(text="Convert", row=6, column=0, command=self.convert_odds)
        self.addButton(text="Help", row = 6, column=1, command=self.show_help)
        self.addButton(text="Exit", row= 7, column=0, columnspan=2, command=self.exit_program)

    def convert_odds(self):
            """Callback for convert button: Convert odds, show result"""
            # Get odds entry from user
            odds_text = self.oddsField.getText()

            # Make sure its not empty
            if odds_text =="":
                self.resultLabel["text"] = "Enter odds please!!"
                return
            
            # Make sure its a number
            try:
                odds = float(odds_text)
            except ValueError:
                self.resultLabel["text"] = "Enter a NUMBER (like +200 or 2.0)"
                return
            
            # Get fornat from dropdown
            format_type = self.formatChoice.getSelectedItem()

            # convert odds via function from calculator 
            try:
                result = convert_odds(odds, format_type)
                self.resultLabel["text"]= f"Converted odds: {result:.2f}"
            except Exception as e:
                self.resultLabel["text"] = "Oopsie, conversion error!!"

    def show_help(self):
         """Callback for help button: Show help Window"""
         # create help window
         help_window = EasyFrame(title="Help : Quick Access Odds Calculators")
         help_window.addLabel(text= "Instructions", row=0, column=0)
         help_window.addLabel(text="1. Enter Odds (i.e +200 or 2.0)", row=1, column=1)
         help_window.addLabel(text="2. choose format (American or decimal)", row = 2, column = 0)
         help_window.addLabel(text="3. click convert", row = 3, column=0)
         help_window.addLabel(text="+200 means you win $2 for every $1 you bet,", row = 4, column=0)
    
    def exit_program(self):
         # AI ASSISTANCE, needed help with message box
         """Callback for exit button, ends the program"""
         if tkinter.messagebox.askyesno("Exit", "Are you sure you are done??"):
              self.destroy()

# Start the program !!!!
if __name__ == "__main__":
     OddsCalculators().mainloop()

   
