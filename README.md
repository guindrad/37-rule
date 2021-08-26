# 37% rule
Simulation about the Secretary Problem (37% rule). Developed in python.


## Problem
The secretary problem demonstrates a scenario involving optimal stopping theory. The goal is to select the best option when we don't have any information about the population.

https://en.wikipedia.org/wiki/Secretary_problem
https://www.businessinsider.com/best-age-to-get-married-is-26-2017-2
https://www.washingtonpost.com/news/wonk/wp/2016/02/16/when-to-stop-dating-and-settle-down-according-to-math/


## Solution (Pseudocode)

```
LOOP(number of simulations)
  
  arr = random()
  best_37% = get_best_of_searchAmount()
  best_all = get_best_of_all()
  
  LOOP(go through all options)
    IF(arr[i]>best_37%)
      arr[i] is our guy!
      IF(arr>best_all)
        We win this game!
```


## Results
Number of games: 100.000 (for each search percentage)
Incremental percentage: 0.01
Start percentage: 0.01
End percentage: 0.99

Best choice probability: 37%-39%

![Simulation output](https://github.com/gui-h-and/37-rule/blob/master/output%20simulation.png)




