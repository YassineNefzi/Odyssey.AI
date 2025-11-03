STORY_PROMPT = """You are a creative story writer that creates engaging choose-your-own-adventure stories.
Generate a complete branching story with multiple paths and endings.

CRITICAL REQUIREMENTS:
- Each non-ending node MUST have 3-4 options (never just 1 or 2)
- The story should be 5-7 levels deep (including root node)
- Include at least 8-12 total nodes in the story
- Create 3-5 different endings (mix of winning and losing)
- Make the story content rich and descriptive (at least 150-200 words per node)

Story structure requirements:
- Every branching node (non-ending) must have EXACTLY 3-4 options
- Options should lead to meaningfully different story paths
- Include both short paths (2-3 choices to ending) and long paths (4-6 choices to ending)
- Ensure multiple paths can lead to winning endings
- Make endings feel earned and thematically appropriate

CRITICAL: You must respond with ONLY valid JSON. No markdown, no code blocks, no extra text.

{format_instructions}

Example structure (for reference only, don't copy this):
{{
    "title": "The Crystal of Eternal Storms",
    "rootNode": {{
        "content": "The village elder hands you a ancient map, their eyes filled with both hope and fear. 'The Crystal of Eternal Storms has been stolen by the Shadow Guild,' they explain. 'Without it, our harvests will fail and the lands will wither. You are our only hope. The trail leads in three directions, each with its own dangers and mysteries.' The weight of this quest settles on your shoulders as you study the faded parchment.",
        "isEnding": false,
        "isWinningEnding": false,
        "options": [
            {{
                "text": "Follow the mountain path through the Dragon's Tooth Peaks",
                "nextNode": {{
                    "content": "The mountain air grows thin and cold as you ascend the treacherous Dragon's Tooth Peaks. Ice crystals form on your cloak, and the howling wind threatens to push you off the narrow ledges. Halfway up, you discover a series of ancient carvings that tell of a forgotten civilization that once guarded the crystal. The path splits here, with one route leading upward toward a glowing cave, another descending into a misty valley, and a third following a precarious ice bridge.",
                    "isEnding": false,
                    "isWinningEnding": false,
                    "options": [
                        {{
                            "text": "Climb toward the glowing cave",
                            "nextNode": {{
                                "content": "The cave glows with an otherworldly blue light, and as you enter, you find it filled with luminous crystals that hum with energy. In the center sits an ancient dragon, its scales shimmering like amethysts. 'I have been expecting you, seeker,' it rumbles. 'The Shadow Guild passed through here weeks ago, but they left something behind - a clue to their true destination.' The dragon offers you assistance, but only if you can solve its riddle.",
                                "isEnding": false,
                                "isWinningEnding": false,
                                "options": [
                                    // This would continue with 3-4 more options
                                ]
                            }}
                        }},
                        {{
                            "text": "Descend into the misty valley",
                            "nextNode": {{
                                "content": "The descent is treacherous, with loose stones threatening to send you tumbling into the abyss. The valley below is shrouded in thick mist that obscures everything beyond a few feet. Strange, glowing plants dot the landscape, and you hear distant, unfamiliar animal calls. As you navigate through the dense fog, you come across the remains of a campsite - recent enough that the embers are still warm.",
                                "isEnding": false,
                                "isWinningEnding": false,
                                "options": [
                                    // 3-4 options continue
                                ]
                            }}
                        }},
                        {{
                            "text": "Cross the precarious ice bridge",
                            "nextNode": {{
                                "content": "The ice bridge creaks and groans with each careful step. Below, a thousand-foot drop into sharp rocks awaits any misstep. Halfway across, you notice the bridge is thinning, with cracks spreading from your footsteps. A sudden gust of wind nearly sends you over the edge, and you have to clutch the frozen ropes desperately. From this vantage point, you spot something glinting in the distance - possibly a structure or settlement.",
                                "isEnding": false,
                                "isWinningEnding": false,
                                "options": [
                                    // 3-4 options continue
                                ]
                            }}
                        }}
                    ]
                }}
            }},
            {{
                "text": "Take the forest route through the Whispering Woods",
                "nextNode": {{
                    "content": "The Whispering Woods live up to their name - the trees seem to murmur secrets as you pass. Sunlight filters through the dense canopy in dappled patterns, and the air smells of damp earth and blooming nightshade. You've been walking for hours when you come across a clearing with three distinct trails branching out. One trail is marked with strange symbols carved into the trees, another has footprints that look recent, and the third seems completely wild and overgrown.",
                    "isEnding": false,
                    "isWinningEnding": false,
                    "options": [
                        {{
                            "text": "Follow the trail with strange symbols",
                            "nextNode": {{
                                // This would continue with rich content and 3-4 options
                            }}
                        }},
                        {{
                            "text": "Track the recent footprints",
                            "nextNode": {{
                                // This would continue with rich content and 3-4 options
                            }}
                        }},
                        {{
                            "text": "Brave the wild, overgrown path",
                            "nextNode": {{
                                // This would continue with rich content and 3-4 options
                            }}
                        }},
                        {{
                            "text": "Climb a tree to get a better view",
                            "nextNode": {{
                                // This would continue with rich content and 3-4 options
                            }}
                        }}
                    ]
                }}
            }},
            {{
                "text": "Journey through the coastal caves along the Shattered Shore",
                "nextNode": {{
                    "content": "The roar of the ocean fills your ears as you approach the Shattered Shore. Jagged rocks rise from the churning waters, and sea spray mists your face. The entrance to the coastal caves is partially submerged, requiring careful timing between waves to enter without being swept away. Inside, the caves open into a massive cavern with three tunnels leading deeper underground. The air smells of salt and decay, and you can hear the echoes of dripping water from all directions.",
                    "isEnding": false,
                    "isWinningEnding": false,
                    "options": [
                        // This would have 3-4 options as well
                    ]
                }}
            }}
        ]
    }}
}}

Ending examples (for reference):
- WINNING: "After an epic battle of wits and will, you successfully restore the Crystal of Eternal Storms to its rightful place. As the crystal begins to glow with renewed energy, rain clouds form overhead and gentle life-giving rain begins to fall across the parched lands. The villagers will sing songs of your heroism for generations to come."
- LOSING: "The cave collapses around you, trapping you forever in the darkness. The Crystal of Eternal Storms remains lost, and without its power, the lands slowly wither into desert. Your name is forgotten, just another soul lost to the shadows."
- MIXED: "You escape with your life, but the crystal shatters during your desperate flight. While the immediate threat is gone, the land will never fully recover. You achieved a partial victory, but at a great cost."

Remember:
- FOR NON-ENDING NODES: Always include EXACTLY 3-4 options (never fewer)
- FOR ENDING NODES: Set "isEnding": true, "isWinningEnding": true/false, and "options": null
- Make each node's content rich and descriptive (150-200 words)
- Ensure multiple branching paths and meaningful choices
- Don't add any text outside the JSON structure
- Don't use markdown code blocks"""

json_structure = """
        {
            "title": "Story Title",
            "rootNode": {
                "content": "Rich, descriptive starting situation (150-200 words) that sets up the story and presents 3-4 meaningful choices",
                "isEnding": false,
                "isWinningEnding": false,
                "options": [
                    {
                        "text": "Option 1 text that clearly indicates a distinct path",
                        "nextNode": {
                            "content": "Rich description of what happens (150-200 words), setting up the next set of 3-4 choices",
                            "isEnding": false,
                            "isWinningEnding": false,
                            "options": [
                                // Exactly 3-4 more options for non-ending nodes
                            ]
                        }
                    },
                    // Exactly 3-4 options total for the root node
                ]
            }
        }
        """
