import tkinter as tk
from tkinter import messagebox

# ----------------------------
# สร้างหน้าต่างหลัก
# ----------------------------
root = tk.Tk()
root.title("XO Game")
root.geometry("420x500")
root.configure(bg="#1f2937")
root.resizable(False, False)

# โหลดไอคอน
try:
    root.iconbitmap("icon.ico")
except:
    pass

current_player = "X"
board = [""] * 9
buttons = []
def rungame():
    # ----------------------------
    # ฟังก์ชันตรวจสอบผู้ชนะ
    # ----------------------------
    def check_winner():
        wins = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]

        for a,b,c in wins:
            if board[a] == board[b] == board[c] != "":
                return board[a]

        if "" not in board:
            return "Draw"

        return None

    # ----------------------------
    # รีเซ็ตเกม
    # ----------------------------
    def reset_game():
        global current_player, board

        current_player = "X"
        board = [""] * 9

        status.config(text="ตาของ X")

        for btn in buttons:
            btn.config(text="", bg="#374151")

    # ----------------------------
    # เมื่อกดปุ่ม
    # ----------------------------
    def click(index):
        global current_player

        if board[index] != "":
            return

        board[index] = current_player

        color = "#38BDF8" if current_player == "X" else "#F43F5E"

        buttons[index].config(
            text=current_player,
            fg=color
        )

        winner = check_winner()

        if winner:

            if winner == "Draw":
                messagebox.showinfo("จบเกม", "เสมอ")
            else:
                messagebox.showinfo("จบเกม", f"{winner} ชนะ!")

            reset_game()
            return

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

        status.config(text=f"ตาของ {current_player}")

    # ----------------------------
    # หัวข้อ
    # ----------------------------
    title = tk.Label(
        root,
        text="TIC TAC TOE",
        font=("Arial",26,"bold"),
        bg="#1f2937",
        fg="#22D3EE"
    )

    title.pack(pady=15)

    status = tk.Label(
        root,
        text="ตาของ X",
        font=("Arial",15,"bold"),
        bg="#1f2937",
        fg="white"
    )

    status.pack()

    frame = tk.Frame(root,bg="#1f2937")
    frame.pack(pady=20)

    # ----------------------------
    # ปุ่มเกม
    # ----------------------------
    for i in range(9):

        btn = tk.Button(
            frame,
            text="",
            width=5,
            height=2,
            font=("Arial",28,"bold"),
            bg="#374151",
            fg="white",
            activebackground="#4B5563",
            relief="flat",
            command=lambda i=i: click(i)
        )

        btn.grid(
            row=i//3,
            column=i%3,
            padx=5,
            pady=5
        )

        buttons.append(btn)

    # ----------------------------
    # ปุ่มรีเซ็ต
    # ----------------------------
    reset_btn = tk.Button(
        root,
        text="เริ่มใหม่",
        font=("Arial",14,"bold"),
        bg="#22C55E",
        fg="white",
        width=15,
        command=reset_game
    )

    reset_btn.pack(pady=20)

    # ----------------------------
    # เริ่มโปรแกรม
    # ----------------------------
    root.mainloop()
if __name__ == "__main__":
    rungame()