# shaibao_result_simulator
簡易型的骰寶結果模擬器

## 骰寶介紹
為一款簡易的賭博遊戲，棋盤為一個畫上1-6的紙，玩家在莊家動作之前將賭注押在他認為骰子會落點的數字（可押一或多），而後莊家擲3個骰子，若骰子的結果中有n個與玩家下注的數字相同的，則玩家掙n倍，否則莊家拿錢。

## 功能
1. 設定下注金額、數量（但一次只能設一種注的類型）
2. 設定模擬次數、單局莊家動作次數
3. 顯示n局後金額期望值與標準差

## 模擬結果示例
設
```Python
    n=1000
    m=15
    bet_money=30
    init_money=150
    number_of_bet=1
```
其中n為局數，m為單局莊家擲骰子的輪數，得到如下結果：
```
-------
一共模擬 1000 局，每一局骰子骰 15 次
-------
initial money: 150
bet money: 30
number of bet: 1
-------
winrate(%): 43.9
loserate(%): 56.1
expectation: 120.39
standard deviation: 130.33
-------
```

## 函數說明
1. `playground_mechanics(n:list,dice_number=3)`

處理棋盤上的骰子和押注機制，輸出字典 [號碼:數量] 

2. `game_bet(m=100,bet_money=10,init_money=100,number_of_bet=1)`

骰子甩m次（稱為一局），由棋盤輸出的結果進行錢的演算，輸出字典 [初始金額,最終金額,賭注額度,賭注數量]

3. `game(n=50,m=15,bet_money=10,init_money=100,number_of_bet=1)`

進行n局，每一局骰子共丟m下，每一局若最終金額大於初始金額，則記為勝利，反之記為失敗，根據n局結果計算勝率、最終金額期望值。輸出字典[勝率,敗率,金額期望,初始金額,賭注金額,賭注數量]

4. `main()`

調整參數的地方，n是總共試驗多少局，m是每一局丟多少次骰子，bet_money是單次賭注的金額，init_money是初始金額,number_of_bet是賭注數量

