function LoadingStatus({theme}) {
    return (
        <div className="loading-container scanlines">
            <h2>Generating Your {theme} Story</h2>

            <div className="pixel-loader">
                {[...Array(9)].map((_, i) => (
                    <div key={i} className="pixel-dot" />
                ))}
            </div>

            <p className="loading-info">
                AI is crafting your pixel adventure...
            </p>
        </div>
    )
}

export default LoadingStatus;