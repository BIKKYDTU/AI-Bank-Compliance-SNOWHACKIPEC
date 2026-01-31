# Deploy BankGuard on Streamlit Community Cloud

Streamlit Cloud needs your code in a **GitHub repository**. Follow these steps.

---

## Step 1: Create a GitHub repository

1. Go to **https://github.com/new**
2. Sign in if needed.
3. Create a **new repository**:
   - **Repository name:** e.g. `AI-Bank-Compliance-SNOWHACKIPEC` or `bankguard`
   - **Public**
   - Do **not** add README, .gitignore, or license (you already have them).
4. Click **Create repository**.
5. Copy the repo URL. It will look like:
   - **HTTPS:** `https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git`
   - **SSH:** `git@github.com:YOUR_USERNAME/YOUR_REPO_NAME.git`

---

## Step 2: Push your code from your PC

Open **PowerShell** or **Command Prompt** and run these commands. Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your GitHub username and repo name.

```powershell
# Go to the project folder (adjust path if your project is elsewhere)
cd "C:\Users\ursha\OneDrive\Desktop\snowhackIPEC01\AI-Bank-Compliance-SNOWHACKIPEC"

# If this folder is not yet a Git repo, run:
git init

# Add GitHub as remote (use YOUR repo URL from Step 1)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# If you already had a remote but wrong URL, fix it with:
# git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Stage all files (data/ is ignored via .gitignore)
git add .

# Commit
git commit -m "Initial commit: BankGuard AI compliance app"

# Push to GitHub (use main or master depending on your default branch)
git branch -M main
git push -u origin main
```

- If GitHub asks for **login**, use a **Personal Access Token** (Settings → Developer settings → Personal access tokens) as the password, or use **GitHub Desktop** / **Git Credential Manager**.
- If you get **"failed to push"** and it says the remote has content (e.g. README), run:
  ```powershell
  git pull origin main --allow-unrelated-histories
  git push -u origin main
  ```

---

## Step 3: Deploy on Streamlit Community Cloud

1. Go to **https://share.streamlit.io**
2. Sign in with **GitHub**.
3. Click **"New app"**.
4. **Repository:** select `YOUR_USERNAME/YOUR_REPO_NAME`.
5. **Branch:** `main` (or `master`).
6. **Main file path:**  
   - If the repo root is the project folder (e.g. only BankGuard files):  
     `frontend/streamlit_app.py`  
   - If the repo contains a subfolder (e.g. repo = snowhackIPEC01 and app is inside AI-Bank-Compliance-SNOWHACKIPEC):  
     `AI-Bank-Compliance-SNOWHACKIPEC/frontend/streamlit_app.py`  
   So: **the path to `streamlit_app.py` from the repo root.**
7. **App URL:** leave default or choose a name.
8. Click **Deploy**.

Streamlit will install from `requirements.txt` in the same folder as `streamlit_app.py`. If your `requirements.txt` is in the repo root, ensure the "Main file path" points to the file inside the same root (e.g. `frontend/streamlit_app.py` and `requirements.txt` both at root). If the app is in a subfolder, put a `requirements.txt` in that subfolder or use "Advanced settings" to set working directory.

---

## Step 4: If the app fails to start

- Check the **logs** in the Streamlit Cloud dashboard.
- Ensure **Python version** is 3.9+ (set in Streamlit Cloud advanced settings if needed).
- Ensure **requirements.txt** is in the same directory as the main file (or set working directory so Streamlit finds it).
- **ChromaDB / HuggingFace:** First run may take a few minutes to download the embedding model; if it times out, try redeploying once.

---

## Summary

| Step | Action |
|------|--------|
| 1 | Create a new **public** repo on GitHub. |
| 2 | In project folder: `git init` → `git remote add origin <URL>` → `git add .` → `git commit` → `git push -u origin main`. |
| 3 | On share.streamlit.io: New app → pick repo & branch → Main file path: `frontend/streamlit_app.py` → Deploy. |

After the repo is pushed, Streamlit Community Cloud can connect to it and deploy.
