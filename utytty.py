p
er_cent={'ткб':5.6,'скб':5.9, 'втб':4.28, 'сбер' :4.0}
money =int(input("введите сумму вклада:"))
deposit=[]
for key in per_cent:
 per_cent[key]=per_cent[key] * money/100
deposit=(list(per_cent.values()))
print(deposit)
print(max(deposit))




