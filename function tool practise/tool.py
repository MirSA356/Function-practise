from agents import Agent, Runner, function_tool
from main import config

@function_tool
def usd_to_pkr():
    return 'Today USD to PKR is 290'

agent = Agent(
    name='An Agent',
    instructions="You Are A HelpFull Assistant. Your task is a help the user with their queries.",
    tools=[usd_to_pkr]
)

result = Runner.run_sync(agent,
                         'what is usd to pkr today?',
                        run_config=config)

print(result.final_output)

#ye sirf porani chezen batata hai. real time data nhi batata or personal data bhi nhi batata
