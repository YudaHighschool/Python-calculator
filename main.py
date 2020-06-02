# 導入 browser 的 document 及 html 物件
from browser import document, html

# 建立計算機 HTML Table 版型
# |   結果    | c |
# | 7 | 8 | 9 | / |
# | 4 | 5 | 6 | * |
# | 1 | 2 | 3 | - |
# | 0 | . | = | + |

calc = html.TABLE()
calc <= html.TR(html.TH(html.DIV("0", id="result"), colspan=3) + html.TD("C"))
lines = ["789/", "456*", "123-", "0.=+"]

calc <= (html.TR(html.TD(x) for x in line) for line in lines)

document <= calc

# 用 id: result 取得 結果欄 
result = document["result"] # direct acces to an element by its id

# action 函式：處理 click 事件
def action(event):
    # 事件的來源物件是 event.target
    element = event.target
    # 來源物件的文字為 element.text
    value = element.text
    if value not in "=C":
        # 點選數字或 +, =, *, /，將點選值加入公式
        if result.text in ["0", "error"]:
            result.text = value
        else:
            result.text = result.text + value
    elif value == "C":
        # 點選 C，重設結果欄
        result.text = "0"
    elif value == "=":
        # 點選 =，計算 result.text 內的公式，並將結果放置結果欄
        try:
            result.text = eval(result.text)
        except:
            result.text = "error"

# 將 action() 函式與 計算機內的 td 標籤按鈕 結合
for button in document.select("td"):
    button.bind("click", action)
