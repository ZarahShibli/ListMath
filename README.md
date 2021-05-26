# listMath

## Project description

list-math is library that works with mathmatical operation on the list 

## Methods

| Method                    | Return                                                |
| -------------             |:-------------:                                        |
|    maximum                | Return the maximum value in the list                  |
| minimum                   |Return the minimum value in the list                   |
| max_squared               | Return the maximum value squared                      |     
| length                    | Return the length of the list                         |
| positive_sum              | Return the sum of all positive numbers in the list    |
| negative_count            | Return the count of all negative number in the list   |
| reverse_list              | Return the reverse of list                            |
| sum_total                 | Return the sum of all element in list                 |
| average                   |Return the average of all element in list              |
| summary                   | Return summary about list                             |


## Usage


```{python}
LM = ListMath()
ls = [4, -3, 5, 7, -6, 8]


print("Min value: ",LM.minimum(ls))
print("Max value: ",LM.maximum(ls))
print("Max squered value: ",LM.max_squared(ls))
print("Length: ",LM.length(ls))
print("Sum of positive number: ",LM.positive_sum(ls))
print("Count of negative number: ",LM.negative_count(ls))
print("Reversed list: ",LM.reverse_list(ls))
print("Avarage : ",LM.average(ls))
print("Sum : ",LM.sum_total(ls))
print(LM.summary(ls))
```