# RagBot

**RagBot** is a sample chatbot using Retrieval-Augmented Generation (RAG) with the Microsoft Bot Framework and OpenAI services.


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

6. Set up environment variables
- Create a **.env** file in the root directory with the following content:

    ```bash
    OpenAIApiKey=<your OpenAI key>
    OpenAIEndpoint=<your OpenAI Endpoint>
    OpenAIApiVersion=<your OpenAI version>
    OpenAIDeployment=<your OpenAI deployment>
    ```

7. Start the bot:

    ```bash
    python app.py
    ```

8. Launch the **Bot Framework Emulator**.
9. Go to **File > Open Bot**.
10. Enter the Bot URL:  
   `http://localhost:3978/api/messages`

---

## Deploy to Azure

- To deploy this bot to Azure, follow the instructions in the  [EchoBot Azure Deployment README](https://github.com/Misaki19840/python_echo_bot)