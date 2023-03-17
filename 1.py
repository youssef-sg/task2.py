#task1
l=[2,3,6]
res=1
for i in range(0,len(l)):
  res=res*l[i]
print(res)
#task2
échantillons = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] 
échantillons.sort(reverse=True)
print('Liste triée:', échantillons)
#task3
d1 = {'a' : 100, 'b' : 200, 'c' : 300}
d2 = {'a' : 300, 'b' : 200, 'd' : 400}
for key in d2:
        d2[key] = d2[key] + d1[key]
print(d2)
#task4
Liste = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] 
Liste.sort(reverse=True)
print('Liste triée:', Liste)
#task5
my_list = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
list1 = sorted(my_list, key=lambda x: float(x[1]), reverse=True)
print(list1)
#task6
my_set = {0, 1, 2, 3, 4}
print(my_set)
for item in my_set:
    print(item)
my_set.add(5)
my_set.update([6, 7])
print(my_set)
my_set.remove(3)
my_set.discard(8)  
print(my_set)
