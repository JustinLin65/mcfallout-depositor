import pyautogui
import time
import keyboard
import sys

# --- 設定座標 (請根據你的螢幕解析度修改) ---
COORD_A = (958, 519)  #開盒
COORD_B = (1269, 228) #按住Shift移動綠寶

# 設定每個 pyautogui 指令之間的預設延遲 (秒)
pyautogui.PAUSE = 0.5

def check_exit():
    """檢查是否按下了 Esc 鍵，若是則立即退出程式"""
    if keyboard.is_pressed('esc'):
        print("\n[偵測到 Esc 鍵] 正在停止腳本並釋放按鍵...")
        pyautogui.keyUp('shift')
        sys.exit(0)

def safe_sleep(seconds):
    """具備 Esc 監聽功能的等待函數"""
    start_time = time.time()
    while time.time() - start_time < seconds:
        check_exit()
        time.sleep(0.1)

def run_script():
    # 開啟安全機制：將滑鼠移至螢幕最左上角也可強制停止
    pyautogui.FAILSAFE = True

    print("=== Depositor 已啟動 ===")
    print("提示：隨時按下 'Esc' 鍵可立即停止腳本。")
    
    loop_count = 0
    
    try:
        while True:
            print("1. 正在等待 5 秒，請切換到遊戲畫面...")
            safe_sleep(5)

            check_exit()
            print(f"2. 右鍵點擊座標 A: {COORD_A}")
            pyautogui.rightClick(COORD_A[0], COORD_A[1])

            check_exit()
            print(f"3. 按住 Shift 點擊座標 B: {COORD_B}")
            # 先將滑鼠移到目標位置，避免移動中點擊失誤
            pyautogui.moveTo(COORD_B[0], COORD_B[1], duration=0.2)
            safe_sleep(0.1)
            
            # 依序執行組合動作
            pyautogui.keyDown('shift')
            safe_sleep(0.1)           # 等待系統辨識 Shift
            pyautogui.mouseDown()     # 按下鼠標左鍵
            safe_sleep(0.1)           # 保持按下一小段時間
            pyautogui.mouseUp()       # 放開鼠標左鍵
            safe_sleep(0.1)           # 確保點擊動作完成
            pyautogui.keyUp('shift')
            safe_sleep(0.1)

            check_exit()
            print("4. 輸入 '/'")
            pyautogui.press('/')

            check_exit()
            print("5. 輸入 'moneysave'")
            pyautogui.press('m')
            pyautogui.press('o')
            pyautogui.press('n')
            pyautogui.press('e')
            pyautogui.press('y')
            pyautogui.press('s')
            pyautogui.press('a')
            pyautogui.press('v')
            pyautogui.press('e')

            check_exit()
            print("6. 按下 'Enter'")
            pyautogui.press('enter')
            safe_sleep(0.1)
            
            safe_sleep(0.3)

    except (KeyboardInterrupt, SystemExit):
        print("\n腳本已停止。")
    except Exception as e:
        print(f"\n發生錯誤: {e}")

if __name__ == "__main__":
    run_script()