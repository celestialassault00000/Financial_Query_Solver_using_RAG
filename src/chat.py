from src.load_Cohere import co 
from src.retriever import retriever
def query_builder(retieved_Context, user_query):
    input_json = {"user_query": user_query, "context": retieved_Context}
    s=""" Attached below is the json format which consists of user_query and conext of the user_query which contain some retrieved information from literature regarding user_query, based on that context you will answer the user query. input json is {}""".format(input_json)
    return s



def main():
    p=0
    responses =[]
    chat_history = [
	{"user_name": "Chatbot", "text": "Hey! How can I help you today?"},]
    while True and p<6:
        input_query = input()
        input_query= query_builder(retriever(input_query), input_query)
        response = co.chat(message=input_query, chat_history=chat_history)
        x={"user_name":"user", "text":input_query}
        chat_history.append(x)
        chat_history.append({"user_name": "Chatbot", "text":response.text})
        p=p+1
        responses.append(response.text)
    return responses


if __name__ == "__main__":
    main()