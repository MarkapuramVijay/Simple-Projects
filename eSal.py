emp=["a","b","c","d"]
sal=[100,200,400,250]
for x,y in enumerate(sal):
    if y>200:
        print(emp[x],f"salay {y}, his salary more than 200")
    else:
        print(emp[x],f"salay {y}, his salary less than 200")