def convert_test(vars):
    labels=['tablet','capsule','solution','suspension','IR','ER','DR','oral','intramuscular','intravenous',
    'inhalation','topical','ophthalmic','transdermal','strength','total_excipients','NDA','ANDA','OTC','NDA authorized generics',
    "UNII: 70097M6I30","UNII: 059QF0KO0R","UNII: OP1R32D61U",
    "UNII: 15FIX9V2JP","UNII: ETJ7Z6XBU4","UNII: O8232NY3SJ","UNII: 55X04QC32I","UNII: 7SEV7J4R1U",
    "UNII: 3NXW29V3WO","UNII: EWQ57Q8I5X","UNII: 6DC9Q167V3","UNII: QTT17582CB",
    "UNII: 3WJQ0SDW1A","UNII: 451W47IQ8X","UNII: EX438O2MRT","UNII: XM0M87F357",
    "UNII: C151H8M554","UNII: 368GB5141J","UNII: M28OL1HH48","UNII: 2G86QN327L",
    "UNII: PDC6A3C0OX","UNII: 1K09F3G675","UNII: H3R47K3TBD","UNII: 35SW5USQ3G",
    "UNII: FZ989GH94E","UNII: L06K8R7DQK","UNII: WZB9127XOA","UNII: 5856J3G2A2",
    "UNII: M28OL1HH48","UNII: OJ245FE5EU","UNII: 3SY5LH9PMK","UNII: 6OZP39ZG8H",
    "UNII: 46N107B71O","UNII: 3K9958V90M","UNII: RFW2ET671P","UNII: A2I8C7HI9T",
    "UNII: XF417D3PSL","UNII: 68401960MK","UNII: 4ELV7Z65AP","UNII: 2968PHW8QP",
    "UNII: Z8IX2SC1OH","UNII: 7FLD91C86K","UNII: 506T60A25R","UNII: B697894SGQ"]
    dic={label:i for i,label in enumerate(labels)}
    array=[0]*len(labels)
    for k,v in vars.items():
        array[dic[k]]=v
    test=np.array(array)
    return test
def load_model():
    pass

def predict(test):
    clf=load_model()
    pass
