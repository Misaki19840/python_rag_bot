from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount
from openai import AzureOpenAI
from rag.retriever import FAISSRetriever

class EchoBot(ActivityHandler):
    def __init__(self, config):
        self.config = config
        self.client = AzureOpenAI(
            api_key=config.OPENAI_API_KEY,
            api_version=config.OPENAI_API_VERSION,
            azure_endpoint=config.OPENAI_ENDPOINT
        )
        self.retriever = FAISSRetriever("rag/corpus.txt")

    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")
    
    async def on_message_activity(self, turn_context: TurnContext):
        user_input = turn_context.activity.text
        docs = self.retriever.query(user_input, top_k=3)
        context = "\n".join(docs)

        prompt = f"Answer based on the following documents:\n\n{context}\n\nQuestion: {user_input}"

        response = self.client.chat.completions.create(
            model=self.config.OPENAI_DEPLOYMENT,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1024,
            temperature=0.7,
            top_p=1.0
        )

        answer = response.choices[0].message.content
        await turn_context.send_activity(answer)
