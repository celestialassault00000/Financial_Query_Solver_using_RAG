import torch
from src.load_model_tokenizer import model, tokenizer




def embeddings(text,model= model , tokenizer= tokenizer):
    batch_tokens = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        last_hidden_state = model(**batch_tokens, output_hidden_states=True, return_dict=True).last_hidden_state
    weights = (
    torch.arange(start=1, end=last_hidden_state.shape[1] + 1)
    .unsqueeze(0)
    .unsqueeze(-1)
    .expand(last_hidden_state.size())
    .float().to(last_hidden_state.device))
    input_mask_expanded = (
    batch_tokens["attention_mask"]
    .unsqueeze(-1)
    .expand(last_hidden_state.size())
    .float())
    sum_embeddings = torch.sum(last_hidden_state * input_mask_expanded * weights, dim=1)
    sum_mask = torch.sum(input_mask_expanded * weights, dim=1)
    
    embeddings = sum_embeddings / sum_mask
    return embeddings.detach().cpu().numpy()[0].tolist()
    

    

    