import sys
import time
import json

class GibworkSDK:
    """
    محاكاة لحزمة تطوير البرمجيات (SDK) الخاصة بمنصة Gibwork
    للإتصال المباشر بنقاط النهاية (API Endpoints) وجلب البيانات.
    """
    def __init__(self, api_key="gw_live_sample_key"):
        self.api_key = api_key
        self.base_url = "https://api.gibwork.com/v1"

    def get_tasks(self):
        print(f"[*] Authenticating with API Key: {self.api_key[:6]}...")
        time.sleep(1)
        print("[*] Fetching live tasks from Gibwork server endpoints...")
        time.sleep(1)
        
        # بيانات افتراضية تمثل الاستجابة الحقيقية من خوادم Gibwork عبر الـ API
        return [
            {"id": 201, "title": "Build a robust Python CLI tool for task automation", "category": "Development", "reward": "$400"},
            {"id": 202, "title": "Like and share our latest tweet on X", "category": "Marketing", "reward": "$15"},
            {"id": 203, "title": "Implement Web3 smart contract security tests", "category": "Development", "reward": "$600"},
            {"id": 204, "title": "Join our Telegram community channel", "category": "Social", "reward": "$10"},
            {"id": 205, "title": "Develop an automated database backup utility in Python", "category": "Backend", "reward": "$250"}
        ]

class TaskFilterEngine:
    """
    محرك التصفية المتقدم (CLI Core Logic) لإزالة المهام التسويقية والاجتماعية
    """
    def __init__(self, tasks):
        self.tasks = tasks
        self.spam_keywords = ["twitter", "retweet", "follow", "marketing", "social", "like", "telegram"]

    def execute_filter(self):
        clean_tasks = []
        for task in self.tasks:
            title_lower = task["title"].lower()
            if not any(word in title_lower for word in self.spam_keywords):
                clean_tasks.append(task)
        return clean_tasks

def main():
    print("=" * 60)
    print("🚀 Gibwork Enterprise SDK & CLI Task Filter - v2.0")
    print("=" * 60)
    
    # 1. تهيئة الـ SDK وجلب البيانات عبر الـ API
    sdk = GibworkSDK(api_key="gw_live_secret_key_98765")
    raw_tasks = sdk.get_tasks()
    
    # 2. تطبيق خوارزمية التصفية عبر محرك الـ CLI
    engine = TaskFilterEngine(raw_tasks)
    filtered_tasks = engine.execute_filter()
    
    # 3. عرض النتائج النهائية بشكل منظم واحترافي
    print(f"\n[+] Total Raw Tasks Fetched: {len(raw_tasks)}")
    print(f"[+] Filtered Out (Spam / Marketing): {len(raw_tasks) - len(filtered_tasks)}")
    print(f"✅ High-Value Technical Tasks Ready for Execution: {len(filtered_tasks)}\n")
    print("-" * 60)
    
    for task in filtered_tasks:
        print(f"📌 Task ID: {task['id']}")
        print(f"   Title:    {task['title']}")
        print(f"   Category: {task['category']} | Reward: {task['reward']}")
        print("-" * 60)

if __name__ == "__main__":
    main()
