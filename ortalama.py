def ortlama (vize ,final):
    ort=vize*40/100,final*60/100
    return ort

def ortalama (vize,final,ortalama_türü):
    kvize=0
    kfinal=0    
    if ortalama_türü =="lisans":
        kvize=40
        kfinal=60   
    elif ortalama_türü =="yüksek lisans":
        kvize,kfinal=50
    else:
        kvize,kfinal=70,30    
        return(vize*kvize/100+final*kfinal/100)

def test(a,b):
    pass 
test(1,2)