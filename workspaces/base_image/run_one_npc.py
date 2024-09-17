import asyncio
from server import run_server
import argparse

def main():
    # Use argparse to capture command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--agent_first_name', type=str, help="Input NPC first name")
    args = parser.parse_args()

    # Run the asyncio task
    asyncio.run(
        run_server(
            # The agent1 is the examinee
            # The agent2 is the sotopia NPC
            # This should match the profile and goals order
            model_dict={
                "env": "gpt-4-turbo",
                "agent1": "rocketchat",
                "agent2": "gpt-4-turbo",
            },
            # Agent Roles are uesless here.
            agents_roles={
                "agent1": "",
                "agent2": "",
            },
            agent_first_name = args.agent_first_name
        )
    )

if __name__ == "__main__":
    main()