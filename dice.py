import random
from statistics import mean, stdev

def playground_mechanics(n:list,dice_number=3):
    ''' 處理棋盤上的骰子和押注機制，輸出字典 [號碼:數量] '''
    dice = [random.randint(1,6) for _ in range(dice_number)]
    res = {}
    for _ in n:
        res[_] = dice.count(_)
    return res

def game_bet(m=100,bet_money=10,init_money=100,number_of_bet=1):
    ''' 骰子甩m次（稱為一局），由棋盤輸出的結果進行錢的演算，輸出字典 [初始金額,最終金額,賭注額度,賭注數量] '''
    money = init_money
    for _ in range(m):
        bet_opt = [random.randint(1,6) for _ in range(number_of_bet)]
        res = playground_mechanics(bet_opt)
        for _ in bet_opt:
            if res[_] == 0:
                money -= 1*bet_money
            else:
                money += res[_]*bet_money
    return [init_money,money,bet_money,number_of_bet]
    
def game(n=50,m=15,bet_money=10,init_money=100,number_of_bet=1):
    '''進行n局，每一局骰子共丟m下，每一局若最終金額大於初始金額，則記為勝利，反之記為失敗，根據n局結果計算勝率、最終金額期望值。輸出字典[勝率,敗率,金額期望,初始金額,賭注金額,賭注數量]'''
    times = 0
    win = 0
    money_res_lst = []
    lose = 0

    for _ in range(n):
        res = game_bet(m,bet_money,init_money,number_of_bet)
        times += 1
        money_res_lst.append(res[1])
        if res[1] >= res[0]:
            win += 1
        else:
            lose += 1
            
    winrate = win*100/times
    loserate = lose*100/times
    expectation =  mean(money_res_lst)
    sigma = stdev(money_res_lst)
    init_money = res[0]
    bet_money = res[2]
    number_of_bet = res[3]
    
    
    return [winrate,loserate,expectation,init_money,bet_money,number_of_bet,sigma]
    
def main():
    '''調整參數的地方，n是總共試驗多少局，m是每一局丟多少次骰子，bet_money是單次賭注的金額，init_money是初始金額,number_of_bet是賭注數量'''
    n=1000
    m=15
    bet_money=30
    init_money=150
    number_of_bet=1
    
    res = game(n,m,bet_money,init_money,number_of_bet)
    print("-------")
    print("一共模擬 %d 局，每一局骰子骰 %d 次" % (n,m))
    print("-------")
    print("initial money: %d" % res[3])
    print("bet money: %d" % res[4])
    print("number of bet: %d" % res[5])
    print("-------")
    print("winrate(%%): %.1f" % res[0])
    print("loserate(%%): %.1f" % res[1])
    print("expectation: %.2f" % res[2])
    print("standard deviation: %.2f" % res[-1])
    print("-------")
        
if __name__ == '__main__':
    main()