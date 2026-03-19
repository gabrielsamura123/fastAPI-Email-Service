# Render Deployment Guide - FastAPI Email Service

Follow these steps to deploy your backend to [Render](https://render.com).

## 1. Prepare Your Repository
- Ensure your code is pushed to a GitHub or GitLab repository.
- Your project structure should look like this:
  ```
  / (root)
  ├── app/
  │   ├── Email_Service/
  │   │   ├── main_email.py
  │   │   ├── requirements.txt
  │   │   └── ...
  ```

## 2. Create a Web Service on Render
- Log in to your Render dashboard.
- Click **New +** and select **Web Service**.
- Connect your GitHub/GitLab repository.

## 3. Configure the Web Service
- **Name**: `fastapi-email-service` (or your choice)
- **Environment**: `Python 3`
- **Build Command**: `pip install -r app/Email_Service/requirements.txt`
- **Start Command**: `uvicorn app.Email_Service.main_email:email_app --host 0.0.0.0 --port 10000`

## 4. Set Environment Variables
Go to the **Environment** tab in your Render service and add the following:
- `MAIL_USERNAME`: `mohamedk@yozservices.com`
- `MAIL_PASSWORD`: `Yoz@1234y` (Use your actual password)
- `MAIL_FROM`: `mohamedk@yozservices.com`
- `DATABASE_URL`: Your PostgreSQL connection string (Render provides a managed PostgreSQL service you can use).

## 5. Security Note
> [!WARNING]
> Never commit your passwords to GitHub. Use the **Environment Variables** section in Render to store sensitive data. I recommend refactoring the code to use `os.getenv()` as outlined in the `deployment_plan.md`.

## 6. Database (Optional)
If you need a database:
- Create a **New PostgreSQL** instance on Render.
- Copy the **Internal Database URL** and paste it into the `DATABASE_URL` environment variable of your Web Service.
