# deepcopy 실험
import copy
from pprint import pprint as pp

tmp_list1 = [[0]*5]*5
tmp_list2 = [[0]*5 for _ in range(5)]
tmp_list3 = copy.deepcopy(tmp_list1)

tmp_list1[0][0] = 3
tmp_list2[0][0] = 4
tmp_list3[0][0] = 5
print('--------tmp_list1---------')
pp(tmp_list1)
print('--------tmp_list2---------')
pp(tmp_list2)
print('--------tmp_list3---------')
pp(tmp_list3)

countlist =  copy.deepcopy([[0] *10]*10)
print('\n\n')
print(f'is id(tmp_list2[1]) == id(tmp_list2[2])?  :  {id(tmp_list2[1]) == id(tmp_list2[2])}')
print(f'is id(countlist[1]) == id(countlist[2])?  :  {id(countlist[1]) == id(countlist[2])}')