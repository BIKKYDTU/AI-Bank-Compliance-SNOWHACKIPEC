# Step-by-step commands: Deploy BankGuard on Streamlit Cloud

Copy and run these in **PowerShell** (Windows). Replace `YOUR_GITHUB_USERNAME` and `ai-bank-compliance-snowhackipec` if your repo name is different.

---

## Step 1: Create the GitHub repo (in browser)

1. Open: **https://github.com/new**
2. **Repository name:** `ai-bank-compliance-snowhackipec` (or any name you like)
3. **Public**
4. Leave **README**, **.gitignore**, **License** unchecked
5. Click **Create repository**
6. Copy the repo URL, e.g. `https://github.com/YOUR_GITHUB_USERNAME/ai-bank-compliance-snowhackipec.git`

---

## Step 2: Open PowerShell and go to project folder

```powershell
cd "C:\Users\ursha\OneDrive\Desktop\snowhackIPEC01\AI-Bank-Compliance-SNOWHACKIPEC"
```

---

## Step 3: Initialize Git (only if not already a repo)

```powershell
git init
```

*(If you see "Reinitialized existing Git repository", that's fine.)*

---

## Step 4: Add the GitHub remote

**Use your actual repo URL from Step 1.**

```powershell
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/ai-bank-compliance-snowhackipec.git
```

If you already added `origin` and want to change it:

```powershell
git remote set-url origin https://github.com/YOUR_GITHUB_USERNAME/ai-bank-compliance-snowhackipec.git
```

---

## Step 5: Stage all files

```powershell
git add .
```

---

## Step 6: Commit

```powershell
git commit -m "Initial commit: BankGuard AI compliance app"
```

*(If you get "nothing to commit", you already committed; skip to Step 7.)*

---

## Step 7: Rename branch to main (if needed)

```powershell
git branch -M main
```

---

## Step 8: Push to GitHub

```powershell
git push -u origin main
```

- If it asks for **username:** your GitHub username  
- If it asks for **password:** use a **Personal Access Token** (not your GitHub password)  
  - Create one: GitHub → Settings → Developer settings → Personal access tokens → Generate new token (classic), tick `repo`, copy the token and paste as password.

If you get **"remote has content"** (e.g. README was added on GitHub):

```powershell
git pull origin main --allow-unrelated-histories
git push -u origin main
```

---

## Step 9: Deploy on Streamlit Cloud (in browser)

1. Go to **https://share.streamlit.io**
2. Sign in with **GitHub**
3. Click **"New app"**
4. **Repository:** `YOUR_GITHUB_USERNAME/ai-bank-compliance-snowhackipec`
5. **Branch:** `main`
6. **Main file path:** `frontend/streamlit_app.py`
7. Click **Deploy**

Streamlit will install from `requirements.txt` and run the app. Your log (`/mount/src/ai-bank-compliance-snowhackipec/`) shows dependencies were installed successfully.

---

## Step 10 (optional): Run locally to test before pushing

```powershell
cd "C:\Users\ursha\OneDrive\Desktop\snowhackIPEC01\AI-Bank-Compliance-SNOWHACKIPEC"
pip install -r requirements.txt
streamlit run frontend/streamlit_app.py
```

Then open **http://localhost:8501** in the browser.

---

## Quick copy-paste block (Steps 2–8)

Replace `YOUR_GITHUB_USERNAME` and repo name, then run all at once:

```powershell
cd "C:\Users\ursha\OneDrive\Desktop\snowhackIPEC01\AI-Bank-Compliance-SNOWHACKIPEC"
git init
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/ai-bank-compliance-snowhackipec.git
git add .
git commit -m "Initial commit: BankGuard AI compliance app"
git branch -M main
git push -u origin main
```

Then do **Step 9** in the browser (share.streamlit.io → New app → select repo → Main file path: `frontend/streamlit_app.py` → Deploy).
