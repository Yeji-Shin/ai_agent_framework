from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

# Step 1: Hugging Face Summarization Pipeline
def get_huggingface_pipeline():
    # Load Hugging Face summarization pipeline
    summarizer = pipeline(
        "summarization",
        model="facebook/bart-large-cnn",  # Pre-trained summarization model
        tokenizer="facebook/bart-large-cnn",
        framework="pt"  # Choose "pt" for PyTorch or "tf" for TensorFlow
    )
    return summarizer

# Step 2: Integrate with LangChain
def create_langchain(summarizer_pipeline):
    # Define LangChain LLM wrapper
    llm = HuggingFacePipeline(pipeline=summarizer_pipeline)
    
    # Define the prompt template
    prompt_template = PromptTemplate(
        input_variables=["text"],
        template="Summarize the following text:\n\n{text}"
    )
    
    # Create LangChain summarization chain
    chain = LLMChain(llm=llm, prompt=prompt_template)
    return chain

# Step 3: Run the summarization
def summarize_text(input_text):
    # Get the Hugging Face pipeline
    summarizer_pipeline = get_huggingface_pipeline()
    
    # Create LangChain
    chain = create_langchain(summarizer_pipeline)
    
    # Run the summarization chain
    summary = chain.run({"text": input_text})
    return summary

