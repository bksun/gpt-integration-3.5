from openai import AzureOpenAI

access_to_resource=AzureOpenAI(
    azure_endpoint="https://sunilopenai.openai.azure.com/",
    api_key="ac4cb79f60ab482aa9d60e3e72d90d4b",
    api_version="2023-09-01-preview"
)



response=access_to_resource.chat.completions.create(
    model='sunilgpt35-162',
    temperature=0.7,
    max_tokens=120,
    messages=[
        {'role':"system",'content':'Act as a Makeup expert'},
        {'role':'user','content':'What FMCG Stock to buy?'},
        {'role':'assistant','content':'Buy ITC Stock'},
        {'role':'user','content':'What Defence Stock to buy?'},
        {'role':'assistant','content':'Buy HAL Stock'},
        {'role':'user','content':'What Energy Stock to buy?'}
    ]

)

print(response.choices[0].message.content)