from langgraph_workflow.workflow import build_graph, AgentState

def main():
    user_query = input("Enter your query: ")
    graph = build_graph()
    final_state = graph.invoke(AgentState(user_query))

    print("\nSubtasks Executed:")
    for task, result in final_state.completed_tasks:
        print(f"{task} -> {result}")

if __name__ == "__main__":
    main()
