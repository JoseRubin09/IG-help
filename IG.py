def missionOrNo(lines):

    i = 0
    word = lines.split(" ")
    while(i < len(word)):
        if word[i] == "help" or word[i] == "helps" or word[i] == "add" or word[i] == "training" or word[i] == "bringing" or word[i] == "promoting" or word[i] == "sharing" or word[i] == "working" or word[i] == "looking" or word[i] == "encouraging" or word[i] == "encourage" or word[i] == "optimizing" or word[i] == "taking" or word[i] == "guiding" or word[i] == "guide" or word[i] == "inspiring" or word[i] == "helping" or word[i] == "support" or word[i] == "showing" or word[i] == "supporting" or word[i] == "teach" or word[i] == "teaching" or word[i] == "empower" or word[i] == "empowering" or word[i] == "found" or word[i] == "qualified" or word[i] == "mlm" or word[i] == "assist" or word[i] == "assisting" or word[i] == "gain" or word[i] == "foreign" or word[i] == "lead" or (word[i] == "create" and word[i-1] == "to") or word[i] == "providing":
            a = True
            break
        else:
            a = False
        i = i + 1    
    return a

def checkFinally(lines):

    i = 0
    word = lines.split(" ")
    while(i < len(word)):
        if word[i] == "finally" or word[i] == "permanently":
            a = True
            break
        else:
            a = False
        i = i + 1    
    return a

def checkWithFrom(lines):

    i = 0
    word = lines.split(" ")
    while(i < len(word)):
        if word[i] == "others":
            a = True
            break
        else:
            a = False
        i = i + 1    
    return a

def checkTO(lines):
    i = 0
    word = lines.split(" ")
    while(i < len(word)):
        if word[i] == "empowering" or word[i] == "permanently":
            a = True
            break
        else:
            a = False
        i = i + 1    
    return a

def checkBrotha(lines):
    
    i = 0
    word = lines.split(" ")
    while(i < len(word)):
        if word[i] == "brotha":
            a = True
            break
        else:
            a = False
        i = i + 1    
    return a

def changingWords(eachCs):

    x = 0
    while(x < len(eachCs)):
        if eachCs[x] == "you":
            eachCs[x] = "others"
        elif eachCs[x] == "your":
            eachCs[x] = "their"
        elif eachCs[x] == "yourself":
            eachCs[x] = "themselves"    
        elif eachCs[x] == "people" or eachCs[x] == "clients":
            eachCs[x] = "others"
        x = x + 1
    return eachCs
    
def missionBio(word):

    csFormat = "love what you're up to in the coach space"
    arrayFormat = csFormat.split(" ")
    arrayFormat[7] = coachType(word)
    restFormat = " and amazing to see the positive impact you're making by"
    if arrayFormat[7] == "nutritionist" or arrayFormat[7] == "dietitian":
        arrayFormat[5] = "as"
        arrayFormat[6] = "a"
        arrayFormat = arrayFormat[:8] + arrayFormat[9:]
        csFormat = (" ").join(arrayFormat)
    elif arrayFormat[7] == "rdn":
        arrayFormat[5] = "as"
        arrayFormat[6] = "a"
        arrayFormat = arrayFormat[:8] + arrayFormat[9:]
        arrayFormat[7] = "dietitian nutritionist"
        csFormat = (" ").join(arrayFormat)    
    else:
        csFormat = (" ").join(arrayFormat).replace("coach","coaching")
    
    j = 0
    eachCs = word.split(" ")
    csPart1 = (" ").join(arrayFormat).strip()
    csPart1 = csPart1.replace("coach","coaching")
    
    eachCs = changingWords(eachCs)    
    while(j < len(eachCs)):
        if eachCs[j] == "help" or eachCs[j] == "helping" or eachCs[j] == "helps":
            mission = eachCs[j+1:]
            a = csPart1 + restFormat + " helping " +" ".join(mission)
            break
        elif eachCs[j] == "support" or eachCs[j] == "supporting":
            mission = eachCs[j+1:]
            a = csPart1 + restFormat + " supporting " +" ".join(mission)
            break
        elif eachCs[j] == "bringing":
            mission = eachCs[j:]
            a = csPart1 + restFormat + " ".join(mission)
            break
        elif eachCs[j] == "sharing":
            mission = eachCs[j+1:]
            a = csPart1 + restFormat + " sharing " +" ".join(mission)
            break
        elif eachCs[j] == "promoting":
            mission = eachCs[j+1:]
            a = csPart1 + restFormat + " promoting " +" ".join(mission)
            break
        elif eachCs[j] == "training":
            mission = eachCs[j+1:]
            a = csPart1 + restFormat + " training " +" ".join(mission)
            break
        elif eachCs[j] == "looking":
            mission = eachCs[j+1:]
            a = csPart1 + restFormat + " looking " +" ".join(mission)
            break
        elif eachCs[j] == "guiding" or eachCs[j] == "guide":
            mission = eachCs[j+1:]
            a = csPart1 + restFormat + " guiding " +" ".join(mission)
            break
        elif eachCs[j] == "inspiring":
            mission = eachCs[j+1:]
            a = csPart1 + restFormat + " inspiring " +" ".join(mission)
            break
        elif eachCs[j] == "showing":
            mission = eachCs[j+1:]
            a = csPart1 + restFormat + " showing " +" ".join(mission)
            break
        elif eachCs[j] == "building":
            mission = eachCs[j+1:]
            a = csPart1 + restFormat + " showing " +" ".join(mission)
            break
        elif eachCs[j] == "assist" or eachCs[j] == "assisting":
            mission = eachCs[j+1:]
            a = csPart1 + restFormat + " assisting " +" ".join(mission)
            break
        elif eachCs[j] == "optimizing":
            mission = eachCs[j+1:]
            a = csPart1 + restFormat + " optimizing " +" ".join(mission)
            break
        elif eachCs[j] == "provide" or eachCs[j] == "providing":
            mission = eachCs[j+1:]
            a = csPart1 + restFormat + " providing " +" ".join(mission)
            break
        elif eachCs[j] == "encouraging" or eachCs[j] == "encourage":
            mission = eachCs[j+1:]
            a = csPart1 + restFormat + " encouraging " +" ".join(mission)
            break
        elif eachCs[j] == "taking":
            mission = eachCs[j+1:]
            a = csPart1 + restFormat + " taking " +" ".join(mission)
            break
        elif eachCs[j] == "teach" or eachCs[j] == "teaching":
            mission = eachCs[j+1:]
            a = csPart1 + restFormat + " teaching " +" ".join(mission)
            break
        elif eachCs[j] == "empower" or eachCs[j] == "empowering":
            mission = eachCs[j+1:]
            a = csPart1 + restFormat + " empowering " +" ".join(mission)
            break
        elif eachCs[j] == "lead":
            mission = eachCs[j+1:]
            a = csPart1 + restFormat + " leading " +" ".join(mission)
            break
        elif eachCs[j] == "work" or eachCs[j] == "working":
            mission = eachCs[j+1:]
            a = csPart1 + restFormat + " working " +" ".join(mission)
            break
        elif eachCs[j] == "add" :
            mission = eachCs[j+1:]
            a = csPart1 + restFormat + " helping others finally " +" ".join(mission)
            break
        elif eachCs[j] == "found":
            a = "not found"
            break
        elif eachCs[j] == "qualified":
            a = "not qualified"
            break
        elif eachCs[j] == "mlm":
            a = "MLM"
            break
        elif eachCs[j] == "foreign":
            a = "foreign"
            break
        else:
            a = csPart1 + restFormat  
        j = j + 1

    if checkBrotha(word):
        array = a.split(" ")
        x = 0
        while (x < len(array)):
            if array[x] == "nutritionist":
                array[x] = "nutritionist brotha"
                break
            elif array[x] == "dietitian":
                array[x] = "dietitian brotha"
                break
            elif array[x] == "space":
                array[x] = "space brotha"
                break
            x = x + 1
        a = (" ").join(array)
    arrayforCword = a.split(" ")

    if checkFinally(a):
        pass
    elif checkTO(a):
        y = 0
        while(y < len(arrayforCword)):
            if arrayforCword[y] == "others" or arrayforCword[y] == "women":
                if arrayforCword[y + 1] == "with" or arrayforCword[y + 1] == "from" or arrayforCword[y + 1] == "towards" or arrayforCword[y + 1] == "around" or arrayforCword[y + 1] == "in" or arrayforCword[y + 1] == "can" or arrayforCword[y + 1] == "who’s" or arrayforCword[y + 1] == "who" or arrayforCword[y + 1] == "through" or arrayforCword[y + 1] == "in":
                    break
                else:
                    arrayforCword[y + 1] = "to finally"
                break
            y = y + 1
    else:
        y = 0
        while(y < len(arrayforCword)):
            if arrayforCword[y] == "others" or arrayforCword[y] == "women" or arrayforCword[y] == "entrepreneurs" or arrayforCword[y] == "achievers" or arrayforCword[y] == "leaders" or arrayforCword[y] == "humans" or arrayforCword[y] == "individuals" or arrayforCword[y] == "professionals" or arrayforCword[y] == "couples" or arrayforCword[y] == "moms":
                if arrayforCword[y + 1] == "with" or arrayforCword[y + 1] == "from" or arrayforCword[y + 1] == "towards" or arrayforCword[y + 1] == "around" or arrayforCword[y + 1] == "in" or arrayforCword[y + 1] == "can" or arrayforCword[y + 1] == "who’s" or arrayforCword[y + 1] == "who" or arrayforCword[y + 1] == "through" or arrayforCword[y + 1] == "in":
                    break
                else:
                    if arrayforCword[y + 1] == "to":
                        arrayforCword[y + 1] = "to finally"
                    else:
                        arrayforCword[y + 1] = "finally " +arrayforCword[y + 1] 
            y = y + 1
    a = (" ").join(arrayforCword)
    a = typeNutritionist(word,a)
    a = typeDietitian(word,a)

    return a.strip()  

def typeNutritionist(lines,a):
    
    i = 0
    word = lines.split(" ")
    a = a.split(" ")
    while(i < len(word)):
        if word[i] == "nutritionist":
            a[6] = "a" + (" ").join(word[:i])
            break
        i = i + 1
    return (" ").join(a)

def typeDietitian(lines,a):
    
    i = 0
    word = lines.split(" ")
    a = a.split(" ")
    while(i < len(word)):
        if word[i] == "dietitian":
            a[6] = "a" + (" ").join(word[:i])
            break
        i = i + 1
    return (" ").join(a)

def connectExtra(word):

    csFormat = "love what you're up to in the coaching space" 
    restFormat = " and amazing to see the positive impact you're making by"
    restFormat = restFormat.split(" ")
    arrayFormat = csFormat.split(" ")
    arrayFormat[7] = coachType(word)
    if arrayFormat[7] == "nutritionist" or arrayFormat[7] == "dietitian":
        arrayFormat[5] = "as"
        arrayFormat[6] = "a"
        arrayFormat = arrayFormat[:8] + arrayFormat[9:]
        csFormat = (" ").join(arrayFormat)
    elif arrayFormat[7] == "rdn":
        arrayFormat[5] = "as"
        arrayFormat[6] = "a"
        arrayFormat = arrayFormat[:8] + arrayFormat[9:]
        arrayFormat[7] = "dietitian nutritionist"
        csFormat = (" ").join(arrayFormat)
    else:
        csFormat = (" ").join(arrayFormat).replace("coach","coaching")
    eachCs = word.split(" ")
    csPart1 = (" ").join(arrayFormat)
    csPart1 = csPart1.replace("coach","coaching")
    j = 0

    while(j < len(eachCs)):
        if eachCs[j] == "mom" or eachCs[j] == "mother" or eachCs[j] == "mama" or eachCs[j] == "mommy":
            cs = (" ").join(restFormat[:-1])
            a = csPart1 + cs + " while being a rockstar mom!"
            break
        elif eachCs[j] == "momwife" or eachCs[j] == "wifemom":
            cs = (" ").join(restFormat[:-1])
            a = csPart1 + cs + " while being a rockstar wife and mom!"
            break
        elif eachCs[j] == "fatherhusband" or eachCs[j] == "husbandfather":
            cs = (" ").join(restFormat[:-1])
            a = csPart1 + cs + " while being a rockstar husband and father!"
            break
        elif eachCs[j] == "dad" or eachCs[j] == "father":
            cs = (" ").join(restFormat[:-1])
            a =  csPart1 + cs + " while being a rockstar father!"
            break
        elif eachCs[j] == "vegan" :
            cs = (" ").join(restFormat[:-1])
            a = csPart1 + cs + " and btw I’ve been a vegan for over a year now and It's been life changing for me!"
            break
        elif eachCs[j] == "iin":
            cs = (" ").join(restFormat[:-1])
            a =  csPart1 + cs + " and btw so cool you went to IIN, I know a few coaches that went through the program and loved it!"
            break
        elif eachCs[j] == "food":
            cs = (" ").join(restFormat[:-1])
            a =  csPart1 + cs + " and btw all the meals on your IG look delicious, definitely makes me want to eat healthier!"
            break
        elif eachCs[j] == "quotes":
            cs = (" ").join(restFormat[:-1])
            a = csPart1 + cs + " and btw fabulous quote posts on your IG, might have to repost a few of them!"
            break
        elif eachCs[j] == "marketing" or (eachCs[j] == "social" and eachCs[j+1] == "media"):
            a = "not qualified"
            break
        elif eachCs[j] == "location":
            cs = (" ").join(restFormat[:-1])
            addingLocation = (" ").join(eachCs[j+1:])
            a =  csPart1 + cs + " out in " + addingLocation.title()
            break
        elif eachCs[j] == "extra":
            cs = (" ").join(restFormat[:9])
            addingExtra = (" ").join(eachCs[j+1:])
            a =  csPart1 + cs + " also making as a " + addingExtra
            break
        elif eachCs[j] == "extrathe":
            cs = (" ").join(restFormat[:9])
            addingExtra = (" ").join(eachCs[j+1:])
            a =  csPart1 + cs + " also making as the " + addingExtra
            break
        elif eachCs[j] == "extraan":
            cs = (" ").join(restFormat[:9])
            addingExtra = (" ").join(eachCs[j+1:])
            a =  csPart1 + cs + " also making as an " + addingExtra
            break
        elif eachCs[j] == "messagesent":
            a =  "already sent message"
            break
        elif eachCs[j] == "notacoach":
            a =  "not a coach"
            break
        else:
            cs = (" ").join(restFormat)
            a = csPart1 + cs 
        j = j + 1

    if checkBrotha(word):
        array = a.split(" ")
        x = 0
        while (x < len(array)):

            if array[x] == "nutritionist":
                array[x] = "nutritionist brotha"
                break
            elif array[x] == "dietitian":
                array[x] = "dietitian brotha"
                break
            elif array[x] == "space":
                array[x] = "space brotha"
                break
            x = x + 1
        a = (" ").join(array)
    
    a = typeNutritionist(word,a)
    a = typeDietitian(word,a)
        
    return a.strip()

def coachType(lines):
    
    i = 0
    j = 0
    a = "hi"
    word = lines.split(" ")
    while(i < len(word)):
        if word[i] == "coach" or word[i] == "coaching":
            if word[i-1] == "coach":
                a = "coach"
            else:
                a = " ".join(word[:i+1])
            break   
        i = i + 1
    if a == "hi":
        while(j < len(word)):
            if word[j] == "nutritionist" or word[j] == "dietitian" or word[j] == "rdn":
                a = word[j]
                break
            j = j + 1
    if a == "hi":
        a = "coach"
    return a.strip()

def everything(): 

    bio = open('biografias.txt', 'r')
    lines = bio.read().replace("#","").replace("+","and").replace("/"," ").replace("?","").replace("\n"," ").replace("\"","").replace("&","and").replace("w/o","without").lower().split("3")
    arrayCs = []
    i = 0
    while (i < len(lines)):
        siono = missionOrNo(lines[i])
        if siono:
            a = missionBio(lines[i])
            a = a.replace(".","").replace("nlp","NLP").replace("Nlp","NLP").replace("christian","Christian")
            arrayCs.append(a)
        else:
            a = connectExtra(lines[i])
            a = a.replace(".","").replace("nlp","NLP").replace("Nlp","NLP").replace("christian","Christian")
            arrayCs.append(a)
        i = i + 1
    z = 0
    with open('csTerminadas.txt', 'w') as writeCS:
        while (z < len(arrayCs)):
            writeCS.write(arrayCs[z]+"\n")
            z = z + 1

def main(): 

    everything()

if __name__ == '__main__':
    
    main()
