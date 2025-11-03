import {useState} from "react"

const themeExamples = [
    "Space Adventure",
    "Medieval Fantasy",
    "Cyberpunk City",
    "Pirate Treasure",
    "Haunted Mansion",
    "Dragon Quest",
    "Time Travel",
    "Superhero Origin"
]

function ThemeInput({onSubmit}) {
    const [theme, setTheme]= useState("");
    const [error, setError] = useState("")

    const handleSubmit = (e) => {
        e.preventDefault();

        if (!theme.trim()) {
            setError("Please enter a theme name");
            return
        }

        onSubmit(theme);
    }

    const handleExampleClick = (exampleTheme) => {
        setTheme(exampleTheme);
        setError("");
    }

    return (
        <div className="theme-input-container scanlines">
            <h2>Generate Your Adventure</h2>
            <p>Enter a theme for your interactive story</p>

            <form onSubmit={handleSubmit}>
                <div className="input-group">
                    <input
                        type="text"
                        value={theme}
                        onChange={(e) => setTheme(e.target.value)}
                        placeholder="Enter a theme (e.g. pirates, space, medieval...)"
                        className={error ? 'error' : ''}
                    />
                    {error && <p className="error-text">{error}</p>}
                </div>
                <button type="submit" className='generate-btn pixel-press'>
                    Generate Story
                </button>
            </form>

            <div className="examples">
                <h3>Try these examples:</h3>
                <div className="example-tags">
                    {themeExamples.map((example, index) => (
                        <span
                            key={index}
                            onClick={() => handleExampleClick(example)}
                            className="example-tag pixel-press"
                        >
                            {example}
                        </span>
                    ))}
                </div>
            </div>
        </div>
    )
}

export default ThemeInput;