# 
graph.add_conditional_edges(
    "increment",
    check_user_input,
    {
        "question": "answer_question",
        "command": "execute_command",
        "unknown": END
    }
)





