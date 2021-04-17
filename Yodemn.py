import random
import time
print('Version 1.0.2.')
print('Designed by dwy.')
print('Coded by zcy.')
print('设定目标数字的区间。注意：此程序要求上下确界的整数位至少相差4。')
min=int(float(input('请输入目标数字的取值下确界:')))
max=int(float(input('请输入目标数字的取值上确界:')))
while min>=max-3:
    print('所输入的数字不符合要求,请重新输入。注意：此程序要求上下确界的整数位至少相差4。')
    min=int(input('请输入目标数字的取值下确界:'))
    max=int(input('请输入目标数字的取值上确界:'))
set=random.randint(min,max)
while set-1<min+1 or set+1>max-1:
    set=random.randint(min,max)
cheat_1=random.randint(min+1,set-1)
cheat_2=random.randint(set+1,max-1)
start=time.time()
times=0
player=int(input('请输入猜测的数:'))
while True:
    if player<cheat_1:
        print('偏小')
        times=times+1
        print('统计信息:次数:',times,'用时:',time.time()-start)
        player=int(input('请输入猜测的数:'))
    if player>=cheat_1 and player<set:
        print('偏大')
        times=times+1
        print('统计信息:次数:',times,'用时:',time.time()-start)
        player=int(input('请输入猜测的数:'))
    if player==set:
        print('错误')
        times=times+1
        print('统计信息:次数:',times,'用时:',time.time()-start)
        player=int(input('请输入猜测的数:'))
    if player>set and player<=cheat_2:
        print('偏小')
        times=times+1
        print('统计信息:次数:',times,'用时:',time.time()-start)
        player=int(input('请输入猜测的数:'))
    if player>cheat_2:
        print('偏大')
        times=times+1
        print('统计信息:次数:',times,'用时:',time.time()-start)
        player=int(input('请输入猜测的数:'))