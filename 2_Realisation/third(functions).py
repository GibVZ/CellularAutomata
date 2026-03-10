
def update_ca(last_state, rule_state, rule_new_state, border_val):
    new_state = [border_val]
    for num in range(1, len(last_state[-1])-1):
        neighboors = ''.join(last_state[-1][num-1:num+2])
        case = rule_state.index(neighboors)
        new_state.append(rule_new_state[case])
    new_state.append(border_val)
    return new_state

def draw_ca(states):
    for raw_ind, raw in enumerate(states):
        for col_ind, el in enumerate(raw):
            if el == '1':
                print('#', end = '')
            else:
                print(' ', end = '')
        print()

# Теперь то, что нужно непосредственно для клеточного автомата
# Сюда мы будем закидывать ВСЕ состояния
#(автомат одномерный, а мы работаем в 2D - почему бы этим не воспользоваться ;))

X, Y = 100, 100
##rule = {'000': '0', '001': '1', '010': '1', '011': '1', '100': '1', '101': '0', '110': '0', '111': '0'}
##rule = {'000': '1', '001': '0', '010': '0', '011': '0', '100': '0', '101': '1', '110': '0', '111': '1'}
rule_state = ['000', '001', '010', '011', '100', '101', '110', '111']
rule_new_state = ['1', '0', '0', '0', '0', '1', '0', '1']


border_val = '1'
##States = [['1' if i==X//2 else '0' for i in range(X)]]
States = [[]]
for i in range(X):
    if i == X//2:
        States[0].append('1')
    else:
        States[0].append('0')

## Здесь мы воспользуемся тем, что список может хранить списки.
## Мы создадим список, который будет хранить состояния ситсетмы последовательно(которые сами являются списками)


## Сделаем нужное количество итерации и сохраним их все
for i in range(Y):
    States.append(update_ca(States[-1], rule_state, rule_new_state, '1'))

## А теперь выведем
draw_ca(States)
