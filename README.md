# EchoBot

This project is a slightly modified version of the original code to support deployment in the Azure Bot environment.

[Original code repository](https://github.com/microsoft/botframework-emulator)

---

## Test Locally Using Bot Framework Emulator

1. Install **Python 3.11** in your local environment.
2. Clone this repository.
3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
    - On **Windows**:

      ```bash
      .\venv\Scripts\activate
      ```

    - On **macOS/Linux**:

      ```bash
      source venv/bin/activate
      ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Start the bot:

    ```bash
    python app.py
    ```

7. Launch the **Bot Framework Emulator**.
8. Go to **File > Open Bot**.
9. Enter the Bot URL:  
   `http://localhost:3978/api/messages`

---

## Deploy to Azure

### 1. Create Azure Web App

- Go to the [Azure Portal](https://portal.azure.com).
- Create a **Web App** with the following settings:
  - **OS**: Linux  
  - **Runtime stack**: Python 3.11  
  - **Pricing tier**: Free (F1)

### 2. Configure Azure Web App

#### a. Platform Settings

- Navigate to **Settings > Configuration > Platform settings**.
- Enable:
  - **SCM Basic Auth Publishing**
  - **FTP Basic Auth Publishing**

#### b. Deployment Settings

- Go to **Deployment > Deployment Center > Settings**.
- Under **Source Control**, select **Local Git**.
- Copy the **Git Clone URL**.
- Under **Local Git/FTPS Credentials**, select **Application Scope**.
- Copy the **Username** and **Password**.

### 3. Create Azure Bot Resource

- Create a new **Azure Bot**:
  - **Type**: Multi-Tenant  
  - **Pricing tier**: Free (F0)
- Go to **Settings > Configuration > Microsoft App ID > Manage Password**.
- Generate a new **Client Secret** (password).

### 4. Set Environment Variables

- Go to your **Web App > Settings > Configuration > Application settings**.
- Add the following environment variables:

    | Name                   | Value                         |
    |------------------------|-------------------------------|
    | `MicrosoftAppId`       | `<Your Azure Bot App ID>`     |
    | `MicrosoftAppPassword` | `<Your Azure Bot App Password>` |
    | `MicrosoftAppTenantId` | `<Your Azure Bot Tenant ID>`  |
    | `MicrosoftAppType`     | `MultiTenant`                 |

### 5. Deploy to Azure

```bash
git remote add azure <Git Clone URL>
git push azure main:master
```

### 6. Test Bot
- Go to your Bot resource.
- Navigate to Settings > Test in Web Chat.

### 7. Debug
- Go to your Web App resource.
- Navigate to Monitoring > Log stream.