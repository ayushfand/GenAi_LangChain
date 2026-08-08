from langchain_community.tools import DuckDuckGoSearchRun;
search_tool = DuckDuckGoSearchRun()
results = search_tool.run("Fifa world cup 2026")
print (results)