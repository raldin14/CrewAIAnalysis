from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewaianalysis.tools.custom_tool import ast_tool, db_tool, diff_tool, transform_tool, dep_tool, test_tool


@CrewBase
class Crewaianalysis():
    agents_config = 'config/agents.yaml'
    tasks_config  = 'config/tasks.yaml'

    @agent
    def archaeologist(self) -> Agent:
        return Agent(config=self.agents_config['archaeologist'],
                     tools=[ast_tool, db_tool], verbose=True)

    @agent
    def architect(self) -> Agent:
        return Agent(config=self.agents_config['architect'],
                     tools=[diff_tool, transform_tool, dep_tool], verbose=True)

    @agent
    def qa_lead(self) -> Agent:
        return Agent(config=self.agents_config['qa_lead'],
                     tools=[test_tool], verbose=True)

    @task
    def discovery_task(self) -> Task:
        return Task(config=self.tasks_config['discovery_task'])

    @task
    def planning_task(self) -> Task:
        return Task(config=self.tasks_config['planning_task'])

    @task
    def validation_task(self) -> Task:
        return Task(config=self.tasks_config['validation_task'])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
