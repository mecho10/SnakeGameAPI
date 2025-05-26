# SnakeGameAPI

https://gameapi-p2vx.onrender.com/

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
- 原生 JavaScript + HTML5 Canvas
- Render 部署

## 部署狀態

- 2025-05-26成功部署至 Render，網站正常運作 
- 修正了部署時的環境變數設定問題  
- 部署過程中遇到的錯誤已解決  
- 雖然成功部署但還有很多地方需要優化
  
- **待優化的部分**  
  - 遊戲動畫速度快的離譜！！根本是地獄模式的貪吃蛇（在不同瀏覽器或部署環境中有不同的執行效率，或可能是時間間隔沒設對。）
  - 註冊功能的響應時間較長，使用者等待較久  
  - 登入功能的響應時間也需優化，提升使用體驗  

# 遇到的問題與解法

1.Build 失敗
**原因**：第一次嘗試部署，對平台的不熟悉，部署時在 Build 階段出錯，導致無法成功完成部署，花了一整天時間嘗試排除問題
  - 環境變數設定錯誤或遺漏  
  - 依賴套件版本不相容  
  - Build 指令配置錯誤  
  - Render 平台特殊設定不熟悉  等等...
**解法**  
  - 詳細檢查並修正環境變數  
  - 重新安裝並鎖定套件版本  
  - 修正 Build 指令與流程  
  - 參考官方文件與社群討論  

2.登入後上傳分數失敗
**原因**：JWT token 未儲存或未加到 Header。  
**解法**：確認登入成功後有將 token 存入 `localStorage`，並加上：

```
js
headers: {
  'Authorization': 'Bearer ' + accessToken
}
```
3.排行榜顯示錯誤或為空
- 沒有使用者上傳過分數
- `/api/rankings/` API 設計問題

**解法**：確保分數成功上傳後再呼叫 `loadRankings()`。

4.staticfiles 資料夾沒有內容

**原因**：忘記執行 `collectstatic`  
**解法**：執行

5.無法正確連接資料庫
**原因**：環境變數設定錯誤
**解法**：到 Render Dashboard → Environment Variables 頁面設定所有需要的變數

```bash
python manage.py collectstatic --noinput
```

**心得分享**  
  部署過程雖然辛苦，但透過不斷嘗試與學習，解決了不少問題。對於初次部署的開發者，建議務必耐心，且多善用官方文件與社群資源以及萬能的chatGPT。
  
# 作者
Made by **Leroy Chang**  
GitHub: [@your-github-username](https://github.com/your-github-username)
