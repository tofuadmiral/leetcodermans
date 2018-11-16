

# helper function to get occurences of ch in text

def findPos(text, ch):
    indexes = []
    startposition = 0

    while True:
        i = text.find(ch, startposition)
        if i == -1: break
        indexes.append(i)
        startposition = i + 1

    return indexes

def rules_engine(charge):
    
    # process and parse the charge
    beg, chargestr, comma, rulestr, endstr = charge.split('"')
    
    # extract features of the charge
    eqpos = findPos(chargestr, '=')
    amppos= findPos(chargestr, '&')

    # everything b/w eqpos and amppos is a feature we want
    country=chargestr[eqpos[0]+1:amppos[0]]
    currency=chargestr[eqpos[1]+1:amppos[1]]
    amount=int(chargestr[eqpos[2]+1:amppos[2]])
    ip=chargestr[eqpos[3]+1:]
    
    # now parse the rules string to get the variables we want
    spacepos=findPos(rulestr, ' ')
    category=rulestr[spacepos[0]+1:spacepos[1]]
    rule=rulestr[spacepos[2]+1:]
    comparison=rulestr[spacepos[1]+1:spacepos[2]]
    
    # select category to compare 
    if category == 'country':
        if rule == '==':
            return country == comparison 
        elif rule == '!=':
            return country != comparison 
    elif category == 'currency':
        if rule == '==':
            return currency == comparison
        elif rule == '!=':
            return currency != comparison 
    elif category == 'amount':
        if rule == '==':
            return amount == int(comparison)
        elif rule == '!=':
            return amount != int(comparison)
        elif rule == '<':
            return amount < int(comparison)
        elif rule == '>':
            return amount > int(comparison)
        elif rule == '<=':
            return amount <= int(comparison)
        elif rule == '>=':
            return amount >= int(comparison)
    elif category == 'ip_country':
        if rule == '==':
            return ip == comparison
        elif rule == '!=':
            return ip != comparison 



    