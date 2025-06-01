# services/gemini_client.py

# Imports
import streamlit as st # Import streamlit for caching
from langchain.agents import load_tools, initialize_agent
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from langchain.prompts import PromptTemplate


# --- Cached Initialization of LangChain Components ---

# Use st.cache_resource to load the LLM only once across app runs
@st.cache_resource
def load_llm():
    """Initializes and caches the Gemini 2.0 Flash LLM."""
    # Initialize Gemini 2.0 Flash (latest compatible with LangChain)
    # Ensure GOOGLE_API_KEY is set in environment variables before this runs
    return ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.4)

# Use st.cache_resource to load tools only once
@st.cache_resource
def load_agent_tools():
    """Loads and caches the necessary tools for the agent."""
    # Ensure SERPAPI_API_KEY is set in environment variables before this runs
    return load_tools(["serpapi"])

# Use st.cache_resource to initialize the agent only once
@st.cache_resource
def initialize_langchain_agent(_llm_instance, _tools_instance):
    """Initializes and caches the LangChain agent."""
    return initialize_agent(
        _tools_instance,
        _llm_instance,
        agent="zero-shot-react-description",
        verbose=True,
        handle_parsing_errors=True
    )

# Use st.cache_resource to create the prompt template only once
@st.cache_resource
def create_prompt_template():
    """Creates and caches the prompt template."""
    return PromptTemplate(
        input_variables=["context", "question", "pincode"],
        template="""
You are a highly knowledgeable and practical agricultural advisor specializing in Indian farming conditions.
Your goal is to provide **comprehensive, detailed, and actionable advice** to Indian farmers.
Use the information in the provided context and the demographic details (like pincode) to give the most accurate, relevant, and in-depth answer possible.

**Context:**
{context}

**Demographic Information:**
Pincode: {pincode}

**Farmer's Question:**
{question}

**Instructions for your detailed answer:**
1.  **Break Down the Problem:** If the question involves multiple steps or aspects, address each one systematically.
2.  **Provide Specifics:** Instead of general statements, offer concrete details (e.g., specific measurements, timings, types of fertilizers/pesticides, varieties of crops).
3.  **Step-by-Step Guidance:** For any process (e.g., planting, pest control, harvesting), provide clear, numbered, step-by-step instructions.
4.  **Consider Local Factors:** Explicitly mention how climate, soil type, water availability, and local practices relevant to the given pincode might influence the advice.
5.  **Common Challenges & Solutions:** Anticipate potential problems or challenges a farmer might face related to the question and offer practical solutions or preventative measures.
6.  **Alternative Approaches:** If applicable, suggest different methods or options, explaining their pros and cons.
7.  **Practical Examples:** Use simple, relatable examples that an Indian farmer can easily understand and apply.
8.  **Language:** Avoid technical jargon. Use simple, clear, and easy-to-understand Hindi or English (as appropriate for the context, but default to clear English unless specified otherwise).
9.  **Formatting:** Structure your answer like an article, using **Markdown** for clear sections and readability.
    * Use **headings** (e.g., `# Main Topic`, `## Sub-section`) to break down the content.
    * Use **bullet points** (`* Item`) or **numbered lists** (`1. Item`) for steps or lists of information.
    * Use **bold text** (`**text**`) for emphasis.
    * Ensure the overall structure is easy to read section by section.

Now, provide a comprehensive and detailed answer based on the above instructions, formatted as an article.
"""
)
# --- Function to get context and run agent ---

def get_serpapi_context_and_run_agent(question, pincode=""):
    """
    Uses SerpAPI to get context based on a question and runs the agent
    with the context and question in the prompt template.

    Args:
        question (str): The question to ask the agent and use as the search query.
        pincode (str): The pincode for demographic context.
    """
    # Retrieve cached components
    llm = load_llm()
    tools = load_agent_tools()
    agent = initialize_langchain_agent(llm, tools)
    prompt_template = create_prompt_template()

    # Find the SerpAPI tool in your list
    serpapi_tool = None
    for tool in tools:
        # The name might vary, check the tool's attributes.
        # Common names include "Search", "serpapi", "SerpAPI"
        if tool.name == "Search":
            serpapi_tool = tool
            break

    if serpapi_tool:
        # Use the question as the search query for the SerpAPI tool
        search_query = f"{question} in pincode {pincode}"

        # Use the SerpAPI tool to perform the search
        try:
            search_results = serpapi_tool.run(search_query)
        except Exception as e:
            print(f"Error during SerpAPI search: {e}")
            search_results = "No information found from search." # Provide a default context

        # Pass the search results as the context
        context_from_serpapi = search_results

        # Format the prompt template with the context from SerpAPI and the question
        formatted_prompt = prompt_template.format(context=context_from_serpapi, question=question, pincode=pincode)

        # Run the agent with the formatted prompt
        # print(f"\nRunning agent with prompt:\n{formatted_prompt}\n")
        final_answer = agent.run(formatted_prompt)
        return final_answer # Return the actual answer
    else:
        print("SerpAPI tool not found in the loaded tools. Cannot fetch context.")
        return "Could not find relevant information."

