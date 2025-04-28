# calculators.py
# author: Evan Harrell
# created: 2025-04-07
# purpose: Functions for sports betting calculations
# CODING ASSISTANCE was used and is annotated

# pseudo code
# Create function to convert odds
# Use if-else to handle American/Decimal formats
# Return converted odds

#CodeASSIST-AI Used Chat GPT to write/verify odds conversions formulas
def convert_odds(odds, format_type):
    # Convert odds between American and Decimal
    # American to decimal, Positive first then Negative
    if format_type == "American":
        if odds > 0:
            decimal_odds= (odds / 100) + 1
            return decimal_odds
        else: 
            decimal_odds = (100 / abs(odds)) + 1 # This section is the main thing ChatGPT helped with
            return decimal_odds
        # Decimal to American
    else:
        if odds >=2: # >=2 in decimal odds means positive, (you win more than original wager)
            american_odds = (odds - 1) * 100
            return american_odds
        else: # Negative in Decimal format
            american_odds= -100 / (odds - 1)
            return american_odds