import pyautogui
import pyperclip
import time
import keyboard
import sys

# --- 設定座標 (請根據你的螢幕解析度修改) ---
COORD_BATCH_MOVE = (1269, 228) #點擊模組的批量移動鈕
   
# 設定每個 pyautogui 指令之間的預設延遲 (秒)
pyautogui.PAUSE = 0.3

# 避免死循環導致無法正確存入綠寶，加入全局變數來控制循環狀態
target_x, target_y = 958, 226
variable_A, variable_B = (0, 0, 0), (0, 0, 0)


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
    
    print("正在等待 5 秒，請將準星對準界伏盒...")
    safe_sleep(5)

    try:
        while True:
            check_exit()
            print("1. 右鍵點擊開啟界伏盒")
            pyautogui.rightClick()

            # 保險機制
            print("2. 正在記錄 A 時間點的顏色...")
            variable_A = pyautogui.pixel(target_x, target_y)
            print(f"變數 A (RGB): {variable_A}")
            
            check_exit()
            print(f"3. 點擊批量移動鈕: {COORD_BATCH_MOVE}")
            # 先將滑鼠移到目標位置，避免移動中點擊失誤
            pyautogui.moveTo(COORD_BATCH_MOVE[0], COORD_BATCH_MOVE[1], duration=0.2)

            # 依序執行組合動作
            pyautogui.keyDown('shift')
            safe_sleep(0.1)           # 等待系統辨識 Shift
            pyautogui.mouseDown()     # 按下鼠標左鍵
            safe_sleep(0.1)           # 保持按下一小段時間
            pyautogui.mouseUp()       # 放開鼠標左鍵
            safe_sleep(0.1)           # 確保點擊動作完成
            pyautogui.keyUp('shift')

            # 檢查 B 時間點的顏色是否「接近」變數 A，允許 10 度的色差 (tolerance)
            # 如果是，則必須按下 "e" 鍵關閉背包
            print("正在檢查 B 時間點的顏色是否接近 A...")
            if pyautogui.pixelMatchesColor(target_x, target_y, variable_A, tolerance=10):
                print("B 時間點的顏色接近 A，按下 'e' 鍵跳出界面")
                pyautogui.press('e')
            
            check_exit()
            print("4. 輸入 '/'")
            pyautogui.press('/')

            check_exit()
            print("貼上 'moneysave'")
            pyperclip.copy("moneysave")
            safe_sleep(0.1)
            pyautogui.hotkey('ctrl', 'v')
            safe_sleep(0.1)

            # 按下 "enter"
            check_exit()
            print("5. 按下 'Enter'")
            pyautogui.press('enter')
            safe_sleep(0.1)

            print(f"正在記錄 B 時間點的顏色...")
            variable_B = pyautogui.pixel(target_x, target_y)
            print(f"變數 B (RGB): {variable_B}")
            
            safe_sleep(0.3)

    except (KeyboardInterrupt, SystemExit):
        print("\n腳本已停止。")
    except Exception as e:
        print(f"\n發生錯誤: {e}")

if __name__ == "__main__":
    run_script()