"""
八皇后问题求解程序
问题描述：在8×8的国际象棋棋盘上放置8个皇后，使得任意两个皇后都不能互相攻击
（即任意两个皇后不能处于同一行、同一列或同一斜线上），输出所有可行解法并统计总数。
"""

def solve_n_queens(n):
    """
    求解n皇后问题
    :param n: 棋盘大小/皇后数量
    :return: 所有可行解法的列表，每个解法是一个列表，下标代表行号，值代表该行皇后所在的列号
    """
    solutions = []
    # 分别记录已使用的列、主对角线（行-列固定）、副对角线（行+列固定）
    used_cols = set()
    used_diag1 = set()  # 主对角线：row - col 相等
    used_diag2 = set()  # 副对角线：row + col 相等

    def backtrack(row, current_placement):
        """
        回溯函数，逐行放置皇后
        :param row: 当前处理的行号
        :param current_placement: 已经放置的皇后位置列表
        """
        # 递归终止条件：所有行都处理完毕，找到一个可行解
        if row == n:
            solutions.append(current_placement.copy())
            return
        
        # 尝试在当前行的每一列放置皇后
        for col in range(n):
            # 检查当前列和两条对角线是否已经被占用
            diag1_key = row - col
            diag2_key = row + col
            if col in used_cols or diag1_key in used_diag1 or diag2_key in used_diag2:
                continue  # 冲突，跳过当前列
            
            # 放置皇后，标记已使用的列和对角线
            used_cols.add(col)
            used_diag1.add(diag1_key)
            used_diag2.add(diag2_key)
            current_placement.append(col)
            
            # 递归处理下一行
            backtrack(row + 1, current_placement)
            
            # 回溯，撤销当前选择
            used_cols.remove(col)
            used_diag1.remove(diag1_key)
            used_diag2.remove(diag2_key)
            current_placement.pop()
    
    # 从第0行开始回溯
    backtrack(0, [])
    return solutions

def print_solution(solution):
    """
    打印单个解法的棋盘样式
    :param solution: 单个解法的位置列表
    """
    n = len(solution)
    for row in range(n):
        line = []
        for col in range(n):
            if solution[row] == col:
                line.append("Q ")
            else:
                line.append(". ")
        print("".join(line))
    print("\n")

if __name__ == "__main__":
    N = 8
    all_solutions = solve_n_queens(N)
    print(f"八皇后问题总共有 {len(all_solutions)} 种解法\n")
    
    # 可以选择打印所有解法，这里默认只打印前3种示例
    print("前3种解法示例：\n")
    for i, sol in enumerate(all_solutions[:3]):
        print(f"解法 {i+1}:")
        print_solution(sol)
