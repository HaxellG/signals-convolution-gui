LIGHT_BLUE_COLOR = '#90d6ff'
MEDIUM_BLUE_COLOR = '#2781ff'
DARK_BLUE_COLOR = '#225eb1'
LIGHT_PURPLE_COLOR = "#a353ff"
DARK_PURPLE_COLOR = '#7955ac'

CSS_STYLES = """
<style>
    /* Main content area */

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #2b5876;
        background-image: linear-gradient(to bottom, #2b5876, #4e4376);
        padding: 2rem 1rem;
    }

    /* Sidebar title (Operaciones de Convolución) */
    [data-testid="stSidebar"] h1 {
        color: #ffffff !important;  /* Set to white */
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 1.5rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }

    .stSelectbox label {
        color: white !important;
        font-size: 40px !important;
    }

    /* Section headers */
    [data-testid="stSidebar"] h2 {
        color: #ffffff !important;  /* Set to white */
        font-size: 1em;
        font-weight: bold;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
        letter-spacing: 0.05em;
    }

    [data-testid="stSidebar"] .stRadio > label:hover {
        color: #ffd700 !important;
    }

    [data-testid="stSidebar"] .stRadio > div > label {
        display: flex;
        align-items: center;
        cursor: pointer;
        margin-bottom: 0.5rem;
    }

    [data-testid="stSidebar"] .stRadio > div > label > div:first-child {
        display: none;
    }

    [data-testid="stSidebar"] .stRadio > div > label > div:last-child {
        display: flex;
        align-items: center;
    }

    [data-testid="stSidebar"] .stRadio > div > label > div:last-child::before {
        content: "•";
        font-size: 1.5em;
        margin-right: 0.5rem;
        color: transparent;
        transition: color 0.3s ease;
    }

    [data-testid="stSidebar"] .stRadio > div > label:hover > div:last-child::before {
        color: #ffd700 !important;
    }

    [data-testid="stSidebar"] .stRadio > div [data-testid="stMarkdownContainer"] p {
        margin: 0;
        color: #ffffff !important; /* Ensure that markdown text is white */
    }

    /* Main content styling */
    .main .block-container {
        padding: 2rem;
    }

    .main h1 {
        color: #2b5876;
        margin-bottom: 1rem;
    }
</style>
"""