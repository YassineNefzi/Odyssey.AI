import {useState, useEffect} from 'react';

function StoryGame({story, onNewStory}) {
    const [currentNodeId, setCurrentNodeId] = useState(null);
    const [currentNode, setCurrentNode] = useState(null);
    const [options, setOptions] = useState([]);
    const [isEnding, setIsEnding] = useState(false);
    const [isWinningEnding, setIsWinningEnding] = useState(false);
    const [displayText, setDisplayText] = useState('');
    const [isTyping, setIsTyping] = useState(false);

    useEffect(() => {
        if (story && story.root_node) {
            const rootNodeId = story.root_node.id;
            setCurrentNodeId(rootNodeId);
        }
    }, [story]);

    useEffect(() => {
        if (currentNodeId && story && story.all_nodes) {
            const node = story.all_nodes[currentNodeId];
            setCurrentNode(node);
            setIsEnding(node.is_ending);
            setIsWinningEnding(node.is_winning_ending);

            if (!node.is_ending && node.options && node.options.length > 0) {
                setOptions(node.options);
            } else {
                setOptions([]);
            }

            if (node && node.content) {
                setIsTyping(true);
                setDisplayText('');
                let currentIndex = 0;
                const typingInterval = setInterval(() => {
                    if (currentIndex <= node.content.length) {
                        setDisplayText(node.content.slice(0, currentIndex));
                        currentIndex++;
                    } else {
                        setIsTyping(false);
                        clearInterval(typingInterval);
                    }
                }, 10);
                return () => clearInterval(typingInterval);
            }
        }
    }, [currentNodeId, story]);

    const chooseOption = (optionId) => {
        setCurrentNodeId(optionId);
    };

    const restartStory = () => {
        if (story && story.root_node) {
            setCurrentNodeId(story.root_node.id);
        }
    };

    return (
        <div className="story-game scanlines">
            <header className="story-header">
                <h2>{story.title}</h2>
            </header>
            <div className="story-content">
                {currentNode && (
                    <div className="story-node">
                        <p className={isTyping ? 'typing-animation' : ''}>
                            {displayText}
                        </p>
                        {isEnding ? (
                            <div className="story-ending">
                                <h3>{isWinningEnding ? "🎉 Congratulations!" : "🏁 The End"}</h3>
                                <div className={isWinningEnding ? 'winning-message' : 'ending-message'}>
                                    {isWinningEnding
                                        ? "You reached a winning ending! Great job!"
                                        : "Your adventure has concluded."
                                    }
                                </div>
                            </div>
                        ) : (
                            !isTyping && (
                                <div className="story-options">
                                    <h3>What will you do?</h3>
                                    <div className="options-list">
                                        {options.map((option, index) => (
                                            <button
                                                key={index}
                                                onClick={() => chooseOption(option.node_id)}
                                                className="option-btn"
                                            >
                                                {option.text}
                                            </button>
                                        ))}
                                    </div>
                                </div>
                            )
                        )}
                    </div>
                )}
                <div className="story-controls">
                    <button onClick={restartStory} className="reset-btn">
                        Restart Story
                    </button>
                    {onNewStory && (
                        <button onClick={onNewStory} className="new-story-btn">
                            New Story
                        </button>
                    )}
                </div>
            </div>
        </div>
    );
}

export default StoryGame;