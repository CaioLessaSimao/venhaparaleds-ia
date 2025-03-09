from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
from lerpdf.tools.custom_tool import PDFReaderTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Carrega a API key do arquivo .env
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Cria uma instância do modelo Gemini
llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=GOOGLE_API_KEY
)

@CrewBase
class LerpdfCrew():
	"""Lerpdf crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def pdf_reader_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['pdf_reader_agent'],
			tools=[PDFReaderTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True,
			llm=llm
		)

	@agent
	def analysis_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['analysis_agent'],
			verbose=True,
			llm=llm
		)
	
	@agent
	def sumary_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['summary_agent'],
			verbose=True,
			llm=llm
		)
	@agent
	def blog_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['blog_agent'],
			verbose=True,
			llm=llm
		)

	@task
	def extraction_task(self) -> Task:
		return Task(
			config=self.tasks_config['extraction_task'],
			agent=self.pdf_reader_agent(),
			output_file='report.md'
		)
	@task
	def analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['analysis_task'],
			agent=self.analysis_agent(),
			output_file='report.md'
		)
	@task
	def sumarize_task(self) -> Task:
		return Task(
			config=self.tasks_config['sumarize_task'],
			agent=self.sumary_agent(),
			output_file='report.md'
		)
	@task
	def blog_task(self) -> Task:
		return Task(
			config=self.tasks_config['blog_task'],
			agent=self.blog_agent(),
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Lerpdf crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=2,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)