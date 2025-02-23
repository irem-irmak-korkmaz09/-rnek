import os 
import json 
test_dict={
    "key1": "value1",
    "key2":{
        "key3": "value3",
        
    },   
}

def f(start_path,search_pattern):
    file_or_folder = os.listdir(start_path)
    for ff in file_or_folder:
        new_path=os.path.join(start_path,ff)
        if os.path.isdir(new_path):
            f(new_path=new_path,search_pattern=search_pattern)
        else:
            if search_pattern in ff:
                print(new_path)
print(f(start_path=".",search_pattern=".md"))
             
         
         
         
          
