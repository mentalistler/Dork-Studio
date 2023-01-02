import random
import string
from .models import *
from pytrends.request import TrendReq
def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

def dorkgenerator(dtype,wlist,ctry,dcount,dcharacter):
    dorkcontent = dorktype.objects.get(name=dtype).dork.all()
    dorks = []
    if(wlist=="random"):
        for i in range(int(dcount)):
            for dork in dorkcontent:
                generate = random_char(int(dcharacter))
                if(ctry == "None"):
                    _dork = dork.dork.replace("{{word}}",generate)
                else:
                    _dork = dork.dork.replace("{{word}}",generate) + f" site:{ctry}"
                dorks.append({'dork':_dork,'keyword':generate})
                if(len(dorks)==int(dcount)):
                    break
            if(len(dorks)==int(dcount)):
                
                    break
    else:
        wordlist_tmp = []
        dorks_tmp = []
        _wordlist = wordlistmain.objects.get(name=wlist).wordlist.all()
        for dork in dorkcontent:
            dorks_tmp.append(dork.dork)
        for word in _wordlist:
            wordlist_tmp.append(word.word)
        
        for i in range(int(dcount)):
            for x in range(len(dorks_tmp)):
                for y in range(len(wordlist_tmp)):
                    if(ctry=="None"):
                        _dork = dorks_tmp[x].replace("{{word}}",wordlist_tmp[y])
                    else:
                        _dork = dorks_tmp[x].replace("{{word}}",wordlist_tmp[y]) + f" site:{ctry}"
                    dorks.append({'dork':_dork,'keyword':wordlist_tmp[y]})
                    if(len(dorks)==int(dcount)):
                        break
                if(len(dorks)==int(dcount)):
                        break
            if(len(dorks)==int(dcount)):
                        break
        
    return dorks

def trendquery(word):
    pytrends = TrendReq(hl='en-US', tz=360)
    _list = [word]
    pytrends.build_payload(_list, cat=0, timeframe='today 12-m')
    result = pytrends.interest_over_time()
    date_values = result.index.tolist()
    word_values = result[word].tolist()
    result_list = []
    for i in range(len(date_values)):
        date_str = date_values[i].strftime('%Y-%m-%d')
        result_list.append([date_str, word_values[i]])
    return result_list