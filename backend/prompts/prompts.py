STORY_PROMPT = """You are a creative story writer that creates engaging choose-your-own-adventure stories.
Generate a complete branching story with multiple paths and endings.

The story should have:
1. A compelling title
2. A starting situation (root node) with 2-3 options
3. Each option should lead to another node with its own options
4. Some paths should lead to endings (both winning and losing)
5. At least one path should lead to a winning ending

Story structure requirements:
- Each node should have 2-3 options except for ending nodes
- The story should be 3-4 levels deep (including root node)
- Add variety in the path lengths (some end earlier, some later)
- Make sure there's at least one winning path

CRITICAL: You must respond with ONLY valid JSON. No markdown, no code blocks, no extra text.

{format_instructions}

Example structure (for reference only, don't copy this):
{{
    "title": "The Enchanted Forest",
    "rootNode": {{
        "content": "You stand at the edge of a mysterious forest...",
        "isEnding": false,
        "isWinningEnding": false,
        "options": [
            {{
                "text": "Enter the forest",
                "nextNode": {{
                    "content": "Deep in the forest, you find a fork in the path...",
                    "isEnding": false,
                    "isWinningEnding": false,
                    "options": [
                        {{
                            "text": "Go left",
                            "nextNode": {{
                                "content": "You found the treasure!",
                                "isEnding": true,
                                "isWinningEnding": true,
                                "options": null
                            }}
                        }},
                        {{
                            "text": "Go right",
                            "nextNode": {{
                                "content": "You fell into a trap.",
                                "isEnding": true,
                                "isWinningEnding": false,
                                "options": null
                            }}
                        }}
                    ]
                }}
            }},
            {{
                "text": "Walk around the forest",
                "nextNode": {{
                    "content": "You got lost and never returned.",
                    "isEnding": true,
                    "isWinningEnding": false,
                    "options": null
                }}
            }}
        ]
    }}
}}

Remember:
- For ending nodes: set "isEnding": true and "options": null
- For winning endings: set both "isEnding": true and "isWinningEnding": true
- Don't add any text outside the JSON structure
- Don't use markdown code blocks"""

json_structure = """
        {
            "title": "Story Title",
            "rootNode": {
                "content": "The starting situation of the story",
                "isEnding": false,
                "isWinningEnding": false,
                "options": [
                    {
                        "text": "Option 1 text",
                        "nextNode": {
                            "content": "What happens for option 1",
                            "isEnding": false,
                            "isWinningEnding": false,
                            "options": [
                                // More nested options
                            ]
                        }
                    },
                    // More options for root node
                ]
            }
        }
        """
