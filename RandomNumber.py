import tkinter as tk
import random

# Whitelist (直接在代码中设置)
whitelist = [13, 20, 42]  # 可以在这里添加任何需要的白名单数字

def generate_random_number():
    try:
        max_num = int(entry_max.get())
        min_num = int(entry_min.get())

        if max_num <= min_num:
            error_message = "最大数必须大于最小数"
            label_result.config(text=error_message)

            return
        
        # 开始跳数字效果
        start_jumping(min_num, max_num)
        
    except ValueError:
        error_message = "请输入有效的数字"
        label_result.config(text=error_message)


def start_jumping(min_num, max_num):
    # 每隔100ms更新显示的随机数字
    jumps = 10  # 跳动次数
    jump_random_number(min_num, max_num, jumps)

def jump_random_number(min_num, max_num, jumps_left):
    if jumps_left > 0:
        # 生成一个随机数字（动画中使用的数字）
        random_num = random.randint(min_num, max_num)
        label_result.config(text=f"跳动的数字: {random_num}")
    
        
        # 延迟100毫秒后再次调用自己，制造跳动效果
        window.after(100, jump_random_number, min_num, max_num, jumps_left - 1)
    else:
        # 结束跳动，生成最终随机数
        show_final_random_number(min_num, max_num)

def show_final_random_number(min_num, max_num):
    # 生成最终的随机数，确保不在白名单中
    final_num = random.randint(min_num, max_num)
    while final_num in whitelist:
        final_num = random.randint(min_num, max_num)
    
    # 显示最终的随机数
    label_result.config(text=f"随机数是：{final_num}")

# 创建主窗口
window = tk.Tk()
window.title("现代随机数生成器")

# 设置窗口大小 720x480
window.geometry("720x480")

# 设置现代化的背景颜色
window.configure(bg='#2E4053')

# 设置最大数输入框及标签
label_max = tk.Label(window, text="请输入最大数：", font=("Helvetica", 16), bg='#2E4053', fg='white')
label_max.pack(pady=10)

entry_max = tk.Entry(window, font=("Helvetica", 14), justify='center', relief='flat', bg='#F2F3F4', fg='#2C3E50', borderwidth=2)
entry_max.pack(pady=10, ipady=5, ipadx=20)

# 设置最小数输入框及标签
label_min = tk.Label(window, text="请输入最小数：", font=("Helvetica", 16), bg='#2E4053', fg='white')
label_min.pack(pady=10)

entry_min = tk.Entry(window, font=("Helvetica", 14), justify='center', relief='flat', bg='#F2F3F4', fg='#2C3E50', borderwidth=2)
entry_min.pack(pady=10, ipady=5, ipadx=20)

# 创建按钮样式
button_style = {
    "font": ("Helvetica", 14),
    "bg": "#58D68D",
    "fg": "white",
    "activebackground": "#45B39D",
    "activeforeground": "white",
    "relief": "flat",
    "borderwidth": 0,
    "width": 15,
    "height": 2
}

# 创建按钮，点击后生成随机数
button_generate = tk.Button(window, text="生成随机数", command=generate_random_number, **button_style)
button_generate.pack(pady=30)

# 显示随机数的标签
label_result = tk.Label(window, text="", font=("Helvetica", 16), bg='#2E4053', fg='#58D68D')
label_result.pack(pady=20)

# 运行主循环
window.mainloop()
