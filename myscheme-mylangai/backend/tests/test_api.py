from app.main import assess,LANGUAGES
def test_missing():assert assess({'state':'Karnataka'},{})['status']=='potentially_eligible'
def test_pass():assert assess({'age':{'min':18}},{'age':20})['status']=='likely_eligible'
def test_fail():assert assess({'age':{'min':18}},{'age':12})['status']=='not_eligible'
def test_languages():assert len(LANGUAGES)==23
