import os
import shutil
import urllib.request
import zipfile

# إعدادات المستودع
GITHUB_USER = "a360n"
GITHUB_REPO = "IOSPytoTesy"
BRANCH = "main"

# رابط تحميل أرشيف الكود
ZIP_URL = f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}/archive/refs/heads/{BRANCH}.zip"
TARGET_DIR = GITHUB_REPO  # اسم المجلد المحلي


def sync_repository(token: str = None):
    zip_temp = "repo_archive.zip"
    extract_temp = "temp_extracted"

    print(f"🔄 جاري سحب آخر التحديثات من: {GITHUB_USER}/{GITHUB_REPO} ({BRANCH})...")

    try:
        # إعداد الطلب
        req = urllib.request.Request(
            ZIP_URL,
            headers={
                "User-Agent": "Pyto-iOS-Sync",
                **({"Authorization": f"token {token}"} if token else {}),
            },
        )

        # تحميل الأرشيف
        with (
            urllib.request.urlopen(req) as response,
            open(zip_temp, "wb") as out_file,
        ):
            shutil.copyfileobj(response, out_file)
        print("📦 تم التحميل بنجاح. جاري استخراج وتحديث الملفات...")

        # استخراج الملفات
        with zipfile.ZipFile(zip_temp, "r") as zip_ref:
            zip_ref.extractall(extract_temp)

        inner_folder = os.path.join(extract_temp, f"{GITHUB_REPO}-{BRANCH}")

        # استبدال المجلد القديم بالجديد
        if os.path.exists(TARGET_DIR):
            shutil.rmtree(TARGET_DIR)
        shutil.move(inner_folder, TARGET_DIR)

        # تنظيف الملفات المؤقتة
        if os.path.exists(zip_temp):
            os.remove(zip_temp)
        if os.path.exists(extract_temp):
            shutil.rmtree(extract_temp)

        print(f"✨ تم تحديث مجلد '{TARGET_DIR}' بنجاح!")
        print(f"📂 محتويات المجلد الآن: {os.listdir(TARGET_DIR)}")

    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("❌ خطأ 404: تأكد من اسم الفرع أو تأكد هل المستودع Private؟")
            print(
                "💡 إذا كان Private، مرر الـ Personal Access Token في الدالة: sync_repository('YOUR_TOKEN')"
            )
        else:
            print(f"❌ خطأ في الاتصال: {e}")
    except Exception as e:
        print(f"❌ حدث خطأ غير متوقع: {e}")


if __name__ == "__main__":
    # إذا كان المستودع عاماً (Public):
    sync_repository()

    # إذا كان المستودع خاصاً (Private)، ضع التوكن هنا:
    # sync_repository(token="ghp_xxxxxxxxxxxxxxxxxxxx")