//
// Created by 蔡颖坤 on 2026/4/29.
//
#include <vector>
using namespace std;

class Solution {
public:
    // AP 覆盖的 3×3 方向
    int dx[9] = {-1,-1,-1, 0,0,0, 1,1,1};
    int dy[9] = {-1,0,1, -1,0,1, -1,0,1};

    int row, col;                // 网格行数、列数
    vector<vector<char>> g;      // 网格地图
    vector<vector<int>> ap_cover;// 预处理：每个AP覆盖哪些格子
    int best;                    // 最优解：最少AP数量

    // ==============================
    // 剪枝策略：选【可选AP最少】的未覆盖空地
    // 你思路里写的：显著减少分支，让搜索飞快
    // ==============================
    int findLeastChoicePos(vector<bool>& vis) {
        int minCnt = 1e9, pos = -1;

        // 遍历所有格子
        for (int i = 0; i < row*col; i++) {
            int x = i / col;
            int y = i % col;

            // 只看【未覆盖的空地】
            if (g[x][y] != '.' || vis[i]) continue;

            // 统计：有多少个AP【能覆盖它】且【不冲突】
            int cnt = 0;
            for (auto& cov : ap_cover) {
                bool ok = true;
                for (int p : cov) if (vis[p]) { ok = false; break; }
                if (ok) for (int p : cov) if (p == i) { cnt++; break; }
            }

            // 这个空地永远无法覆盖 → 无解
            if (cnt == 0) return -2;

            // 找【可选最少】的
            if (cnt < minCnt) {
                minCnt = cnt;
                pos = i;
            }
        }
        return pos;
    }

    // ==============================
    // DFS 核心：完全按你思路实现
    // 1. 选一个未覆盖空地
    // 2. 枚举能覆盖它的AP
    // 3. 不冲突就选
    // 4. 更新最优解
    // ==============================
    void dfs(vector<bool> vis, int cnt) {
        // 剪枝：当前数量已不优于最优解 → 直接返回
        if (cnt >= best) return;

        // 挑选：可选AP最少的空地（你写的关键优化）
        int p = findLeastChoicePos(vis);

        // 全部覆盖 → 更新最优
        if (p == -1) {
            best = cnt;
            return;
        }
        // 无解
        if (p == -2) return;

        // 枚举所有能覆盖这个空地的AP
        for (auto& cov : ap_cover) {
            // 判断：AP覆盖区是否和已选区域冲突（不能重叠）
            bool conflict = false;
            for (int cell : cov) {
                if (vis[cell]) {
                    conflict = true;
                    break;
                }
            }
            if (conflict) continue;

            // 判断：这个AP能否覆盖当前选中的空地
            bool canCover = false;
            for (int cell : cov) {
                if (cell == p) {
                    canCover = true;
                    break;
                }
            }
            if (!canCover) continue;

            // 选择这个AP → 标记覆盖
            for (int cell : cov) vis[cell] = true;

            // 继续搜索
            dfs(vis, cnt + 1);

            // 回溯：撤销选择
            for (int cell : cov) vis[cell] = false;
        }
    }

    // ==============================
    // 主函数：完全按你思路
    // 1. 枚举所有合法AP位置
    // 2. 预处理每个AP覆盖哪些格子
    // 3. DFS搜索最少AP
    // ==============================
    int networkPlanning(vector<vector<char>>& roomArrangement) {
        g = roomArrangement;
        row = g.size();
        if (row == 0) return -1;
        col = g[0].size();
        best = 1e9;
        ap_cover.clear();

        // ========= 预处理所有可放AP的位置（所有空地）=========
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (g[i][j] == '.') { // 只有空地能放AP
                    vector<int> cover;
                    // 记录这个AP覆盖的所有格子
                    for (int d = 0; d < 9; d++) {
                        int x = i + dx[d];
                        int y = j + dy[d];
                        if (x >= 0 && x < row && y >= 0 && y < col) {
                            cover.push_back(x * col + y);
                        }
                    }
                    ap_cover.push_back(cover);
                }
            }
        }

        // 开始DFS搜索
        vector<bool> vis(row * col, false);
        dfs(vis, 0);

        // 最优解仍为无穷大 → 无法覆盖，返回-1
        return best == 1e9 ? -1 : best;
    }
};

