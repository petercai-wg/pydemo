from rapidfuzz import fuzz, process
print(fuzz.ratio("Manual Charges", "manual charge"))
# print(fuzz.partial_ratio("this is a test", "This is a  test."))

# print(fuzz.token_sort_ratio("this is a test", "is this a  test"))
# print(fuzz.token_set_ratio("this is a test", "is this a  test"))
# print(fuzz.ratio(" test", "This is a  test.", processor=None, score_cutoff= 85) )


tab1 = ["Derivative","Sept Charge", "Additional Funding Cost", "Additional CFLA Cost", "1yr Liquidity Clearing - Loans", "Manual Charges", "Goodwill & Intagibles"]

tab2 = ["Additional Funding Costs", "Loan", "manual charge", "GoodWill/Intangible", "September charges", "IHC", "Derivatives", "CFLA cost"]

for t in tab1:
    match_one = process.extractOne(t, tab2, scorer= fuzz.QRatio, score_cutoff= 65 )
    print(f"t: {t},  {match_one}")

for t in tab1:
    match_list = process.extractOne(t, tab2, scorer= fuzz.partial_token_ratio, score_cutoff= 65 )
    print(f"t: {t},  {match_list}")
