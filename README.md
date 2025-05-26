# SnakeGameAPI
使用 Django + JWT 認證 + 貪食蛇遊戲前端的全端小專案。
這是一個結合 Django REST Framework 與 JavaScript 前端的貪食蛇遊戲，實作使用者註冊、登入、分數儲存與排行榜查詢。使用 JWT 驗證並部署至 Render，全端功能完整。
第一次嘗試開發完整專案

# 專案結構
```
gameapi/
├── gameapi/             # Django 專案設定
│   └── settings.py
├── users/               # 使用者 App
├── static/              # 放置 snake_game_fixed.html
│   └── snake_game.html
├── manage.py
├── requirements.txt
├── render.yaml
├── Procfile
└── .gitignore
```

# 技術棧
- Django 5.2.1
- Django REST Framework
- Simple JWT
- SQLite（開發用）
- 原生 JavaScript + HTML5 Canvas
- Render 部署

# 遇到的問題與解法
1.登入後上傳分數失敗
**原因**：JWT token 未儲存或未加到 Header。  
**解法**：請確認登入成功後有將 token 存入 `localStorage`，並加上：

```js
headers: {
  'Authorization': 'Bearer ' + accessToken
}

2.排行榜顯示錯誤或為空
- 沒有使用者上傳過分數
- `/api/rankings/` API 設計問題

**解法**：確保分數成功上傳後再呼叫 `loadRankings()`。

3.staticfiles 資料夾沒有內容

**原因**：忘記執行 `collectstatic`  
**解法**：執行：

```bash
python manage.py collectstatic --noinput
```
# 作者
Made by **Leroy Chang**  
GitHub: [@your-github-username](https://github.com/your-github-username)
