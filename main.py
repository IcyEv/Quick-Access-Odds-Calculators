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

class OddsCalculators(EasyFrame):
    """Displays GUI converting sports betting odds."""

    def __init__(self):
        """Sets up windows and widgets."""
       # Initialize easyframe, add widgets
        EasyFrame.__init__(self, title="Quick Access Odds Calculators")

        # Add title label
        self.addLabel(text="Quick Access Odds Calculators",row=0, column=0, columnspan=2)

        # Add label and input field for odds
        self.addLabel(text="Enter odds (example, +200):", row=1, column=0)
        self.oddsField = self.addTextField(text="", row=1,column=1)
        
   
