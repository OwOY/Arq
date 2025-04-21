<p style="font-size:100px;text-align:center;color: green">Arq</p>

<br>

## Intro
arq 是一個基於 Python 的輕量級佇列，利用了高效率的庫和可靠的Redis資料儲存。  
這個開源專案由 Samuel Colvin 開發，旨在為開發者提供簡單的機器人的工具來管理後台任務，實現任務調度和梯度執行，從而提高應用效能並解耦複雜的工作流程。

arq 的核心特性在於它結合了非同步程式設計（透過 asyncio）和持久化資料儲存（借助 Redis）。  
這使得 arq 能夠支援大量並發任務，並在進程間共享工作負載，保證任務的有序性和一致性。此外，它還提供了強大的錯誤處理機制，確保即使在任務失敗時也能優雅地恢復。

<br>

## How to use
1. 需要建立兩個伺服器，一個 server(任務佇列伺服器) 以及 main(主程序)  
    ### [server.py](/src/server.py)  
    ### [main.py](/src/main.py)

2. 執行 arq Server
```shell
arq server.WorkerSettings
```
<br>
<br>
3. 任何 main.py 執行的任務都會被丟到 redis，由 server 去做消化  


## 參考來源
[推薦開源項目：Arq 強大的Python異步任務隊列系統](https://blog.csdn.net/gitblog_00027/article/details/138747227)