from pykiwoom.kiwoom import *
import time

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

# 주식계좌
accounts = kiwoom.GetLoginInfo("ACCNO")
stock_account = accounts[0]

# 매수 Test
# kiwoom.SendOrder("시장가매수", "0101", stock_account, 1, "005930", 1, 0, "03", "")

# 조건식 load
kiwoom.GetConditionLoad()
conditions = kiwoom.GetConditionNameList()
print(conditions)

# 0번 조건식에 해당하는 종목 리스트 출력
condition_index = conditions[0][0]
condition_name = conditions[0][1]
print(condition_index, condition_name)
codes = kiwoom.SendCondition("0101", condition_name, condition_index, 0)
print(codes)

# 조건식 종목, 시장가주문 매수
for code in codes:
    kiwoom.SendOrder("시장가매수", "0101", stock_account, 1, code, 1, 0, "03", "")
    time.sleep(0.2)
    print(code, "매수 완료")



