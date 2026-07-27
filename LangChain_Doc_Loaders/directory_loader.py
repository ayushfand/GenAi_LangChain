from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader =  DirectoryLoader(
    path='books', #add a folder named books and add pdfs in that 
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()

print(len(docs))