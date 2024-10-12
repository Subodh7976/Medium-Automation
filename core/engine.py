from llama_index.core.workflow import (
    step, 
    Context, 
    Workflow, 
    Event, 
    StartEvent,
    StopEvent 
)
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from time import time 

from .events import *

class AutomationWorkflow(Workflow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    @step 
    async def extractor(self, ctx: Context, event: StartEvent) -> GoogleSearchEvent:
        pass 

    @step(num_workers=3)
    async def google_search(self, ctx: Context, event: GoogleSearchEvent) -> ResultEvent:
        pass 
    
    @step 
    async def article_generator(self, ctx: Context, event: ResultEvent) -> ImageGeneratorEvent | StopEvent:
        pass 
    
    @step(num_workers=2)
    async def image_generator(self, ctx: Context, event: ImageGeneratorEvent) -> StopEvent:
        pass 