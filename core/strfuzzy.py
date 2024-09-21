from rapidfuzz import fuzz, process
print(fuzz.ratio("Manual Charges", "manual charge"))
# print(fuzz.partial_ratio("this is a test", "This is a  test."))

# print(fuzz.token_sort_ratio("this is a test", "is this a  test"))
# print(fuzz.token_set_ratio("this is a test", "is this a  test"))
# print(fuzz.ratio(" test", "This is a  test.", processor=None, score_cutoff= 85) )


result = {}
tab1 = ["Derivative","Sept Charge", "Additional Funding Cost", "Additional CFLA Cost", "1yr Liquidity Clearing - Loans", "Manual Charges", "Goodwill & Intagibles"]

tab2 = ["Additional Funding Costs", "Loan", "manual charge", "GoodWill/Intangible", "September charges", "IHC", "Derivatives", "CFLA cost"]

for t in tab1:
    match_one = process.extractOne(t, tab2, scorer= fuzz.QRatio, score_cutoff= 80 )
    print(f"t: {t},  {match_one}")
    if match_one is not None:
        v = match_one[0]
        result[t] = v
        tab1.remove(t)
        tab2.remove(v)

print(f"----- {tab1} ---------- ")
print(f"----- {tab2} ---------- ")
for t in tab1:
    match_one = process.extractOne(t, tab2, scorer= fuzz.partial_token_ratio, score_cutoff= 60  )
    print(f"t: {t},  {match_one}")
    if match_one is not None:
        v = match_one[0]
        result[t] = v
        tab1.remove(t)
        tab2.remove(v)

print(result)