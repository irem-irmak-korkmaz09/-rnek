import os 
import json 
test_dict={
    "key1": "value1",
    "key2":{
        "key3": "value3",
        
    },   
}

def f (start_ path search pattern): 
      file or folders = os.listdir(start_path)
      for ff in file or folders:
         new_path = os.path.join(start_path, ff)
         if os.path.isdir(ff):
            f(start __path__=new_path, search_pattern=search_pattern)
         else:
             #dosya
                print(new_path)
print(f{start_path=".", search_pattern="*.md"})                
         
         
         
          